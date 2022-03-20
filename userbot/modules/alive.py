""" Userbot module for getting information about the server. """

import asyncio
import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version, uname
from shutil import which

import psutil
from telethon import __version__, version

from userbot import (
    ALIVE_LOGO,
    ALIVE_NAME,
    BOT_VER,
    CMD_HELP,
    StartTime,
    bot,
)
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

modules = CMD_HELP


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]

    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

@register(outgoing=True, pattern=r"^\.(?:alive)\s?(.)?")
async def amireallyalive(alive):
    await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    output = (
        f"💢 ᴏᴡɴᴇʀ : [Zhu](t.me/triplenineee)             ㅤ \n"
        f"💢 ꜱʏꜱᴛᴇᴍ. : Ubuntu 20.10            \n"
        f"💢 ᴛᴇʟᴇᴛʜᴏɴ : v.{version.__version__}                ㅤㅤ  \n"
        f"💢 ᴘʏᴛʜᴏɴ. : v.{python_version()} ㅤㅤ\n"
        f"💢 ʙᴏᴛ : v.{BOT_VER}                ㅤㅤㅤ \n"
        f"💢 ᴍᴏᴅᴜʟᴇ : {len(modules)} ㅤㅤㅤㅤㅤㅤㅤ   \n"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(200)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`The provided logo is invalid."
                "\nMake sure the link is directed to the logo picture`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()

@register(outgoing=True, pattern="^.aliveu")
async def amireallyaliveuser(username):
    """For .aliveu command, change the username in the .alive command."""
    message = username.text
    output = ".aliveu [new username] tidak boleh kosong"
    if not (message == ".aliveu" and message[7:8] != " "):
        newuser = message[8:]
        global DEFAULTUSER  # global statement
        DEFAULTUSER = username
        output = "Successfully changed user to " + newuser + "!"
    await username.edit("`" f"{output}" "`")


@register(outgoing=True, pattern=r"^\.resetalive$")
async def amireallyalivereset(ureset):
    global DEFAULTUSER  # global statement
    DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
    await ureset.edit("`" "Successfully reset user for alive!" "`")



CMD_HELP.update(
    {
        "alive": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.alive` or `.on` or `zhu`"
        "\n↳ : To see whether your bot is working or not."
        "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.aliveu` <text>"
        "\n↳ : Changes the 'user' in alive to the text you want."
        "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.restalive`"
        "\n↳ : Resets the user to default."
