import asyncio
import importlib

from pyrogram import idle
from config import OWNER_ID
from nexichat import LOGGER, nexichat
from nexichat.modules import ALL_MODULES

async def init():

    await nexichat.start()

    for all_module in ALL_MODULES:
        importlib.import_module("nexichat.modules" + all_module)
        LOGGER.info(f"Successfully imported: {all_module}")

    LOGGER.info(f"@{nexichat.username} Started.")
    try:
        await nexichat.send_message(int(OWNER_ID), f"{nexichat.mention} has started")
    except Exception as ex:
        LOGGER.info(f"@{nexichat.username} started, please check from owner ID.")
    
    await idle()

if __name__ == "__main__":
        asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())