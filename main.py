import pyrogram
from pyrogram import Client, filters
import requests
import json

# Your Credentials
api_id = 34818480
api_hash = "a82911ecbf23a7ead187d410a34cf47a"
bot_token = "8474423811:AAEWPnVwWmKpMxEROHcAy3JaMtMp4BXlwI4"

app = Client("my_terabox_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Bot is Ready! Send me a Terabox link.")

@app.on_message(filters.text)
async def handle_link(client, message):
    url = message.text
    if "terabox" in url or "terashare" in url:
        status = await message.reply_text("Processing link... Please wait ⏳")
        try:
            # Using a different reliable API source
            api_url = f"https://terabox-downloader-five.vercel.app/api?url={url}"
            response = requests.get(api_url).json()
            
            if "download_url" in response:
                video_url = response["download_url"]
                title = response.get("title", "video.mp4")
                
                await status.edit("Uploading video to Telegram... 📤")
                await client.send_video(
                    chat_id=message.chat.id,
                    video=video_url,
                    caption=f"✅ **File:** `{title}`"
                )
                await status.delete()
            else:
                await status.edit("The bypass server is down. Please try again after some time.")
        except Exception as e:
            await status.edit(f"Connection Error: The download server is not responding.")
    else:
        await message.reply_text("Please send a valid Terabox link.")

app.run()
