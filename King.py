
import discord
from discord.ext import commands
import asyncio
import sqlite3


client = discord.Client()

@client.event
async def on_ready():
    print("✔ Connected!\n")


prefix = ","
Client = discord.Client()
client = commands.Bot(command_prefix = ',')
owner = int(303152083891257344)


@client.event
async def on_member_join(member):
    await member.guild.get_channel(582546718336483329).edit(name="Castle: {} Members".format(member.guild.member_count))
    #ez = await member.guild.get_channel(582286500503355402)
    await member.guild.get_channel(582286500503355402).send(f'<a:wavee:582898412177981470> **Welcome** to the **Castle**, {member.mention}! Take a seat in <#582286500503355402> and enjoy yourself | Now: **{member.guild.member_count} Members**')
    await member.guild.get_channel(582290523067514880).send(file=discord.File("welcomered.png"))
    await member.guild.get_channel(582290523067514880).send(f'<a:clap:582898012989423616>    **Welcome** to the castle {member.mention}!\n\nVisit these channels:\n<:king:582903520596852756> <#582291711263375376> - To obtain free roles and let people know more about you\n<:kingpink:582903796854947841> <#582563570345050135> - Introduce yourself to the other members\n<:kinggold:582903797152743446> <#582286500503355402> - The main chat where everyones talking\n<:kingblue:582903797324709908> <#582288580878008320> - For a full tour around the server\n----------------------------------------------------\n<:kingblack:582904880721690636> **Enjoy your stay at the castle!** <:kingblack:582904880721690636>')


@client.event
async def on_member_remove(member):
    await member.guild.get_channel(582546718336483329).edit(name="Castle: {} Members".format(member.guild.member_count))
    await member.guild.get_channel(582545882692452372).send(f'<a:wavee:582898412177981470> **Goodbye** {member.mention} ({member.name})! [*Opening castle doors*] and go fuck yourself | Now: **{member.guild.member_count} Members**')

@client.command()
async def mem(ctx, *, member: discord.Member=None):
    if ctx.author.id == owner:
        await ctx.guild.get_channel(582286500503355402).send(f'<a:wavee:582898412177981470> **Welcome** to the **Castle**, {member.mention}! Take a seat in <#582286500503355402> and enjoy yourself | Now: **{ctx.guild.member_count} Members**')
        await ctx.guild.get_channel(582290523067514880).send(file=discord.File("welcomered.png"))
        await ctx.guild.get_channel(582290523067514880).send(f'<a:clap:582898012989423616> **Welcome** to the castle {member.mention}!\n\nVisit these channels:\n<:king:582903520596852756> <#582291711263375376> - To obtain free roles and let people know more about you\n<:kingpink:582903796854947841> <#582563570345050135> - Introduce yourself to the other members\n<:kinggold:582903797152743446> <#582286500503355402> - The main chat where everyones talking\n<:kingblue:582903797324709908> <#582288580878008320> - For a full tour around the server\n----------------------------------------------------\n<:kingblack:582904880721690636> **Enjoy your stay at the castle!** <:kingblack:582904880721690636>')



token = "NDgwMDQzMTEwNjgwODg3MzM2.DrH4lA.e96wOyoGm9-C6yWnnUHbMsM-zRA"


client.run(token, reconnect=True)
