import discord
from discord.ext import commands
import time
import random
 
app = commands.Bot(command_prefix='-')
 
@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def 따라말해(ctx, *, text):
    tosend = '"' + text + '"라고 말하셨습니다.'
    await ctx.send(tosend)

@app.command()
async def 민초는(ctx):
    await ctx.send("마시쪄요!")

@app.command()
async def 핑(ctx):
    await ctx.send("퐁!")

@app.command()
async def 도움(ctx):
    embed = discord.Embed(title='파랑봇 도움말',description='`-따라말해 (단어)`:  (단어)라고 말하셨습니다.\n`-민초는`:  마시쪄\n`-핑`: 퐁\n`-야`: 네, 파랑봇이에요!', color = 0x00ff00)
    await ctx.send(embed=embed)

@app.command()
async def 민쵸는(ctx):
    await ctx.send("마시쪄")
    time.sleep(0.5)
    await ctx.send("근데 님 그 `-민쵸는` 말고 `-민초는`이라고 해야되는데..?")

@app.command()
async def 야(ctx):
    await ctx.send("네, 파랑봇이에요!")

@app.command()
async def 환영해줘(ctx, *, uname):
    await ctx.send(uname+"님, 반가워요!")
    
app.run('NzgxMzczMTQzOTM5OTQwMzky.X78scg.8SqmQH4VeHgdszJUCiK-VGE6Eyo')


