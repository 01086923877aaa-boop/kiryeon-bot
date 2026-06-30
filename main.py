import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

COGS = [
    "cogs.economy",
    "cogs.level",
    "cogs.stock",
    "cogs.gacha",
    "cogs.verify",
    "cogs.ticket",
    "cogs.ranking",
]

@bot.event
async def on_ready():
    print("=" * 40)
    print(f"로그인 : {bot.user}")
    print(f"서버 : {len(bot.guilds)}개")
    print("=" * 40)

    await bot.change_presence(
        activity=discord.Game("기련봇 | !도움말")
    )

async def load_extensions():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"{cog} 로드 완료")
        except Exception as e:
            print(f"{cog} 오류 : {e}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())