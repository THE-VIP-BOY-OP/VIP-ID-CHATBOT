import asyncio
import importlib

from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from nexichat import LOGGER, nexichat
from nexichat.modules import ALL_MODULES

async def anony_boot():
    try:
        await nexichat.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    # Import all modules dynamically
    for all_module in ALL_MODULES:
        importlib.import_module("nexichat.modules." + all_module)
        LOGGER.info(f"Successfully imported: {all_module}")

    # Set userbot commands
    try:
        # Adjust the command list to fit userbot context if needed
        await nexichat.set_bot_commands(
            commands=[
                BotCommand("start", "Start the userbot"),
                BotCommand("help", "Get the help menu"),
                BotCommand("ping", "Check if the userbot is alive or dead"),
                BotCommand("lang", "Select reply language"),
                BotCommand("resetlang", "Reset to default reply language"),
                BotCommand("id", "Get your user_id"),
                BotCommand("stats", "Check userbot stats"),
                BotCommand("gcast", "Broadcast any message to groups/users"),
                BotCommand("chatbot", "Enable or disable chatbot"),
                BotCommand("status", "Check chatbot status in chat"),
                BotCommand("shayri", "Get random shayari for love"),
                BotCommand("repo", "Get userbot source code"),
            ]
        )
        LOGGER.info("Userbot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set userbot commands: {ex}")

    LOGGER.info(f"@{nexichat.username} Started.")
    try:
        await nexichat.send_message(int(OWNER_ID), f"{nexichat.mention} has started")
    except Exception as ex:
        LOGGER.info(f"@{nexichat.username} started, please check from owner ID.")
    
    await idle()

if __name__ == "__main__":
    asyncio.run(anony_boot())
    LOGGER.info("Stopping nexichat Userbot...")
