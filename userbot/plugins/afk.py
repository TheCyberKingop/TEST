# by uniborg...Thanks @Legend_Mr_Hacker
# Now will be used in LEGENDlBOT too....
import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types
from userbot import CMD_HELP
from userbot import ALIVE_NAME, LEGENDversion
from LEGENDBOT.utils import admin_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"

LEGEND = bot.uid


global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    came_back = datetime.now()
    afk_end = came_back.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        LEGENDBOT = await borg.send_message(
            event.chat_id,
            "đĨđđĒđŦđ´ đđĩđ˛đŋđŽ!\n**đđŦ đđŦđĢđ¤đĸđ¯ đđŖđ¨.**\nâąī¸ `ÕĄÎąs ÎąÕĸk for:``"
            + total_afk_time
            + "`", file=LEGENDpic
        )
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "#AFKFALSE \nSet AFK mode to False\n"
                + "đĨđđĒđŦđ´ đđĩđ˛đŋđŽ!\n**đđŦ đđŦđĢđ¤đĸđ¯ đđŖđ¨.**\nâąī¸ `ÕĄÎąs ÎąÕĸk for:``"
                + total_afk_time
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` "
                + "for the proper functioning of afk functionality "
                + "Ask in @Legend_Mr_Hacker to get help setting this value\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        await asyncio.sleep(5)
        await LEGENDBOT.delete()
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    cum_back = datetime.now()
    afk_end = cum_back.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None
        
        message_to_reply = (
            f"ââ¯đ đŽđžđ / âŗđžđđđ¤!! Éąá§ âÎĩÉ ÎĩÉŗâ ÉąÎąā¸ŖÆ­ÎĩÉž [{DEFAULTUSER}](tg://user?id={LEGEND}) ÎšŅ Ī˛ĪŅŅŅĐ¸ĪâÎŗ ÎŋÆÆâÎšŅ... sÃ­Õ˛cŌŊ ÕĄÕ°ŌŊÕ˛? `{total_afk_time}`\n"
            + f"\n\nđđŊđđđđđđ :-\n`{reason}`"
  if reason
            else f"ââ¯đ đŽđžđ / âŗđžđđđ¤!\nÎš ÎąĐŧ Ī˛ĪŅŅŅĐ¸ĪâÎŗ ĪĐ¸ÎąÎŊÎąÎšâÎąĪâŅđ. Îš ŅŅĪâÎŗ Ī ÎąÆĪŅŅ Ī˛ÎŋĐŧŅ ĪÎąĪ˛ÎēÎŋĐ¸âÎšĐ¸Ņ.\n__Since when, you ask? From__ `{total_afk_time}`\nI'll be back when I feel to comeđļđ"
        )
        msg = await event.reply(message_to_reply, file=LEGENDpic)
        await asyncio.sleep(2)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602


@borg.on(admin_cmd(pattern=r"afk (.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    aura = await event.get_reply_message()
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    global reason
    global LEGENDpic
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    LEGENDpic = await event.client.download_media(aura)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason} {LEGENDpic}"  # pylint:disable=E0602
        if reason:
            await borg.send_message(
                event.chat_id, f"Îš'Đŧ gÎŋÎšĐ¸g ÎąÆÎēđļ \nâī¸ đŊđđđđđ `{reason}`", file=LEGENDpic
            )
        else:
            await borg.send_message(event.chat_id, f"Îš'Đŧ gÎŋÎšĐ¸g ÎąÆÎē !đļ", file=LEGENDpic)
        await asyncio.sleep(0.001)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                f"#AFKTRUE \nSet AFK mode to True, and Reason is {reason}",file=LEGENDpic
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


CmdHelp("afk").add_command(
  'afk', '<reply to media>/<or type a reson>', 'Marks you AFK(Away from Keyboard) with reason(if given) also shows afk time. Media also supported.'
).add()
