import discord
from discord.ext import commands
import asyncio
import sqlite3


Client = discord.Client()
client = commands.Bot(command_prefix=",")


conn = sqlite3.connect('MainDB.sqlite')
cur = conn.cursor()
owner = "303152083891257344"


@client.event
async def on_message(message):
    if message.content.startswith(",add"):
        example = discord.utils.get(message.server.roles, name='🍎')
        if message.author.server_permissions.administrator or example in [role for role in message.author.roles]:
            server = message.server.id
            splitted = message.content.split()
            word = splitted[1]
            args = message.content.split(" ")
            cur.execute('SELECT * FROM "{}" WHERE (cmd=?)'.format(message.server.id), (splitted[1],))
            row = cur.fetchone()
            if row is None:
                if message.content.startswith(",add-d"):
                    cur.execute('INSERT INTO "{}" (cmd, text, del) values (?, ?, ?)'.format(message.server.id), (splitted[1], (" ".join(args[2:])), "True"))
                    conn.commit()
                    author1 = message.author.id
                    profile = message.server.get_member(author1)
                    pfp = profile.avatar_url
                    embed = discord.Embed(colour=discord.Colour.red())
                    embed.set_author(name="Created by " + message.author.name, icon_url=pfp)
                    await client.delete_message(message)
                    embed.set_thumbnail(url="https://png.pngtree.com/svg/20170104/icon_paperclip_818073.png")
                    embed.add_field(name="Tag name", value="," + word, inline=True)
                    embed.add_field(name="Message", value=message.content[len(word) + 7:], inline=True)
                    embed.add_field(name="Automatically Delete?", value="Yeah", inline=True)
                    return await client.send_message(message.channel, embed=embed)
                else:
                    cur.execute('INSERT INTO "{}" (cmd, text) values (?, ?)'.format(message.server.id), (splitted[1], (" ".join(args[2:]))))
                    conn.commit()
                    author1 = message.author.id
                    profile = message.server.get_member(author1)
                    pfp = profile.avatar_url
                    embed = discord.Embed(colour=discord.Colour.red())
                    embed.set_author(name="Created by " + message.author.name, icon_url=pfp)
                    await client.delete_message(message)
                    embed.set_thumbnail(url="https://png.pngtree.com/svg/20170104/icon_paperclip_818073.png")
                    embed.add_field(name="Tag name", value=","+word , inline=True)
                    embed.add_field(name="Message", value=message.content[len(word) + 5:]  , inline=True)
                    embed.add_field(name="Automatically Delete?", value="Nah", inline=True)
                    return await client.send_message(message.channel, embed=embed)
            else:
                msg = '<:error:513794294763618305> **The tag name you gave already exists.. Try another**'
                return await client.send_message(message.channel, msg)
        else:
            noperm = await client.send_message(message.channel, "<:applepolice:505111043622567937> **You need the 🍎 role to be able to add custom commands**")
            await asyncio.sleep(5)
            await client.delete_message(noperm)
            await client.delete_message(message)

    if message.content.startswith(",del"):
        row = cur.fetchone()
        example = discord.utils.get(message.server.roles, name='🍎')
        if message.author.server_permissions.administrator or example in [role for role in message.author.roles]:
            spleet = message.content.split()
            word = spleet[1]
            cur.execute(
                'DELETE FROM "{}" WHERE cmd=?'.format(message.server.id), (word,))
            conn.commit()
            return await client.send_message(message.channel, "**<:greenytick:481431838586306560> Ok, I deleted the `," + word + "` tag**")
        else:
            noperm = await client.send_message(message.channel, "<:applepolice:505111043622567937> **You need the 🍎 role to be able to delete custom commands**")
            await asyncio.sleep(5)
            await client.delete_message(noperm)
            await client.delete_message(message)

    if message.content.startswith(",edit"):
        example = discord.utils.get(message.server.roles, name='🍎')
        if message.author.server_permissions.administrator or example in [role for role in message.author.roles]:
            spleet = message.content.split()
            word = spleet[1]
            cur.execute('SELECT text FROM "{}" WHERE cmd=?'.format(message.server.id), (spleet[1],))
            d = str(cur.fetchone()[0])
            cur.execute('DELETE FROM "{}" WHERE cmd=?'.format(message.server.id), (word,))
            conn.commit()
            args = message.content.split(" ")
            cur.execute('SELECT * FROM "{}" WHERE (cmd=?)'.format(message.server.id), (spleet[1],))
            row = cur.fetchone()
            if row is None:
                    cur.execute('INSERT INTO "{}" (cmd, text) values (?, ?)'.format(message.server.id), (spleet[1], (" ".join(args[2:]))))
                    conn.commit()
                    author1 = message.author.id
                    profile = message.server.get_member(author1)
                    pfp = profile.avatar_url
                    embed = discord.Embed(colour=discord.Colour.orange())
                    embed.set_author(name="Edited by " + message.author.name, icon_url=pfp)
                    await client.delete_message(message)
                    embed.set_thumbnail(url="https://png.pngtree.com/svg/20170104/icon_paperclip_818073.png")
                    embed.add_field(name="Tag name", value=","+word , inline=True)
                    embed.add_field(name="Old message", value=d, inline=True)
                    embed.add_field(name="New message", value=message.content[len(word) + 6:]  , inline=True)
                    return await client.send_message(message.channel, embed=embed)

    if message.content.startswith(",database") or message.content.startswith(",taglist"):
        if message.author.id == "303152083891257344":
            server = message.server.id
            await client.send_message(message.channel, "Heres the database:")
            await client.send_file(message.channel, "database.sqlite")


    if message.content.startswith(",enable customcmd") or message.content.startswith(",enable add"):
        example = discord.utils.get(message.server.roles, name='🍎')
        if message.author.server_permissions.administrator or example in [role for role in message.author.roles]:
            conn.execute('CREATE TABLE "{}" (cmd TEXT, text TEXT, del TEXT)'.format(message.server.id))
            embed = discord.Embed(colour=discord.Colour.gold(), title="Custom commands help:")
            embed.add_field(name=",add [tag_name] [message]", value="This creates the custom commands.\nE.g: `,add serverinvite https://discord.gg/hvUuGM9`", inline=True)
            embed.add_field(name=",del [tag_name]", value="This deletes the custom commands.\nE.g: `,delete serverinvite`", inline=True)
            embed.add_field(name=",[tagname]", value="This makes the custom command send.\nE.g: `,severinvite`", inline=True)
            await client.send_message(message.channel, "<:Successful:558558879110266880> **Enabled custom commands plugin for this server!**")
            await client.send_message(message.channel, embed=embed)
        else:
            noperm = await client.send_message(message.channel, "<:applepolice:505111043622567937> **You must be an admin to enable this plugin.**")
            await asyncio.sleep(5)
            await client.delete_message(noperm)
            await client.delete_message(message)

    if message.content.startswith(",commands"):
        example = discord.utils.get(message.server.roles, name='🍎')
        if message.author.server_permissions.administrator or example in [role for role in message.author.roles]:
            cur.execute('SELECT cmd FROM "' + message.server.id + '" ')
            final = [i[0] for i in cur.fetchall()]
            final2 = '\n,'.join(map(str, (final)))
            server = message.server
            embed = discord.Embed(colour=discord.Colour.red(), title=final2)
            embed.set_author(name="{}'s custom commands".format(message.server.name), icon_url=message.server.icon_url)
            return await client.send_message(message.channel, embed=embed)

    if message.content.startswith("," + message.content.replace(",", "")):
            cmd = message.content
            split_parts = cmd.split(',')
            cur.execute('SELECT del FROM "{}" WHERE cmd=?'.format(message.server.id), (split_parts[1],))
            d = str(cur.fetchone()[0])
            if d == "True":
                await client.delete_message(message)
                cur.execute('SELECT text FROM "{}" WHERE cmd=?'.format(message.server.id), (split_parts[1],))
                await client.send_message(message.channel, *cur.fetchone())
            elif d == "False":
                cur.execute('SELECT text FROM "{}" WHERE cmd=?'.format(message.server.id), (split_parts[1],))
                await client.send_message(message.channel, *cur.fetchone())
            else:
                cur.execute('SELECT text FROM "{}" WHERE cmd=?'.format(message.server.id), (split_parts[1],))
                await client.send_message(message.channel, *cur.fetchone())




token="NDgwMDQzMTEwNjgwODg3MzM2.DrH4lA.e96wOyoGm9-C6yWnnUHbMsM-zRA"





client.run(token) #End of script
