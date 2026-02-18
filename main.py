import pyrogram
from pyrogram import Client, filters
import requests

api_id = 34818480
api_hash = "a82911ecbf23a7ead187d410a34cf47a"
bot_token = "8474423811:AAEWPnVwWmKpMxEROHcAy3JaMtMp4BXlwI4"

app = Client("my_terabox_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("I am Online! Send me a Terabox link.")

@app.on_message(filters.text)
async def download_handler(client, message):
    url = message.text
    if "terabox" in url or "terashare" in url:
        status = await message.reply_text("Trying to fetch video... ⏳")
        try:
            # alternative stable API
            api_url = f"https://terabox-dl.echoas.workers.dev/api/get-info?url={url}"
            req = requests.get(api_url)
            
            if req.status_code != 200:
                return await status.edit("Bypass server is currently busy. Please try another link or wait.")

            response = req.json()
            if "download_link" in response:
                await client.send_video(
                    chat_id=message.chat.id,
                    video=response["download_link"],
                    caption=f"✅ **File:** `{response.get('title', 'video.mp4')}`"
                )
                await status.delete()
            else:
                await status.edit("Could not extract the download link. Try after some time.")
        except Exception as e:
            await status.edit(f"API Error: Please check back later.")
    else:
        await message.reply_text("Please send a valid Terabox link.")

app.run()
