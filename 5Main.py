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
client = commands.Bot(command_prefix = '!')
owner = int(303152083891257344)
winners = []
conn = sqlite3.connect('Users.sqlite')
cur = conn.cursor()


def z_99(current_xp: int):
    return 0 if current_xp > 13_034_431 else "{:,}".format(13_034_431 - current_xp)


def x_99(current_xp: int):
    return 0 if current_xp > 200_000_000 else "{:,}".format(200_000_000 - current_xp)


@client.event
async def on_ready():
    channel = client.get_channel(579002075036254208)
    await channel.send('✔ Connected to Discord!')
    print("✔ Connected to Discord!\n-----------------------------")


@client.command()
async def pfp(ctx, *, member: discord.Member=None):
    try:
        if member is None:
            await ctx.channel.send(str(ctx.author.avatar_url).replace(".webp", ".png"))
        else:
            await ctx.channel.send(str(member.avatar_url).replace(".webp", ".png"))
    except discord.NotFound:
        await ctx.channel.send("That member wasnt found")


@client.command()
async def check(ctx, *, member: discord.Member=None):
    duration = datetime.utcnow() - member.created_at
    print(duration)
    print(member.joined_at)
    ds = duration.total_seconds() // (60*60*24)
    print(ds)
    #print(member.joined_at)


@client.command()
async def g(ctx, *, member: discord.Member=None):
    await ctx.channel.send(member.activities)


@client.command()
async def say(ctx):
    if ctx.author.id == owner:
        await ctx.message.delete()
        await ctx.guild.get_channel(int(ctx.message.content.split()[1])).send("%s" % (" ".join(ctx.message.content.split(" ")[2:])))


@client.command()
async def roll(ctx):
    embed = discord.Embed(colour=discord.Colour.red(),description= f'<a:dicegif:487670982065127424> | {ctx.author.mention} You rolled a **{str(random.randint(1, int(ctx.message.content.split()[1])))}**')
    embed.set_footer(text=f'On a 1-{str(int(ctx.message.content.split()[1]))}dice')
    await ctx.channel.send(embed=embed)


@client.command()
async def kick(ctx, member: discord.Member=None, *, reason=None):
    bot = ctx.message.channel
    if ctx.author.guild_permissions.kick_members or ctx.user.id == 575141146037321729:
        try:
            if member == ctx.message.author:
                await bot.send("You can't kick yourself 🤦")
            if member is None:
                await bot.send("You didn't specify the user you wish to kick 🤦")
            else:
                if member.guild_permissions.kick_members:
                    await bot.send("You can't kick another staff member")
                else:
                    await member.kick(reason=reason)
                    embed = discord.Embed(color=0xFF0000, title="Reason: {}".format(reason))
                    embed.set_author(name="{} was kicked.".format(member.name), icon_url=member.avatar_url)
                    await bot.send(embed=embed)
                    localtime = time.asctime(time.localtime(time.time()))
                    f = open("ban-kick-logs.txt", "a")
                    f.write("[{}] {} was kicked by {} | Reason: {}\n".format(localtime, member.name, ctx.author.name, reason))
                    f.close()
        except discord.Forbidden:
            await bot.send("This user has admin, I wont be able to kick them.")
    else:
        await bot.send("You dont have enough permissions to kick other members.")


@client.command()
async def ban(ctx, member: discord.Member=None, *, reason=None):
    bot = ctx.message.channel
    if ctx.author.guild_permissions.ban_members or ctx.user.id == 575141146037321729:
        try:
            if member == ctx.message.author:
                await bot.send("You can't ban yourself 🤦")
            if member is None:
                await bot.send("You didn't specify the user you wish to ban.. 🤦")
            else:
                if member.guild_permissions.ban_members:
                    await bot.send("You can't ban another staff member")
                else:
                    await member.ban(reason=reason)
                    embed = discord.Embed(color=0xFF0000, title="Reason: {}".format(reason))
                    embed.set_author(name="{} was banned.".format(member.name), icon_url=member.avatar_url)
                    await bot.send(embed=embed)
                    localtime = time.asctime(time.localtime(time.time()))
                    f = open("ban-kick-logs.txt", "a")
                    f.write("[{}] {} was banned by {} | Reason: {}\n".format(localtime, member.name, ctx.author.name, reason))
                    f.close()
        except discord.Forbidden:
            await bot.send("This user has admin, I wont be able to ban them.")
    else:
        await bot.send("You dont have enough permissions to ban other members.")


