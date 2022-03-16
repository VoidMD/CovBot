import discord
import urllib.request as urllib2
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
from time import sleep


url = 'https://corona-v.com/%D8%A7%D9%84%D8%AF%D9%88%D9%84-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9/%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9/'
respond = requests.get(url)
page = respond.content
soup = BeautifulSoup(page, "html.parser")




day = soup.find("span", {'style': "color:#ADFF2F"}).string

total = soup.find("div", {'class': "dDiv"}).find('b').find_next('b').string

totdeath = soup.find("span", {'style': "color:#ff5722"}).find('b').findNext('b').string

totalrecov = soup.find('b').findNext('b').findNext('b').findNext('b').findNext('b').findNext('b').findNext('b').string

newcov = soup.find("span", {'class': "fixRTL"}).string

newdeath = soup.find("span", {'style': "color:#ff5722"}).find('b').string

newrecov = soup.find("div", {'class': "bDiv"}).find('span', {'style': "color:#ADFF2F"}).findNext('span', {'style': "color:#ADFF2F"}).string


print(f'{day}')
print(total)
print(totdeath)
print(newcov)
print(newdeath)
print(newrecov)
print(totalrecov)

#discord bot
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    clientPing = round(client.latency*1000)
    if clientPing >= 200:
        await ctx.send(f'{clientPing}ms :( ')
    else:
        await ctx.send(f'{clientPing}ms :) ')

#command section :D
@client.command()
async def مجموعالحالات(ctx):
    await ctx.send(f'مجموع الحالات :{total} \n مجموع حالات الوفيات رحمهم الله :{totdeath} \n مجموع حالات التعافي : {totalrecov}\n ')
    await ctx.send(f'ليوم {day}')

@client.command()
async def الحالات(ctx):
    await ctx.send(f'عدد الحالات الجديدة ليوم {day}')
    await ctx.send(f'الحالات :{newcov} \n  الوفيات رحمهم الله :{newdeath} \n  التعافي : {newrecov}\n ')

@client.command()
async def hi(ctx):
    await ctx.send('hey! How can i help you?')

client.run(#discord API key here)