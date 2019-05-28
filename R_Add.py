
import discord
from discord.ext import commands
import asyncio
import sqlite3


client = discord.Client()

@client.event
async def on_ready():
    print("✔ Connected!\n")

conn = sqlite3.connect('MainDB.sqlite')
cur = conn.cursor()
owner = "303152083891257344"

@client.event
async def on_message(message):
    bot = message.channel
    if message.content.startswith(",add"):
        example = discord.utils.get(message.guild.roles, name='🍎')
        if message.author.guild_permissions.administrator or example in [role for role in message.author.roles]:
            server = message.guild.id
            splitted = message.content.split()
            word = splitted[1]
            args = message.content.split(" ")
            cur.execute('SELECT * FROM "{}" WHERE (cmd=?)'.format(message.guild.id), (splitted[1],))
            row = cur.fetchone()
            if row is None:
                if message.content.startswith(",add-d"):
                    cur.execute('INSERT INTO "{}" (cmd, text, del) values (?, ?, ?)'.format(message.guild.id), (splitted[1], (" ".join(args[2:])), "True"))
                    conn.commit()
                    author1 = message.author.id
                    profile = message.guild.get_member(author1)
                    pfp = profile.avatar_url
                    embed = discord.Embed(colour=discord.Colour.red())
                    embed.set_author(name="Created by " + message.author.name, icon_url=pfp)
                    await message.delete()
                    embed.set_thumbnail(url="https://png.pngtree.com/svg/20170104/icon_paperclip_818073.png")
                    embed.add_field(name="Tag name", value="," + word, inline=True)
                    embed.add_field(name="Message", value=message.content[len(word) + 7:], inline=True)
                    embed.add_field(name="Automatically Delete?", value="Yeah", inline=True)
                    return await bot.send(embed=embed)
                else:
                    cur.execute('INSERT INTO "{}" (cmd, text) values (?, ?)'.format(message.guild.id),(splitted[1], (" ".join(args[2:]))))
                    conn.commit()
                    author1 = message.author.id
                    profile = message.guild.get_member(author1)
                    pfp = profile.avatar_url
                    embed = discord.Embed(colour=discord.Colour.red())
                    embed.set_author(name="Created by " + message.author.name, icon_url=pfp)
                    await message.delete()
                    embed.set_thumbnail(url="https://png.pngtree.com/svg/20170104/icon_paperclip_818073.png")
                    embed.add_field(name="Tag name", value="," + word, inline=True)
                    embed.add_field(name="Message", value=message.content[len(word) + 5:], inline=True)
                    embed.add_field(name="Automatically Delete?", value="Nah", inline=True)
                    return await bot.send(embed=embed)
        else:
            noperm = await bot.send("<:applepolice:505111043622567937> **You need the 🍎 role to be able to add custom commands**")
            await asyncio.sleep(5)
            await noperm.delete()
            await message.delete()

    if message.content.startswith(",del"):
        example = discord.utils.get(message.guild.roles, name='🍎')
        if message.author.guild_permissions.administrator or example in [role for role in message.author.roles]:
            row = cur.fetchone()
            spleet = message.content.split()
            word = spleet[1]
            cur.execute('DELETE FROM "{}" WHERE cmd=?'.format(message.guild.id), (word,))
            conn.commit()
            return await bot.send("**<:greenytick:481431838586306560> Ok, I deleted the `," + word + "` tag**")
        else:
            noperm = await bot.send("<:applepolice:505111043622567937> **You need the 🍎 role to be able to delete custom commands**")
            await asyncio.sleep(5)
            await noperm.delete()
            await message.delete()

    if message.content.startswith(",database") or message.content.startswith(",taglist"):
        if message.author.id == 303152083891257344:
            await bot.send("Heres the database:")
            await bot.send(file=discord.File("MainDB.sqlite"))


    if message.content.startswith(",enable customcmd") or message.content.startswith(",enable add"):
        example = discord.utils.get(message.guild.roles, name='🍎')
        if message.author.guild_permissions.administrator or example in [role for role in message.author.roles]:
            conn.execute('CREATE TABLE "{}" (cmd TEXT, text TEXT, del TEXT)'.format(message.guild.id))
            embed = discord.Embed(colour=discord.Colour.gold(), title="Custom commands help:")
            embed.add_field(name=",add [tag_name] [message]", value="This creates the custom commands.\nE.g: `,add serverinvite https://discord.gg/hvUuGM9`", inline=True)
            embed.add_field(name=",del [tag_name]", value="This deletes the custom commands.\nE.g: `,delete serverinvite`", inline=True)
            embed.add_field(name=",[tagname]", value="This makes the custom command send.\nE.g: `,severinvite`", inline=True)
            await bot.send("<:Successful:558558879110266880> **Enabled custom commands plugin for this server!**")
            await bot.send(embed=embed)
        else:
            noperm = await bot.send("<:applepolice:505111043622567937> **You must be an admin to enable this plugin.**")
            await asyncio.sleep(5)
            await noperm.delete()
            await message.delete()

    if message.content.startswith(",commands"):
        example = discord.utils.get(message.guild.roles, name='🍎')
        if message.author.guild_permissions.administrator or example in [role for role in message.author.roles]:
            print(message.guild.id)
            cur.execute('SELECT cmd FROM "{}"'.format(message.guild.id))
            final = [i[0] for i in cur.fetchall()]
            final2 = '\n,'.join(map(str, (final)))
            server = message.guild
            embed = discord.Embed(colour=discord.Colour.red(), title=final2)
            embed.set_author(name="{}'s custom commands".format(message.guild.name), icon_url=message.guild.icon_url)
            return await bot.send(embed=embed)

    if message.content.startswith(",com"):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name="Commands:", icon_url="https://cdn.discordapp.com/attachments/543133545951133696/577521396939489293/unknown.png")
        embed.add_field(name="• Keys", value="`!keys / !keys @user`\nIs used to check your own keys or someone elses.", inline=False)
        embed.add_field(name="• Wallet", value="`!w / !w @user`\nIs used to check your own wallet or someone elses.", inline=False)
        embed.add_field(name="• Private wallet", value="`!privacy {on/off}`\nTo hide or show your wallet.", inline=False)
        embed.add_field(name="• Swapping wallet gold", value="`!swap {rs3/07} {amount}`\nTo swap specific amount of wallet gold from 07 to rs3 or vice versa.", inline=False)
        embed.add_field(name="• Wager", value="`!wager / !wager @user`\nTo check yours or someone elses overall wager in the server.", inline=False)
        embed.add_field(name="• Weekly Wager", value="`!thisweek / !thisweek @user`\nTo check yours or someone elses wager within the current week.", inline=False)
        embed.add_field(name="• Top wagers", value="`!top {07/rs3}`\nTo see the top 5 wagers within a week.", inline=False)
        embed.add_field(name="• Transfer wallet money", value="`!transfer {07/rs3} {@user} {amount}`\nTo transfer specific amount of gold from your wallet to others.", inline=False)
        embed.add_field(name="• Cashin/out", value="`!cashin {07/rs3} {amount} / !cashout {07/rs3} {amount}`\nTo cash gold in from RuneScape into your wallet..", inline=False)
        embed.set_footer(text="📌 Need more help? Talk to a staff member.")
        await bot.send(embed=embed)

    if message.content.startswith(",dom"):
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(name="Games:", icon_url="https://cdn.discordapp.com/attachments/543133545951133696/577521396939489293/unknown.png")
        embed.add_field(name="• Blackjack", value="`!bj {07/rs3} {amount}`\nIs used to start a blackjack game.", inline=False)
        embed.add_field(name="• High Low", value="`!hl {07/rs3} {amount}`\nIs used to start a high low game.", inline=False)
        embed.add_field(name="• 40x1.5", value="`!40 <rs3/07> <amount>`\nUsed to start 40x1.5 game (if you hit any number 41-100 you'll be paid your bet x1.5).", inline=False)
        embed.add_field(name="• 45x1.55", value="`!45 <rs3/07> <amount>`\nUsed to start 45x1.55 game (if you hit any number 46-100 you'll be paid your bet x1.55).", inline=False)
        embed.add_field(name="• 50x1.9", value="` !50 <rs3/07> <amount>`\nUsed to start 50x1.9 game (if you hit any number 51-100 you'll be paid your bet x1.9).", inline=False)
        embed.add_field(name="• 54x2", value="`!54 <rs3/07> <amount>`\nUsed to start 54x2 game (if you hit any number 55-100 you'll be paid your bet x2).", inline=False)
        embed.add_field(name="• 75x3", value="`!75 <rs3/07> <amount>`\nUsed to start 75x3 game (if you hit any number 76-100 you'll be paid your bet x3).", inline=False)
        embed.add_field(name="• 90x7", value="`!90 <rs3/07> <amount>`\nUsed to start 90x7 game (if you hit any number 91-100 you'll be paid your bet x7).", inline=False)
        embed.add_field(name="• 95x10", value="`!95 <rs3/07> <amount>`\nUsed to start 95x10 game (if you hit any number 96-100 you'll be paid your bet x10).", inline=False)
        embed.set_footer(text="📌 Good luck! - HB Team")
        await bot.send(embed=embed)


    if message.content.startswith("," + message.content.replace(",", "")):
            cmd = message.content
            split_parts = cmd.split(',')
            cur.execute('SELECT del FROM "{}" WHERE cmd=?'.format(message.guild.id), (split_parts[1],))
            d = str(cur.fetchone()[0])
            if d == "True":
                await bot.delete(message)
                cur.execute('SELECT text FROM "{}" WHERE cmd=?'.format(message.guild.id), (split_parts[1],))
                await bot.send(*cur.fetchone())
            elif d == "False":
                cur.execute('SELECT text FROM "{}" WHERE cmd=?'.format(message.guild.id), (split_parts[1],))
                await bot.send(*cur.fetchone())
            else:
                cur.execute('SELECT text FROM "{}" WHERE cmd=?'.format(message.guild.id), (split_parts[1],))
                await bot.send(*cur.fetchone())

token = "NDgwMDQzMTEwNjgwODg3MzM2.DrH4lA.e96wOyoGm9-C6yWnnUHbMsM-zRA"


client.run(token)
