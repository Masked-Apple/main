import discord
from discord.ext import commands
import asyncio
import sqlite3
import time
import datetime
import random
import secrets
import json
import os
import requests
import math
import textwrap
from datetime import datetime
import sqlite3
import aiohttp
import aiofiles
import numpy as np
import re
from PIL import Image
import PIL.ImageOps
import secrets
import textwrap
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps


prefix = ","
Client = discord.Client()
client = commands.Bot(command_prefix = ',')
owner = 303152083891257344


conn = sqlite3.connect('Users.sqlite')
cur = conn.cursor()




@client.command()
async def profile(ctx, *, member: discord.Member=None):
    if member is None:
        member = ctx.author
    async with aiohttp.ClientSession().get(str(member.avatar_url)) as resp:
        image_file = await aiofiles.open('pfp.png', mode='wb')
        await image_file.write(await resp.read())
        await image_file.close()
        im = Image.open("pfp.png").convert("RGB").resize((254,254)).save("pfp.png")
        cur.execute("SELECT userid FROM users WHERE userid=?", (member.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)":
            info = False
        else:
            info = True
    npImage = np.array(Image.open("pfp.png").convert("RGB"))
    h, w = Image.open("pfp.png").convert("RGB").size
    alpha = Image.new('L', Image.open("pfp.png").convert("RGB").size, 0)
    ImageDraw.Draw(alpha).pieslice([0, 0, h, w], 0, 360, fill=255)
    Image.fromarray(np.dstack((npImage, np.array(alpha)))).save('pfp.png')
    img = Image.open("profile.png").convert("RGBA")
    Image.open("pfp.png")
    img.paste(Image.open("pfp.png"), (64,47), Image.open("pfp.png"))
    ImageDraw.Draw(img).text((350,125), member.name, (225, 225, 225), font=ImageFont.truetype("inkfree.ttf", 80))
    if info is False:
        img.save("card.png")
        return await ctx.channel.send(file=discord.File("card.png"))
    if info is True:
        cur.execute("SELECT rsn FROM users WHERE userid=?", (member.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)":
            ImageDraw.Draw(img).text((406,230), "No RSN set", (225, 225, 225), font= ImageFont.truetype("inkfree.ttf", 47))
        else:
            ImageDraw.Draw(img).text((406,230), row[0], (225, 225, 225), font= ImageFont.truetype("inkfree.ttf", 47))
        #
        cur.execute("SELECT wins FROM users WHERE userid=?", (member.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)":
            ImageDraw.Draw(img).text((406,290), "0", (225, 225, 225), font= ImageFont.truetype("inkfree.ttf", 47))
        else:
            ImageDraw.Draw(img).text((406,290), row[0], (225, 225, 225), font= ImageFont.truetype("inkfree.ttf", 47))
        cur.execute("SELECT rep FROM users WHERE userid=?", (member.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)":
            ImageDraw.Draw(img).text((575,290), "0", (255,255,255), font= ImageFont.truetype("inkfree.ttf", 47))
        else:
            ImageDraw.Draw(img).text((575,290), row[0], (255,255,255), font= ImageFont.truetype("inkfree.ttf", 47))
            img.save("card.png")
    return await ctx.channel.send(file=discord.File("card.png"))




































        
        

        
token = "NDgwMDQzMTEwNjgwODg3MzM2.DrH4lA.e96wOyoGm9-C6yWnnUHbMsM-zRA"


client.run(token, reconnect=True)
