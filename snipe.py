
import discord
from discord.ext import commands
import asyncio
import time
import os
import os.path
from datetime import date
import sqlite3
import discord
import random
import os

client = commands.Bot(command_prefix=",")
msgs = {}# my mouse broke

users = []

conn = sqlite3.connect('snipedata.sqlite')
cur = conn.cursor()

@client.event
async def on_message_delete(message):
    print("{} : {}".format(message.author.name, message.content))
    cur.execute('DELETE FROM "{}" WHERE channel=?'.format("snipe"), (message.channel.id,))
    conn.commit()
    pfp = message.server.get_member(message.author.id).avatar_url
    cur.execute('INSERT INTO "{}" (channel, name, pfp, message) values (?, ?, ?, ?)'.format("snipe"), (message.channel.id, message.author.name, pfp , message.content))
    conn.commit()

@client.event
async def on_message(message):

    if message.content.startswith(",snipe") or message.content.startswith(",snake"):
        cur.execute("SELECT message FROM snipe WHERE channel = ?", (message.channel.id,))
        con = str(cur.fetchone()[0])
        embed= discord.Embed(colour=discord.Colour.green(), description=con)
        cur.execute("SELECT name FROM snipe WHERE channel = ?", (message.channel.id,))
        name = str(cur.fetchone()[0])
        cur.execute("SELECT pfp FROM snipe WHERE channel = ?", (message.channel.id,))
        pfp = str(cur.fetchone()[0])
        embed.set_author(name=name, icon_url=pfp)
        d1 = random.randint(1, 7)
        if d1 == 1:
            embed.set_footer(text="🐍 #1 Snake")
        if d1 == 2:
            embed.set_footer(text="Causing trouble since 2018")
        if d1 == 3:
            embed.set_footer(text="Another successful snake by Apple Bot")
        if d1 == 4:
            embed.set_footer(text="Busted lul")
        if d1 == 5:
            embed.set_footer(text="^ massive balls for saying that")
        if d1 == 6:
            embed.set_footer(text="Breaking friendships since 2018")
        if d1 == 7:
            embed.set_footer(text="Just call me Snake Bot.")
        await client.send_message(message.channel, embed=embed)


token= 'NDgwMDQzMTEwNjgwODg3MzM2.DrH4lA.e96wOyoGm9-C6yWnnUHbMsM-zRA'





client.run(token) #End of script
