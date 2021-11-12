import time
import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice,create_option
import poeninja
import asyncio


client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)

@slash.slash(
    name="Search_orb_price",
    description = "Price",
    guild_ids = [557482649279528990],
    options=[
        create_option(
            name = "option",
            description = "Price",
            required = True,
            option_type = 3,
            choices = [
            create_choice(
            name="Mirror of kalandra",
            value="mirror-of-kalandra"
            ),
            create_choice(
            name="Exalted orb",
            value="exalted-orb"
            )
            ] 
        ),
    ]

) 


# re try

async def Search_orb_price(ctx: SlashContext, option:str):
    # poeprice = poeninja.get_orb_price(option)
    # print(poeprice)
    await ctx.send("Checking price")
    start = time.time()
    poeprice = poeninja.get_orb_price(option)
    end = time.time()
    end = end - start
    print(end)
    await asyncio.sleep(3)
    await ctx.send('``` {} [{}] [{}] {} [{}] [{}] \n {} [{}] [{}] {} [{}] [{}] ```'.format(poeprice[0],poeprice[1],poeprice[2],poeprice[3],poeprice[4],poeprice[5],poeprice[6],poeprice[7],poeprice[8],poeprice[9],poeprice[10],poeprice[11]))


client.run("")