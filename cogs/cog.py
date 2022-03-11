import discord, aiohttp, aiosqlite
from discord.ext import commands, tasks
from rich.console import Console

# --- Constants --- #

console = Console()

# --- Cog --- #

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Pings the bot and returns latency", aliases=['p'], usage='')
    async def ping(self, ctx):
        await ctx.reply(f"Pong, {round(self.bot.latency, 1)}ms.", mention_author=False)

# --- Setup --- #

def setup(bot):
    bot.add_cog(Cog(bot))
    console.log(f"{__file__} loaded.")

def teardown(bot):
    console.log(f"{__file__} unloaded.")

# ------------------------ #
