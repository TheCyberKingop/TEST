# Thanks to @PYTHON_CODER_SRINIVAS.. 
# animation Idea by @PYTHON_CODER_SRINIVAS
# Made by @PYTHON_CODER_SRINIVAS...and thanks to @PYTHON_CODER_SRINIVAS...the logos...
# Kang with credits else gay...
import asyncio
import random
from telethon import events
from LEGENDBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"

# Thanks to LEGEND BRO.. 
# animation Idea by @PYTHON_CODER_SRINIVAS (op coder)
# Made by @PYTHON_CODER_SRINIVAS...and thanks to @koi_nhi_apna for the logos...
# Kang with credits else gay...
# alive.py for

edit_time = 5
""" =======================CONSTANTS====================== """
file1="https://telegra.ph/file/2d41a6b1b3713579c63c2.jpg"
file2="https://telegra.ph/file/d80f4df893d30ed11ec87.jpg"
file3="https://telegra.ph/file/498446e602ba527c5ee3a.jpg"
file4="https://telegra.ph/file/22d0976cc9c7627d48319.jpg"""" =======================CONSTANTS====================== """
pm_caption = "γπ±π± πͺ π¬ πͺ π³ π© π±γ Is OP\n\n"
pm_caption += "ππ **ππ¨π,πππ πππ ππππππππ , πππ ππΊππΎ πΌπΊππΎ ππΏ ππ π»πΎππππΎ .. πππππππ πππ ππΎππ πππΌππ«π.**ππ\n\n"
pm_caption += "ΰΌΰΌππΉAbout Me \n\n"
pm_caption += "π«π«**my assistant**π«π« >>γ 15.0.0\n"
pm_caption += "ππ**LEGEND HERE**ππ   >>γ [OWNER](https://t.me/Legend_Mr_Hacker)\n"
pm_caption += f"π°π°**α΄α΄sα΄α΄Κ**π°π°  >>γ {DEFAULTUSER}\n"
pm_caption += "β£β£ **α΄Κα΄α΄α΄α΄Κ**β£β£ >>γ [CREATOR](https://t.me/Legend_Mr_Hacker)\n\n"
pm_caption += "ππ **LEGEND FEDS**ππ  >>γ [FEDS](https://t.me/Legend_Mr_Feds)\n\n"
pm_caption += "[....βββββββββ\n....βββββββββ\n.......ββββ£πΉπ«ππ«πΉβ£ββββ\n...............βββ\n](https://t.me/Legend_Mr_Hacker)\n\n"
@borg.on(admin_cmd(pattern=r"op"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
    CmdHelp("op").add_command(
      'op', None , 'BEST alive command'
).add()
