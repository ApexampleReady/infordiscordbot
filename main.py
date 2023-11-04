import discord
from discord.ext import commands
import random
import os
from decouple import config


TOKEN = config('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='/')

ans = set({})

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command()
async def start_game(ctx):
    ans.clear()
    while len(ans) < 4:
        ans.add(random.randint(1, 9))
    print(ans)
    await ctx.respond('我選好號碼了，開始猜八')
@bot.slash_command()
async def cheat(ctx):
    await ctx.respond(ans)


@bot.slash_command()
async def guess(ctx, guess: str):
    if len(set(guess)) != 4 or not guess.isdigit():
        await ctx.respond('請只輸入4位正整數')
        return

    guesslist = list(guess)
    anslist = list(map(str, ans))

    a = 0
    b = 0

    for i in range(4):
        if guesslist[i] == anslist[i]:
            a += 1
        elif guesslist[i] in anslist:
            b += 1

    if a == 4:
        await ctx.respond('恭喜，你猜對拉 ' + ''.join(anslist))
    else:
        response = f'{guess}, {a}A{b}B'
        await ctx.respond(response)

bot.run(TOKEN)
