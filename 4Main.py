

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import datetime
import os.path
import shutil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import aiohttp
import aiofiles
import numpy as np
import re
from PIL import Image
import PIL.ImageOps
import json
import secrets
import json
import requests
import textwrap
import math

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = ",") #Initialise client bot
winners = []


@client.event
async def on_ready():
    print('Ready.')


def z_99(current_xp: int):
    return 0 if current_xp > 13_034_431 else "{:,}".format(13_034_431 - current_xp)


def x_99(current_xp: int):
    return 0 if current_xp > 200_000_000 else "{:,}".format(200_000_000 - current_xp)

@client.event
async def on_message(message):
    if message.content.startswith(",combatlvl <@") or message.content.startswith(",combatlevel <@"):
        for user in message.mentions:
            name = message.content.split()[1]
            realName = name.replace("!", "")
            realName1 = realName.replace("<", "")
            realName2 = realName1.replace(">", "")
            realName3 = realName2.replace("@", "")
            exist = os.path.isfile(realName3 + "rsn.txt")
            if exist == True:
                file = open(realName3 + "rsn.txt", "r").read()
                url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
                # await client.send_message(channel, "Grabbing **" + username + "'s** stats...")
                response = requests.get(url)
                if response.status_code == requests.codes.not_found:
                    notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                    await client.send_message(message.channel, notfound)
                # await client.send_message(channel, embed = embed)
                stats = response.text.split(",")
                del stats[0]
                del stats[1]
                del stats[2]

                for i in range(0, int(len(stats) / 2)):
                    print(i)

                    del stats[i + 1]
                del stats[23]
                del stats[23]
                del stats[23]
                del stats[23]
                del stats[23]
                new_stats = response.text.split(",")
                stats.insert(1, new_stats[3])
                Base = 0.25 * (int(stats[2]) + int(stats[4]) +
                               math.floor(int(stats[6]) // int(2)))
                Melee = 0.325 * (int(stats[1]) + int(stats[3]))
                Final = math.floor(Base + Melee)
                msg = "**" + user.name + "'s Combat Level is `%s" % Final + "`**"
                await client.send_message(message.channel, msg)
                file.close()
            if exist == False:
                msg = '**<:error:513794294763618305>' + user.name + ' hasnt set their rsn yet, so I cant search for its stats**\nYou can search for others stats tho.. `,stats [Rsn]`'
                await client.send_message(message.channel, msg)

    if message.content == ",combatlvl" or message.content == ",combatlevel":
        realName3 = message.author.id
        exist = os.path.isfile(realName3 + "rsn.txt")
        if exist == True:
            file = open(realName3 + "rsn.txt", "r").read()
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
            # await client.send_message(channel, "Grabbing **" + username + "'s** stats...")
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, notfound)
            # await client.send_message(channel, embed = embed)
            stats = response.text.split(",")
            del stats[0]
            del stats[1]
            del stats[2]

            for i in range(0, int(len(stats) / 2)):
                print(i)

                del stats[i + 1]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            new_stats = response.text.split(",")
            stats.insert(1, new_stats[3])
            Base = 0.25 * (int(stats[2]) + int(stats[4]) +
                           math.floor(int(stats[6]) // int(2)))
            Melee = 0.325 * (int(stats[1]) + int(stats[3]))
            Final = math.floor(Base + Melee)
            msg = "**" + message.author.name + "'s Combat Level is `%s" % Final + "`**"
            await client.send_message(message.channel, msg)
            file.close()
        if exist == False:
            msg = '**<:error:513794294763618305>' + name + ' hasnt set their rsn yet, so I cant search for its stats**\nYou can search for others stats tho.. `,stats [Rsn]`'
            await client.send_message(message.channel, msg)

    if message.content.startswith(",combat a") or message.content.startswith(",combat b") or message.content.startswith(
            ",combat c") or message.content.startswith(",combat d") or message.content.startswith(
        ",combatlvl e") or message.content.startswith(",combat lvl f") or message.content.startswith(
        ",combatlvl g") or message.content.startswith(",combat lvl h") or message.content.startswith(
        ",combatlvl i") or message.content.startswith(",combat lvl j") or message.content.startswith(
        ",combatlvl k") or message.content.startswith(",combat lvl l") or message.content.startswith(
        ",combatlvl m") or message.content.startswith(",combat lvl n") or message.content.startswith(
        ",combatlvl o") or message.content.startswith(",combat lvl p") or message.content.startswith(
        ",combatlvl q") or message.content.startswith(",combat lvl r") or message.content.startswith(
        ",combatlvl s") or message.content.startswith(",combat lvl t") or message.content.startswith(
        ",combatlvl u") or message.content.startswith(",combat lvl v") or message.content.startswith(
        ",combatlvl w") or message.content.startswith(",combat lvl x") or message.content.startswith(
        ",combatlvl y") or message.content.startswith(",combat lvl z") or message.content.startswith(
        ",combatlvl 1") or message.content.startswith(",combat lvl 2") or message.content.startswith(
        ",combatlvl 3") or message.content.startswith(",combat lvl 4") or message.content.startswith(
        ",combatlvl 5") or message.content.startswith(",combat lvl 6") or message.content.startswith(
        ",combatlvl 7") or message.content.startswith(",combat lvl 8") or message.content.startswith(
        ",combatlvl 9") or message.content.startswith(",combat lvl 0") or message.content.startswith(
        ",combatlvl A") or message.content.startswith(",combat lvl B") or message.content.startswith(
        ",combatlvl C") or message.content.startswith(",combat lvl D") or message.content.startswith(
        ",combatlvl E") or message.content.startswith(",combat lvl F") or message.content.startswith(
        ",combatlvl G") or message.content.startswith(",combat lvl H") or message.content.startswith(
        ",combatlvl I") or message.content.startswith(",combat lvl J") or message.content.startswith(
        ",combatlvl K") or message.content.startswith(",combat lvl L") or message.content.startswith(
        ",combatlvl M") or message.content.startswith(",combat lvl N") or message.content.startswith(
        ",combatlvl O") or message.content.startswith(",combat lvl P") or message.content.startswith(
        ",combatlvl Q") or message.content.startswith(",combat lvl R") or message.content.startswith(
        ",combatlvl S") or message.content.startswith(",combat lvl T") or message.content.startswith(
        ",combatlvl U") or message.content.startswith(",combat lvl V") or message.content.startswith(
        ",combatlvl W") or message.content.startswith(",combat lvl X") or message.content.startswith(
        ",combatlvl Y") or message.content.startswith(",combat lvl Z") or message.content.startswith(
        ",combatlevel a") or message.content.startswith(",combatlevel b") or message.content.startswith(
        ",combatlevel c") or message.content.startswith(",combatlevel d") or message.content.startswith(
        ",combatlevel e") or message.content.startswith(",combat level f") or message.content.startswith(
        ",combatlevel g") or message.content.startswith(",combat level h") or message.content.startswith(
        ",combatlevel i") or message.content.startswith(",combat level j") or message.content.startswith(
        ",combatlevel k") or message.content.startswith(",combat level l") or message.content.startswith(
        ",combatlevel m") or message.content.startswith(",combat level n") or message.content.startswith(
        ",combatlevel o") or message.content.startswith(",combat level p") or message.content.startswith(
        ",combatlevel q") or message.content.startswith(",combat level r") or message.content.startswith(
        ",combatlevel s") or message.content.startswith(",combat level t") or message.content.startswith(
        ",combatlevel u") or message.content.startswith(",combat level v") or message.content.startswith(
        ",combatlevel w") or message.content.startswith(",combat level x") or message.content.startswith(
        ",combatlevel y") or message.content.startswith(",combat level z") or message.content.startswith(
        ",combatlevel 1") or message.content.startswith(",combat level 2") or message.content.startswith(
        ",combatlevel 3") or message.content.startswith(",combat level 4") or message.content.startswith(
        ",combatlevel 5") or message.content.startswith(",combat level 6") or message.content.startswith(
        ",combatlevel 7") or message.content.startswith(",combat level 8") or message.content.startswith(
        ",combatlevel 9") or message.content.startswith(",combat level 0") or message.content.startswith(
        ",combatlevel A") or message.content.startswith(",combat level B") or message.content.startswith(
        ",combatlevel C") or message.content.startswith(",combat level D") or message.content.startswith(
        ",combatlevel E") or message.content.startswith(",combat level F") or message.content.startswith(
        ",combatlevel G") or message.content.startswith(",combat level H") or message.content.startswith(
        ",combatlevel I") or message.content.startswith(",combat level J") or message.content.startswith(
        ",combatlevel K") or message.content.startswith(",combat level L") or message.content.startswith(
        ",combatlevel M") or message.content.startswith(",combat level N") or message.content.startswith(
        ",combatlevel O") or message.content.startswith(",combat level P") or message.content.startswith(
        ",combatlevel Q") or message.content.startswith(",combat level R") or message.content.startswith(
        ",combatlevel S") or message.content.startswith(",combat level T") or message.content.startswith(
        ",combatlevel U") or message.content.startswith(",combat level V") or message.content.startswith(
        ",combatlevel W") or message.content.startswith(",combat level X") or message.content.startswith(
        ",combatlevel Y") or message.content.startswith(",combat level Z"):
        _, username = message.content.split(' ', 1)
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(username)
        # await client.send_message(channel, "Grabbing **" + username + "'s** stats...")
        response = requests.get(url)
        if response.status_code == requests.codes.not_found:
            notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
            await client.send_message(message.channel, notfound)
        # await client.send_message(channel, embed = embed)
        stats = response.text.split(",")
        del stats[0]
        del stats[1]
        del stats[2]

        for i in range(0, int(len(stats) / 2)):
            print(i)

            del stats[i + 1]
        del stats[23]
        del stats[23]
        del stats[23]
        del stats[23]
        del stats[23]
        new_stats = response.text.split(",")
        stats.insert(1, new_stats[3])
        Base = 0.25 * (int(stats[2]) + int(stats[4]) +
                       math.floor(int(stats[6]) // int(2)))
        Melee = 0.325 * (int(stats[1]) + int(stats[3]))
        Final = math.floor(Base + Melee)
        msg = "**" + username + "'s Combat Level is `%s" % Final + "`**"
        await client.send_message(message.channel, msg)

    if message.content.startswith(",combat <@"):
        name = message.content.split()[1]
        realName = name.replace("!", "")
        realName1 = realName.replace("<", "")
        realName2 = realName1.replace(">", "")
        realName3 = realName2.replace("@", "")
        exist = os.path.isfile(realName3 + "rsn.txt")
        if exist == True:
            file = open(realName3 + "rsn.txt", "r").read()
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
            # await client.send_message(channel, "Grabbing **" + username + "'s** stats...")
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, notfound)
            # await client.send_message(channel, embed = embed)
            stats = response.text.split(",")
            del stats[0]
            del stats[1]
            del stats[2]

            for i in range(0, int(len(stats) / 2)):
                print(i)

                del stats[i + 1]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            new_stats = response.text.split(",")
            stats.insert(1, new_stats[3])
            Base = 0.25 * (int(stats[2]) + int(stats[4]) +
                           math.floor(int(stats[6]) // int(2)))
            Melee = 0.325 * (int(stats[1]) + int(stats[3]))
            Final = math.floor(Base + Melee)
            embed = discord.Embed(color=0xFF0000, description=" <:Attack:498591810210496515> " + stats[1] + " <:Strength:498592002288517121>" + stats[
                                3] + " <:Defence:498591848974254083>" + stats[2] + " <:Ranged:498592002129133570>" +
                                  stats[5] + " <:Prayer:498592002276065280>" + stats[6] + " <:Magic:498591928909299762>" +
                                  stats[7] + " <:Hitpoints:498591928938397707>" + stats[4]+ " **Combat Level: %s" % Final + "**", inline=True)
            embed.set_author(name=file,
                             icon_url="https://cdn.discordapp.com/attachments/488429052445851651/498557211321171968/latest.png")  # This is for clean look
            embed.set_author(name='Combat stats for ' + file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")  # This is for clean look
            await client.send_message(message.channel, embed=embed)
            file.close()
        if exist == False:
            msg = '**<:error:513794294763618305>' + name + ' hasnt set their rsn yet, so I cant search for its stats**\nYou can search for others stats tho.. `,stats [Rsn]`'
            await client.send_message(message.channel, msg)

        if message.content.startswith(",combat a") or message.content.startswith(",combat b") or message.content.startswith(
            ",combat c") or message.content.startswith(",combat d") or message.content.startswith(
            ",combat e") or message.content.startswith(",combat f") or message.content.startswith(
            ",combat g") or message.content.startswith(",combat h") or message.content.startswith(
            ",combat i") or message.content.startswith(",combat j") or message.content.startswith(
            ",combat k") or message.content.startswith(",combat l") or message.content.startswith(
            ",combat m") or message.content.startswith(",combat n") or message.content.startswith(
            ",combat o") or message.content.startswith(",combat p") or message.content.startswith(
            ",combat q") or message.content.startswith(",combat r") or message.content.startswith(
            ",combat s") or message.content.startswith(",combat t") or message.content.startswith(
            ",combat u") or message.content.startswith(",combat v") or message.content.startswith(
            ",combat w") or message.content.startswith(",combat x") or message.content.startswith(
            ",combat y") or message.content.startswith(",combat z") or message.content.startswith(
            ",combat 1") or message.content.startswith(",combat 2") or message.content.startswith(
            ",combat 3") or message.content.startswith(",combat 4") or message.content.startswith(
            ",combat 5") or message.content.startswith(",combat 6") or message.content.startswith(
            ",combat 7") or message.content.startswith(",combat 8") or message.content.startswith(
            ",combat 9") or message.content.startswith(",combat 0") or message.content.startswith(
            ",combat A") or message.content.startswith(",combat B") or message.content.startswith(
            ",combat C") or message.content.startswith(",combat D") or message.content.startswith(
            ",combat E") or message.content.startswith(",combat F") or message.content.startswith(
            ",combat G") or message.content.startswith(",combat H") or message.content.startswith(
            ",combat I") or message.content.startswith(",combat J") or message.content.startswith(
            ",combat K") or message.content.startswith(",combat L") or message.content.startswith(
            ",combat M") or message.content.startswith(",combat N") or message.content.startswith(
            ",combat O") or message.content.startswith(",combat P") or message.content.startswith(
            ",combat Q") or message.content.startswith(",combat R") or message.content.startswith(
            ",combat S") or message.content.startswith(",combat T") or message.content.startswith(
            ",combat U") or message.content.startswith(",combat V") or message.content.startswith(
            ",combat W") or message.content.startswith(",combat X") or message.content.startswith(
            ",combat Y") or message.content.startswith(",combat Z"):
            _, username = message.content.split(' ', 1)
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(username)
            # await client.send_message(channel, "Grabbing **" + username + "'s** stats...")
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, notfound)
            # await client.send_message(channel, embed = embed)
            stats = response.text.split(",")
            del stats[0]
            del stats[1]
            del stats[2]

            for i in range(0, int(len(stats) / 2)):
                print(i)

                del stats[i + 1]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            new_stats = response.text.split(",")
            stats.insert(1, new_stats[3])
            Base = 0.25 * (int(stats[2]) + int(stats[4]) +
                           math.floor(int(stats[6]) // int(2)))
            Melee = 0.325 * (int(stats[1]) + int(stats[3]))
            Final = math.floor(Base + Melee)
            embed = discord.Embed(color=0xFF0000, description=" <:Attack:498591810210496515> " + stats[1] + " <:Strength:498592002288517121>" + stats[
                                3] + " <:Defence:498591848974254083>" + stats[2] + " <:Ranged:498592002129133570>" +
                                  stats[5] + " <:Prayer:498592002276065280>" + stats[6] + " <:Magic:498591928909299762>" +
                                  stats[7] + " <:Hitpoints:498591928938397707>" + stats[4]+ " **Combat Level: %s" % Final + "**", inline=True)
            embed.set_author(name=username,
                             icon_url="https://cdn.discordapp.com/attachments/488429052445851651/498557211321171968/latest.png")  # This is for clean look
            embed.set_author(name='Combat stats for ' + username,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")  # This is for clean look
            await client.send_message(message.channel, embed=embed)

    if message.content == ",combat":
        realName3 = message.author.id
        exist = os.path.isfile(realName3 + "rsn.txt")
        if exist == True:
            file = open(realName3 + "rsn.txt", "r").read()
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
            # await client.send_message(channel, "Grabbing **" + username + "'s** stats...")
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, notfound)
            # await client.send_message(channel, embed = embed)
            stats = response.text.split(",")
            del stats[0]
            del stats[1]
            del stats[2]

            for i in range(0, int(len(stats) / 2)):
                print(i)

                del stats[i + 1]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            new_stats = response.text.split(",")
            stats.insert(1, new_stats[3])
            Base = 0.25 * (int(stats[2]) + int(stats[4]) +
                           math.floor(int(stats[6]) // int(2)))
            Melee = 0.325 * (int(stats[1]) + int(stats[3]))
            Final = math.floor(Base + Melee)
            embed = discord.Embed(color=0xFF0000,
                                  description=" <:Attack:498591810210496515> " + stats[1] + " <:Strength:498592002288517121>" +
                                              stats[
                                                  3] + " <:Defence:498591848974254083>" + stats[
                                                  2] + " <:Ranged:498592002129133570>" +
                                              stats[5] + " <:Prayer:498592002276065280>" + stats[
                                                  6] + " <:Magic:498591928909299762>" +
                                              stats[7] + " <:Hitpoints:498591928938397707>" + stats[
                                                  4] + " **Combat Level: %s" % Final + "**", inline=True)
            embed.set_author(name=file,
                             icon_url="https://cdn.discordapp.com/attachments/488429052445851651/498557211321171968/latest.png")  # This is for clean look
            embed.set_author(name='Combat stats for ' + file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")  # This is for clean look
            await client.send_message(message.channel, embed=embed)
            file.close()
        if exist == False:
            msg = '**<:error:513794294763618305>' + name + ' hasnt set their rsn yet, so I cant search for its stats**\nYou can search for others stats tho.. `,stats [Rsn]`'
            await client.send_message(message.channel, msg)

    if message.content.startswith(",stats <@"):
        await client.send_typing(message.channel)
        name = message.content.split()[1]
        realName = name.replace("!", "")
        realName1 = realName.replace("<", "")
        realName2 = realName1.replace(">", "")
        realName3 = realName2.replace("@", "")
        exist = os.path.isfile(realName3 + "rsn.txt")
        if exist == True:
            file = open(realName3 + "rsn.txt", "r").read()
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
            # await client.send_message(channel, "Grabbing **" + username + "'s** stats...")
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, notfound)
            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name="ez",
                             icon_url="https://cdn.discordapp.com/attachments/488429052445851651/498557211321171968/latest.png")  # This is for clean look
            # await client.send_message(channel, embed = embed)
            stats = response.text.split(",")
            del stats[0]
            del stats[1]
            del stats[2]

            for i in range(0, int(len(stats) / 2)):
                print(i)

                del stats[i + 1]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            Base = 0.25 * (int(stats[2]) + int(stats[4]) +
                           math.floor(int(stats[6]) // int(2)))
            Melee = 0.325 * (int(stats[1]) + int(stats[3]))
            Final = math.floor(Base + Melee)
            new_stats = response.text.split(",")
            stats.insert(1, new_stats[3])
            embed.add_field(name='\u200b',
                            value=" <:Attack:498591810210496515>" + stats[1] + "\n<:Strength:498592002288517121>" +
                                  stats[3] + "\n<:Defence:498591848974254083>" + stats[
                                      2] + "\n<:Ranged:498592002129133570>" + stats[
                                      5] + "\n<:Prayer:498592002276065280>" + stats[
                                      6] + "\n<:Magic:498591928909299762>" + stats[
                                      7] + "\n<:Runecrafting:498592002259156993>" + stats[
                                      21] + "\n<:Construction:498591820477890600>" + stats[23]+ "\n**Combat Level: %s" % Final + "**", inline=True)
            embed.add_field(name='\u200b',
                            value="<:Hitpoints:498591928938397707>" + stats[4] + "\n<:Agility:498591795006013471>" +
                                  stats[17] + "\n<:Herblore:498591928816893954>" + stats[
                                      16] + "\n<:Thieving:498592002435186688>" + stats[
                                      18] + "\n<:Crafting:498591838652071956>" + stats[
                                      13] + "\n<:Fletching:498591893513306112>" + stats[
                                      10] + "\n<:Slayer:498592001902510092>" + stats[
                                      19] + "\n<:Hunter:498591928779145217>" + stats[22], inline=True)
            embed.add_field(name='\u200b',
                            value="<:Mining:498591929433456642>" + stats[15] + "\n<:Smithing:498592002276065281>" +
                                  stats[14] + "\n<:Fishing:498591879852589056>" + stats[
                                      11] + "\n<:Cooking:498591829357494272>" + stats[
                                      8] + "\n<:Firemaking:498591866258980916>" + stats[
                                      12] + "\n<:Woodcutting:498592002393243648>" + stats[
                                      9] + "\n<:Farming:498591858046271498>" + stats[
                                      20] + "\n<:skillltotal:533043559989903360>" + stats[0], inline=True)
            embed.set_author(name='Stats for ' + file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")  # This is for clean look
            await client.send_message(message.channel, embed=embed)
            file.close()
        if exist == False:
            msg = '**<:error:513794294763618305>' + name + ' hasnt set their rsn yet, so I cant search for its stats**\nYou can search for others stats tho.. `,stats [Rsn]`'
            await client.send_message(message.channel, msg)

    elif message.content.startswith(",xp <@"):
        await client.send_typing(message.channel)
        name = message.content.split()[1]
        realName = name.replace("!", "")
        realName1 = realName.replace("<", "")
        realName2 = realName1.replace(">", "")
        realName3 = realName2.replace("@", "")
        exist = os.path.isfile(realName3 + "rsn.txt")
        if exist == True:
            file = open(realName3 + "rsn.txt", "r").read()
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, notfound)
            stats = response.text.split(",")
            print(stats)
            attxp = stats[4]
            skill_total = stats[2].split("\n")[0]
            attxp1 = attxp.split("\n")
            realattxp = attxp1[0]

            del stats[0]
            del stats[1]
            del stats[2]
            print(stats)

            for i in range(0, int(len(stats) / 2)):
                print(i)

                del stats[i]  # +1
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            new_stats = response.text.split(",")
            stats.insert(1, new_stats[3])
            # stats is now [total,+23skills]
            stats = [i.split("\n", 1)[0] for i in stats]

            print(stats)

            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name="XP for " + file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")  # This is for clean look
            embed.add_field(name='\u200b', value="<:Attack:498591810210496515>" + format(int(realattxp),
                                                                                         ",d") + "\n <:Strength:498592002288517121>" + format(
                int(stats[3]), ",d") + "\n  <:Defence:498591848974254083>" + format(int(stats[2]),
                                                                                    ",d") + "\n  <:Ranged:498592002129133570>" + format(
                int(stats[5]), ",d") + "\n  <:Prayer:498592002276065280>" + format(int(stats[6]),
                                                                                   ",d") + "\n <:Magic:498591928909299762>" + format(
                int(stats[7]), ",d") + "\n<:Runecrafting:498592002259156993>" + format(int(stats[21]),
                                                                                       ",d") + "\n<:Construction:498591820477890600>" + format(
                int(stats[23]), ",d"+ "\n**Combat Level: %s" % Final + "**"), inline=True)
            embed.add_field(name='\u200b', value="<:Hitpoints:498591928938397707>" + format(int(stats[4]),
                                                                                            ",d") + "\n<:Agility:498591795006013471>" + format(
                int(stats[17]), ",d") + "\n<:Herblore:498591928816893954>" + format(int(stats[16]),
                                                                                    ",d") + "\n <:Thieving:498592002435186688>" + format(
                int(stats[18]), ",d") + "\n<:Crafting:498591838652071956>" + format(int(stats[13]),
                                                                                    ",d") + "\n<:Fletching:498591893513306112>" + format(
                int(stats[10]), ",d") + "\n<:Slayer:498592001902510092>" + format(int(stats[19]),
                                                                                  ",d") + "\n<:Hunter:498591928779145217>" + format(
                int(stats[22]), ",d"), inline=True)
            embed.add_field(name='\u200b', value="<:Mining:498591929433456642>" + format(int(stats[15]),
                                                                                         ",d") + "\n<:Smithing:498592002276065281>" + format(
                int(stats[14]), ",d") + "\n<:Fishing:498591879852589056>" + format(int(stats[11]),
                                                                                   ",d") + "\n<:Cooking:498591829357494272>" + format(
                int(stats[8]), ",d") + "\n <:Fishing:498591879852589056>" + format(int(stats[11]),
                                                                                   ",d") + "\n<:Woodcutting:498592002393243648>" + format(
                int(stats[9]), ",d") + "\n<:Farming:498591858046271498>" + format(int(stats[20]),
                                                                                  ",d") + "\n<:skilltotal:533043559989903360>" + format(
                int(skill_total), ",d"), inline=True)
            await client.send_message(message.channel, embed=embed)
            file.close()
        if exist == False:
            msg = '**<:error:513794294763618305>' + name + ' hasnt set their rsn yet, so I cant search for its xp**\nYou can search for others xp tho.. `,xp [Rsn]`'
            await client.send_message(message.channel, msg)

    if message.content == ",stats":
        await client.send_typing(message.channel)
        # channel = discord.Object(id='493882750521049108')
        me = message.author.id
        exist = os.path.isfile(me + "rsn.txt")
        if exist == True:
            file = open(me + "rsn.txt", "r").read()
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
            # await client.send_message(channel, "Grabbing **" + username + "'s** stats...")
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, notfound)
            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name="ez",
                             icon_url="https://cdn.discordapp.com/attachments/488429052445851651/498557211321171968/latest.png")  # This is for clean look
            # await client.send_message(channel, embed = embed)
            stats = response.text.split(",")
            del stats[0]
            del stats[1]
            del stats[2]

            for i in range(0, int(len(stats) / 2)):
                print(i)

                del stats[i + 1]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            Base = 0.25 * (int(stats[2]) + int(stats[4]) +
                           math.floor(int(stats[6]) // int(2)))
            Melee = 0.325 * (int(stats[1]) + int(stats[3]))
            Final = math.floor(Base + Melee)
            new_stats = response.text.split(",")
            stats.insert(1, new_stats[3])
            embed.add_field(name='\u200b',
                            value=" <:Attack:498591810210496515>" + stats[1] + "\n<:Strength:498592002288517121>" +
                                  stats[3] + "\n<:Defence:498591848974254083>" + stats[
                                      2] + "\n<:Ranged:498592002129133570>" + stats[
                                      5] + "\n<:Prayer:498592002276065280>" + stats[
                                      6] + "\n<:Magic:498591928909299762>" + stats[
                                      7] + "\n<:Runecrafting:498592002259156993>" + stats[
                                      21] + "\n<:Construction:498591820477890600>" + stats[23]+ "\n**Combat Level: %s" % Final + "**", inline=True)
            embed.add_field(name='\u200b',
                            value="<:Hitpoints:498591928938397707>" + stats[4] + "\n<:Agility:498591795006013471>" +
                                  stats[17] + "\n<:Herblore:498591928816893954>" + stats[
                                      16] + "\n<:Thieving:498592002435186688>" + stats[
                                      18] + "\n<:Crafting:498591838652071956>" + stats[
                                      13] + "\n<:Fletching:498591893513306112>" + stats[
                                      10] + "\n<:Slayer:498592001902510092>" + stats[
                                      19] + "\n<:Hunter:498591928779145217>" + stats[22], inline=True)
            embed.add_field(name='\u200b',
                            value="<:Mining:498591929433456642>" + stats[15] + "\n<:Smithing:498592002276065281>" +
                                  stats[14] + "\n<:Fishing:498591879852589056>" + stats[
                                      11] + "\n<:Cooking:498591829357494272>" + stats[
                                      8] + "\n<:Firemaking:498591866258980916>" + stats[
                                      12] + "\n<:Woodcutting:498592002393243648>" + stats[
                                      9] + "\n<:Farming:498591858046271498>" + stats[
                                      20] + "\n<:skillltotal:533043559989903360>" + stats[0], inline=True)
            embed.set_author(name='Stats for ' + file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")  # This is for clean look
            await client.send_message(message.channel, embed=embed)
            file.close()
        if exist == False:
            msg = '**<:error:513794294763618305> You havent set your rsn yet, so I cant search for its stats**\nYou can search for others stats tho.. `,stats [Rsn]`'
            await client.send_message(message.channel, msg)

    elif message.content.startswith(",stats a") or message.content.startswith(",stats b") or message.content.startswith(
            ",stats c") or message.content.startswith(",stats d") or message.content.startswith(
            ",stats e") or message.content.startswith(",stats f") or message.content.startswith(
            ",stats g") or message.content.startswith(",stats h") or message.content.startswith(
            ",stats i") or message.content.startswith(",stats j") or message.content.startswith(
            ",stats k") or message.content.startswith(",stats l") or message.content.startswith(
            ",stats m") or message.content.startswith(",stats n") or message.content.startswith(
            ",stats o") or message.content.startswith(",stats p") or message.content.startswith(
            ",stats q") or message.content.startswith(",stats r") or message.content.startswith(
            ",stats s") or message.content.startswith(",stats t") or message.content.startswith(
            ",stats u") or message.content.startswith(",stats v") or message.content.startswith(
            ",stats w") or message.content.startswith(",stats x") or message.content.startswith(
            ",stats y") or message.content.startswith(",stats z") or message.content.startswith(
            ",stats 1") or message.content.startswith(",stats 2") or message.content.startswith(
            ",stats 3") or message.content.startswith(",stats 4") or message.content.startswith(
            ",stats 5") or message.content.startswith(",stats 6") or message.content.startswith(
            ",stats 7") or message.content.startswith(",stats 8") or message.content.startswith(
            ",stats 9") or message.content.startswith(",stats 0") or message.content.startswith(
            ",stats A") or message.content.startswith(",stats B") or message.content.startswith(
            ",stats C") or message.content.startswith(",stats D") or message.content.startswith(
            ",stats E") or message.content.startswith(",stats F") or message.content.startswith(
            ",stats G") or message.content.startswith(",stats H") or message.content.startswith(
            ",stats I") or message.content.startswith(",stats J") or message.content.startswith(
            ",stats K") or message.content.startswith(",stats L") or message.content.startswith(
            ",stats M") or message.content.startswith(",stats N") or message.content.startswith(
            ",stats O") or message.content.startswith(",stats P") or message.content.startswith(
            ",stats Q") or message.content.startswith(",stats R") or message.content.startswith(
            ",stats S") or message.content.startswith(",stats T") or message.content.startswith(
            ",stats U") or message.content.startswith(",stats V") or message.content.startswith(
            ",stats W") or message.content.startswith(",stats X") or message.content.startswith(
            ",stats Y") or message.content.startswith(",stats Z"):
        # channel = discord.Object(id='493882750521049108')
        await client.send_typing(message.channel)
        _, username = message.content.split(' ', 1)
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(username)
        # await client.send_message(channel, "Grabbing **" + username + "'s** stats...")
        response = requests.get(url)
        if response.status_code == requests.codes.not_found:
            notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
            await client.send_message(message.channel, notfound)
        embed = discord.Embed(color=0xFF0000)
        embed.set_author(name=username,
                         icon_url="https://cdn.discordapp.com/attachments/488429052445851651/498557211321171968/latest.png")  # This is for clean look
        # await client.send_message(channel, embed = embed)
        stats = response.text.split(",")
        del stats[0]
        del stats[1]
        del stats[2]

        for i in range(0, int(len(stats) / 2)):
            print(i)

            del stats[i + 1]
        del stats[23]
        del stats[23]
        del stats[23]
        del stats[23]
        del stats[23]
        new_stats = response.text.split(",")
        stats.insert(1, new_stats[3])
        Base = 0.25 * (int(stats[2]) + int(stats[4]) +
                       math.floor(int(stats[6]) // int(2)))
        Melee = 0.325 * (int(stats[1]) + int(stats[3]))
        Final = math.floor(Base + Melee)
        embed.add_field(name='\u200b',
                        value=" <:Attack:498591810210496515>" + stats[1] + "\n<:Strength:498592002288517121>" + stats[
                            3] + "\n<:Defence:498591848974254083>" + stats[2] + "\n<:Ranged:498592002129133570>" +
                              stats[5] + "\n<:Prayer:498592002276065280>" + stats[6] + "\n<:Magic:498591928909299762>" +
                              stats[7] + "\n<:Runecrafting:498592002259156993>" + stats[
                                  21] + "\n<:Construction:498591820477890600>" + stats[23] + "\n**Combat Level: %s" % Final + "**", inline=True)
        embed.add_field(name='\u200b',
                        value="<:Hitpoints:498591928938397707>" + stats[4] + "\n<:Agility:498591795006013471>" + stats[
                            17] + "\n<:Herblore:498591928816893954>" + stats[16] + "\n<:Thieving:498592002435186688>" +
                              stats[18] + "\n<:Crafting:498591838652071956>" + stats[
                                  13] + "\n<:Fletching:498591893513306112>" + stats[
                                  10] + "\n<:Slayer:498592001902510092>" + stats[
                                  19] + "\n<:Hunter:498591928779145217>" + stats[22], inline=True)
        embed.add_field(name='\u200b',
                        value="<:Mining:498591929433456642>" + stats[15] + "\n<:Smithing:498592002276065281>" + stats[
                            14] + "\n<:Fishing:498591879852589056>" + stats[11] + "\n<:Cooking:498591829357494272>" +
                              stats[8] + "\n<:Firemaking:498591866258980916>" + stats[
                                  12] + "\n<:Woodcutting:498592002393243648>" + stats[
                                  9] + "\n<:Farming:498591858046271498>" + stats[
                                  20] + "\n<:skillltotal:533043559989903360>" + stats[0], inline=True)
        embed.set_author(name='Stats for ' + username,
                         icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")  # This is for clean look
        await client.send_message(message.channel, embed=embed)


    elif message.content == ",xp":
        await client.send_typing(message.channel)
        me = message.author.id
        exist = os.path.isfile(me + "rsn.txt")
        if exist == True:
            file = open(me + "rsn.txt", "r").read()
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, notfound)
            stats = response.text.split(",")
            print(stats)
            attxp = stats[4]
            skill_total = stats[2].split("\n")[0]
            attxp1 = attxp.split("\n")
            realattxp = attxp1[0]

            del stats[0]
            del stats[1]
            del stats[2]
            print(stats)

            for i in range(0, int(len(stats) / 2)):
                print(i)

                del stats[i]  # +1
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            del stats[23]
            new_stats = response.text.split(",")
            stats.insert(1, new_stats[3])
            # stats is now [total,+23skills]
            stats = [i.split("\n", 1)[0] for i in stats]
            print(stats)

            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name="XP for " + file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")  # This is for clean look
            embed.add_field(name='\u200b', value="<:Attack:498591810210496515>" + format(int(realattxp),
                                                                                         ",d") + "\n <:Strength:498592002288517121>" + format(
                int(stats[3]), ",d") + "\n  <:Defence:498591848974254083>" + format(int(stats[2]),
                                                                                    ",d") + "\n  <:Ranged:498592002129133570>" + format(
                int(stats[5]), ",d") + "\n  <:Prayer:498592002276065280>" + format(int(stats[6]),
                                                                                   ",d") + "\n <:Magic:498591928909299762>" + format(
                int(stats[7]), ",d") + "\n<:Runecrafting:498592002259156993>" + format(int(stats[21]),
                                                                                       ",d") + "\n<:Construction:498591820477890600>" + format(
                int(stats[23]), ",d"), inline=True)
            embed.add_field(name='\u200b', value="<:Hitpoints:498591928938397707>" + format(int(stats[4]),
                                                                                            ",d") + "\n<:Agility:498591795006013471>" + format(
                int(stats[17]), ",d") + "\n<:Herblore:498591928816893954>" + format(int(stats[16]),
                                                                                    ",d") + "\n <:Thieving:498592002435186688>" + format(
                int(stats[18]), ",d") + "\n<:Crafting:498591838652071956>" + format(int(stats[13]),
                                                                                    ",d") + "\n<:Fletching:498591893513306112>" + format(
                int(stats[10]), ",d") + "\n<:Slayer:498592001902510092>" + format(int(stats[19]),
                                                                                  ",d") + "\n<:Hunter:498591928779145217>" + format(
                int(stats[22]), ",d"), inline=True)
            embed.add_field(name='\u200b', value="<:Mining:498591929433456642>" + format(int(stats[15]),
                                                                                         ",d") + "\n<:Smithing:498592002276065281>" + format(
                int(stats[14]), ",d") + "\n<:Fishing:498591879852589056>" + format(int(stats[11]),
                                                                                   ",d") + "\n<:Cooking:498591829357494272>" + format(
                int(stats[8]), ",d") + "\n <:Fishing:498591879852589056>" + format(int(stats[11]),
                                                                                   ",d") + "\n<:Woodcutting:498592002393243648>" + format(
                int(stats[9]), ",d") + "\n<:Farming:498591858046271498>" + format(int(stats[20]),
                                                                                  ",d") + "\n<:skilltotal:533043559989903360>" + format(
                int(skill_total), ",d"), inline=True)
            await client.send_message(message.channel, embed=embed)
            file.close()
        if exist == False:
            msg = '**<:error:513794294763618305> You havent set your rsn yet, so I cant search for its xp**\nYou can search for others xp tho.. `,xp [Rsn]`'
            await client.send_message(message.channel, msg)











    elif message.content.startswith(",xp a") or message.content.startswith(",xp b") or message.content.startswith(
            ",xp c") or message.content.startswith(",xp d") or message.content.startswith(
            ",xp e") or message.content.startswith(",xp f") or message.content.startswith(
            ",xp g") or message.content.startswith(",xp h") or message.content.startswith(
            ",xp i") or message.content.startswith(",xp j") or message.content.startswith(
            ",xp k") or message.content.startswith(",xp l") or message.content.startswith(
            ",xp m") or message.content.startswith(",xp n") or message.content.startswith(
            ",xp o") or message.content.startswith(",xp p") or message.content.startswith(
            ",xp q") or message.content.startswith(",xp r") or message.content.startswith(
            ",xp s") or message.content.startswith(",xp t") or message.content.startswith(
            ",xp u") or message.content.startswith(",xp v") or message.content.startswith(
            ",xp w") or message.content.startswith(",xp x") or message.content.startswith(
            ",xp y") or message.content.startswith(",xp z") or message.content.startswith(
            ",xp 1") or message.content.startswith(",xp 2") or message.content.startswith(
            ",xp 3") or message.content.startswith(",xp 4") or message.content.startswith(
            ",xp 5") or message.content.startswith(",xp 6") or message.content.startswith(
            ",xp 7") or message.content.startswith(",xp 8") or message.content.startswith(
            ",xp 9") or message.content.startswith(",xp 0") or message.content.startswith(
            ",xp A") or message.content.startswith(",xp B") or message.content.startswith(
            ",xp C") or message.content.startswith(",xp D") or message.content.startswith(
            ",xp E") or message.content.startswith(",xp F") or message.content.startswith(
            ",xp G") or message.content.startswith(",xp H") or message.content.startswith(
            ",xp I") or message.content.startswith(",xp J") or message.content.startswith(
            ",xp K") or message.content.startswith(",xp L") or message.content.startswith(
            ",xp M") or message.content.startswith(",xp N") or message.content.startswith(
            ",xp O") or message.content.startswith(",xp P") or message.content.startswith(
            ",xp Q") or message.content.startswith(",xp R") or message.content.startswith(
            ",xp S") or message.content.startswith(",xp T") or message.content.startswith(
            ",xp U") or message.content.startswith(",xp V") or message.content.startswith(
            ",xp W") or message.content.startswith(",xp X") or message.content.startswith(
            ",xp Y") or message.content.startswith(",xp Z"):
        await client.send_typing(message.channel)
        _, username = message.content.split(' ', 1)
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(username)
        response = requests.get(url)
        if response.status_code == requests.codes.not_found:
            notfound = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
            await client.send_message(message.channel, notfound)
        stats = response.text.split(",")
        print(stats)
        attxp = stats[4]
        skill_total = stats[2].split("\n")[0]
        attxp1 = attxp.split("\n")
        realattxp = attxp1[0]

        del stats[0]
        del stats[1]
        del stats[2]
        print(stats)
        for i in range(0, int(len(stats) / 2)):
            print(i)

            del stats[i]  # +1
        del stats[23]
        del stats[23]
        del stats[23]
        del stats[23]
        del stats[23]
        new_stats = response.text.split(",")
        stats.insert(1, new_stats[3])
        # stats is now [total,+23skills]
        stats = [i.split("\n", 1)[0] for i in stats]

        print(stats)

        embed = discord.Embed(color=0xFF0000)
        embed.set_author(name="XP for " + username,
                         icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")  # This is for clean look
        embed.add_field(name='\u200b', value="<:Attack:498591810210496515>" + format(int(realattxp),
                                                                                     ",d") + "\n <:Strength:498592002288517121>" + format(
            int(stats[3]), ",d") + "\n  <:Defence:498591848974254083>" + format(int(stats[2]),
                                                                                ",d") + "\n  <:Ranged:498592002129133570>" + format(
            int(stats[5]), ",d") + "\n  <:Prayer:498592002276065280>" + format(int(stats[6]),
                                                                               ",d") + "\n <:Magic:498591928909299762>" + format(
            int(stats[7]), ",d") + "\n<:Runecrafting:498592002259156993>" + format(int(stats[21]),
                                                                                   ",d") + "\n<:Construction:498591820477890600>" + format(
            int(stats[23]), ",d"), inline=True)
        embed.add_field(name='\u200b', value="<:Hitpoints:498591928938397707>" + format(int(stats[4]),
                                                                                        ",d") + "\n<:Agility:498591795006013471>" + format(
            int(stats[17]), ",d") + "\n<:Herblore:498591928816893954>" + format(int(stats[16]),
                                                                                ",d") + "\n <:Thieving:498592002435186688>" + format(
            int(stats[18]), ",d") + "\n<:Crafting:498591838652071956>" + format(int(stats[13]),
                                                                                ",d") + "\n<:Fletching:498591893513306112>" + format(
            int(stats[10]), ",d") + "\n<:Slayer:498592001902510092>" + format(int(stats[19]),
                                                                              ",d") + "\n<:Hunter:498591928779145217>" + format(
            int(stats[22]), ",d"), inline=True)
        embed.add_field(name='\u200b', value="<:Mining:498591929433456642>" + format(int(stats[15]),
                                                                                     ",d") + "\n<:Smithing:498592002276065281>" + format(
            int(stats[14]), ",d") + "\n<:Fishing:498591879852589056>" + format(int(stats[11]),
                                                                               ",d") + "\n<:Cooking:498591829357494272>" + format(
            int(stats[8]), ",d") + "\n <:Fishing:498591879852589056>" + format(int(stats[11]),
                                                                               ",d") + "\n<:Woodcutting:498592002393243648>" + format(
            int(stats[9]), ",d") + "\n<:Farming:498591858046271498>" + format(int(stats[20]),
                                                                              ",d") + "\n<:skilltotal:533043559989903360>" + format(
            int(skill_total), ",d"), inline=True)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(",xpto99 <@"):
        await client.send_typing(message.channel)
        name = message.content.split()[1]
        realName = name.replace("!", "")
        realName1 = realName.replace("<", "")
        realName2 = realName1.replace(">", "")
        realName3 = realName2.replace("@", "")
        exist = os.path.isfile(realName3 + "rsn.txt")
        if exist == True:
            file = open(realName3 + "rsn.txt", "r").read()
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                not_found = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, not_found)
            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name=file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")
            stats = response.text.split(",")
            print(stats)
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
            f"\n<:Hunter:498591928779145217> {z_99(int(stats[22]))}"
                            , inline=True)
            embed.add_field(name='\u200b', value=f"\n<:Mining:498591929433456642> {z_99(int(stats[15]))}"
            f"\n<:Smithing:498592002276065281> {z_99(int(stats[14]))}"
            f"\n<:Fishing:498591879852589056> {z_99(int(stats[11]))}"
            f"\n<:Cooking:498591829357494272> {z_99(int(stats[8]))}"
            f"\n<:Fishing:498591879852589056> {z_99(int(stats[11]))}"
            f"\n<:Woodcutting:498592002393243648> {z_99(int(stats[9]))}"
            f"\n<:Farming:498591858046271498> {z_99(int(stats[20]))}"
            f"\n<:skilltotal:533043559989903360> {x_99(int(skill_total))}"
                            , inline=True)
            embed.set_author(name="XP to 99 for " + file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")
            await client.send_message(message.channel, embed=embed)
            file.close()
        if exist == False:
            msg = '**<:error:513794294763618305>' + name + ' hasnt set their rsn yet, so I cant search for its xp to 99**\nYou can search for others xpto99 tho.. `,xpto99 [Rsn]`'
            await client.send_message(message.channel, msg)






    elif message.content == ",xpto99":
        await client.send_typing(message.channel)
        me = message.author.id
        exist = os.path.isfile(me + "rsn.txt")
        if exist == True:
            file = open(me + "rsn.txt", "r").read()
            url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(file)
            response = requests.get(url)
            if response.status_code == requests.codes.not_found:
                not_found = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
                await client.send_message(message.channel, not_found)
            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name=file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")
            stats = response.text.split(",")
            print(stats)
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
            f"\n<:Construction:498591820477890600> {z_99(int(stats[23]))}"
                            , inline=True)
            embed.add_field(name='\u200b', value=f"\n<:Hitpoints:498591928938397707> {z_99(int(stats[4]))}"
            f"\n<:Agility:498591795006013471> {z_99(int(stats[17]))}"
            f"\n<:Herblore:498591928816893954> {z_99(int(stats[16]))}"
            f"\n<:Thieving:498592002435186688> {z_99(int(stats[18]))}"
            f"\n<:Crafting:498591838652071956> {z_99(int(stats[13]))}"
            f"\n<:Fletching:498591893513306112> {z_99(int(stats[10]))}"
            f"\n<:Slayer:498592001902510092> {z_99(int(stats[19]))}"
            f"\n<:Hunter:498591928779145217> {z_99(int(stats[22]))}"
                            , inline=True)
            embed.add_field(name='\u200b', value=f"\n<:Mining:498591929433456642> {z_99(int(stats[15]))}"
            f"\n<:Smithing:498592002276065281> {z_99(int(stats[14]))}"
            f"\n<:Fishing:498591879852589056> {z_99(int(stats[11]))}"
            f"\n<:Cooking:498591829357494272> {z_99(int(stats[8]))}"
            f"\n<:Fishing:498591879852589056> {z_99(int(stats[11]))}"
            f"\n<:Woodcutting:498592002393243648> {z_99(int(stats[9]))}"
            f"\n<:Farming:498591858046271498> {z_99(int(stats[20]))}"
            f"\n<:skilltotal:533043559989903360> {x_99(int(skill_total))}"
                            , inline=True)
            embed.set_author(name="XP to 99 for " + file,
                             icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")
            await client.send_message(message.channel, embed=embed)
            file.close()
        if exist == False:
            msg = '**<:error:513794294763618305> You havent set your rsn yet, so I cant search for its xp to 99**\nYou can search for others xpto99 tho.. `,xpto99 [Rsn]`'
            await client.send_message(message.channel, msg)





    elif message.content.startswith(",xpto99 a") or message.content.startswith(
            ",xpto99 b") or message.content.startswith(",xpto99 c") or message.content.startswith(
            ",xpto99 d") or message.content.startswith(",xpto99 e") or message.content.startswith(
            ",xpto99 f") or message.content.startswith(",xpto99 g") or message.content.startswith(
            ",xpto99 h") or message.content.startswith(",xpto99 i") or message.content.startswith(
            ",xpto99 j") or message.content.startswith(",xpto99 k") or message.content.startswith(
            ",xpto99 l") or message.content.startswith(",xpto99 m") or message.content.startswith(
            ",xpto99 n") or message.content.startswith(",xpto99 o") or message.content.startswith(
            ",xpto99 p") or message.content.startswith(",xpto99 q") or message.content.startswith(
            ",xpto99 r") or message.content.startswith(",xpto99 s") or message.content.startswith(
            ",xpto99 t") or message.content.startswith(",xpto99 u") or message.content.startswith(
            ",xpto99 v") or message.content.startswith(",xpto99 w") or message.content.startswith(
            ",xpto99 x") or message.content.startswith(",xpto99 y") or message.content.startswith(
            ",xpto99 z") or message.content.startswith(",xpto99 1") or message.content.startswith(
            ",xpto99 2") or message.content.startswith(",xpto99 3") or message.content.startswith(
            ",xpto99 4") or message.content.startswith(",xpto99 5") or message.content.startswith(
            ",xpto99 6") or message.content.startswith(",xpto99 7") or message.content.startswith(
            ",xpto99 8") or message.content.startswith(",xpto99 9") or message.content.startswith(
            ",xpto99 0") or message.content.startswith(",xpto99 A") or message.content.startswith(
            ",xpto99 B") or message.content.startswith(",xpto99 C") or message.content.startswith(
            ",xpto99 D") or message.content.startswith(",xpto99 E") or message.content.startswith(
            ",xpto99 F") or message.content.startswith(",xpto99 G") or message.content.startswith(
            ",xpto99 H") or message.content.startswith(",xpto99 I") or message.content.startswith(
            ",xpto99 J") or message.content.startswith(",xpto99 K") or message.content.startswith(
            ",xpto99 L") or message.content.startswith(",xpto99 M") or message.content.startswith(
            ",xpto99 N") or message.content.startswith(",xpto99 O") or message.content.startswith(
            ",xpto99 P") or message.content.startswith(",xpto99 Q") or message.content.startswith(
            ",xpto99 R") or message.content.startswith(",xpto99 S") or message.content.startswith(
            ",xpto99 T") or message.content.startswith(",xpto99 U") or message.content.startswith(
            ",xpto99 V") or message.content.startswith(",xpto99 W") or message.content.startswith(
            ",xpto99 X") or message.content.startswith(",xpto99 Y") or message.content.startswith(",xpto99 Z"):
        await client.send_typing(message.channel)
        username = message.content.split(' ', 1)[1]
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(username)
        response = requests.get(url)
        if response.status_code == requests.codes.not_found:
            not_found = "**<:error:513794294763618305> Stats weren't found, the account might not exist / is banned.**"
            await client.send_message(message.channel, not_found)
        embed = discord.Embed(color=0xFF0000)
        embed.set_author(name=username,
                         icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")
        stats = response.text.split(",")
        print(stats)
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
        f"\n<:Construction:498591820477890600> {z_99(int(stats[23]))}"
                        , inline=True)
        embed.add_field(name='\u200b', value=f"\n<:Hitpoints:498591928938397707> {z_99(int(stats[4]))}"
        f"\n<:Agility:498591795006013471> {z_99(int(stats[17]))}"
        f"\n<:Herblore:498591928816893954> {z_99(int(stats[16]))}"
        f"\n<:Thieving:498592002435186688> {z_99(int(stats[18]))}"
        f"\n<:Crafting:498591838652071956> {z_99(int(stats[13]))}"
        f"\n<:Fletching:498591893513306112> {z_99(int(stats[10]))}"
        f"\n<:Slayer:498592001902510092> {z_99(int(stats[19]))}"
        f"\n<:Hunter:498591928779145217> {z_99(int(stats[22]))}"
                        , inline=True)
        embed.add_field(name='\u200b', value=f"\n<:Mining:498591929433456642> {z_99(int(stats[15]))}"
        f"\n<:Smithing:498592002276065281> {z_99(int(stats[14]))}"
        f"\n<:Fishing:498591879852589056> {z_99(int(stats[11]))}"
        f"\n<:Cooking:498591829357494272> {z_99(int(stats[8]))}"
        f"\n<:Fishing:498591879852589056> {z_99(int(stats[11]))}"
        f"\n<:Woodcutting:498592002393243648> {z_99(int(stats[9]))}"
        f"\n<:Farming:498591858046271498> {z_99(int(stats[20]))}"
        f"\n<:skilltotal:533043559989903360> {x_99(int(skill_total))}"
                        , inline=True)
        embed.set_author(name="XP to 99 for " + username,
                         icon_url="https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png")
        await client.send_message(message.channel, embed=embed)

    if message.content == (",rsn"):
        me = message.author.id
        exist = os.path.isfile("./" + me + "rsn.txt")
        profile = message.server.get_member(me)
        pfp = profile.avatar_url
        if exist == True:
            profile = message.server.get_member(me)
            pfp = profile.avatar_url
            file = open(f'{me}rsn.txt').read()
            embed = discord.Embed(colour= 0xFF0000 )
            embed.set_author(name= message.author.name + "'s Rsn", icon_url=pfp)
            embed.set_footer(text=f'{file}', icon_url='https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png')
            await client.send_message(message.channel, embed=embed)
            file.close()
        if exist == False:
            msg = '**' + message.author.name + '**, you havent set your rsn yet :confused: \nGet started by doing `,setrsn [YourRsn]`'
            await client.send_message(message.channel, msg)
            
    elif message.content.startswith(",rsn"):
        for user in message.mentions:
            name = message.content.split()[1]
            realName = name.replace("!", "")
            realName1 = realName.replace("<", "")
            realName2 = realName1.replace(">", "")
            realName3 = realName2.replace("@", "")
            exist = os.path.isfile("./" + realName3 + "rsn.txt")
            if exist == True:
                profile = message.server.get_member(realName3)
                pfp = profile.avatar_url
                file = open(f'{realName3}rsn.txt').read()
                embed = discord.Embed(colour= 0xFF0000 )
                embed.set_author(name= "{}'s Rsn".format(user.name), icon_url=pfp)
                embed.set_footer(text=f'{file}', icon_url='https://imgb.apk.tools/115/b/c/2/com.jagex.oldscape.android.png')
                await client.send_message(message.channel, embed=embed)
                file.close()
            if exist == False:
                msg = '**{}'.format(user.name) + '** hasnt set their rsn yet :confused: \nGet started by doing `,setrsn [YourRsn]`'
                await client.send_message(message.channel, msg)
            
    elif message.content.startswith("a") or message.content.startswith("b") or message.content.startswith("c") or message.content.startswith("d") or message.content.startswith("e") or message.content.startswith("f") or message.content.startswith("g") or message.content.startswith("h") or message.content.startswith("i") or message.content.startswith("j") or message.content.startswith("k") or message.content.startswith("l") or message.content.startswith("m") or message.content.startswith("n") or message.content.startswith("o") or message.content.startswith("p") or message.content.startswith("q") or message.content.startswith("r") or message.content.startswith("s") or message.content.startswith("t") or message.content.startswith("u") or message.content.startswith("v") or message.content.startswith("w") or message.content.startswith("x") or message.content.startswith("y") or message.content.startswith("z") or message.content.startswith("1") or message.content.startswith("2") or message.content.startswith("3") or message.content.startswith("4") or message.content.startswith("5") or message.content.startswith("6") or message.content.startswith("7") or message.content.startswith("8") or message.content.startswith("9") or message.content.startswith("0") or message.content.startswith("A") or message.content.startswith("B") or message.content.startswith("C") or message.content.startswith("D") or message.content.startswith("E") or message.content.startswith("F") or message.content.startswith("G") or message.content.startswith("H") or message.content.startswith("I") or message.content.startswith("J") or message.content.startswith("K") or message.content.startswith("L") or message.content.startswith("M") or message.content.startswith("N") or message.content.startswith("O") or message.content.startswith("P") or message.content.startswith("Q") or message.content.startswith("R") or message.content.startswith("S") or message.content.startswith("T") or message.content.startswith("U") or message.content.startswith("V") or message.content.startswith("W") or message.content.startswith("X") or message.content.startswith("Y") or message.content.startswith("Z"):
        if message.channel.id == "520632721400266752" or message.channel.id == "550744249155452960":
            await client.add_reaction(message, "\U0001F44D")

    elif message.content.startswith(",slap"):
        spleet = message.content.split()
        name = spleet[1]
        embed = discord.Embed(colour=discord.Colour.purple(), description ="<@" + message.author.id + "> aggressively slaps " + name)
        num = random.randint(1,12)
        if num == 1:
            embed.set_image(url="https://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif")
        if num == 2:
            embed.set_image(url="https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif?itemid=7958720")
        if num == 3:
            embed.set_image(url="https://media.giphy.com/media/NHRq0xgayvOQU/giphy.gif")
        if num == 4:
            embed.set_image(url="https://pa1.narvii.com/5845/71abe5ba3f14270105b4e53ce380a8b9672e0559_hq.gif")
        if num == 5:
            embed.set_image(url="https://cdn.discordapp.com/attachments/479391734699261982/480790043028619284/slap2.gif")
        if num == 6:
            embed.set_image(url="http://i.imgur.com/HGxqG1N.gif")
        if num == 7:
            embed.set_image(url="https://cdn.discordapp.com/attachments/479391734699261982/480790723793518603/slap3.gif")
        if num ==8:
            embed.set_image(url="https://cdn.discordapp.com/attachments/479391734699261982/480790723793518603/slap3.gif")
        if num ==9:
            embed.set_image(url="https://media1.tenor.com/images/9c7245d363a7ccd5840bd7d1532347c6/tenor.gif?itemid=4878708")
        if num ==10:
            embed.set_image(url="https://media.giphy.com/media/swoGNQawNCM7K/giphy.gif")
        if num ==11:
            embed.set_image(url="https://media.giphy.com/media/rCftUAVPLExZC/giphy.gif")
        if num ==12:
            embed.set_image(url="https://i.kym-cdn.com/photos/images/original/000/846/661/240.gif")
        await asyncio.sleep(1)
        await client.send_message(message.channel, embed=embed)
        
    elif message.content == ",pfp" or message.content == ",avatar":
        realName3 = message.author.id
        profile = message.server.get_member(realName3)
        pfp = profile.avatar_url
        await client.send_message(message.channel, pfp)

    elif message.content.startswith(",pfp") or message.content.startswith(",avatar") or message.content.startswith(",av"):
        for user in message.mentions:
            pfp = message.server.get_member(user.id).avatar_url
            pfp1 = pfp.replace(".webp", ".png")
            await client.send_message(message.channel, pfp1)

    if message.content.startswith("!tagnotify") or message.content.startswith(",tagnotify"):
            role = discord.utils.get(message.server.roles, name="Notify")
            print(role)
            await client.edit_role(message.server, role, mentionable=True)
            await client.send_message(message.author, "<:Successful:558558879110266880> **You are now able to tag @Notify, for the next 50 seconds..**")
            await asyncio.sleep(50)
            await client.edit_role(message.server, role, mentionable=False)

    if message.content.startswith("!notify on") or message.content.startswith(",notify on") or message.content.startswith("!Notify on") or message.content.startswith("!Notify On"):
            role = discord.utils.get(message.server.roles, name="Notify")
            await client.add_reaction(message, "✅")
            await client.send_message(message.author, "<:Successful:558558879110266880> **You'll now be notified for giveaways, key promos and much more!**")
            await client.add_roles(message.author, role)

    if message.content.startswith("!notify off") or message.content.startswith(",notify off") or message.content.startswith("!Notify off") or message.content.startswith("!Notify Off"):
            role = discord.utils.get(message.server.roles, name="Notify")
            await client.add_reaction(message, "✅")
            await client.send_message(message.author,"<:Successful:558558879110266880> **Notify role removed, you wont be notified anymore..**")

    elif message.content.startswith(',f'):
        await client.delete_message(message)
        args = message.content.split(" ")
        messagge = "**" + message.author.name + "** paid their respects for **" + (" ".join(args[1:])) + "**"
        sendd = await client.send_message(message.channel, messagge)
        print(sendd.content)
        await client.add_reaction(sendd, "\U0001F1EB")#\U000020E3
        await asyncio.sleep(1)
        for x in range(40):
            res = await client.wait_for_reaction(['\U0001F1EB', '\U0001F1EB'], message=sendd)
            msg = "**{0.user.name}**".format(res)
            if msg not in sendd.content:
                sendd = await client.edit_message(sendd, msg + ", " + sendd.content)
            else:
                print("Alr")




    elif message.content.startswith(",punch"):
        spleet = message.content.split()
        name = spleet[1]
        embed = discord.Embed(colour=discord.Colour.purple(), description ="<@" + message.author.id + "> punches the crap out of " + name)
        num = random.randint(1,2)
        if num == 1:
            embed.set_image(url="http://gifimage.net/wp-content/uploads/2017/09/anime-punch-gif-3.gif")
        if num == 2:
            embed.set_image(url="https://i.kym-cdn.com/photos/images/original/000/641/427/824.gif")
        await asyncio.sleep(1)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(",kiss"):
        spleet = message.content.split()
        name = spleet[1]
        embed = discord.Embed(colour=discord.Colour.purple(), description ="<@" + message.author.id + "> gently kisses " + name)
        num = random.randint(1,2)
        if num == 1:
            embed.set_image(url="https://media.giphy.com/media/12VXIxKaIEarL2/giphy.gif")
        if num == 2:
            embed.set_image(url="https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865")
        await asyncio.sleep(1)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(",kill"):
        spleet = message.content.split()
        name = spleet[1]
        embed = discord.Embed(colour=discord.Colour.purple(), description ="<@" + message.author.id + "> happily kills " + name)
        num = random.randint(1,3)
        if num == 1:
            embed.set_image(url="https://orig00.deviantart.net/ded9/f/2014/065/b/0/akame_by_excaliburne-d79790s.gif")
        if num == 2:
            embed.set_image(url="http://gifimage.net/wp-content/uploads/2017/09/anime-kill-gif-10.gif")
        if num == 3:
            embed.set_image(url="http://gifimage.net/wp-content/uploads/2017/09/anime-kill-gif-10.gif")
        await asyncio.sleep(1)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(",fight"):
        spleet = message.content.split()
        name = spleet[1]
        embed = discord.Embed(colour=discord.Colour.purple(), description ="<@" + message.author.id + "> wields his bronze dagger and fights " + name)
        num = random.randint(1,3)
        if num == 1:
            embed.set_image(url="https://media3.giphy.com/media/eR7OEDQDyA7Cg/giphy-downsized.gif")
        if num == 2:
            embed.set_image(url="https://media.giphy.com/media/4N57n3Rei8iEE/giphy.gif")
        if num == 3:
            embed.set_image(url="https://78.media.tumblr.com/e52837285c2eeb3c81e3d8fe331275d2/tumblr_nt5ah8u6DN1t89rpeo2_500.gif")
        await asyncio.sleep(1)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(",kick"):
        spleet = message.content.split()
        name = spleet[1]
        embed = discord.Embed(colour=discord.Colour.purple(), description ="<@" + message.author.id + "> swings their foot out and kicks " + name)
        num = random.randint(1,5)
        if num == 1:
            embed.set_image(url="https://media.giphy.com/media/wOly8pa4s4W88/giphy.gif")
        if num == 2:
            embed.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/001/053/707/042.gif")
        if num == 3:
            embed.set_image(url="http://gifimage.net/wp-content/uploads/2017/09/anime-kick-gif-9.gif")
        if num == 4:
            embed.set_image(url="https://media1.tenor.com/images/c2c0bfb2b48e1dd32dae803ec4e5f17c/tenor.gif?itemid=9394812")
        if num == 5:
            embed.set_image(url="https://i.kym-cdn.com/photos/images/original/001/228/265/7bf.gif")
        await asyncio.sleep(1)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith(',say'):
        if message.author.id == "303152083891257344":
            spleet = message.content.split()
            chan = spleet[1]
            args = message.content.split(" ")
            await client.send_message(client.get_channel(chan), "%s" % (" ".join(args[2:])))
            await client.delete_message(message)

    elif message.content.startswith(",roll"):
        spleet = message.content.split()
        max = int(spleet[1])
        min = 1
        roll = random.randint(min, max)
        embed = discord.Embed(colour = discord.Colour.red(), description="<a:dicegif:487670982065127424> | <@" + message.author.id + "> You rolled a **" + str(roll) + "**")
        embed.set_footer(text="On a " + str(min) + "-" + str(max) + " dice")
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(",8ball"):
        spleet = message.content.split()
        name = spleet[1]
        embed = discord.Embed(colour=discord.Colour.purple(), description ="<@" + message.author.id + "> aggressively slaps " + name)
        num = random.randint(1,12)
        if num == 1:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | Sorry, no.")
        if num == 2:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | Yes...but only for the next FIVE MINUTES")
        if num == 3:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | Lmao Yes! but dont tell anyone.")
        if num == 4:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | l0l why would u even ask that")
        if num == 5:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | lololol in ur dreams, dumbass")
        if num == 6:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | Holy CRAP yes")
        if num == 7:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | wat u dumb or something? The answer is no")
        if num == 8:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | no, but u are")
        if num == 9:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | yh i think")
        if num == 10:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | <:thinkinn:542079853109968907> are u mentally challenged. Aint gonna even answer that question")
        if num == 11:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | hell yea")
        if num == 12:
            embed = discord.Embed(colour = discord.Colour.red(), title=":8ball: | No?")
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(",run"):
        os.system('partner.py')
        await client.send_file(message.channel, "infoimg2.png")

    elif message.content.startswith(",autoend") or message.content.startswith(",autostop"):
        exist = os.path.isfile("auto.txt")
        if exist == True:
            os.remove("auto.txt")
            await client.send_message(message.channel, "Ended the auto-messages :thumbsup:")
        if exist == False:
            await client.send_message(message.channel, "I didnt find any auto running messages :frowning:")

    elif message.content.startswith(",auto"):
        if message.author.id == "303152083891257344" or "485760579437592576" in [role.id for role in message.author.roles]:
            file = open("auto.txt", "a")
            file.close()
            args = message.content.split(" ")
            delay = message.content.split()[2]
            number = int(message.content.split()[1])
            msg = await client.send_message(message.channel, '<a:Auto:503469931388600361> Ok **' + message.author.name + '**, your message will now be said **' + str(number) + ' times** every **' + str(delay) + ' seconds** :clap:')
            for x in range(1, number+1):
                exist = os.path.isfile("auto.txt")
                if exist:
                    print("ez")
                    msg = "%sᅠ" % (" ".join(args[3:]))
                    await client.send_message(message.channel, msg)
                    await asyncio.sleep(float(delay))
                if exist == False:
                    print("eneded")

    if "!g" in message.content and "01" in message.content:
        if "535883583819218964" in [role.id for role in message.author.roles]:
            name = message.content.split()[2]
            realName = name.replace("!", "")
            realName1 = realName.replace("<", "")
            realName2 = realName1.replace(">", "")
            realName3 = realName2.replace("@", "")
            if ("<@" + realName3 + ">") not in open("fkey.txt").read():
                file2 = open("faudit.txt", "a")
                file = open("fkey.txt", "a")
                file2.write(message.author.mention + " gave a key to <@" + realName3 + ">\n")
                file2.close()
                file.write("<@" + realName3 + ">\n")
                file.close()
                await client.add_reaction(message, "✅")
            elif ("<@" + realName3 + ">") in open("fkey.txt").read():
                return await client.send_message(message.channel, ":warning: **This person already got their free key**")

    if message.content.startswith(",check"):
        if "535883583819218964" in [role.id for role in message.author.roles]:
            name = message.content.split()[1]
            realName = name.replace("!", "")
            realName1 = realName.replace("<", "")
            realName2 = realName1.replace(">", "")
            realName3 = realName2.replace("@", "")
            if ("<@" + realName3 + ">") in open("fkey.txt").read():
                await client.send_message(message.channel, "<:error:513794294763618305> **This member `already` recieved their free key.**")
            if ("<@" + realName3 + ">") not in open("fkey.txt").read():
                await client.send_message(message.channel, "<:greenytick:481431838586306560> **This member `hasnt` recieved their free key**")

    if message.content.startswith(",keys audit"):
        if "535883583819218964" in [role.id for role in message.author.roles]:
            file = open("faudit.txt").read()#
            embed = discord.Embed(colour=discord.Colour.red(), description=file)
            embed.set_author(name="Burned Key Promo Audit", icon_url="https://cdn.discordapp.com/emojis/541656954175619111.png?v=1")
            await client.send_message(message.channel, embed=embed)
            file.close()


    elif message.content.startswith(",scale"):
        spleet = message.content.split()
        name = spleet[1]
        embed = discord.Embed(colour=discord.Colour.purple(), description = message.author.name + ", I rate " + name)
        num = random.randint(1,10)
        if num == 1:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **1/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498075293945298945/unknown.png")
        if num == 2:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **2/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498075248399220756/unknown.png")
        if num == 3:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **3/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498075218921783307/unknown.png")
        if num == 4:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **4/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498075185941839893/unknown.png")
        if num == 5:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **5/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498075151775170560/unknown.png")
        if num == 6:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **6/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498075107940368394/unknown.png")
        if num == 7:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **7/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498075065250742272/unknown.png")
        if num ==8:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **8/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498074870198829056/unknown.png")
        if num ==9:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **9/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498074714057474048/unknown.png")
        if num ==10:
            embed = discord.Embed(colour = discord.Colour.red(), description = "**" + message.author.name + "**, I rate " + name + "\n\n **10/10**")
            embed.set_image(url="https://cdn.discordapp.com/attachments/488429052445851651/498074642142199808/unknown.png")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith(",start"):
        global winners
        with open('words.json') as json_file:
            data = json.load(json_file)
        random_word = secrets.choice(data)
        embed1 = discord.Embed(title="A game has opened up.  It will begin in 5 seconds.", color=0x00bfff)
        message = await client.send_message(message.channel, embed=embed1)
        await asyncio.sleep(1)

        for x in range(4):
            await client.edit_message(message, embed=discord.Embed(title="A game has opened up.  It will begin in {0} seconds.".format(4 - x), color=0x00bfff))
            await asyncio.sleep(1)
        await client.edit_message(message,embed=discord.Embed(title="The word is **{0}**".format(random_word), color=0x0000ff))

        def check(m):
            return m.content == random_word and m.channel == message.channel

        msg = await client.wait_for_message(timeout=7, check=check)
        print(winners)

        try:
            await client.send_message(message.channel, "<a:winner:537014272228851723> **{0} Wins!**".format(msg.author.mention))
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
                await client.send_message(message.channel,"**<:streak:537704790487072769> {0} is on a {1} win streak!**".format(msg.author.mention, len(winners)))
        except:
            await client.send_message(message.channel,"<a:cloudclock:536988420132569131> **Times up! There was no winner..**")

    if message.content.startswith(",start"):
        with open('words.json') as json_file:
            data = json.load(json_file)
        random_word = secrets.choice(data)
        embed1 = discord.Embed(title="A game has opened up.  It will begin in 5 seconds.", color=0x00bfff)
        message = await client.send_message(message.channel, embed=embed1)
        await asyncio.sleep(1)

        for x in range(4):
            await client.edit_message(message, embed=discord.Embed(
                title="A game has opened up.  It will begin in {0} seconds.".format(4 - x), color=0x00bfff))
            await asyncio.sleep(1)
        await client.edit_message(message,
                                  embed=discord.Embed(title="The word is **{0}**".format(random_word), color=0x0000ff))

        def check(m):
            return m.content == random_word and m.channel == message.channel

        msg = await client.wait_for_message(timeout=7, check=check)
        print(winners)

        try:
            await client.send_message(message.channel,
                                      "<a:winner:537014272228851723> **{0} Wins!**".format(msg.author.mention))
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
                await client.send_message(message.channel, "**<:streak:537704790487072769> {0} is on a {1} win streak!**".format(msg.author.mention, len(winners)))
        except:
            await client.send_message(message.channel, "<a:cloudclock:536988420132569131> **Times up! There was no winner..**")

    if message.content.startswith(",pet"):
        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        img = Image.open("pet.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("OSRSFont.ttf", 16) #Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = text.split("\n")
        lists = (textwrap.TextWrapper(width=58,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        #draw.text((13,58), "{}".format(body), (0, 0, 0), font=font)
        draw.text((11,56), "{}" ":".format(body), (0, 0, 0), font=font)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")
    if ",trump" in message.content:
        img = Image.open("infoimgimg.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial", 22) #Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = text.split("\n")
        lists = (textwrap.TextWrapper(width=50,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        draw.text((43, 86), "{}".format(body), (0,0,0), font=font)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
    if ",upgrade" in message.content:
        rsns = (" ".join(message.content.split(" ")[1:])).split(",")
        rsn1 = rsns[0]
        rsn2 = rsns[1]
        rsn3 = rsns[2]
        img = Image.open("upgrade.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("basicsanssf.ttf", 60) #Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = rsn1.split("\n")
        lists = (textwrap.TextWrapper(width=15,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        #
        lines2 = rsn2.split("\n")
        lists2 = (textwrap.TextWrapper(width=15,break_long_words=False).wrap(line) for line in lines2)
        body2  = "\n".join("\n".join(list) for list in lists2)
        #
        lines3 = rsn3.split("\n")
        lists3 = (textwrap.TextWrapper(width=15,break_long_words=False).wrap(line) for line in lines3)
        body3  = "\n".join("\n".join(list) for list in lists3)
        draw.text((43, 66), "{}".format(body), (0,0,0), font=font)
        draw.text((43, 520), "{}".format(body2), (0,0,0), font=font)
        draw.text((43, 920), "{}".format(body3), (0,0,0), font=font)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")
    if ",ohno" in message.content:
        img = Image.open("ohno.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial", 30) #Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = text.split("\n")
        lists = (textwrap.TextWrapper(width=20,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        draw.text((340, 29), "{}".format(body), (0,0,0), font=font)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")

    if ",invert" in message.content:
        img_url = None
        pfp = message.author.avatar_url
        async for message in client.logs_from(message.channel, limit=500):
            url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                             message.content)
            try:
                if url[0].split('.')[-1] == 'png' or url[0].split('.')[-1] == 'jpg' or url[0].split('.')[
                    -1] == 'jpeg' or url[0].split('.')[-1] == 'gyazo.com':
                    img_url = url[0]
            except:
                pass
            if img_url:
                with aiohttp.ClientSession() as session:
                    pfp = img_url
                    async with session.get(pfp) as resp:
                        if resp.status == 200:
                            image_file = await aiofiles.open('temp.jpg', mode='wb')
                            await image_file.write(await resp.read())
                            await image_file.close()
                            image = Image.open("temp.jpg").convert("RGB")#
                            if image.mode == 'RGBA':
                                r, g, b, a = image.split()
                                rgb_image = Image.merge('RGB', (r, g, b))

                                inverted_image = PIL.ImageOps.invert(rgb_image)

                                r2, g2, b2 = inverted_image.split()

                                final_transparent_image = Image.merge('RGBA', (r2, g2, b2, a))

                                final_transparent_image.save('inverted.png')

                            else:
                                inverted_image = PIL.ImageOps.invert(image)
                                inverted_image.save('inverted.png')
                                return await client.send_file(message.channel, "inverted.png")
            if message.attachments:
                with aiohttp.ClientSession() as session:
                    pfp = message.attachments[0]['url']
                    async with session.get(pfp) as resp:
                        if resp.status == 200:
                            image_file = await aiofiles.open('temp.jpg', mode='wb')
                            await image_file.write(await resp.read())
                            await image_file.close()
                            image = Image.open("temp.jpg").convert("RGB")#
                            if image.mode == 'RGBA':
                                r, g, b, a = image.split()
                                rgb_image = Image.merge('RGB', (r, g, b))

                                inverted_image = PIL.ImageOps.invert(rgb_image)

                                r2, g2, b2 = inverted_image.split()

                                final_transparent_image = Image.merge('RGBA', (r2, g2, b2, a))

                                final_transparent_image.save('inverted.png')

                            else:
                                inverted_image = PIL.ImageOps.invert(image)
                                inverted_image.save('inverted.png')
                                return await client.send_file(message.channel, "inverted.png")


    if message.content == (",mirror"):
        img_url = None
        pfp = message.author.avatar_url
        async for message in client.logs_from(message.channel, limit=500):
            url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
            try:
                if url[0].split('.')[-1] == 'png' or url[0].split('.')[-1] == 'jpg' or url[0].split('.')[-1] == 'jpeg'  or url[0].split('.')[-1] == 'gyazo.com':
                    img_url=url[0]
            except:
                pass
            if img_url:
                with aiohttp.ClientSession() as session:
                    pfp1 =img_url
                    async with session.get(pfp) as resp:
                        if resp.status == 200:
                            async with session.get(pfp1) as resp2:
                                if resp2.status == 200:
                                    image_file = await aiofiles.open('temp.jpg', mode='wb')
                                    image_file2 = await aiofiles.open('temp2.jpg', mode='wb')
                                    await image_file2.write(await resp2.read())
                                    await image_file.write(await resp.read())
                                    await image_file.close()
                                    await image_file2.close()
                                    realName3 = message.author.id
                                    im = Image.open("temp.jpg").convert("RGB")#
                                    i1 = Image.open("temp2.jpg").convert("RGB")
                                    new_img = im.resize((260,260))#
                                    new_img2 = i1.resize((260,260))
                                    new_img.save("temp2_resized.png")#
                                    new_img2.save("temp3_resized.png")
                                    #### end of saving images and resizing
                                    im2 = Image.open("temp2_resized.png").convert("RGBA")#
                                    i2 = Image.open("temp3_resized.png").convert("RGBA")
                                    img = Image.open("mirror.png").convert("RGBA")#the image im pasting onto
                                    position = ((img.width - im2.width) // 1, #the image im pasting onto
                                                (img.height - im2.height) // 2)#the image im pasting onto
                                    final = Image.open("temp2_resized.png").convert("RGB")
                                    final2 = Image.open("temp3_resized.png").convert("RGB")
                                    npImage = np.array(final)#
                                    npImage2 = np.array(final2)
                                    h, w = final.size#
                                    alpha = Image.new('L', final.size, 0)#
                                    alpha2 = Image.new('L', final2.size, 0)
                                    draw = ImageDraw.Draw(alpha)#
                                    draw2 = ImageDraw.Draw(alpha2)
                                    draw.pieslice([0, 0, h, w], 0, 360, fill=255)#
                                    draw2.pieslice([0, 0, h, w], 0, 360, fill=255)
                                    npAlpha = np.array(alpha)#
                                    npImage = np.dstack((npImage, npAlpha))#
                                    npAlpha2 = np.array(alpha2)
                                    npImage2 = np.dstack((npImage2, npAlpha2))
                                    Image.fromarray(npImage).save('result1.png')#
                                    Image.fromarray(npImage2).save('result02.png')
                                    Image.open("result1.png")#
                                    im4 = Image.open("result1.png")#
                                    im02 = Image.open("result02.png")
                                    img.paste(im4,(348,190), im4)#
                                    img.paste(im02,(36,190), im02)
                                    img.save("result1.png")#
                                    return await client.send_file(message.channel, "result1.png")
            if message.attachments:
                with aiohttp.ClientSession() as session:
                    pfp1 = message.attachments[0]['url']
                    async with session.get(pfp) as resp:
                        if resp.status == 200:
                            async with session.get(pfp1) as resp2:
                                if resp2.status == 200:
                                    image_file = await aiofiles.open('temp.jpg', mode='wb')
                                    image_file2 = await aiofiles.open('temp2.jpg', mode='wb')
                                    await image_file2.write(await resp2.read())
                                    await image_file.write(await resp.read())
                                    await image_file.close()
                                    await image_file2.close()
                                    realName3 = message.author.id
                                    im = Image.open("temp.jpg").convert("RGB")#
                                    i1 = Image.open("temp2.jpg").convert("RGB")
                                    new_img = im.resize((260,260))#
                                    new_img2 = i1.resize((260,260))
                                    new_img.save("temp2_resized.png")#
                                    new_img2.save("temp3_resized.png")
                                    #### end of saving images and resizing
                                    im2 = Image.open("temp2_resized.png").convert("RGBA")#
                                    i2 = Image.open("temp3_resized.png").convert("RGBA")
                                    img = Image.open("mirror.png").convert("RGBA")#the image im pasting onto
                                    position = ((img.width - im2.width) // 1, #the image im pasting onto
                                                (img.height - im2.height) // 2)#the image im pasting onto
                                    final = Image.open("temp2_resized.png").convert("RGB")
                                    final2 = Image.open("temp3_resized.png").convert("RGB")
                                    npImage = np.array(final)#
                                    npImage2 = np.array(final2)
                                    h, w = final.size#
                                    alpha = Image.new('L', final.size, 0)#
                                    alpha2 = Image.new('L', final2.size, 0)
                                    draw = ImageDraw.Draw(alpha)#
                                    draw2 = ImageDraw.Draw(alpha2)
                                    draw.pieslice([0, 0, h, w], 0, 360, fill=255)#
                                    draw2.pieslice([0, 0, h, w], 0, 360, fill=255)
                                    npAlpha = np.array(alpha)#
                                    npImage = np.dstack((npImage, npAlpha))#
                                    npAlpha2 = np.array(alpha2)
                                    npImage2 = np.dstack((npImage2, npAlpha2))
                                    Image.fromarray(npImage).save('result1.png')#
                                    Image.fromarray(npImage2).save('result02.png')
                                    Image.open("result1.png")#
                                    im4 = Image.open("result1.png")#
                                    im02 = Image.open("result02.png")
                                    img.paste(im4,(348,190), im4)#
                                    img.paste(im02,(36,190), im02)
                                    img.save("result1.png")#
                                    return await client.send_file(message.channel, "result1.png")

    if message.content.startswith(",mirror"):
        name = message.content.split()[1]
        realName = name.replace("!", "")
        realName1 = realName.replace("<", "")
        realName2 = realName1.replace(">", "")
        realName3 = realName2.replace("@", "")
        profile = message.server.get_member(realName3)
        pfp = profile.avatar_url
        img_url = None
        async for message in client.logs_from(message.channel, limit=500):
            url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
            try:
                if url[0].split('.')[-1] == 'png' or url[0].split('.')[-1] == 'jpg' or url[0].split('.')[-1] == 'jpeg'  or url[0].split('.')[-1] == 'gyazo.com':
                    img_url=url[0]
            except:
                pass
            if img_url:
                with aiohttp.ClientSession() as session:
                    pfp1 =img_url
                    async with session.get(pfp) as resp:
                        if resp.status == 200:
                            async with session.get(pfp1) as resp2:
                                if resp2.status == 200:
                                    image_file = await aiofiles.open('temp.jpg', mode='wb')
                                    image_file2 = await aiofiles.open('temp2.jpg', mode='wb')
                                    await image_file2.write(await resp2.read())
                                    await image_file.write(await resp.read())
                                    await image_file.close()
                                    await image_file2.close()
                                    realName3 = message.author.id
                                    im = Image.open("temp.jpg").convert("RGB")#
                                    i1 = Image.open("temp2.jpg").convert("RGB")
                                    new_img = im.resize((260,260))#
                                    new_img2 = i1.resize((260,260))
                                    new_img.save("temp2_resized.png")#
                                    new_img2.save("temp3_resized.png")
                                    #### end of saving images and resizing
                                    im2 = Image.open("temp2_resized.png").convert("RGBA")#
                                    i2 = Image.open("temp3_resized.png").convert("RGBA")
                                    img = Image.open("mirror.png").convert("RGBA")#the image im pasting onto
                                    position = ((img.width - im2.width) // 1, #the image im pasting onto
                                                (img.height - im2.height) // 2)#the image im pasting onto
                                    final = Image.open("temp2_resized.png").convert("RGB")
                                    final2 = Image.open("temp3_resized.png").convert("RGB")
                                    npImage = np.array(final)#
                                    npImage2 = np.array(final2)
                                    h, w = final.size#
                                    alpha = Image.new('L', final.size, 0)#
                                    alpha2 = Image.new('L', final2.size, 0)
                                    draw = ImageDraw.Draw(alpha)#
                                    draw2 = ImageDraw.Draw(alpha2)
                                    draw.pieslice([0, 0, h, w], 0, 360, fill=255)#
                                    draw2.pieslice([0, 0, h, w], 0, 360, fill=255)
                                    npAlpha = np.array(alpha)#
                                    npImage = np.dstack((npImage, npAlpha))#
                                    npAlpha2 = np.array(alpha2)
                                    npImage2 = np.dstack((npImage2, npAlpha2))
                                    Image.fromarray(npImage).save('result1.png')#
                                    Image.fromarray(npImage2).save('result02.png')
                                    Image.open("result1.png")#
                                    im4 = Image.open("result1.png")#
                                    im02 = Image.open("result02.png")
                                    img.paste(im4,(348,190), im4)#
                                    img.paste(im02,(36,190), im02)
                                    img.save("result1.png")#
                                    return await client.send_file(message.channel, "result1.png")
            if message.attachments:
                with aiohttp.ClientSession() as session:
                    pfp1 = message.attachments[0]['url']
                    async with session.get(pfp) as resp:
                        if resp.status == 200:
                            async with session.get(pfp1) as resp2:
                                if resp2.status == 200:
                                    image_file = await aiofiles.open('temp.jpg', mode='wb')
                                    image_file2 = await aiofiles.open('temp2.jpg', mode='wb')
                                    await image_file2.write(await resp2.read())
                                    await image_file.write(await resp.read())
                                    await image_file.close()
                                    await image_file2.close()
                                    realName3 = message.author.id
                                    im = Image.open("temp.jpg").convert("RGB")#
                                    i1 = Image.open("temp2.jpg").convert("RGB")
                                    new_img = im.resize((260,260))#
                                    new_img2 = i1.resize((260,260))
                                    new_img.save("temp2_resized.png")#
                                    new_img2.save("temp3_resized.png")
                                    #### end of saving images and resizing
                                    im2 = Image.open("temp2_resized.png").convert("RGBA")#
                                    i2 = Image.open("temp3_resized.png").convert("RGBA")
                                    img = Image.open("mirror.png").convert("RGBA")#the image im pasting onto
                                    position = ((img.width - im2.width) // 1, #the image im pasting onto
                                                (img.height - im2.height) // 2)#the image im pasting onto
                                    final = Image.open("temp2_resized.png").convert("RGB")
                                    final2 = Image.open("temp3_resized.png").convert("RGB")
                                    npImage = np.array(final)#
                                    npImage2 = np.array(final2)
                                    h, w = final.size#
                                    alpha = Image.new('L', final.size, 0)#
                                    alpha2 = Image.new('L', final2.size, 0)
                                    draw = ImageDraw.Draw(alpha)#
                                    draw2 = ImageDraw.Draw(alpha2)
                                    draw.pieslice([0, 0, h, w], 0, 360, fill=255)#
                                    draw2.pieslice([0, 0, h, w], 0, 360, fill=255)
                                    npAlpha = np.array(alpha)#
                                    npImage = np.dstack((npImage, npAlpha))#
                                    npAlpha2 = np.array(alpha2)
                                    npImage2 = np.dstack((npImage2, npAlpha2))
                                    Image.fromarray(npImage).save('result1.png')#
                                    Image.fromarray(npImage2).save('result02.png')
                                    Image.open("result1.png")#
                                    im4 = Image.open("result1.png")#
                                    im02 = Image.open("result02.png")
                                    img.paste(im4,(348,190), im4)#
                                    img.paste(im02,(36,190), im02)
                                    img.save("result1.png")#
                                    return await client.send_file(message.channel, "result1.png")



    if ",facts" in message.content:
        img = Image.open("facts.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial", 30) #Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = text.split("\n")
        lists = (textwrap.TextWrapper(width=24,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        draw.text((40, 504), "{}".format(body), (0,0,0), font=font)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")
    if ",button" in message.content:
        rsns = (" ".join(message.content.split(" ")[1:])).split(",")
        rsn1 = rsns[0]
        rsn2 = rsns[1]
        im=Image.open("button.png")
        font = ImageFont.truetype("basicsanssf.ttf", 30)
        txt=Image.new('L', (250,500))
        draw = ImageDraw.Draw(txt)

        lines = rsn1.split("\n")
        lists = (textwrap.TextWrapper(width=14,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)

        draw.text((0, 0), body,  font=font, fill=255)
        w=txt.rotate(10.5,  expand=1)
        im.paste(ImageOps.colorize(w, (0,0,0), (0,0,0)), (48,44),  w)
        ###
        txt2=Image.new('L', (250,500))
        draw2 = ImageDraw.Draw(txt2)

        lines2 = rsn2.split("\n")
        lists2 = (textwrap.TextWrapper(width=14,break_long_words=False).wrap(line) for line in lines2)
        body2  = "\n".join("\n".join(list) for list in lists2)

        draw2.text((0, 0), body2,  font=font, fill=255)
        w2=txt2.rotate(10.5,  expand=1)
        im.paste(ImageOps.colorize(w2, (0,0,0), (0,0,0)), (230,14),  w2)
        im.save('infoimg2.png') #Change infoimg2.png if needed.
        print(body2)
        await client.send_file(message.channel, "infoimg2.png")

    if ",cmm" in message.content:
        _, text = message.content.split(' ', 1)
        im=Image.open("changemymind.png")
        font = ImageFont.truetype("basicsanssf.ttf", 30)
        txt=Image.new('L', (250,500))
        draw = ImageDraw.Draw(txt)

        lines = text.split("\n")
        lists = (textwrap.TextWrapper(width=14,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)

        draw.text((0, 0), body,  font=font, fill=255)
        w=txt.rotate(8,  expand=1)
        im.paste(ImageOps.colorize(w, (0,0,0), (0,0,0)), (260,260),  w)
        im.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")
    if ",meeting" in message.content:
        rsns = (" ".join(message.content.split(" ")[1:])).split(",")
        rsn1 = rsns[0]
        rsn2 = rsns[1]
        rsn3 = rsns[2]
        rsn4 = rsns[3]
        img = Image.open("meeting.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("basicsanssf.ttf", 24)
        font2 = ImageFont.truetype("basicsanssf.ttf", 20)#Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = rsn1.split("\n")
        lists = (textwrap.TextWrapper(width=28,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        #
        lines2 = rsn2.split("\n")
        lists2 = (textwrap.TextWrapper(width=8,break_long_words=False).wrap(line) for line in lines2)
        body2  = "\n".join("\n".join(list) for list in lists2)
        #
        lines3 = rsn3.split("\n")
        lists3 = (textwrap.TextWrapper(width=8,break_long_words=False).wrap(line) for line in lines3)
        body3  = "\n".join("\n".join(list) for list in lists3)
        #
        lines4 = rsn4.split("\n")
        lists4 = (textwrap.TextWrapper(width=14,break_long_words=False).wrap(line) for line in lines4)
        body4  = "\n".join("\n".join(list) for list in lists4)
        draw.text((160, 3), "{}".format(body), (0,0,0), font=font)
        draw.text((30, 238), "{}".format(body2), (0,0,0), font=font2)
        draw.text((170, 238), "{}".format(body3), (0,0,0), font=font2)
        draw.text((310, 248), "{}".format(body4), (0,0,0), font=font2)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")
    if ",jemmy" in message.content:
        img = Image.open("jemmy.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("whitney-book.otf", 24) #Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = text.split("\n")
        lists = (textwrap.TextWrapper(width=66,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        draw.text((120,60), "{}".format(body), (227 ,228, 234), font=font)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")
    if ",pm" in message.content:
        img = Image.open("pm.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("OSRSFont.ttf", 16) #Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = text.split("\n")
        lists = (textwrap.TextWrapper(width=58,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        draw.text((37,84), "{}".format(body), (0, 0, 0), font=font)
        draw.text((36,83), "{}".format(body), (0, 255, 255), font=font)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")
    if ",fakepet" in message.content:
        img = Image.open("pet.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("OSRSFont.ttf", 16) #Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = text.split("\n")
        lists = (textwrap.TextWrapper(width=58,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        #draw.text((13,58), "{}".format(body), (0, 0, 0), font=font)
        draw.text((11,56), "{}" ":".format(body), (0, 0, 0), font=font)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")
    if ",ely" in message.content:
        img = Image.open("ely.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("OSRSFont.ttf", 16) #Make sure you insert a valid font from your folder.
        _, text = message.content.split(' ', 1)
        lines = text.split("\n")
        lists = (textwrap.TextWrapper(width=50,break_long_words=False).wrap(line) for line in lines)
        body  = "\n".join("\n".join(list) for list in lists)
        kc = message.content.split()[1]
        name = message.content.split(" ")
        draw.text((202,90), "{}".format(kc), (255,0,0), font=font)
        draw.text((11,104), "{}" " received a drop: Elysian sigil".format("%s" % (" ".join(name[2:]))), (0, 95, 1), font=font)
        draw.text((11,120), "{}" ":".format("%s" % (" ".join(name[2:]))), (0, 0, 0), font=font)
        img.save('infoimg2.png') #Change infoimg2.png if needed.
        await client.send_file(message.channel, "infoimg2.png")

    if message.content == (",pcard") or message.content == (",profile background") or message.content == (",background"):
        profile = message.server.get_member(message.author.id)
        pfp = profile.avatar_url
        embed = discord.Embed(color=0xFF0000, title="Change Profile Background to:", description="**Background 1: `,setbackground 1` \nBackground 2: `,setbackground 2`**")
        embed.set_footer(text="To check background cards do ,view [number]")
        embed.set_author(name=message.author.name + "'s backgrounds", icon_url=pfp)
        msg = await client.send_message(message.channel, embed=embed)

    if message.content == (",view"):
        await client.send_message(message.channel, "Please specify a `background number`\nE.g `,view 2`")

    if message.content == (",view 1"):
        await client.send_message(message.channel, "`background 1`")
        await client.send_file(message.channel, "profile.png")

    if message.content == (",view 2"):
        await client.send_message(message.channel, "`background 2`")
        await client.send_file(message.channel, "profile2.png")

    if message.content == (",setbackground 2"):
        User = "<@" + message.author.id + ">"  # if ("<@" + realName3 + ">") not in open("pcard.txt").read():
        if (User) in open("pcard.txt").read():
            await client.send_message(message.channel, "**<:error:513794294763618305> You already have `background 2` set..**")
        if (User) not in open("pcard.txt").read():
            file = open("pcard.txt", "a")
            file.write(User + "\n")
            file.close()
            await client.send_message(message.channel, "**<:Successful:558558879110266880> `background 2` is now your profile background.**")

    if message.content == (",setbackground 1"):
        User = "<@" + message.author.id + ">"  # if ("<@" + realName3 + ">") not in open("pcard.txt").read():
        with open("pcard.txt", "r") as f:
            lines = f.readlines()
        with open("pcard.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != User:
                    f.write(line)
        await client.send_message(message.channel,"**<:Successful:558558879110266880> `background 1` is now your profile background.**" )

    if message.content.startswith(",rep"):
        with aiohttp.ClientSession() as session:
            name = message.content.split()[1]
            realName = name.replace("!", "")
            realName1 = realName.replace("<", "")
            realName2 = realName1.replace(">", "")
            realName3 = realName2.replace("@", "")
            profile = message.server.get_member(realName3)
            pfp = profile.avatar_url
            async with session.get(pfp) as resp:
                if resp.status == 200:
                    date = time.time()
                    timefile = os.path.isfile("reptime" + message.author.id + ".txt")

                    if timefile == False:

                        if message.content.split()[1] != "<@!" + message.author.id + ">" and message.content.split()[1] != "<@" + message.author.id + ">":
                            name = message.content.split()[1]
                            realName = name.replace("!", "")
                            realName1 = realName.replace("<", "")
                            realName2 = realName1.replace(">", "")
                            realName3 = realName2.replace("@", "")
                            exist = os.path.isfile("rep" + realName3 + ".txt")
                            if exist == False:
                                file = open("rep" + realName3 + ".txt","w")
                                file.write("1")
                                file.close()
                                image_file = await aiofiles.open('temp.jpg', mode='wb')
                                await image_file.write(await resp.read())
                                await image_file.close()
                                realName3 = message.author.id
                                im = Image.open("temp.jpg").convert("RGB")
                                img = Image.open("rep.png").convert("RGBA")
                                new_img = im.resize((50, 50))
                                new_img.save("temp2_resized.jpg")
                                im3 = Image.open('temp2_resized.jpg')
                                im3.save("temp2_resized.png")
                                final = Image.open("temp2_resized.png").convert("RGB")
                                npImage = np.array(final)
                                h, w = final.size
                                alpha = Image.new('L', final.size, 0)
                                draw = ImageDraw.Draw(alpha)
                                draw.pieslice([0, 0, h, w], 0, 360, fill=255)  #
                                npAlpha = np.array(alpha)
                                npImage = np.dstack((npImage, npAlpha))
                                Image.fromarray(npImage).save('result1.png')
                                Image.open("result1.png")
                                im4 = Image.open("result1.png")
                                position = ((img.width - img.width) // 1, (img.height - img.height) // 2)
                                img.paste(im4, (10,1), im4)
                                img.save("reputation.png")
                                await client.send_file(message.channel, "reputation.png")
                            if exist == True:
                                file = open("rep" + realName3 + ".txt","r")
                                a = file.read()
                                newRep = int(a) + 1
                                file.close()
                                file = open("rep" + realName3 + ".txt","w")
                                file.write(str(newRep))
                                file.close()
                                image_file = await aiofiles.open('temp.jpg', mode='wb')
                                await image_file.write(await resp.read())
                                await image_file.close()
                                realName3 = message.author.id
                                im = Image.open("temp.jpg").convert("RGB")
                                img = Image.open("rep.png").convert("RGBA")
                                new_img = im.resize((50, 50))
                                new_img.save("temp2_resized.jpg")
                                im3 = Image.open('temp2_resized.jpg')
                                im3.save("temp2_resized.png")
                                final = Image.open("temp2_resized.png").convert("RGB")
                                npImage = np.array(final)
                                h, w = final.size
                                alpha = Image.new('L', final.size, 0)
                                draw = ImageDraw.Draw(alpha)
                                draw.pieslice([0, 0, h, w], 0, 360, fill=255)  #
                                npAlpha = np.array(alpha)
                                npImage = np.dstack((npImage, npAlpha))
                                Image.fromarray(npImage).save('result1.png')
                                Image.open("result1.png")
                                im4 = Image.open("result1.png")
                                position = ((img.width - img.width) // 1, (img.height - img.height) // 2)
                                img.paste(im4, (10,1), im4)
                                img.save("reputation.png")
                                await client.send_file(message.channel, "reputation.png")
                            timed = open("reptime" + message.author.id + ".txt","w")

                            timed.write(str(int(date)))
                            timed.close()
                        else:
                            await client.send_message(message.channel, "You cant rep yourself lol")

                    if timefile == True:
                        file = open("reptime" + message.author.id + ".txt")
                        old = file.read()
                        diff = int(time.time()) - int(old)
                        file.close()
                        if diff >= 86400: #24hrs
                            os.remove("reptime" + message.author.id + ".txt")
                            if message.content.split()[1] != "<@!" + message.author.id + ">" and message.content.split()[1] != "<@" + message.author.id + ">":
                                name = message.content.split()[1]
                                realName = name.replace("!", "")
                                realName1 = realName.replace("<", "")
                                realName2 = realName1.replace(">", "")
                                realName3 = realName2.replace("@", "")
                                exist = os.path.isfile("rep" + realName3 + ".txt")
                                if exist == False:
                                    file = open("rep" + realName3 + ".txt","w")
                                    file.write("1")
                                    file.close()
                                    image_file = await aiofiles.open('temp.jpg', mode='wb')
                                    await image_file.write(await resp.read())
                                    await image_file.close()
                                    realName3 = message.author.id
                                    im = Image.open("temp.jpg").convert("RGB")
                                    img = Image.open("rep.png").convert("RGBA")
                                    new_img = im.resize((50, 50))
                                    new_img.save("temp2_resized.jpg")
                                    im3 = Image.open('temp2_resized.jpg')
                                    im3.save("temp2_resized.png")
                                    final = Image.open("temp2_resized.png").convert("RGB")
                                    npImage = np.array(final)
                                    h, w = final.size
                                    alpha = Image.new('L', final.size, 0)
                                    draw = ImageDraw.Draw(alpha)
                                    draw.pieslice([0, 0, h, w], 0, 360, fill=255)  #
                                    npAlpha = np.array(alpha)
                                    npImage = np.dstack((npImage, npAlpha))
                                    Image.fromarray(npImage).save('result1.png')
                                    Image.open("result1.png")
                                    im4 = Image.open("result1.png")
                                    position = ((img.width - img.width) // 1, (img.height - img.height) // 2)
                                    img.paste(im4, (10,1), im4)
                                    img.save("reputation.png")
                                    await client.send_file(message.channel, "reputation.png")
                                if exist == True:
                                    file = open("rep" + realName3 + ".txt","r")
                                    a = file.read()
                                    newRep = int(a) + 1
                                    file.close()
                                    file = open("rep" + realName3 + ".txt","w")
                                    file.write(str(newRep))
                                    file.close()
                                    image_file = await aiofiles.open('temp.jpg', mode='wb')
                                    await image_file.write(await resp.read())
                                    await image_file.close()
                                    realName3 = message.author.id
                                    im = Image.open("temp.jpg").convert("RGB")
                                    img = Image.open("rep.png").convert("RGBA")
                                    new_img = im.resize((50, 50))
                                    new_img.save("temp2_resized.jpg")
                                    im3 = Image.open('temp2_resized.jpg')
                                    im3.save("temp2_resized.png")
                                    final = Image.open("temp2_resized.png").convert("RGB")
                                    npImage = np.array(final)
                                    h, w = final.size
                                    alpha = Image.new('L', final.size, 0)
                                    draw = ImageDraw.Draw(alpha)
                                    draw.pieslice([0, 0, h, w], 0, 360, fill=255)  #
                                    npAlpha = np.array(alpha)
                                    npImage = np.dstack((npImage, npAlpha))
                                    Image.fromarray(npImage).save('result1.png')
                                    Image.open("result1.png")
                                    im4 = Image.open("result1.png")
                                    position = ((img.width - img.width) // 1, (img.height - img.height) // 2)
                                    img.paste(im4, position, im4)
                                    img.save("reputation.png")
                                    await client.send_file(message.channel, "reputation.png")
                                timed = open("reptime" + message.author.id + ".txt","w")

                                timed.write(str(int(date)))
                                timed.close()
                        if diff < 86400:
                            await client.send_message(message.channel, "You cant rep again today..")

    if message.content == (",profile") or message.content == (",p"):
        with aiohttp.ClientSession() as session:
            pfp = message.author.avatar_url
            async with session.get(pfp) as resp:
                if resp.status == 200:
                    image_file = await aiofiles.open('temp.jpg', mode='wb')
                    await image_file.write(await resp.read())
                    await image_file.close()
                    realName3 = message.author.id
                    im = Image.open("temp.jpg").convert("RGB")
                    new_img = im.resize((254, 254))
                    new_img.save("temp2_resized.jpg")
                    font1 = ImageFont.truetype("inkfree.ttf", 47)
                    font2 = ImageFont.truetype("inkfree.ttf", 47)  # Make sure you insert a valid font from your folder.
                    font = ImageFont.truetype("inkfree.ttf", 80)
                    profile = os.path.isfile(realName3 + "profilee.png")
                    exist = os.path.isfile(realName3 + "rsn.txt")
                    exis = os.path.isfile("rep" + realName3 + ".txt")
                    exi = os.path.isfile("credits" + realName3 + ".txt")
                    ex = os.path.isfile(realName3 + "wins.txt")
                    if profile == True:
                        image_file = await aiofiles.open('temp.jpg', mode='wb')
                        await image_file.write(await resp.read())
                        await image_file.close()
                        realName3 = message.author.id
                        im = Image.open("temp.jpg").convert("RGB")
                        img = Image.open("profile.png").convert("RGBA")
                        new_img = im.resize((250, 250))
                        new_img.save("temp2_resized.jpg")
                        im3 = Image.open('temp2_resized.jpg')
                        im3.save("temp2_resized.png")
                        final = Image.open("temp2_resized.png").convert("RGB")
                        npImage = np.array(final)
                        h, w = final.size
                        alpha = Image.new('L', final.size, 0)
                        draw = ImageDraw.Draw(alpha)
                        draw.pieslice([0, 0, h, w], 0, 360, fill=255)  #
                        npAlpha = np.array(alpha)
                        npImage = np.dstack((npImage, npAlpha))
                        Image.fromarray(npImage).save('result1.png')
                        Image.open("result1.png")
                        im4 = Image.open("result1.png")
                        position = ((img.width - img.width) // 1, (img.height - img.height) // 2)
                        img.paste(im4, position, im4)
                    if profile == False:
                        image_file = await aiofiles.open('temp.jpg', mode='wb')
                        await image_file.write(await resp.read())
                        await image_file.close()
                        realName3 = message.author.id
                        im = Image.open("temp.jpg").convert("RGB")
                        if ("<@" + realName3 + ">") not in open("pcard.txt").read():
                            img = Image.open("profile.png").convert("RGBA")
                        else:
                            img = Image.open("profile2.png").convert("RGBA")
                        new_img = im.resize((256, 255))
                        new_img.save("temp2_resized.jpg")
                        im3 = Image.open('temp2_resized.jpg')
                        im3.save("temp2_resized.png")
                        final = Image.open("temp2_resized.png").convert("RGB")
                        npImage = np.array(final)
                        h, w = final.size
                        alpha = Image.new('L', final.size, 0)
                        draw = ImageDraw.Draw(alpha)
                        draw.pieslice([0, 0, h, w], 0, 360, fill=255)
                        npAlpha = np.array(alpha)
                        npImage = np.dstack((npImage, npAlpha))
                        Image.fromarray(npImage).save('result1.png')
                        Image.open("result1.png")
                        im4 = Image.open("result1.png")
                        img.paste(im4, (64,47), im4)
                    if exist == False:
                        draw = ImageDraw.Draw(img)
                        draw.text((350,125), message.author.name, (225, 225, 225), font=font)
                        draw.text((406,230), "Rsn Not Set", (225, 225, 225), font=font1)
                    if exist == True:
                        realName3 = message.author.id
                        file = open(realName3 + "rsn.txt").read()
                        draw = ImageDraw.Draw(img)
                        draw.text((350,125), message.author.name, (225, 225, 225), font=font)
                        draw.text((406,230), file, (225, 225, 225), font=font1)
                    if exis == True:
                        realName3 = message.author.id
                        file = open("rep" + realName3 + ".txt", "r")
                        draw = ImageDraw.Draw(img)
                        a = file.read()
                        draw.text((575,290), a + " Rep", (255,255,255), font=font2)
                        file.close()
                    if exis == False:
                        draw = ImageDraw.Draw(img)
                        draw.text((575,290), "0 Rep", (255,255,255), font=font2)
                    if exi == True:
                        realName3 = message.author.id
                        file = open("credits" + realName3 + ".txt", "r")
                        draw = ImageDraw.Draw(img)
                        b = file.read()
                        #draw.text((855, 210), b, (225, 225, 225), font=font1)
                        file.close()
                    if exi == False:
                        print("none")
                        #draw.text((855, 210), "0", (225, 225, 225), font=font1)
                    if ex == True:
                        realName3 = message.author.id
                        file = open(realName3 + "wins.txt", "r")
                        draw = ImageDraw.Draw(img)
                        b = file.read()
                        draw.text((406,290), b, (225, 225, 225), font=font1)
                        file.close()
                        img.save("temp2.png")
                        await client.send_file(message.channel, r'temp2.png')
                    if ex == False:
                        draw.text((406,290), "0", (225, 225, 225), font=font1)
                        img.save("temp2.png")
                        await client.send_file(message.channel, r'temp2.png')

    if message.content.startswith(",profile") or message.content.startswith(",p "):
            with aiohttp.ClientSession() as session:
                for user in message.mentions:
                    name = message.content.split()[1]
                    realName = name.replace("!", "")
                    realName1 = realName.replace("<", "")
                    realName2 = realName1.replace(">", "")
                    realName3 = realName2.replace("@", "")
                    profile = message.server.get_member(realName3)
                    pfp = profile.avatar_url
                    async with session.get(pfp) as resp:
                        if resp.status == 200:
                            image_file = await aiofiles.open('temp.jpg', mode='wb')
                            await image_file.write(await resp.read())
                            await image_file.close()
                            im = Image.open("temp.jpg").convert("RGB")
                            new_img = im.resize((254, 254))
                            new_img.save("temp2_resized.jpg")
                            font1 = ImageFont.truetype("inkfree.ttf", 47)
                            font2 = ImageFont.truetype("inkfree.ttf",
                                                       47)  # Make sure you insert a valid font from your folder.
                            font = ImageFont.truetype("inkfree.ttf", 80)
                            profile = os.path.isfile(realName3 + "profile.png")
                            exist = os.path.isfile(realName3 + "rsn.txt")
                            exis = os.path.isfile("rep" + realName3 + ".txt")
                            exi = os.path.isfile("credits" + realName3 + ".txt")
                            ex = os.path.isfile(realName3 + "wins.txt")
                            if profile == True:
                                image_file = await aiofiles.open('temp.jpg', mode='wb')
                                await image_file.write(await resp.read())
                                await image_file.close()
                                im = Image.open("temp.jpg").convert("RGB")
                                if ("<@" + realName3 + ">") not in open("pcard.txt").read():
                                    img = Image.open("profile.png").convert("RGBA")
                                else:
                                    img = Image.open("profile2.png").convert("RGBA")
                                new_img = im.resize((250, 250))
                                new_img.save("temp2_resized.jpg")
                                im3 = Image.open('temp2_resized.jpg')
                                im3.save("temp2_resized.png")
                                final = Image.open("temp2_resized.png").convert("RGB")
                                npImage = np.array(final)
                                h, w = final.size
                                alpha = Image.new('L', final.size, 0)
                                draw = ImageDraw.Draw(alpha)
                                draw.pieslice([0, 0, h, w], 0, 360, fill=255)  #
                                npAlpha = np.array(alpha)
                                npImage = np.dstack((npImage, npAlpha))
                                Image.fromarray(npImage).save('result1.png')
                                Image.open("result1.png")
                                im4 = Image.open("result1.png")
                                position = ((img.width - img.width) // 1, (img.height - img.height) // 2)
                                img.paste(im4, position, im4)
                            if profile == False:
                                image_file = await aiofiles.open('temp.jpg', mode='wb')
                                await image_file.write(await resp.read())
                                await image_file.close()
                                im = Image.open("temp.jpg").convert("RGB")
                                if ("<@" + realName3 + ">") not in open("pcard.txt").read():
                                    img = Image.open("profile.png").convert("RGBA")
                                else:
                                    img = Image.open("profile2.png").convert("RGBA")
                                new_img = im.resize((256, 255))
                                new_img.save("temp2_resized.jpg")
                                im3 = Image.open('temp2_resized.jpg')
                                im3.save("temp2_resized.png")
                                final = Image.open("temp2_resized.png").convert("RGB")
                                npImage = np.array(final)
                                h, w = final.size
                                alpha = Image.new('L', final.size, 0)
                                draw = ImageDraw.Draw(alpha)
                                draw.pieslice([0, 0, h, w], 0, 360, fill=255)
                                npAlpha = np.array(alpha)
                                npImage = np.dstack((npImage, npAlpha))
                                Image.fromarray(npImage).save('result1.png')
                                Image.open("result1.png")
                                im4 = Image.open("result1.png")
                                img.paste(im4, (64, 47), im4)
                            if exist == False:
                                draw = ImageDraw.Draw(img)
                                draw.text((350, 125), "{}".format(user.name), (225, 225, 225), font=font)
                                draw.text((406, 230), "Rsn Not Set", (225, 225, 225), font=font1)
                            if exist == True:
                                file = open(realName3 + "rsn.txt").read()
                                draw = ImageDraw.Draw(img)
                                draw.text((350, 125), "{}".format(user.name), (225, 225, 225), font=font)
                                draw.text((406, 230), file, (225, 225, 225), font=font1)
                            if exis == True:
                                file = open("rep" + realName3 + ".txt", "r")
                                draw = ImageDraw.Draw(img)
                                a = file.read()
                                draw.text((575, 290), a + " Rep", (255, 255, 255), font=font2)
                                file.close()
                            if exis == False:
                                draw = ImageDraw.Draw(img)
                                draw.text((575, 290), "0 Rep", (255, 255, 255), font=font2)
                            if exi == True:
                                file = open("credits" + realName3 + ".txt", "r")
                                draw = ImageDraw.Draw(img)
                                b = file.read()
                                # draw.text((855, 210), b, (225, 225, 225), font=font1)
                                file.close()
                            if exi == False:
                                print("none")
                                # draw.text((855, 210), "0", (225, 225, 225), font=font1)
                            if ex == True:
                                file = open(realName3 + "wins.txt", "r")
                                draw = ImageDraw.Draw(img)
                                b = file.read()
                                draw.text((406, 290), b, (225, 225, 225), font=font1)
                                file.close()
                                img.save("temp2.png")
                                await client.send_file(message.channel, r'temp2.png')
                            if ex == False:
                                draw.text((406, 290), "0", (225, 225, 225), font=font1)
                                img.save("temp2.png")
                                await client.send_file(message.channel, r'temp2.png')

    if message.content.startswith(",setrsn"):
        args = message.content.split(" ")
        file = open(message.author.id + "rsn.txt", "w")
        file.write("%s" % (" ".join(args[1:])))
        file.close()
        msg = "<:appletick:479728914432786443> RSN successfully added."
        await client.send_message(message.channel, msg)
        
    if message.content.startswith(",quest"):
        questname = message.content.split()
        if len(questname) == 2:
            query = questname[1].upper()
            print(query)
            with open("quests.json", encoding="utf8") as jsonfile:
                data = json.load(jsonfile)
                embed = discord.Embed(
                    title=questname[1], description=data[query]["description"])
                embed.add_field(name='**Difficulty**',
                                value=data[query]["difficulty"])
                embed.add_field(name='**Length**',
                                value=data[query]["length"])
                embed.add_field(name='Requirements',
                                value=data[query]["requirements"][0])
                embed.add_field(name='Rewards',
                                value=', '.join(data[query]["rewards"]))
                await client.send_message(message.channel, embed=embed)
        elif len(questname) == 3:
            query2 = ''.join(questname[1].upper() + questname[2].upper())
            print(query2)
            with open("quests.json", encoding="utf8") as jsonfile:
                data = json.load(jsonfile)
                embed = discord.Embed(
                    title=''.join(questname[1] + " " + questname[2]), description=data[query2]["description"])
                embed.add_field(name = '**Difficulty**',
                                value = data[query2]["difficulty"])
                embed.add_field(name = '**Length**',
                                value = data[query2]["length"])
                embed.add_field(name = 'Requirements',
                                value = data[query2]["requirements"][0])
                embed.add_field(name = 'Rewards',
                                value = ', '.join(data[query2]["rewards"]))
                await client.send_message(message.channel, embed = embed)
        elif len(questname) == 4:
            query3=''.join(questname[1].upper(
            ) + questname[2].upper() + questname[3].upper())
            print(query2)
            with open("quests.json", encoding = "utf8") as jsonfile:
                data=json.load(jsonfile)
                embed=discord.Embed(
                    title=' '.join(questname[1] + " " + questname[2] + " " + questname[3]), description=data[query]["description"])
                embed.add_field(name='**Difficulty**',
                                value=data[query3]["difficulty"])
                embed.add_field(name='**Length**',
                                value=data[query3]["length"])
                embed.add_field(name='Requirements',
                                value=data[query3]["requirements"][0])
                embed.add_field(name='Rewards',
                                value=', '.join(data[query3]["rewards"]))
                await client.send_message(message.channel, embed=embed)
        elif len(questname) == 5:
            query4 = ''.join(questname[1].upper(
            ) + questname[2].upper() + questname[3] + questname[4].upper())
            print(query2)
            with open("quests.json", encoding="utf8") as jsonfile:
                data = json.load(jsonfile)
                embed = discord.Embed(
                    title=' '.join(questname[1] + " " + questname[2] + " " + questname[3] + " " + questname[4]), description=data[query]["description"])
                embed.add_field(name='**Difficulty**',
                                value=data[query4]["difficulty"])
                embed.add_field(name='**Length**',
                                value=data[query4]["length"])
                embed.add_field(name='Requirements',
                                value=data[query4]["requirements"][0])
                embed.add_field(name='Rewards',
                                value=', '.join(data[query4]["rewards"]))
        elif len(questname) == 6:
            query5 = ''.join(questname[1].upper(
            ) + questname[2].upper() + questname[3] + questname[4] + questname[5].upper())
            print(query2)
            with open("quests.json", encoding="utf8") as jsonfile:
                data = json.load(jsonfile)
                embed = discord.Embed(
                    title=' '.join(questname[1] + " " + questname[2] + " " + questname[3] + " " + questname[4] + questname[5]), description=data[query]["description"])
                embed.add_field(name='**Difficulty**',
                                value=data[query5]["difficulty"])
                embed.add_field(name='**Length**',
                                value=data[query5]["length"])
                embed.add_field(name='Requirements',
                                value=data[query5]["requirements"][0])
                embed.add_field(name='Rewards',
                                value=', '.join(data[query5]["rewards"]))
                await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(""):
        if message.channel.id == "520632721400266752" or message.channel.id == "550744249155452960":
            you = message.author.id
            args = message.content.split(" ")
            file = open(message.author.id + "rsn.txt", "w")
            file.write("%s" % (" ".join(args[0:])))
            file.write(args)
            file.close()
            await client.delete_message(message)

    if message.content.startswith(",suggest ") or message.content.startswith(",request") or message.content.startswith(",feature") or message.content.startswith(",make"):
        args = message.content.split(" ")
        msg = ':triangular_flag_on_post: Your suggestion was sent to Apple and he\'ll decide if he can make it or not'
        msg2 = "%s" % (" ".join(args[1:])) + "\n\n**From: " + message.author.mention + " \nServer: `" + message.server.name + "`**"
        await client.send_message(client.get_channel('546644834836938772'), msg2)
        await client.send_message(message.channel, msg)

    if message.content == (",suggest"):
        await client.send_message(message.channel, 'You have to suggest something \nEg: `,suggest create a ranking system`')







            
client.run("NTYwNTUwODA1MDU3NTY4NzY5.D31lIg.E8f8YLMmoLv0kPBLci2y3V1ZGP0") #End of script
