import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
print(TOKEN)
intents = discord.Intents.all()

class CinnamonBot(commands.Bot):
    def __init__(self):
        super().__init__(intents=intents)
    async def on_ready(self):
        print(f"Bot名:{self.user} On ready!!")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(error, ephemeral=True)
        else:
            raise error

if __name__ == "__main__":
    bot = CinnamonBot()
    bot.run(TOKEN)
