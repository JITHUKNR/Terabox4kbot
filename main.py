import pyrogram
from pyrogram import Client, filters
import requests
import re

# Your Credentials
api_id = 34818480
api_hash = "a82911ecbf23a7ead187d410a34cf47a"
bot_token = "8474423811:AAEWPnVwWmKpMxEROHcAy3JaMtMp4BXlwI4"

# Your Terabox NDUS Cookie
NDUS_COOKIE = "877a11e9d5836de7ca9e8282e0e2245cc9687996622cddcd5381d63c275180414313157ee12a92e236a7e64ec35c3fea1a4b9ee61731170effd4c70134b66b16e9644fd35824c6378fbaf36a7c15d10781698daf3ff7f29f08f426650d8899dc3f2f3a3c8edd0a2fe8f9c7dcf1a6583a"

app = Client("my_terabox_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Bot is Ready! Send me a Terabox link.")

@app.on_message(filters.text)
async def handle_link(client, message):
    url = message.text
    if "terabox" in url or "terashare" in url:
        status = await message.reply_text("Processing... ⏳")
        try:
            # Cleaning the link
            url = re.findall(r'https?://[^\s]+', url)[0]
            
            # Using a reliable direct bypass method
            bypass_url = f"https://terabox-dl.echoas.workers.dev/api/get-info?url={url}"
            headers = {"Cookie": f"ndus={NDUS_COOKIE}"}
            
            response = requests.get(bypass_url, headers=headers).json()
            
            if "download_link" in response:
                await client.send_video(
                    chat_id=message.chat.id,
                    video=response["download_link"],
                    caption=f"✅ **File:** `{response.get('title', 'video.mp4')}`"
                )
                await status.delete()
            else:
                await status.edit("API is not responding. Please try another link or check back later.")
        except Exception as e:
            await status.edit(f"Error: {str(e)}")
    else:
        await message.reply_text("Please send a valid Terabox link.")

app.run()
