
import discord
from discord.ext import commands
import libneko


prefix = ","
Client = discord.Client()
client = commands.Bot(command_prefix = '!')
owner = int(303152083891257344)
winners = []


@client.event
async def on_ready():
    print("✔ Connected!\n")
    ez = client.load_extension("libneko.extras.superuser")
    print("Loaded cog")





token = "NDgwMDQzMTEwNjgwODg3MzM2.DrH4lA.e96wOyoGm9-C6yWnnUHbMsM-zRA"


client.run(token)
