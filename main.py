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
    await message.reply_text("Hello! I am active. Send me a Terabox link to download.")

@app.on_message(filters.text)
async def download_handler(client, message):
    url = message.text
    if "terabox" in url or "terashare" in url:
        status_msg = await message.reply_text("Fetching video details... ⏳")
        
        try:
            # Updated API request with error handling
            api_url = f"https://terabox-dl.qtcloud.workers.dev/api/get-info?url={url}"
            response = requests.get(api_url)
            
            # സർവർ മറുപടി നൽകുന്നില്ലെങ്കിൽ ഇത് കാണിക്കും
            if response.status_code != 200:
                return await status_msg.edit("Server error. The bypass API might be down. Please try again later.")

            data = response.json()
            
            if "download_link" in data:
                video_url = data["download_link"]
                file_name = data.get("title", "video.mp4")
                
                await status_msg.edit("Uploading to Telegram... 📤")
                
                # വീഡിയോ നേരിട്ട് ടെലിഗ്രാമിലേക്ക് അയക്കുന്നു
                await client.send_video(
                    chat_id=message.chat.id,
                    video=video_url,
                    caption=f"✅ **Done:** `{file_name}`"
                )
                await status_msg.delete()
            else:
                await status_msg.edit("Could not find a download link for this specific file.")
                
        except Exception as e:
            await status_msg.edit(f"Error: {str(e)}")
    else:
        await message.reply_text("Please send a valid link containing 'terabox'.")

if __name__ == "__main__":
    app.run()