@client.command()
async def start(ctx):
    bot = ctx.channel
    global winners
    with open('words.json') as json_file:
        data = json.load(json_file)
    random_word = secrets.choice(data)
    embed1 = discord.Embed(title="A game has opened up.  It will begin in 5 seconds.", color=0x00bfff)
    message = await bot.send(embed=embed1)
    await asyncio.sleep(1)
    for x in range(4):
        await message.edit(embed=discord.Embed(title="A game has opened up.  It will begin in {0} seconds.".format(4 - x), color=0x00bfff))
        await asyncio.sleep(1)
    await message.edit(embed=discord.Embed(title="The word is **{0}**".format(random_word), color=0x0000ff))

    def check(m):
        return m.content == random_word and m.channel == message.channel

    msg = await client.wait_for('message', timeout=7, check=check)
    print(winners)
    try:
        await bot.send("<a:winner:537014272228851723> **{0} Wins!**".format(msg.author.mention))
        exist = os.path.isfile(msg.author.id + "wins.txt")
        if exist == False:
            file = open(msg.author.id + "wins.txt", "a")
            file.write("1\n")
            file.close()
        if exist == True:
            file = open(msg.author.id + "wins.txt", "r")
            oldwin = file.read()
            newwin = int("1\n") + int(oldwin)
            file.close()
            file = open(msg.author.id + "wins.txt", "w")
            file.write(str(newwin))
            file.close()
        if len(winners) > 0 and winners[0] != msg.author.id:
            winners = []
        winners.append(msg.author.id)
        if len(winners) > 2:
            await bot.send("**<:streak:537704790487072769> {0} is on a {1} win streak!**".format(msg.author.mention, len(winners)))
    except asyncio.TimeoutError:
        await bot.send("<a:cloudclock:536988420132569131> **Times up! There was no winner..**")


@client.command()
async def yikes(ctx, member: discord.Member=None):
    print("wow")


