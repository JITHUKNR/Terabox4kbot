import pyrogram
from pyrogram import Client, filters
import requests
import asyncio

# Your Credentials
api_id = 34818480
api_hash = "a82911ecbf23a7ead187d410a34cf47a"
bot_token = "8474423811:AAEWPnVwWmKpMxEROHcAy3JaMtMp4BXlwI4"

app = Client("my_terabox_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello! Send me a Terabox link, and I will download the video for you.")

@app.on_message(filters.text)
async def download_handler(client, message):
    url = message.text
    if "terabox" in url or "terashare" in url:
        status_msg = await message.reply_text("Processing your link... Please wait ⏳")
        
        try:
            # Using a public Terabox bypass API
            api_url = f"https://terabox-dl.qtcloud.workers.dev/api/get-info?url={url}"
            data = requests.get(api_url).json()
            
            if "download_link" in data:
                video_url = data["download_link"]
                file_name = data.get("title", "video.mp4")
                
                # Uploading the video directly to Telegram
                await client.send_video(
                    chat_id=message.chat.id,
                    video=video_url,
                    caption=f"✅ **File Ready:** `{file_name}`"
                )
                await status_msg.delete()
            else:
                await status_msg.edit("Sorry, I couldn't fetch the download link. Make sure the link is valid.")
                
        except Exception as e:
            await status_msg.edit(f"An error occurred: {str(e)}")
    else:
        await message.reply_text("Please send a valid Terabox link.")

if __name__ == "__main__":
    app.run()
