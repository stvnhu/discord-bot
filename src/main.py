
from pathlib import Path
from dotenv import dotenv_values
import discord
from discord.ext import commands

ROOT_DIR = Path(__file__).parent.parent
COG_DIR = ROOT_DIR / "src" / "cogs"
BOT_TOKEN = dotenv_values(ROOT_DIR / ".env").get("BOT_TOKEN")

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="/", intents=intents)

    async def setup_hook(self):
        for cog in COG_DIR.iterdir():
            if cog.suffix == ".py" and cog.stem != "__init__":
                try:
                    await self.load_extension(f"cogs.{cog.stem}")
                    print(f"Loaded {cog.name}")
                except Exception as e:
                    print(f"Failed to load {cog.name}")

    async def on_ready(self):
        print("Bot Ready")

def main():
    bot = Bot()
    bot.run(BOT_TOKEN)

if __name__ == "__main__":
    main()
