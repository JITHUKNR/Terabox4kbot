import pyrogram
from pyrogram import Client, filters
import requests

# നിങ്ങളുടെ വിവരങ്ങൾ ഇവിടെ നൽകുക
api_id = 34818480  # my.telegram.org-ൽ നിന്നുള്ള നമ്പർ
api_hash = "a82911ecbf23a7ead187d410a34cf47a" 
bot_token = "8474423811:AAEWPnVwWmKpMxEROHcAy3JaMtMp4BXlwI4"
cookies = "877a11e9d5836de7ca9e8282e0e2245cc9687996622cddcd5381d63c275180414313157ee12a92e236a7e64ec35c3fea1a4b9ee61731170effd4c70134b66b16e9644fd35824c6378fbaf36a7c15d10781698daf3ff7f29f08f426650d8899dc3f2f3a3c8edd0a2fe8f9c7dcf1a6583a"

app = Client("my_terabox_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("ഹലോ! ടെറാബോക്സ് ലിങ്ക് അയച്ചു തരൂ, ഞാൻ അത് ഡൗൺലോഡ് ചെയ്ത് തരാം.")

@app.on_message(filters.text)
async def download(client, message):
    if "terabox.com" in message.text:
        await message.reply_text("ലിങ്ക് പരിശോധിക്കുന്നു... ദയവായി കാത്തിരിക്കൂ.")
        # ഇവിടെയാണ് ലിങ്ക് ബൈപാസ് ചെയ്യാനുള്ള ലോജിക് വരേണ്ടത്
        # നിലവിൽ ടെറാബോക്സ് API-കൾ മാറിവരുന്നതുകൊണ്ട് കൃത്യമായ ബൈപാസ് ലിങ്ക് ഉപയോഗിക്കണം
    else:
        await message.reply_text("ഇത് സാധുവായ ടെറാബോക്സ് ലിങ്ക് അല്ല.")

app.run()
