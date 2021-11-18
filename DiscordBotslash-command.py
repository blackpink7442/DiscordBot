import time
import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice,create_option
import poeninja
import asyncio
import poeninjaAPI
import requests


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
            name="Exalted Orb",
            value="Exalted Orb"
            ),
            create_choice(
            name="Prime Sextant",
            value="Prime Sextant"
            ),
            create_choice(
            name="TheNurse",
            value="TheNurse"
            ),
            create_choice(
            name="TheDoctor",
            value="TheDoctor"
            ),
            create_choice(
            name="Headhunter",
            value="Headhunter"
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
    print(option)
    if option == "TheNurse"or option =="TheDoctor":
        print("123")
        poeprice = poeninjaAPI.get_divination_cards_price(option)
    elif option == "Headhunter":
        poeprice = poeninjaAPI.get_Unique_Accessories(option)
    else:
        poeprice = poeninjaAPI.get_orb_price(option)
    print(poeprice)
    end = time.time()
    end = end - start
    print(end)
    await asyncio.sleep(2)
    await ctx.send('``` {} ```'.format(poeprice))


client.run("")