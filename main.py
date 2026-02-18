import pyrogram
from pyrogram import Client, filters
import requests

# നിങ്ങളുടെ വിവരങ്ങൾ ഇവിടെ നൽകുക
api_id = 1234567  # my.telegram.org-ൽ നിന്നുള്ള നമ്പർ
api_hash = "your_api_hash" 
bot_token = "your_bot_token"
cookies = "your_ndus_cookie_here"

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
