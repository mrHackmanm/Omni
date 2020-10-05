import discord
import os
import matplotlib.pyplot as plt
import numpy as np
import time
import random
import requests
import wikipedia
import html.parser
import asyncio
from commands import curse_words

from commands import urbandictionary as ud
from commands import calculator
from keep_alive import keep_alive

client = discord.Client()
money_list = {}
prefix_list = {}
roshambo_list = {}
cooldown = {}
swear_disabled = {}
nou_list = {}
dadmode_list = {}
onesec_list = {}
info_list = {}
trivia_wins = {}
time_a = {}
time_b = {}
flip_list = ["heads", "tails"]
eightball_list = ["It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def command_check(m, x):
  for i in x:
    if m.lower().startswith(i):
      return True

@client.event
async def on_ready():     
  await client.change_presence(game=discord.Game(name=".help"))

@client.event
async def on_message(message):
  try:
    prefix = prefix_list[message.author.server.id]
  except:
    prefix = "."

  if message.author.bot:
    return

  if command_check(message.content, [curse_words.curse_words]):
    if message.content.startswith(prefix):
      return
    try:
      if swear_disabled[message.author.server.id] == True:
        await client.send_message(message.channel, "No swearing! :rage:")
        try:
          await client.delete_message(message)
        except:
          await client.send_message(message.channel, ":( I couldn't remove the offending message because I don't have the `Manage Messages`")
    except:
      return

  if command_check(message.content, ["i'm ", "im "]):
    if command_check(message.content, ["im "]):
      try:
        if dadmode_list[message.author.server.id] == True:
          return
        else:
          x = message.content[3: ]
        msg = "Hi " + x + ", I'm dad"
      except:
        x = message.content[3: ]
        msg = "Hi " + x + ", I'm dad"
    else :
      try:
        if dadmode_list[message.author.server.id] == True:
          return
        else:
          x = message.content[4: ]
        msg = "Hi " + x + ", I'm dad"
      except:
        x = message.content[4: ]
        msg = "Hi " + x + ", I'm dad"
    await client.send_message(message.channel, msg)
  
  elif command_check(message.content, ["no u"]):
    try:
      if nou_list[message.author.server.id] == True:
        return
      else:
        await client.send_message(message.channel, "no u")
    except:
      await client.send_message(message.channel, "no u")

  elif command_check(message.content, ["one sec"]):
    try:
      if onesec_list[message.author.server.id] == True:
        return
      else:
        await client.send_message(message.channel, "it's been a second")
    except:
      await client.send_message(message.channel, "it's been a second")

  elif message.content.lower().startswith("{}help".format(prefix)):
    if message.content.lower().strip() == "{}help".strip().format(prefix):
      embed = discord.Embed(title="Command Catagories", colour=discord.Colour(0x4a90e2))
      embed.set_footer(text="Made by Cloud9c with ❤️", icon_url="https://avatars0.githubusercontent.com/u/19523195?s=400&v=4")
      embed.add_field(name=":tools: Utility", value="`{}help utility`".format(prefix), inline=True)
      embed.add_field(name=":gear: Config", value="`{}help config`".format(prefix), inline=True)
      embed.add_field(name=":moneybag: Currency", value="`{}help currency`".format(prefix), inline=True)
      embed.add_field(name=":smile: Fun", value="`{}help fun`".format(prefix), inline=True)
      embed.add_field(name=":hammer: Moderation", value="`{}help moderation`".format(prefix), inline=True)
      embed.add_field(name=":information_source: Math", value="`{}help math`".format(prefix), inline=True)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help config".format(prefix)]):
      embed = discord.Embed(title=":gear: Config", colour=discord.Colour(0x4a90e2), description="noswears, no-u, dad-mode, one-sec, info, info-edit\n\ndo `{}help [command]` for information on a specific command".format(prefix))
      embed.set_footer(text="use '{}' before every command!".format(prefix))
      await client.send_message(message.channel, embed=embed)

    elif command_check(message.content, ["{}help currency".format(prefix)]):
      embed = discord.Embed(title=":moneybag: Currency", colour=discord.Colour(0x4a90e2), description="work, balance, gamble, share\n\ndo `{}help [command]` for information on a specific command".format(prefix))
      embed.set_footer(text="use '{}' before every command!".format(prefix))
      await client.send_message(message.channel, embed=embed)

    elif command_check(message.content, ["{}help math".format(prefix)]):
      embed = discord.Embed(title=":information_source: Math Commands", colour=discord.Colour(0x4a90e2), description="calc, plot, python\n\ndo `{}help [command]` for information on a specific command".format(prefix))
      embed.set_footer(text="use '{}' before every command!".format(prefix))
      await client.send_message(message.channel, embed=embed)

    elif command_check(message.content, ["{}help utility".format(prefix)]):
      embed = discord.Embed(title=":tools: Utility Commands", colour=discord.Colour(0x4a90e2), description="ping, choose, flip, roll, color, wikipedia, timer\n\ndo `{}help [command]` for information on a specific command".format(prefix))
      embed.set_footer(text="use '{}' before every command!".format(prefix))
      await client.send_message(message.channel, embed=embed)

    elif command_check(message.content, ["{}help moderation".format(prefix)]):
      embed = discord.Embed(title=":hammer: Moderation Commands", colour=discord.Colour(0x4a90e2), description="clear, prefix, kick, ban\n\ndo `{}help [command]` for information on a specific command".format(prefix))
      embed.set_footer(text="use '{}' before every command!".format(prefix))
      await client.send_message(message.channel, embed=embed)
    
    elif command_check(message.content, ["{}help fun".format(prefix)]):
      embed = discord.Embed(title=":smile: Fun Commands", colour=discord.Colour(0x4a90e2), description="say, 8ball, roshambo, pun, xkcd, gif, oatmeal, urban, howcool, trivia\n\ndo `{}help [command]` for information on a specific command".format(prefix))
      embed.set_footer(text="use '{}' before every command!".format(prefix))
      await client.send_message(message.channel, embed=embed)  

#specific-help
    elif command_check(message.content, ["{}help python".format(prefix), "{}help py".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "evaluates python code (and spits the results)".format(prefix),inline = False)
      embed.add_field(name = "Usage", value = "`{}python [code]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "python, py", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help gamble".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Gamble your money away!".format(prefix),inline = False)
      embed.add_field(name = "Usage", value = "`{}gamble [amount]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "balance", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help balance".format(prefix), "{}help bal".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "See your balance (or tag a user to see theirs)".format(prefix),inline = False)
      embed.add_field(name = "Usage", value = "`{}balance [user]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "balance, bal", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help work".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Work a job and earn a random amount between 1 and 100 coins".format(prefix),inline = False)
      embed.add_field(name = "Usage", value = "`{}work`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "work", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help timer".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Set a timer in seconds, minutes or hours".format(prefix),inline = False)
      embed.add_field(name = "Usage", value = "`{}trivia`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "trivia", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help trivia".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Challenge yourself with a trivia question (use {}info to check your wins)".format(prefix),inline = False)
      embed.add_field(name = "Usage", value = "`{}trivia`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "trivia", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help howcool".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Tells you how cool someone is",inline = False)
      embed.add_field(name = "Usage", value = "`{}howcool [someone]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "howcool", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help info".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "A facebook-esque customisable page which shows a user's stats",inline = False)
      embed.add_field(name = "Usage", value = "`{}info [@user]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "info", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help info-edit".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Customize your description in `{}info` (350 character limit)".format(prefix),inline = False)
      embed.add_field(name = "Usage", value = "`{}info-edit [custom description]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "info-edit", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help dad-mode".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Disable/enable the dad-mode autoresponse in the server",inline = False)
      embed.add_field(name = "Usage", value = "`{}dad-mode`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "dad-mode", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help no-u".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Disable/enable the \"no u\" autoresponse in the server",inline = False)
      embed.add_field(name = "Usage", value = "`{}no-u`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "no-u", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help one-sec".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Disable/enable the \"one sec\" autoresponse in the server",inline = False)
      embed.add_field(name = "Usage", value = "`{}one-sec`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "one-sec", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help noswears".format(prefix), "{}help noswear".format(prefix), "{}help sweartoggle".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Disable/enable swearing in the server",inline = False)
      embed.add_field(name = "Usage", value = "`{}noswears`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "noswears, noswear, sweartoggle", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help urban".format(prefix), "{}help urbandictionary".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Find every slang in the world using Urban Dictionary",inline = False)
      embed.add_field(name = "Usage", value = "`{}urban [search term]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "urban, urbandictionary", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help wikipedia".format(prefix), "{}help wiki".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Provides a summarized wikipedia page of your search term",inline = False)
      embed.add_field(name = "Usage", value = "`{}wikipedia [search term]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "wikipedia, wiki", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help oatmeal".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "A random webcomic from The Oatmeal",inline = False)
      embed.add_field(name = "Usage", value = "`{}oatmeal`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "oatmeal", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help gif".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Search for a GIF on giphy.com",inline = False)
      embed.add_field(name = "Usage", value = "`{}gif [search term]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "gif, giphy", inline = False)
      await client.send_message(message.channel, embed = embed) 

    elif command_check(message.content, ["{}help xkcd".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "A random webcomic from XKCD",inline = False)
      embed.add_field(name = "Usage", value = "`{}xkcd`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "xkcd", inline = False)
      await client.send_message(message.channel, embed = embed) 

    elif command_check(message.content, ["{}help roshambo".format(prefix), "{}help rps".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Play Rock-Paper-Scissors against me (use {}info to check your score)",inline = False)
      embed.add_field(name = "Usage", value = "`{}roshambo [rock, paper or scissors]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "roshambo, rps", inline = False)
      await client.send_message(message.channel, embed = embed)
      
    elif command_check(message.content, ["{}help say".format(prefix), "{}help echo".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Repeats whatever you say",inline = False)
      embed.add_field(name = "Usage", value = "`{}say [something]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "say, echo", inline = False)
      await client.send_message(message.channel, embed = embed)       

    elif command_check(message.content, ["{}help calc".format(prefix), "{}help calculate".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Calculate some stuff (add +, subtract -, multiply *, divide /, square ^)",inline = False)
      embed.add_field(name = "Usage", value = "`{}calc [hard math]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "calc, calculate", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help plot".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Make a graph in your DM",inline = False)
      embed.add_field(name = "Usage", value = "`{}plot`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "plot", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help ping".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Check Omni's response time",inline = False)
      embed.add_field(name = "Usage", value = "`{}ping`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "ping", inline = False)
      await client.send_message(message.channel, embed = embed)    

    elif command_check(message.content, ["{}help clear".format(prefix), "{}help clean".format(prefix), "{}help purge".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Clear 10 messages, or however many you specify",inline = False)
      embed.add_field(name = "Usage", value = "`{}clear [amount]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "clear, clean, purge", inline = False)
      await client.send_message(message.channel, embed = embed)  

    elif command_check(message.content, ["{}help choose".format(prefix), "{}help random".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Help randomly choose something for you",inline = False)
      embed.add_field(name = "Usage", value = "`{}choose [item 1], [item 2], etc.`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "choose, random", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help 8ball".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "The 8-Ball reaches into the future, to find the answers to your questions",inline = False)
      embed.add_field(name = "Usage", value = "`{}8ball`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "8ball", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help prefix".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Change Omni's prefix",inline = False)
      embed.add_field(name = "Usage", value = "`{}prefix [prefix of your choice]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "prefix", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help kick".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Warning: this will kick your target if the bot has the correct permissions",inline = False)
      embed.add_field(name = "Usage", value = "`{}kick [@user]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "kick", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help ban".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Warning: this will ban your target if the bot has the correct permissions",inline = False)
      embed.add_field(name = "Usage", value = "`{}ban [@user]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "ban", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help flip".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Flip a coin (heads or tails)",inline = False)
      embed.add_field(name = "Usage", value = "`{}flip`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "flip", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help roll".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Roll a 6-sided die, or however many sides you provide",inline = False)
      embed.add_field(name = "Usage", value = "`{}roll [number of sides]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "roll", inline = False)
      await client.send_message(message.channel, embed = embed)

    elif command_check(message.content, ["{}help color".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "Visualize and translate any hex/rgb color",inline = False)
      embed.add_field(name = "Usage", value = "`{}color [hex or RGB]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "color", inline = False)
      await client.send_message(message.channel, embed = embed)  

    elif command_check(message.content, ["{}help dadjoke".format(prefix), "{}help pun".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "A dad joke... A pun... What's the difference?",inline = False)
      embed.add_field(name = "Usage", value = "`{}pun`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "pun, dadjoke", inline = False)
      await client.send_message(message.channel, embed = embed)  

    elif command_check(message.content, ["{}help share".format(prefix), "{}help give".format(prefix)]):
      embed = discord.Embed(colour = discord.Colour(0x4a90e2))
      embed.add_field(name = "Description", value = "share some coins with someone",inline = False)
      embed.add_field(name = "Usage", value = "`{}share [user] [amount]`".format(prefix), inline = False)
      embed.add_field(name = "Aliases", value = "share, give", inline = False)
      await client.send_message(message.channel, embed = embed)   
  #commands
  elif command_check(message.content, ["{}share".format(prefix), "{}give".format(prefix)]):
    if message.content.lower().startswith("{}share".format(prefix)):
      x = message.content[5 + len(prefix):].strip()
    else:
      x = message.content[4 + len(prefix):].strip()
    if not x:
      await client.send_message(message.channel, "Enter how much you want to give, and tag who you are giving to\nExample: `{}give [user] 10`".format(prefix))
      return
    x = x.replace("  ", " ")
    x = x.split(" ")
    x = sorted(x, reverse=False)
    amount = x[0]
    amount = int(amount)
    person = x[1]
    person = person.replace("<", "")
    person = person.replace("!", "")
    person = person.replace("@", "")
    person = person.replace(">", "")
    if money_list.get(person) == None:
      money_list[person] = 0
    if amount < 1:
      await client.send_message(message.channel, "You have to share more than zero! Don't try to break me plz :(".format(prefix))
      return      
    try:
      if amount > money_list[message.author.id]:
        await client.send_message(message.channel, "You only have **{}** coins".format(money_list[message.author.id]))
      else:
        money_list[message.author.id] = money_list[message.author.id] - amount
        money_list[person] = money_list[person] + amount
        await client.send_message(message.channel, "You gave {0} {1}, now you have {2} and they've got {3}".format(message.server.get_member(person).display_name, amount, money_list[message.author.id], money_list[person]))
    except KeyError:
      await client.send_message(message.channel, "You have **0** coins".format(prefix))

  elif command_check(message.content, ["{}python".format(prefix), "{}py".format(prefix)]):
    if message.content.lower().startswith("{}python".format(prefix)):
      x = message.content[6 + len(prefix):].strip()
    else:
      x = message.content[2 + len(prefix):].strip()
    if not x:
      await client.send_message(message.channel, "There's no code to evaluate!")
      return
    try:
      y = eval(x)
      await client.send_message(message.channel, "``` {}```".format(y))
    except Exception as e: 
      await client.send_message(message.channel, "``` ERROR: {}```".format(e))

  elif command_check(message.content, ["{}gamble".format(prefix), "{}bet".format(prefix)]):
    if message.content.lower().startswith("{}gamble".format(prefix)):
      x = message.content[6 + len(prefix):].strip()
    else:
      x = message.content[3 + len(prefix):].strip()
    try:
      balance = money_list[message.author.id]
    except:
      await client.send_message(message.channel, "You have no coins to bet!")
      return
    if not x:
      await client.send_message(message.channel, "You have to gamble something!\nExample: `{}gamble `#/all/half`")
      return
    elif x == "all":
      gamble_amount = balance
    elif x == "half":
      gamble_amount = round(balance/2)
    elif x.isdigit() == False:
      await client.send_message(message.channel, "You have to bet an actual number!")
      return
    elif int(x) == 0:
      await client.send_message(message.channel, "You have to gamble a number greater than zero!")
      return
    else:
      gamble_amount = int(x)
    flip = random.randint(0, 1)
    if flip == 0:
      await client.send_message(message.channel, "You lost **{}** coins...".format(gamble_amount))
      money_list[message.author.id] = money_list[message.author.id] - gamble_amount
    else:
      percent = random.randint(0, 150)
      win_percent = 1 + (percent/100)
      loot = round(gamble_amount * win_percent)
      await client.send_message(message.channel, "You won **{0}**\nPercent of bet won: **{1}%**".format(loot, percent))
      money_list[message.author.id] = money_list[message.author.id] + loot

  elif command_check(message.content, ["{}bal".format(prefix), "{}balance".format(prefix)]):
    if message.content.lower().startswith("{}balance".format(prefix)):
      x = message.content[7 + len(prefix):].strip()
    else:
      x = message.content[3 + len(prefix):].strip()
    if not x:
      try:
        balance = money_list[message.author.id]
      except:
        balance = 0
      name = message.server.get_member(message.author.id).display_name
    else:
      x = x.replace("<", "")
      x = x.replace("@", "")
      x = x.replace("!", "")
      x = x.replace(">", "")  
      try:     
        balance = money_list.get[x]
      except:
        balance = 0
      try:
        name = message.server.get_member(x).display_name
      except:
        try:
          balance = money_list[message.author.id]
        except:
          balance = 0
        name = message.server.get_member(message.author.id).display_name

    embed = discord.Embed(title="{}'s balance:".format(name), colour=discord.Colour(0x4a90e2), description="{} coins".format(balance))
    await client.send_message(message.channel, embed=embed)

  elif command_check(message.content, ["{}work".format(prefix)]):
    try:
      if cooldown[message.author.id] > 0:
        if cooldown[message.author.id] > 60:
          visible = round(cooldown[message.author.id]/60)
          if visible > 1:
            grammar = "minutes"
          else:
            round(cooldown[message.author.id])
            grammar = "minute"
        else:
          visible = cooldown[message.author.id]
          grammar = "seconds"
        embed = discord.Embed(title="Slow down!", colour=discord.Colour(0x4a90e2), description="You have to wait {0} {1} before you can work again!".format(visible, grammar))
        await client.send_message(message.channel, embed=embed)
        return
    except:
      pass
    if message.author.id not in money_list:
      money_list[message.author.id] = 0
    x = random.randint(1, 100)
    money_list[message.author.id] = money_list[message.author.id] + x
    if x < 10:
      y = ["beggar"]
    elif x < 20:
      y = ["janitor", "bus driver", "construction worker", "butcher"]
    elif x < 30:
      y = ["mechanic", "head chef", "mail carrier", "librarian"]
    elif x < 40:
      y = ["accountant", "nurse", "psychologist", "police officer"]
    elif x < 50:
      y = ["software developer", "veterinarian", "civil engineer", "business analyst"]
    elif x < 60:
      y = ["lawyer", "pharmacist", "air traffic controller"]
    elif x < 70:
      y = ["manager", "judge", "astronaut", "singer"]
    elif x < 80:
      y = ["surgeon", "criminal", "photographer", "youtuber"]
    elif x < 90:
      y = ["chief executive", "pediatrician", "orthodontist", "stock manager"]
    else:
      y = ["doctor", "CEO", "president", "life coach"]
    y = random.choice(y)
    embed = discord.Embed(title="{0} worked as a **{1}** for an hour...".format(message.server.get_member(message.author.id).display_name, y), colour=discord.Colour(0x4a90e2), description="You earned **{}** coins!".format(x))
    await client.send_message(message.channel, embed=embed)

  elif command_check(message.content, ["{}timer".format(prefix)]):
    try:
      if message.content[5 + len(prefix)] != " ":
        return
      x = message.content[6 + len(prefix):].strip()
    except:
      await client.send_message(message.channel, "Set an amount in `sec`, `hour`, `min`!\nExample: `{}timer 5 sec`".format(prefix))
      return
    y = ''.join(i for i in x if i.isdigit())
    if "sec" in x:
      await client.send_message(message.channel, "A timer is set for `{}` seconds".format(y))
      await asyncio.sleep(int(y))
    elif "min" in x:
      await client.send_message(message.channel, "A timer is set for `{}` minutes".format(y))
      await asyncio.sleep(int(y)*60)
    elif "hour" in x:
      await client.send_message(message.channel, "A timer is set for `{}` hours".format(y))
      await asyncio.sleep(int(y)*3600)
    else:
      await client.send_message(message.channel, "Set an amount in `sec`, `hour`, `min`!\nExample: `{}timer 5 sec`".format(prefix))
      return      
    await client.send_message(message.channel, "<@{}>, time is up!".format(message.author.id))

  elif command_check(message.content, ["{}trivia".format(prefix)]):
    r = requests.get('https://opentdb.com/api.php?amount=1')
    r.raise_for_status()
    trivia = r.json()['results'][0]

    question = html.parser.HTMLParser().unescape(trivia.get("question"))
    difficulty = html.parser.HTMLParser().unescape(trivia.get("difficulty"))
    category = html.parser.HTMLParser().unescape(trivia.get("category"))
    ans1 = html.parser.HTMLParser().unescape(trivia.get("correct_answer"))
    ans2 = html.parser.HTMLParser().unescape(trivia.get("incorrect_answers")[0])
    try:
      ans3 = html.parser.HTMLParser().unescape(trivia.get("incorrect_answers")[1])
      ans4 = html.parser.HTMLParser().unescape(trivia.get("incorrect_answers")[2])
      y = [ans1, ans2, ans3, ans4]
      random.shuffle(y)
      x = "1) {0}\n2) {1}\n3) {2}\n4) {3}".format(y[0], y[1], y[2], y[3])
    except:
      y = [ans1, ans2]
      random.shuffle(y)
      x = "1) {0}\n2) {1}".format(y[0], y[1])
    embed = discord.Embed(colour=discord.Colour(0x4a90e2),
    title="**{}**".format(question),
    description="*Please choose an answer within 25s*")
    embed.set_author(name="{}'s question:".format(message.server.get_member(message.author.id).display_name))
    embed.set_footer(text="Provided by Open Trivia DB")
    embed.add_field(name="Choose one of the following:", value=x, inline=False)
    embed.add_field(name="Difficulty", value="`{}`".format(difficulty), inline=True)
    embed.add_field(name="Category", value="`{}`".format(category), inline=True)
    await client.send_message(message.channel, embed=embed)
    response = await client.wait_for_message(author=message.author, timeout=25)
    x = y.index(ans1)
    try:
      if response.content != str(x + 1):
        msg = "Incorrect! The answer was `{}`".format(ans1)
      elif response.content == str(x + 1):
        msg = "Correct! (+1 win)"
        try:
          trivia_wins[message.author.id] = trivia_wins[message.author.id] + 1
        except:
          trivia_wins[message.author.id] = 1
    except:
      msg = "Oops! You didn't answer in time"
    await client.send_message(message.channel, msg)


  elif command_check(message.content, ["{}howcool".format(prefix)]):
    try:
      if message.content[7 + len(prefix)] != " ":
        return
      x = message.content[8 + len(prefix):].strip()
    except:
      x = message.content[8 + len(prefix):].strip()
    if not x:
      name = "You"
      grammar = "are"
    else:
      name = x
      grammar = "is"
    percentage = random.randint(0, 100)
    if percentage < 25:
      emoji = ":nerd:"
    elif percentage < 50:
      emoji = ":expressionless: "
    elif percentage < 75:
      emoji = ":smirk: "
    else:
      emoji = ":sunglasses:"
    embed = discord.Embed(title="Coolness Machine", colour=discord.Colour(0x4a90e2), description="{0} {1} {2}% cool {3}".format(name, grammar, percentage, emoji))
    await client.send_message(message.channel, embed=embed)

  elif command_check(message.content, ["{}dad-mode".format(prefix)]):
    if message.author.server_permissions.manage_messages:
      try:
        if dadmode_list[message.author.server.id] == True:
          dadmode_list[message.author.server.id] = False
          msg = ":smile: Dad-mode is now enabled"
        else:
          dadmode_list[message.author.server.id] = True
          msg = ":cry: Dad-mode is now disabled"
      except:
        dadmode_list[message.author.server.id] = True
        msg = ":cry: Dad-mode is now disabled"
    else:
      msg = "You are missing the `Manage Messages` permissions"
    await client.send_message(message.channel, msg)
    
  elif command_check(message.content, ["{}one-sec".format(prefix)]):
    if message.author.server_permissions.manage_messages:
      try:
        if onesec_list[message.author.server.id] == True:
          onesec_list[message.author.server.id] = False
          msg = ":smile: One-sec is now enabled"
        else:
          onesec_list[message.author.server.id] = True
          msg = ":cry: One-sec is now disabled"
      except:
        onesec_list[message.author.server.id] = True
        msg = ":cry: One-sec is now disabled"
    else:
      msg = "You are missing the `Manage Messages` permissions"
    await client.send_message(message.channel, msg)

  elif command_check(message.content, ["{}no-u".format(prefix)]):
    if message.author.server_permissions.manage_messages:
      try:
        if nou_list[message.author.server.id] == True:
          nou_list[message.author.server.id] = False
          msg = ":smile: No-u is now enabled"
        else:
          nou_list[message.author.server.id] = True
          msg = ":cry: No-u is now disabled"
      except:
        nou_list[message.author.server.id] = True
        msg = ":cry: No-u is now disabled"
    else:
      msg = "You are missing the `Manage Messages` permissions"
    await client.send_message(message.channel, msg)

  elif command_check(message.content, ["{}noswears".format(prefix), "{}noswear".format(prefix), "{}sweartoggle".format(prefix)]):
    if message.author.server_permissions.manage_messages:
      try:     
        if swear_disabled[message.author.server.id] == False:
          swear_disabled[message.author.server.id] = True
          msg = ":sunglasses: Swearing is now disabled in this server!"
        elif swear_disabled[message.author.server.id] == True:
          swear_disabled[message.author.server.id] = False
          msg = ":rage: Swearing is now allowed in this server!"
      except:
        swear_disabled[message.author.server.id] = True
        msg = ":sunglasses: Swearing is now disabled in this server!"
    else:
      msg = "You are missing the `Manage Messages` permissions"
    await client.send_message(message.channel, msg)
     
  elif command_check(message.content, ["{}urban".format(prefix), "{}urbandictionary".format(prefix)]):
    if message.author.server.id == "437048931827056642":
      return
    try:
      if message.content.startswith("{}urbandictionary".format(prefix)):
        if message.content[15 + len(prefix)] != " ":
          return
        x = message.content[16 + len(prefix):].strip()
      else:
        if message.content[5 + len(prefix)] != " ":
          return
        x = message.content[6 + len(prefix):].strip()        
    except:
      if message.content.startswith("{}giphy".format(prefix)):
        await client.send_message(message.channel, "What do you want to search on Urban Dictionary???\nExample: `{}urban koolaid`")
        return
      else:
        await client.send_message(message.channel, "What do you want to search on Urban Dictionary???\nExample: `{}urban koolaid`")
        return
    definition = str(ud.define(x)[0].definition)
    example = ud.define(x)[0].example
    word = "Definition of "+ ud.define(x)[0].word
    downvote = ud.define(x)[0].downvotes
    upvote = ud.define(x)[0].upvotes

    embed = discord.Embed(title=word, colour=discord.Colour(0x4a90e2), description=definition)
    embed.set_thumbnail(url="https://lh3.ggpht.com/oJ67p2f1o35dzQQ9fVMdGRtA7jKQdxUFSQ7vYstyqTp-Xh-H5BAN4T5_abmev3kz55GH=s360-rw")
    embed.set_footer(text="Provided by Urban Dictionary")
    embed.add_field(name="Example", value=example, inline=False)
    embed.add_field(name=":thumbsup:", value=upvote, inline=True)
    embed.add_field(name=":thumbsdown:", value=downvote, inline=True)
    await client.send_message(message.channel, embed=embed)


  elif command_check(message.content, ["{}wikipedia".format(prefix), "{}wiki".format(prefix)]):
    try:
      if message.content.startswith("{}wikipedia".format(prefix)):
        if message.content[9 + len(prefix)] != " ":
          return
        x = message.content[10 + len(prefix):].strip()
      else:
        if message.content[4 + len(prefix)] != " ":
          return
        x = message.content[5 + len(prefix):].strip()        
    except:
      if message.content.startswith("{}giphy".format(prefix)):
        await client.send_message(message.channel, "Include what you want to search on Wikipedia!\nExample: `!wikipedia bunny`")
        return
      else:
        await client.send_message(message.channel, "Include what you want to search on Wikipedia!\nExample: `!wikipedia bunny`")
        return
    y = await client.send_message(message.channel, "Researching...")
    try:
      page = wikipedia.suggest(x)
      if page == None:
        page = wikipedia.search(x, results=1)
      else:
        page = wikipedia.search(page, results=1)
      page = wikipedia.page(page[0])
      url = page.url
      title = page.title
      summary = wikipedia.summary(x, sentences=3)
      image = page.images[0]
    except wikipedia.exceptions.DisambiguationError:
      await client.send_message(message.channel, "`{}` does not match any pages. Try another query!".format(x))
      await client.delete_message(y)
      return
    except wikipedia.exceptions.PageError:
      await client.send_message(message.channel, "Too generic...\nExample: `{}wikipedia Mercury (planet)`".format(prefix))
      await client.delete_message(y)
      return        
    y = await client.edit_message(y, "Almost done...")
    embed = discord.Embed(title=title, colour=discord.Colour(0x4a90e2), url=url, description=summary)
    embed.set_thumbnail(url=image)
    embed.set_footer(text="Provided by Wikipedia, the free internet encyclopedia")
    await client.delete_message(y)
    await client.send_message(message.channel, embed=embed)

  elif command_check(message.content, ["{}oatmeal".format(prefix)]):
    if message.content.strip() != "{}oatmeal".format(prefix):
      return
    embed = discord.Embed(title="Random Oatmeal webcomic", colour=discord.Colour(0x4a90e2), url="http://theoatmeal.com/random")
    embed.set_footer(text="Provided by the The Oatmeal")
    await client.send_message(message.channel, embed=embed)

  elif command_check(message.content, ["{}calculate".format(prefix), "{}calc".format(prefix)]):
    try:
      if command_check(message.content, ["{}calculate ".format(prefix)]):
        msg = calculator.calc(message.content[10 + len(prefix): ])
      else:
        msg = calculator.calc(message.content[5 + len(prefix): ])
    except TypeError:
      msg = "Give me a math problem!\nExample: `3^7 - (9/2)`"
    except:
      msg = "Invalid syntax. Use `{}help calc` for more information".format(prefix)
    await client.send_message(message.channel, msg)

  elif command_check(message.content, ["{}pun".format(prefix), "{}dadjoke".format(prefix)]):
    await client.send_message(message.channel, html.parser.HTMLParser().unescape(requests.get('https://icanhazdadjoke.com', headers={"Accept": "text/plain"}).text))

  elif command_check(message.content, ["{}giphy".format(prefix), "{}gif".format(prefix)]):
    try:
      if message.content.startswith("{}giphy".format(prefix)):
        if message.content[5 + len(prefix)] != " ":
          return
        tag = message.content[6 + len(prefix):].strip()
      else:
        if message.content[3 + len(prefix)] != " ":
          return
        tag = message.content[4 + len(prefix):].strip()        
    except:
      if message.content.startswith("{}giphy".format(prefix)):
        await client.send_message(message.channel, "Search for what???\nExample: `{}gif dog`".format(prefix))
        return
      else:
        await client.send_message(message.channel, "Search for what???\nExample: `{}gif dog`".format(prefix))
        return

    r = requests.get('http://api.giphy.com/v1/gifs/search?q=' + tag + '&api_key=hCKgiae5XgjiYbKPTdgrSuh8P7l2xWMT')
    q = r.json()
    try:
      x = q['data'][0]['url']
    except:
      await client.send_message(message.channel, "Sorry! We searched far and wide, and there was no GIF to match your search term")
      return
    x = "https://media.giphy.com/media/" + x.rsplit("-", 1)[1] + "/giphy.gif"
    embed = discord.Embed(title="First result for \"" + tag + "\"", colour=discord.Colour(0x4a90e2))
    embed.set_thumbnail(url="https://raw.githubusercontent.com/Zozman/TheGifOracleChrome/master/screenshots/giphyLogo.gif")
    embed.set_image(url=x)
    embed.set_footer(text="Powered by GIPHY")
    await client.send_message(message.channel, embed=embed)
    
  elif command_check(message.content, ["{}xkcd".format(prefix)]):
    if message.content.strip() != "{}xkcd".format(prefix):
      return
    latest = requests.get('https://xkcd.com/info.0.json').json()
    num = random.randint(1, latest['num'])
    comic = requests.get('https://xkcd.com/' + str(num) + '/info.0.json').json()
    embed = discord.Embed(title="xkcd #" + str(num), colour=discord.Colour(0x4a90e2))
    embed.set_image(url=comic['img'])
    embed.set_footer(text=comic['alt'])
    await client.send_message(message.channel, embed=embed)

  elif command_check(message.content, ["{}info-edit".format(prefix)]):
    x = message.content[10 + len(prefix):].strip()
    x = (x[:350] + '..') if len(x) > 350 else x
    if not x:
      msg = "Include a custom description (350 character limit)\nExample: `{}info-edit I'm the coolest cat in the house!`".format(prefix)
    elif info_list.get(message.author.id) == None:
      info_list[message.author.id] = x
      msg = "Your description is now `{}`".format(x)
    else:
      y = info_list[message.author.id]
      msg = "Your description changed from `{0}` `{1}`".format(y, x)
      info_list[message.author.id] = x
    await client.send_message(message.channel, msg)

  elif command_check(message.content, ["{}info".format(prefix)]):
    try:
      if message.content[4 + len(prefix)] != " ":
        return
      x = message.content[4 + len(prefix):].strip()
    except:
      x = message.content[4 + len(prefix):].strip()
    if not x:
      try:
        avatar = message.server.get_member(message.author.id).avatar_url
      except:
        avatar = message.server.get_member(message.author.id).default_avatar_url
      nickname = message.server.get_member(message.author.id).display_name
      if info_list.get(message.author.id) != None:
        description = info_list[message.author.id]
      else:
        description = "Empty description (use `{}info-edit` to change it)".format(prefix)
      if roshambo_list.get(message.author.id) == None:
        roshambo_list[message.author.id] = 0
      if trivia_wins.get(message.author.id) == None:
        trivia_wins[message.author.id] = 0
      if money_list.get(message.author.id) == None:
        money_list[message.author.id] = 0
      embed = discord.Embed(title=nickname, colour=discord.Colour(0x4a90e2), description=description.format(prefix))
      embed.set_thumbnail(url=avatar)
      embed.add_field(name="Balance: **{}** coins".format(money_list[message.author.id]), value= "__ __", inline=False)
      embed.add_field(name="Roshambo (RPS)", value= "Score: **{}**".format(roshambo_list[message.author.id]), inline=True)
      embed.add_field(name="Trivia", value= "Wins: **{}**".format(trivia_wins[message.author.id]), inline=True)
      await client.send_message(message.channel, embed=embed)
      return
    try:
      x = x.replace("<", "")
      x = x.replace("@", "")
      x = x.replace("!", "")
      x = x.replace(">", "")
      try:
        avatar = message.server.get_member(x).avatar_url
      except:
        avatar = message.server.get_member(x).default_avatar_url
      nickname = message.server.get_member(x).display_name
      if info_list.get(x) != None:
        description = info_list[x]
      else:
        description = "Empty description (use `{}info-edit` to change it)".format(prefix)
      if roshambo_list.get(x) == None:
        roshambo_list[x] = 0
      if trivia_wins.get(x) == None:
        trivia_wins[x] = 0
      if money_list.get(x) == None:
        money_list[x] = 0
      embed = discord.Embed(title=nickname, colour=discord.Colour(0x4a90e2), description=description)
      embed.set_thumbnail(url=avatar)
      embed.add_field(name="Balance: **{}** coins".format(money_list[x]), value= "__ __", inline=False)
      embed.add_field(name="Roshambo (RPS)", value= "Score: **{}**".format(roshambo_list[x]), inline=True)
      embed.add_field(name="Trivia", value="Wins: **{}**".format(trivia_wins[x]), inline=True)
      await client.send_message(message.channel, embed=embed)
    except:
      await client.send_message(message.channel, "You need to tag a user (or leave it blank to see your own)")
      
  elif command_check(message.content, ["{}clear".format(prefix), "{}clean".format(prefix), "{}purge".format(prefix)]):
    if message.author.server_permissions.manage_messages:
      if message.content == "{}clear".strip() or message.content == "{}purge".strip() or message.content == "{}clean".strip():
        amount_cleared = 10
      elif message.content[6 + len(prefix):].isdigit() == True:
        amount_cleared = int(message.content[6 + len(prefix):]) + 1
        msg = []
        async for x in client.logs_from(message.channel, limit = amount_cleared):
          msg.append(x)
        try:
          await client.delete_messages(msg)
          y = await client.send_message(message.channel, "Deleted `{}` messages".format(str(len(msg) - 1)))
          time.sleep(1)
          await client.delete_message(y)
        except discord.Forbidden:
          await client.send_message(message.channel, "Error! Make sure I have `Manage Messages` permission")
          return
        except:
          y = await client.send_message(message.channel, "Sorry! Bots can only delete messages under 14 days old")
          time.sleep(1)
          await client.delete_message(y)
      else:
        await client.send_message(message.channel, "Enter an amount of messages you want to clear\nExample: `{}clear 17`".format(prefix))
    else:
      await client.send_message(message.channel, "You are missing the `Manage Messages` permission")

  elif command_check(message.content, ["{}ping".format(prefix)]):
    t1 = time.perf_counter()
    msg = await client.send_message(message.channel, "Pong! :ping_pong:")
    t2 = time.perf_counter()
    await client.edit_message(msg,"Pong! :ping_pong: `{}ms`".format(round((t2-t1)*1000)))

  elif command_check(message.content, ["{}say".format(prefix), "{}echo ".format(prefix)]):
    if command_check(message.content, ["{}say ".format(prefix)]):
      msg = message.content[4 + len(prefix):]
    else:
      msg = message.content[5 + len(prefix): ]
    if not msg:
      msg = "What do you want me to say?"
    await client.send_message(message.channel, msg)

  # elif command_check(message.content, ["{}meme".format(prefix)]):
  #TODO

  elif command_check(message.content, ["{}color".format(prefix)]):
    x = message.content[6 + len(prefix):]
    if not x:
      await client.send_message(message.channel, "Give me a color!\nProvide either a hex (Example: `000000`) or RGB (Example: `100, 100, 100`)")
    else:
      x = x.split(",")
      if len(x) == 1 or len(x) == 3:
        if len(x) == 3:
          while " " in x:
            x = x.replace(" ", "")
          rgb_form = list(map(int, tuple(x)))
          hex_form = '#%02x%02x%02x' % (rgb_form[0], rgb_form[1], rgb_form[2])
          decimal_form = int("0x" + hex_form[1:], 0)
        elif len(x[0]) == 6:
          decimal_form = int("0x" + x[0], 0)
          hex_form = str(x[0]).upper()
          rgb_form = tuple(int(hex_form[i:i+2], 16) for i in (0, 2 ,4))
        else:
          await client.send_message(message.channel, "Invalid format!\nProvide either a hex (Example: `000000`) or RGB (Example: `100, 100, 100`)")
        embed = discord.Embed(title="Color Visualizer", colour=discord.Colour(decimal_form))
        embed.add_field(name="Hex", value="#{}".format(hex_form), inline=True)
        embed.add_field(name="RGB", value="rgb{}".format(rgb_form), inline=True)
        await client.send_message(message.channel, embed=embed)

  elif command_check(message.content, ["{}ban".format(prefix)]):
    if message.author.server_permissions.ban_members:
      try:
        og = message.content[3  + len(prefix):].strip()
        msg = og[2:] 
        msg = msg[:-1]     
        await client.ban(message.server.get_member(msg), delete_message_days = 0)
        await client.send_message(message.channel, "{} has been banned!".format(og))
      except AttributeError:
        await client.send_message(message.channel, "You need to tag someone (besides me)")
      except:
        await client.send_message(message.channel, "I'm missing the `Ban Members` permission.\nMake sure Omni has access to **ban members** and try again")               
    else:
      await client.send_message(message.channel, "You are missing the `Ban Members` permission") 

  elif command_check(message.content, ["{}kick".format(prefix)]):
    if message.author.server_permissions.kick_members:
      try:
        og = message.content[4  + len(prefix):].strip()
        msg = og[2:]
        msg = msg[:-1]
        await client.kick(message.server.get_member(msg))
        await client.send_message(message.channel, "{} has been kicked!".format(og))
      except AttributeError:
        await client.send_message(message.channel, "You need to tag someone (besides me)!")  
      except:
        await client.send_message(message.channel, "I'm missing the `Kick Members` permission.\nMake sure Omni has access to **kick members** and try again")
    else:
      await client.send_message(message.channel, "You are missing the `Kick Members` permission")     

  elif command_check(message.content, ["{}flip".format(prefix)]):
    msg = "It was " + random.choice(flip_list) + "!"
    await client.send_message(message.channel, msg)

  elif command_check(message.content, ["{}roshambo".format(prefix), "{}rps".format(prefix)]):
    if roshambo_list.get(message.author.id) == None: 
      roshambo_list[message.author.id] = 0
    if message.content.startswith("{}roshambo".format(prefix)):
      x = message.content[9 + len(prefix):].strip().lower()
    else:
      x = message.content[4 + len(prefix):].strip().lower()
    if not x or x not in ["rock", "paper", "scissors"]:
      msg = "Choose either rock, paper, or scissors\nExample: `{}roshambo paper`".format(prefix)
    else:
      y = random.choice(("rock", "paper", "scissors"))
      player_tie = False
      player_win = False
      if x == "rock":
        if y == "scissors":
          player_win = True
        elif y == "rock":
          player_tie = True

      elif x == "paper":
        if y == "rock":
          player_win = True
        elif y == "paper":
          player_tie = True

      else:
        if y == "paper":
          player_win = True
        elif y == "scissors":
          player_tie = True

      if player_tie == True:
        msg = "We Tied! (+0 point)"
      elif player_win == True:
        msg = "Your `{0}` destroyed my `{1}`... (+1 point)".format(x,y)
        roshambo_list[message.author.id] = roshambo_list[message.author.id] + 1
      else:
        msg = "Your puny `{0}` stood no chance for my `{1}` (-1 point)".format(x,y)
        if roshambo_list[message.author.id] > 0:
          roshambo_list[message.author.id] = roshambo_list[message.author.id] - 1
    x = await client.send_message(message.channel, msg)

  elif command_check(message.content, ["{}roll".format(prefix)]):
    x = message.content[5 + len(prefix):]
    if not x:
      amount_rolled = 6
      msg = str(random.randint(1, amount_rolled))
    elif x.isdigit():
      amount_rolled = int(x)
      msg = str(random.randint(1, amount_rolled))
    else:
      msg = "Give me number of sides (or leave it blank for a 6 sided die)"
      await client.send_message(message.channel, msg)
      return 
    await client.send_message(message.channel, "You rolled a " + msg + "!") 

  elif command_check(message.content, ["{}choose".format(prefix), "{}random ".format(prefix)]):
    msg = message.content[7 + len(prefix):]
    msg = msg.split(",")
    msg = random.choice(msg)
    while '  ' in msg:
      msg = msg.replace('  ', ' ')
    msg = msg.strip()
    if not msg:
      msg = "Give me something to choose!"
    await client.send_message(message.channel, "I choose `" + msg + "`") 

  elif command_check(message.content, ["{}8ball".format(prefix)]):
    msg = random.choice(eightball_list)
    await client.send_message(message.channel, msg) 

  elif command_check(message.content, ["{}prefix".format(prefix)]):
    if message.author.server_permissions.manage_server or message.author.id == "393979327248728074":
      y = message.content[7 + len(prefix):].strip()
      if not y:
        if prefix == ".":
          await client.send_message(message.channel, "What do you want your new prefix to be?\nExample: `{}prefix !`".format(prefix))
        if prefix == "!":
          await client.send_message(message.channel, "What do you want your new prefix to be?\nExample: `{}prefix .`".format(prefix))        
        return
      x = message.author.server.id
      prefix_list[x] = y
      await client.send_message(message.channel, "Prefix successfully changed to `{}`".format(y))
    else:
      await client.send_message(message.channel, "You are missing the `Manage Server` permission")

  elif command_check(message.content, ["{}plot".format(prefix)]):
    x_points = []
    y_points = []
    await client.send_message(message.channel, "Sent to your DM for furthur instructions, <@{}>".format(message.author.id))
    embed = discord.Embed(title="What is the graph's title (Question 1/5)", colour=discord.Colour(0x4a90e2), description="Examples: *Olympic Games Winning Time*, *Reading vs Writing Scores*")
    embed.set_footer(text="Answer within 30s | Made with matplotlib.py")
    await client.send_message(message.author, embed=embed)
    response1 = await client.wait_for_message(author=message.author, timeout=30)
    if response1 is None:
      await client.send_message("Oops! You didn't answer in time")
    graph_title = response1.content

    embed = discord.Embed(title="What is the x-axis label? (Question 2/5)", colour=discord.Colour(0x4a90e2), description="Examples: *Cost in dollars*, *Test scores*")
    embed.set_footer(text="Answer within 30s | Made with matplotlib.py")
    await client.send_message(message.author, embed=embed)
    response2 = await client.wait_for_message(author=message.author, timeout=30)
    if response2 is None:
      await client.send_message("Oops! You didn't answer in time")
    x_label = response2.content

    embed = discord.Embed(title="What is the y-axis label? (Question 3/5)", colour=discord.Colour(0x4a90e2), description="Examples: *Year*, *Automobile speed (kph)*")
    embed.set_footer(text="Answer within 30s | Made with matplotlib.py")
    await client.send_message(message.author, embed=embed)
    response3 = await client.wait_for_message(author=message.author, timeout=30)
    if response3 is None:
      await client.send_message("Oops! You didn't answer in time")
    y_label = response3.content

    embed = discord.Embed(title="What are the x-axis points? (Question 4/5)", colour=discord.Colour(0x4a90e2), description="Example: 1, 3, 6, 9, 12")
    embed.set_footer(text="Answer within 30s | Made with matplotlib.py")
    await client.send_message(message.author, embed=embed)
    response4 = await client.wait_for_message(author=message.author, timeout=30)
    if response4 is None:
      await client.send_message("Oops! You didn't answer in time")
    x_points = response4.content

    embed = discord.Embed(title="What are the y-axis points? (Question 5/5)", colour=discord.Colour(0x4a90e2), description="Example: 4, 7, 5, 8, 9 (Make sure its in the same order you answered your x-axis points!)")
    embed.set_footer(text="Answer within 30s | Made with matplotlib.py")
    await client.send_message(message.author, embed=embed)
    response5 = await client.wait_for_message(author=message.author, timeout=30)
    if response5 is None:
      await client.send_message("Oops! You didn't answer in time")
    y_points = response5.content
    x_points = x_points.replace(" ", "")
    x_points = x_points.split(",")
    x = np.array(x_points)
    y_points = y_points.replace(" ", "")
    y_points = y_points.split(",")
    y = np.array(y_points)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(graph_title)
    await client.send_message(message.author, "Compiling data...")
    try:
      plt.plot(x, y)
    except:
      await client.send_message(message.author, "Error! X and Y should have the same number of points")
      return
    plt.grid(b=True)
    plt.savefig('graph')
    await client.send_file(message.author, 'graph.png')

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)