@client.command()
async def stats(ctx):
    bot = ctx.channel
    if ctx.message.content == ",stats":
        cur.execute("SELECT rsn FROM users WHERE userid=?", (ctx.author.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)":
            return await ctx.channel.send(file=discord.File("norsn.png"))
        else:
            cur.execute("SELECT rsn FROM users WHERE userid = ?", (ctx.author.id,))
            rsn = str(cur.fetchone()[0])
    if ctx.message.content.startswith(",stats "):
        rsn = ctx.message.content[7:]
    for user in ctx.message.mentions:
        cur.execute("SELECT rsn FROM users WHERE userid=?", (user.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)": # IF RSN ISNT SET
            return await ctx.channel.send(file=discord.File("nouserrsn.png"))
        else:                                # IF RSN IS SET
            cur.execute("SELECT rsn FROM users WHERE userid = ?", (user.id,))
            rsn = str(cur.fetchone()[0])
    async with ctx.channel.typing():
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(rsn)
        print(rsn)
        response = requests.get(url)
        if response.status_code == requests.codes.not_found:
            return await bot.send("**<:notfound:580829420378652673> Account wasnt found, you might've spelt the username incorrect or the account is banned.**\nMore info type: `,notfound`")
        embed = discord.Embed(color=0x00F6FF)
        stats = response.text.split(",")
        del stats[0]
        del stats[1]
        del stats[2]
        for i in range(0, int(len(stats) / 2)):
            del stats[i + 1]
        del stats[23]
        Base = 0.25 * (int(stats[2]) + int(stats[4]) + math.floor(int(stats[6]) // int(2)))
        Melee = 0.325 * (int(stats[1]) + int(stats[3]))
        Final = math.floor(Base + Melee)
        new_stats = response.text.split(",")
        stats.insert(1, new_stats[3])
        embed.add_field(name='\u200b', value=" <:Attack:498591810210496515>" + stats[1] + "\n<:Strength:498592002288517121>" + stats[3] + "\n<:Defence:498591848974254083>" + stats[2] + "\n<:Ranged:498592002129133570>" + stats[5] + "\n<:Prayer:498592002276065280>" + stats[6] + "\n<:Magic:498591928909299762>" + stats[7] + "\n<:Runecrafting:498592002259156993>" + stats[21] + "\n<:Construction:498591820477890600>" + stats[23], inline=True)
        embed.add_field(name='\u200b',value="<:Hitpoints:498591928938397707>" + stats[4] + "\n<:Agility:498591795006013471>" +stats[17] + "\n<:Herblore:498591928816893954>" + stats[16] + "\n<:Thieving:498592002435186688>" + stats[18] + "\n<:Crafting:498591838652071956>" + stats[13] + "\n<:Fletching:498591893513306112>" + stats[10] + "\n<:Slayer:498592001902510092>" + stats[19] + "\n<:Hunter:498591928779145217>" + stats[22], inline=True)
        embed.add_field(name='\u200b',value="<:Mining:498591929433456642>" + stats[15] + "\n<:Smithing:498592002276065281>" +stats[14] + "\n<:Fishing:498591879852589056>" + stats[11] + "\n<:Cooking:498591829357494272>" + stats[8] + "\n<:Firemaking:498591866258980916>" + stats[12] + "\n<:Woodcutting:498592002393243648>" + stats[9] + "\n<:Farming:498591858046271498>" + stats[20] + "\n<:skillltotal:533043559989903360>" + stats[0], inline=True)
        embed.set_author(name=f'Stats for {rsn}', icon_url="https://cdn.discordapp.com/attachments/560548659675267073/580824966983843860/155854976112590977.png")
        embed.set_footer(text='Combat Level: %s' % Final)
        await bot.send(embed=embed)


@client.command()
async def xp(ctx):
    bot = ctx.channel
    if ctx.message.content == ",xp":
        cur.execute("SELECT rsn FROM users WHERE userid=?", (ctx.author.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)":
            return await ctx.channel.send(file=discord.File("norsn.png"))
        else:
            cur.execute("SELECT rsn FROM users WHERE userid = ?", (ctx.author.id,))
            rsn = str(cur.fetchone()[0])
    if ctx.message.content.startswith(",xp "):
        rsn = ctx.message.content[4:]
    for user in ctx.message.mentions:
        cur.execute("SELECT rsn FROM users WHERE userid=?", (user.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)": # IF RSN ISNT SET
            return await ctx.channel.send(file=discord.File("nouserrsn.png"))
        else:                                # IF RSN IS SET
            cur.execute("SELECT rsn FROM users WHERE userid = ?", (user.id,))
            rsn = str(cur.fetchone()[0])
    async with ctx.channel.typing():
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(rsn)
        response = requests.get(url)
        if response.status_code == requests.codes.not_found:
            notfound = "**<:notfound:580829420378652673> Account wasnt found, you might've spelt the username incorrect or the account is banned.**\nMore info type: `,notfound`"
            await bot.send(notfound)
        stats = response.text.split(",")
        attxp = stats[4]
        skill_total = stats[2].split("\n")[0]
        attxp1 = attxp.split("\n")
        realattxp = attxp1[0]
        del stats[0]
        del stats[1]
        del stats[2]
        for i in range(0, int(len(stats) / 2)):
            del stats[i]
        del stats[23]
        new_stats = response.text.split(",")
        stats.insert(1, new_stats[3])
        stats = [i.split("\n", 1)[0] for i in stats]
        embed = discord.Embed(color=0x00F6FF)
        embed.set_author(name="XP for " + rsn, icon_url="https://cdn.discordapp.com/attachments/560548659675267073/580824966983843860/155854976112590977.png")
        embed.add_field(name='\u200b', value="<:Attack:498591810210496515>" + format(int(realattxp),",d") + "\n <:Strength:498592002288517121>" + format(int(stats[3]), ",d") + "\n  <:Defence:498591848974254083>" + format(int(stats[2]),",d") + "\n  <:Ranged:498592002129133570>" + format(int(stats[5]), ",d") + "\n  <:Prayer:498592002276065280>" + format(int(stats[6]),",d") + "\n <:Magic:498591928909299762>" + format(int(stats[7]), ",d") + "\n<:Runecrafting:498592002259156993>" + format(int(stats[21]),",d") + "\n<:Construction:498591820477890600>" + format(int(stats[23]), ",d"), inline=True)
        embed.add_field(name='\u200b', value="<:Hitpoints:498591928938397707>" + format(int(stats[4]),",d") + "\n<:Agility:498591795006013471>" + format(int(stats[17]), ",d") + "\n<:Herblore:498591928816893954>" + format(int(stats[16]),",d") + "\n <:Thieving:498592002435186688>" + format(int(stats[18]), ",d") + "\n<:Crafting:498591838652071956>" + format(int(stats[13]),",d") + "\n<:Fletching:498591893513306112>" + format(int(stats[10]), ",d") + "\n<:Slayer:498592001902510092>" + format(int(stats[19]),",d") + "\n<:Hunter:498591928779145217>" + format(int(stats[22]), ",d"), inline=True)
        embed.add_field(name='\u200b', value="<:Mining:498591929433456642>" + format(int(stats[15]),",d") + "\n<:Smithing:498592002276065281>" + format(int(stats[14]), ",d") + "\n<:Fishing:498591879852589056>" + format(int(stats[11]),",d") + "\n<:Cooking:498591829357494272>" + format(int(stats[8]), ",d") + "\n <:Fishing:498591879852589056>" + format(int(stats[11]),",d") + "\n<:Woodcutting:498592002393243648>" + format(int(stats[9]), ",d") + "\n<:Farming:498591858046271498>" + format(int(stats[20]),",d") + "\n<:skilltotal:533043559989903360>" + format(int(skill_total), ",d"), inline=True)
        await bot.send(embed=embed)


@client.command()
async def xpto99(ctx):
    bot = ctx.channel
    if ctx.message.content == ",xpto99":
        cur.execute("SELECT rsn FROM users WHERE userid=?", (ctx.author.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)":
            return await ctx.channel.send(file=discord.File("norsn.png"))
        else:
            cur.execute("SELECT rsn FROM users WHERE userid = ?", (ctx.author.id,))
            rsn = str(cur.fetchone()[0])
    if ctx.message.content.startswith(",xpto99 "):
        rsn = ctx.message.content[8:]
    for user in ctx.message.mentions:
        cur.execute("SELECT rsn FROM users WHERE userid=?", (user.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)": # IF RSN ISNT SET
            return await ctx.channel.send(file=discord.File("nouserrsn.png"))
        else:                                # IF RSN IS SET
            cur.execute("SELECT rsn FROM users WHERE userid = ?", (user.id,))
            rsn = str(cur.fetchone()[0])
    async with ctx.channel.typing():
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(rsn)
        response = requests.get(url)
        if response.status_code == requests.codes.not_found:
            not_found = "**<:notfound:580829420378652673> Account wasnt found, you might've spelt the username incorrect or the account is banned.**\nMore info type: `,notfound`"
            await bot.send(not_found)
        embed = discord.Embed(color=0x00F6FF)
        stats = response.text.split(",")
        attxp = stats[4]
        attxp1 = attxp.split("\n")
        skill_total = stats[2].split("\n")[0]
        realattxp = attxp1[0]

        del stats[0]
        del stats[1]
        del stats[2]
        for i in range(0, int(len(stats) / 2)):
            del stats[i]  # +1
        del stats[23]
        del stats[23]
        del stats[23]
        del stats[23]
        del stats[23]
        new_stats = response.text.split(",")
        stats.insert(1, new_stats[3])
        stats = [i.split("\n", 1)[0] for i in stats]
        embed.add_field(name='\u200b', value=f"\n<:Attack:498591810210496515> {z_99(int(realattxp))}"
        f"\n<:Strength:498592002288517121> {z_99(int(stats[3]))}"
        f"\n<:Defence:498591848974254083> {z_99(int(stats[2]))}"
        f"\n<:Ranged:498592002129133570> {z_99(int(stats[5]))}"
        f"\n<:Prayer:498592002276065280> {z_99(int(stats[6]))}"
        f"\n<:Magic:498591928909299762> {z_99(int(stats[7]))}"
        f"\n<:Runecrafting:498592002259156993> {z_99(int(stats[21]))}"
        f"\n<:Construction:498591820477890600> {z_99(int(stats[23]))}", inline=True)
        embed.add_field(name='\u200b', value=f"\n<:Hitpoints:498591928938397707> {z_99(int(stats[4]))}"
        f"\n<:Agility:498591795006013471> {z_99(int(stats[17]))}"
        f"\n<:Herblore:498591928816893954> {z_99(int(stats[16]))}"
        f"\n<:Thieving:498592002435186688> {z_99(int(stats[18]))}"
        f"\n<:Crafting:498591838652071956> {z_99(int(stats[13]))}"
        f"\n<:Fletching:498591893513306112> {z_99(int(stats[10]))}"
        f"\n<:Slayer:498592001902510092> {z_99(int(stats[19]))}"
        f"\n<:Hunter:498591928779145217> {z_99(int(stats[22]))}", inline=True)
        embed.add_field(name='\u200b', value=f"\n<:Mining:498591929433456642> {z_99(int(stats[15]))}"
        f"\n<:Smithing:498592002276065281> {z_99(int(stats[14]))}"
        f"\n<:Fishing:498591879852589056> {z_99(int(stats[11]))}"
        f"\n<:Cooking:498591829357494272> {z_99(int(stats[8]))}"
        f"\n<:Fishing:498591879852589056> {z_99(int(stats[11]))}"
        f"\n<:Woodcutting:498592002393243648> {z_99(int(stats[9]))}"
        f"\n<:Farming:498591858046271498> {z_99(int(stats[20]))}"
        f"\n<:skilltotal:533043559989903360> {x_99(int(skill_total))}", inline=True)
        embed.set_author(name="XP to 99 for " + rsn,icon_url="https://cdn.discordapp.com/attachments/560548659675267073/580824966983843860/155854976112590977.png")
        await bot.send(embed=embed)


@client.command()
async def notfound(ctx):
    await ctx.channel.send(file=discord.File("notfound.png"))



@client.command()
async def tagnotify(ctx):
    if ctx.author.guild_permissions.administrator or 539719903452856332 in [role.id for role in ctx.author.roles]:
        role = discord.utils.get(ctx.guild.roles, name="Notify")
        await ctx.message.delete()
        await role.edit(mentionable=True)
        await ctx.author.send("<:Successful:558558879110266880> **You are now able to tag @Notify, for the next 30 seconds..**")
        await asyncio.sleep(30)
        await role.edit(mentionable=False)


@client.command()
async def tagbettor(ctx):
    if ctx.author.guild_permissions.administrator or 539719903452856332 in [role.id for role in ctx.author.roles]:
        role = discord.utils.get(ctx.guild.roles, name="Bettor")
        await ctx.message.delete()
        await role.edit(mentionable=True)
        await ctx.author.send("<:Successful:558558879110266880> **You are now able to tag @Bettor, for the next 30 seconds.. Remember that some bettors dont like to be tagged :/**")
        await asyncio.sleep(30)
        await role.edit(mentionable=False)


@client.command()
async def pet(ctx):
    img = Image.open("pet.png")  # Replace infoimgimg.png with your background image.
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("OSRSFont.ttf", 16)  # Make sure you insert a valid font from your folder.
    _, text = ctx.message.content.split(' ', 1)
    lines = text.split("\n")
    lists = (textwrap.TextWrapper(width=58, break_long_words=False).wrap(line) for line in lines)
    body = "\n".join("\n".join(list) for list in lists)
    # draw.text((13,58), "{}".format(body), (0, 0, 0), font=font)
    draw.text((11, 56), "{}" ":".format(body), (0, 0, 0), font=font)
    img.save('applebot.png')  # Change infoimg2.png if needed.
    await ctx.channel.send(file=discord.File("applebot.png"))

@client.command()
async def ely(ctx):
    img = Image.open("ely.png") #Replace infoimgimg.png with your background image.
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("OSRSFont.ttf", 16) #Make sure you insert a valid font from your folder.
    _, text = ctx.message.content.split(' ', 1)
    lines = text.split("\n")
    lists = (textwrap.TextWrapper(width=50,break_long_words=False).wrap(line) for line in lines)
    body  = "\n".join("\n".join(list) for list in lists)
    kc = ctx.message.content.split()[1]
    name = ctx.message.content.split(" ")
    draw.text((202,90), "{}".format(kc), (255,0,0), font=font)
    draw.text((11,104), "{}" " received a drop: Elysian sigil".format("%s" % (" ".join(name[2:]))), (0, 95, 1), font=font)
    draw.text((11,120), "{}" ":".format("%s" % (" ".join(name[2:]))), (0, 0, 0), font=font)
    img.save('infoimg2.png') #Change infoimg2.png if needed.
    await ctx.channel.send(file=discord.File("applebot.png"))


@client.command()
async def auto(ctx):
    if ctx.author.id == owner:
        for x in range(int(ctx.message.content.split()[1])):
            await ctx.channel.send("%s" % (" ".join(ctx.message.content.split(" ")[3:])))
            await asyncio.sleep(float(ctx.message.content.split()[2]))
    else:
        await ctx.channel.send("Only the bot owner can use this command.")


@client.command()
async def setrsn(ctx):
    rsn = "%s" % (" ".join(ctx.message.content.split(" ")[1:]))
    cur.execute("SELECT userid FROM users WHERE userid=?", (ctx.author.id,))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO users (userid, rsn, rep, wins) values (?, '-', '-', '-')",(ctx.author.id,))
        conn.commit()
        print("done inserting")
        cur.execute("UPDATE users SET rsn = '{}' WHERE userid = {}".format(rsn, ctx.author.id))
        conn.commit()
    else:
        cur.execute("UPDATE users SET rsn = '{}' WHERE userid = {}".format(rsn, ctx.author.id))
        conn.commit()
    await ctx.channel.send(file=discord.File("added.png"))


@client.command()
async def rsn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        cur.execute("SELECT rsn FROM users WHERE userid=?", (ctx.author.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)":
            return await ctx.channel.send(file=discord.File("norsn.png"))
        else:
            cur.execute("SELECT rsn FROM users WHERE userid = ?", (ctx.author.id,))
            rsn = str(cur.fetchone()[0])
            embed = discord.Embed(colour=0x00F6FF)
            embed.set_author(name=f'{ctx.author.name}\'s rsn', icon_url=ctx.author.avatar_url)
    else:
        cur.execute("SELECT rsn FROM users WHERE userid=?", (member.id,))
        row = cur.fetchone()
        strow = str(row)
        if row is None or strow == "('-',)": # IF RSN ISNT SET
            return await ctx.channel.send(file=discord.File("norsn.png"))
        else:                                # IF RSN IS SET
            cur.execute("SELECT rsn FROM users WHERE userid = ?", (member.id,))
            rsn = str(cur.fetchone()[0])
            embed = discord.Embed(colour=0x00F6FF)
            embed.set_author(name=f'{member.name}\'s rsn', icon_url=member.avatar_url)
    embed.set_footer(text=rsn, icon_url="https://images-ext-1.discordapp.net/external/zD0H7FDkW2S37DGa7fQAzREr9YR9lbtRfr6ml0p86Jg/https/imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")
    await ctx.channel.send(embed=embed)






token = "NDgwMDQzMTEwNjgwODg3MzM2.DrH4lA.e96wOyoGm9-C6yWnnUHbMsM-zRA"


client.run(token, reconnect=True)
