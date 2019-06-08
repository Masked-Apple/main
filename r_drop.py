import discord
from discord.ext import commands
import asyncio
import sqlite3
import time
import datetime
import re
import random
import secrets
import json
import os
import requests
import math
import textwrap
from datetime import datetime


prefix = ","
Client = discord.Client()
client = commands.Bot(command_prefix = ',')
owner = int(303152083891257344)
winners = []


@client.event
async def on_ready():
    channel = client.get_channel(579002075036254208)
    await channel.send('✔ Connected to Discord!')
    print("✔ Connected to Discord!\n-----------------------------")


@client.command()
async def drop(ctx):
    spleet = ctx.message.content.split()
    amount = "%s" % (" ".join(ctx.message.content.split(" ")[1:]))
    if amount.startswith(".") or amount.startswith("0."):
        amount = float(amount) * 1000
        amount = f'{amount}k'
    else:
        amount = amount
    embed1 = discord.Embed(colour=0x00FF00, title="Type  **pickup**  to pick it up quick!")
    embed1.set_author(name="{} dropped {}".format(ctx.author.name, amount),icon_url="https://images-ext-2.discordapp.net/external/bKClkePYK5oY8hI1uNUuWqhE63PqsXW9HBH_lhV856o/http/pa1.narvii.com/6292/33c7cda3e5cc4b21250a70c98e0826d3c0708248_00.gif")
    await ctx.channel.send(embed=embed1)
    def check(m):
        return m.content == 'pickup' and m.channel == ctx.channel
    msg = await client.wait_for('message', check=check)
    await ctx.channel.send("{.author.mention} picked up the **{}**\nYou need to wait for **{}** to transfer you the money.".format(msg, amount, ctx.author.name))
    embed = discord.Embed(colour=discord.Colour.red(), description="Or copy and paste this: ```!transfer 07 {.author} {}```".format(msg, amount))
    embed.add_field(name='**Winner**', value="{.author}".format(msg))
    embed.add_field(name='**Payout**', value="{}".format(amount))
    embed.set_author(name="{}, pay out your winners!".format(ctx.author.name), icon_url=ctx.guild.get_member(ctx.author.id).avatar_url)
    ez = client.get_channel(574337466060767262)
    await ez.send(embed=embed)

@client.command()
async def dropm(ctx):
    spleet = ctx.message.content.split()
    amount = "%s" % (" ".join(ctx.message.content.split(" ")[1:]))
    if amount.startswith(".") or amount.startswith("0."):
        amount = float(amount) * 1000
        amount = f'{amount}k'
    else:
        amount = amount
    role = discord.utils.get(ctx.guild.roles, name="Notify")
    await role.edit(mentionable=True)
    await ctx.channel.send("<@&551699240825651220> **I sense someone is going to drop their wallet**")
    await asyncio.sleep(4)
    embed1 = discord.Embed(colour=0x00FF00, title="Type  **pickup**  to pick it up quick!")
    embed1.set_author(name="{} dropped {}".format(ctx.author.name, amount),icon_url="https://images-ext-2.discordapp.net/external/bKClkePYK5oY8hI1uNUuWqhE63PqsXW9HBH_lhV856o/http/pa1.narvii.com/6292/33c7cda3e5cc4b21250a70c98e0826d3c0708248_00.gif")
    await ctx.channel.send(embed=embed1)
    def check(m):
        return m.content == 'pickup' and m.channel == ctx.channel
    msg = await client.wait_for('message', check=check)
    await ctx.channel.send("{.author.mention} picked up the **{}**\nYou need to wait for **{}** to transfer you the money.".format(msg, amount, ctx.author.name))
    embed = discord.Embed(colour=discord.Colour.red(), description="Or copy and paste this: ```!transfer 07 {.author} {}```".format(msg, amount))
    embed.add_field(name='**Winner**', value="{.author}".format(msg))
    embed.add_field(name='**Payout**', value="{}".format(amount))
    embed.set_author(name="{}, pay out your winners!".format(ctx.author.name), icon_url=ctx.guild.get_member(ctx.author.id).avatar_url)
    ez = client.get_channel(574337466060767262)
    await ez.send(embed=embed)
    await role.edit(mentionable=False)

token = "NDgwMDQzMTEwNjgwODg3MzM2.DrH4lA.e96wOyoGm9-C6yWnnUHbMsM-zRA"


client.run(token, reconnect=True)
