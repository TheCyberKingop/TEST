import random
from . import *

xd = ["Your message has been read and Ignored successfully ┐(´∀｀)┌","Umm My Ears Were Shut 🙉"]

@bot.on(admin_cmd(pattern="ignore$"))
async def _(event):
  rd = random.choice(xd)
  await eor(event, rd)
 
 
@bot.on(admin_cmd(pattern="cantignore$") 
async def _(event):
  await eor(event, "In Mind: **Im Trying To Ignore But I Cant (ｰ ｰ;)**")
  
  
  CmdHelp("ignore").add_commans(
  'ignore', None, 'Use and See'
 ).add_command(
 'cantignore', None, 'Use and See'
 ).add()
