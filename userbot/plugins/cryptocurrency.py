"""
✘ Commands Available
• `{i}cp <cryptocurrency>`
    Gives Price Of Cryptocurrency.
• `{i}cgas`
    Gives Gas Of Eth Cryptocurrency.
• `{i}ccalc <cryptocurrency>`
    Calculates Cryptocurrency.
    Eg: .calc eth 200
• `{i}cindex`
    Gives Index Of Cryptocurrency.
• `{i}cdefi`
    Gives Defi Of Cryptocurrency.
• `{i}ccap <cryptocurrency>`
    Gives MartketCap.
• `{i}clink <cryptocurrency>`
    Gives Official SocialMedia Links/Links Of Cryptocurrency.
• `{i}cvol <cryptocurrency>`
    Gives Vol Of Cryptocurrency.
• `{i}cgoogle <cryptocurrency>`
    Gives GoogleTrend Of Cryptocurrency.
Made By @Legend_Mr_Hacker
"""

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from . import *


admin_cmd(pattern="cp(.*)$")
async def demn(ult):
    input = ult.pattern_match.group(1)
    chat = "@Cryptowhalebot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=331761115))
            await ult.client.send_message(chat, f"/p {input}")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @Cryptowhalebot")    
            return
        x = response.text
        z = x.split("\n")[(len(x.split("\n")))-1]
        await eor(ult, x.replace(z,""))

admin_cmd(pattern="cgas(.*)$")
async def demn(ult):
    input = ult.pattern_match.group(1)
    chat = "@Cryptowhalebot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=331761115))
            await ult.client.send_message(chat, f"/gas {input}")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @Cryptowhalebot")    
            return
        x = response.text
        z = x.split("\n")[(len(x.split("\n")))-1]
        await eor(ult, x.replace(z,""))


admin_cmd(pattern="ccalc(.*)$")
async def demn(ult):
    input = ult.pattern_match.group(1)
    chat = "@Cryptowhalebot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=331761115))
            await ult.client.send_message(chat, f"/calc {input}")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @Cryptowhalebot")    
            return
        x = response.text
        z = x.split("\n")[(len(x.split("\n")))-1]
        await eor(ult, x.replace(z,""))

admin_cmd(pattern="cindex$")
async def demn(ult):
    chat = "@Cryptowhalebot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=331761115))
            await ult.client.send_message(chat, f"/index")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @Cryptowhalebot")    
            return
        x = response.text
        z = x.split("\n")[(len(x.split("\n")))-1]
        await eor(ult, x.replace(z,""))


admin_cmd(pattern="cdefi$")
async def demn(ult):
    chat = "@Cryptowhalebot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=331761115))
            await ult.client.send_message(chat, f"/defi")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @Cryptowhalebot")    
            return
        x = response.text
        await eor(ult, x)


admin_cmd(pattern="ccap(.*)$")
async def demn(ult):
    input = ult.pattern_match.group(1)
    chat = "@Cryptowhalebot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=331761115))
            await ult.client.send_message(chat, f"/cap {input}")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @Cryptowhalebot")    
            return
        x = response.text
        z = x.split("\n")[(len(x.split("\n")))-1]
        await ult.reply(x.replace(z,""), file=response.media)


admin_cmd(pattern="clink(.*)$")
async def demn(ult):
    input = ult.pattern_match.group(1)
    chat = "@Cryptowhalebot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=331761115))
            await ult.client.send_message(chat, f"/link {input}")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @Cryptowhalebot")    
            return
        x = response.text
        await eor(ult, x)


admin_cmd(pattern="cvol(.*)$")
async def demn(ult):
    input = ult.pattern_match.group(1)
    chat = "@Cryptowhalebot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=331761115))
            await ult.client.send_message(chat, f"/vol {input}")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @Cryptowhalebot")    
            return
        x = response.text
        z = x.split("\n")[(len(x.split("\n")))-1]
        await eor(ult, x.replace(z,""))


admin_cmd(pattern="cgoogle(.*)$")
async def demn(ult):
    input = ult.pattern_match.group(1)
    chat = "@Cryptowhalebot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=331761115))
            await ult.client.send_message(chat, f"/google {input}")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @Cryptowhalebot")    
            return
        x = response.text
        z = x.split("\n")[(len(x.split("\n")))-1]
        await ult.reply(input, file=response.media)
CmdHelp("CryptoCurrency").add_command(
"cp",None, "Use and See"
).add_command(
"cgas",None, "Use and See"
).add_command(
"ccalc",None, "Use and See"
).add_command(
"cindex",None, "Use and See"
).add_command(
"cdefi",None, "Use and See"
).add_commnad(
"ccap",None, "Use andSee"
).add_command(
"clink",None, "Use and See"
).add()