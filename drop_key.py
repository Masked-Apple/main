
import discord
from discord.ext import commands
import asyncio
import time
import random
import os
import datetime
import textwrap
import os.path


client = commands.Bot(command_prefix=",")
msgs = []# my mouse broke


@client.event
async def on_message(message):
        if message.content.startswith(",drop"):
            example = discord.utils.get(message.server.roles, name='Giveaways')
            if message.author.server_permissions.administrator or example in [role for role in message.author.roles]:
                spleet = message.content.split()
                amount = spleet[1]
                if amount.startswith(".") or amount.startswith("0."):
                    namount = float(amount) * 1000
                    embed1 = discord.Embed(colour=discord.Colour.red())
                    embed1.set_author(name="{}k was dropped, click 💸 to pick it up quickkk".format(namount), icon_url="http://pa1.narvii.com/6292/33c7cda3e5cc4b21250a70c98e0826d3c0708248_00.gif")
                    msg = await client.send_message(message.channel, embed=embed1)
                    await asyncio.sleep(3)
                    await client.add_reaction(msg,"💸")
                    await asyncio.sleep(1)
                    res = await client.wait_for_reaction(['💸'], message=msg)
                    await client.send_message(message.channel, '{0.user.mention} picked up the **'.format(res) + str(namount) + 'k**!')
                    winner = '{0.user.mention}'.format(res)
                    print(winner)
                    embed = discord.Embed(colour = discord.Colour.red(), description="Or copy and paste this: ```!transfer 07 {} {}k```".format(winner, namount))
                    embed.add_field(name='**Winner**',value="{0.user}".format(res))
                    embed.add_field(name='**Payout**',value="{}k".format(namount))
                    embed.set_author(name="{}, pay out your winners!".format(message.author.name), icon_url=message.server.get_member(message.author.id).avatar_url)
                    await client.send_message(client.get_channel('574337466060767262'), message.author.mention)
                    await client.send_message(client.get_channel('574337466060767262'), embed=embed)
                    print("1")
                elif "m" in amount:
                    embed1 = discord.Embed(colour=discord.Colour.red())
                    embed1.set_author(name="{} was dropped, click 💸 to pick it up quickkk".format(amount), icon_url="http://pa1.narvii.com/6292/33c7cda3e5cc4b21250a70c98e0826d3c0708248_00.gif")
                    msg = await client.send_message(message.channel, embed=embed1)
                    await asyncio.sleep(3)
                    await client.add_reaction(msg,"💸")
                    await asyncio.sleep(1)
                    res = await client.wait_for_reaction(['💸'], message=msg)
                    await client.send_message(message.channel, '{0.user.mention} picked up the **'.format(res) + str(amount) + '**!')
                    winner = '{0.user.mention}'.format(res)
                    print(winner)
                    embed = discord.Embed(colour=discord.Colour.red(),description="Or copy and paste this: ```!transfer 07 {} {}```".format(winner,amount))
                    embed.add_field(name='**Winner**', value="{0.user}".format(res))
                    embed.add_field(name='**Payout**', value="{}".format(amount))
                    embed.set_author(name="{}, pay out your winners!".format(message.author.name),icon_url=message.server.get_member(message.author.id).avatar_url)
                    await client.send_message(client.get_channel('574337466060767262'), message.author.mention)
                    await client.send_message(client.get_channel('574337466060767262'), embed=embed)
                    print("3")
                elif "k" in amount:
                    embed1 = discord.Embed(colour=discord.Colour.red())
                    embed1.set_author(name="{} was dropped, click 💸 to pick it up quickkk".format(amount), icon_url="http://pa1.narvii.com/6292/33c7cda3e5cc4b21250a70c98e0826d3c0708248_00.gif")
                    msg = await client.send_message(message.channel, embed=embed1)
                    await asyncio.sleep(3)
                    await client.add_reaction(msg,"💸")
                    await asyncio.sleep(1)
                    res = await client.wait_for_reaction(['💸'], message=msg)
                    await client.send_message(message.channel,'{0.user.mention} picked up the **'.format(res) + str(amount) + '**!')
                    winner = '{0.user.mention}'.format(res)
                    print(winner)
                    embed = discord.Embed(colour=discord.Colour.red(),description="Or copy and paste this: ```!transfer 07 {} {}```".format(winner,amount))
                    embed.add_field(name='**Winner**', value="{0.user}".format(res))
                    embed.add_field(name='**Payout**', value="{}".format(amount))
                    embed.set_author(name="{}, pay out your winners!".format(message.author.name),icon_url=message.server.get_member(message.author.id).avatar_url)
                    await client.send_message(client.get_channel('574337466060767262'), message.author.mention)
                    await client.send_message(client.get_channel('574337466060767262'), embed=embed)
                    print("3")
                elif "m" or "k" not in amount:
                    embed1 = discord.Embed(colour=discord.Colour.red())
                    embed1.set_author(name="{}m was dropped, click 💸 to pick it up quickkk".format(amount), icon_url="http://pa1.narvii.com/6292/33c7cda3e5cc4b21250a70c98e0826d3c0708248_00.gif")
                    msg = await client.send_message(message.channel, embed=embed1)
                    await asyncio.sleep(3)
                    await client.add_reaction(msg,"💸")
                    await asyncio.sleep(1)
                    res = await client.wait_for_reaction(['💸'], message=msg)
                    await client.send_message(message.channel, '{0.user.mention} picked up the **'.format(res) + str(amount) + 'm**!')
                    winner = '{0.user.mention}'.format(res)
                    print(winner)
                    embed = discord.Embed(colour = discord.Colour.red(), description="Or copy and paste this: ```!transfer 07 {} {}m```".format(winner, amount))
                    embed.add_field(name='**Winner**',value="{0.user}".format(res))
                    embed.add_field(name='**Payout**',value="{}m".format(amount))
                    embed.set_author(name="{}, pay out your winners!".format(message.author.name), icon_url=message.server.get_member(message.author.id).avatar_url)
                    await client.send_message(client.get_channel('574337466060767262'), message.author.mention)
                    await client.send_message(client.get_channel('574337466060767262'), embed=embed)
                    print("2")
                else:
                    embed1 = discord.Embed(colour=discord.Colour.red())
                    embed1.set_author(name="{} was dropped, click 💸 to pick it up quickkk".format(amount), icon_url="http://pa1.narvii.com/6292/33c7cda3e5cc4b21250a70c98e0826d3c0708248_00.gif")
                    msg = await client.send_message(message.channel, embed=embed1)
                    await asyncio.sleep(3)
                    await client.add_reaction(msg,"💸")
                    await asyncio.sleep(1)
                    res = await client.wait_for_reaction(['💸'], message=msg)
                    await client.send_message(message.channel, '{0.user.mention} picked up the **'.format(res) + str(amount) + '**!')
                    winner = '{0.user.mention}'.format(res)
                    print(winner)
                    embed = discord.Embed(colour = discord.Colour.red(), description="Or copy and paste this: ```!transfer 07 {} {}```".format(winner, amount))
                    embed.add_field(name='**Winner**',value="{0.user}".format(res))
                    embed.add_field(name='**Payout**',value="{}".format(amount))
                    embed.set_author(name="{}, pay out your winners!".format(message.author.name), icon_url=message.server.get_member(message.author.id).avatar_url)
                    await client.send_message(client.get_channel('574337466060767262'), message.author.mention)
                    await client.send_message(client.get_channel('574337466060767262'), embed=embed)
                    print("3")


token = "NDgwMDQzMTEwNjgwODg3MzM2.DrH4lA.e96wOyoGm9-C6yWnnUHbMsM-zRA"

client.run(token)  # End of script
