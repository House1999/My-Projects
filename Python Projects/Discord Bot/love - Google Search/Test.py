##Import msg
import discord
from discord.ext import commands
import random as rdm

import nest_asyncio
nest_asyncio.apply()

bot = commands.Bot("?")
user = bot.user

@bot.event
async def on_ready():
    print("Bot is Online !")
    emile = bot.get_user(654351460250812417)
    await emile.create_dm()
    emileDM = emile.dm_channel
    for i in range(1,176):
        await emileDM.send(file = discord.File("Tests ("+str(i)+").jpg"))



#Returns if str1 contains str2
def contains(str1, str2):
    i = 0

    for k in range(len(str1)):
        if ((i != len(str2)) and (str1[k] == str2[i])):
            i = i + 1

    return(i == len(str2))


bot.run("Njg0MzYzMTIxNTQ0MjY1NzM5.Xl5Lcg.sX4le6CRTHQVWv1Rg0ZkHR-O1kw")
