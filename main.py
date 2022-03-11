import discord, aiosqlite, json
from discord.ext import commands, tasks
from rich.console import Console

# --- Constants --- #

console = Console()
with open('config.json', 'r', encoding='utf-8') as handler:
    config = json.load(handler)
bot = commands.Bot(prefix=config['prefix'], help_command=None, self_bot=True)

# --- Events --- #

@bot.event
async def on_ready() -> None:
    """Event: on_ready"""
    console.log(
        f"Connected to Discord Socket as {bot.user} (ID: {bot.user.id}) and in {len(bot.guilds)} guilds.\n\nGuilds - \n- "
        + "\n- ".join(
            [
                f"{guild.name} ({guild.id}) - {guild.member_count} Members"
                for guild in bot.guilds
            ]
        )
        + "\n----------------\n"
    )
    print(f"Connected as {bot.user} and in {len(bot.guilds)} guilds.")
    print("----------------")
    await readyDatabase()

# --- Database --- #

async def readyDatabase():
    async with aiosqlite.connect("database.db") as db:
        ...
    return True

# --- Loading Cogs --- #

for filename in os.listdir(f"./cogs"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{category}.{filename[:-3]}")
            console.log(f"[green]Cog[/green]: {filename} was successfully loaded.")
        except Exception as e:
            console.log(f"[red]Cog[/red]: {filename} could not be loaded.\nException: {e}\n---")
            continue
    else:
        continue

# --- Running --- #

bot.run(config['token'])
