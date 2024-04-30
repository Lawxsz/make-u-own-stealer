import fs from 'fs/promises';
import path from 'path';

async function findAntivirusFolders(baseFolder) {
    const antivirusNames = new Set([
        "Avast", "AVG", "Bitdefender", "Kaspersky", "McAfee", "Norton", "Sophos",
        "ESET", "Malwarebytes", "Avira", "Panda", "Trend Micro", "F-Secure", "Comodo",
        "BullGuard", "360 Total Security", "Ad-Aware", "Dr.Web", "G-Data", "Vipre",
        "ClamWin", "ZoneAlarm", "Cylance", "Webroot", "Palo Alto Networks", "Symantec",
        "SentinelOne", "CrowdStrike", "Emsisoft", "HitmanPro", "Fortinet", "FireEye",
        "Zemana", "Windows Defender"
    ]);
    const antivirusFoldersDict = {};

    try {
        if (await fs.stat(baseFolder).then(stat => stat.isDirectory())) {
            const folders = await fs.readdir(baseFolder);
            for (const folder of folders) {
                const fullPath = path.join(baseFolder, folder);
                try {
                    if (await fs.stat(fullPath).then(stat => stat.isDirectory())) {
                        antivirusNames.forEach(antivirusName => {
                            if (folder.toLowerCase().includes(antivirusName.toLowerCase())) {
                                antivirusFoldersDict[antivirusName] = folder;
                            }
                        });
                    }
                } catch (err) {
                    console.error(`Error accessing ${fullPath}: ${err.message}`);
                }
            }
        }
    } catch (err) {
        console.error(`Error reading ${baseFolder}: ${err.message}`);
    }

    return antivirusFoldersDict;
}

async function main() {
    const baseFolder = "C:\\Program Files";
    const antivirusFolders = await findAntivirusFolders(baseFolder);

    if (Object.keys(antivirusFolders).length > 0) {
        console.log("Antivirus found - t.me/lawxszchannel\n");
        Object.entries(antivirusFolders).forEach(([antivirusName, folderName]) => {
            console.log(`${antivirusName}: ${folderName}`);
            // Optional: Write to file asynchronously
            // fs.writeFile("antivirus.txt", `${antivirusName}: ${folderName}\n`, { flag: 'a' });
        });
    } else {
        console.log("No antivirus found.");
    }
}

main();
