
## Deprecated after gpt-4o-mini was retired

import re
from pathlib import Path
from dotenv import dotenv_values
from discord.ext import commands
from discord import app_commands
from openai import OpenAI
import base64
from io import BytesIO

OPENAI_API_KEY = dotenv_values(Path(__file__).parent.parent.parent / ".env").get("OPENAI_API_KEY")

class ChatGPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.AI = OpenAI(api_key=OPENAI_API_KEY)
        self.history = [{"role": "system", "content": "Answer as if you are a human expert on the topic with no mention of being an AI."}]
        self.SPLIT_SIZE = 1800

    gpt = app_commands.Group(name="gpt", description="ChatGPT related commands.")
    
    @gpt.command(name="ask", description="Ask ChatGPT a question.")
    async def gptAsk(self, interaction, question: str):
        await interaction.response.defer()
        try:
            self.history.append({"role": "user", "content": question})
            response = self.AI.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.history
            )
            totalResponseMessage = f"{question} \n\n {response.choices[0].message.content}"
            breaks = [b.start() + 1 for b in re.finditer(r"\n\s*\n", totalResponseMessage)]
            start = 0
            for b in breaks:
                if b > start + self.SPLIT_SIZE:
                    await interaction.followup.send(f"```{totalResponseMessage[start:b - 1]}```")
                    start = b - 1
            await interaction.followup.send(f"```{totalResponseMessage[start:]}```")
        except Exception as e:
            await interaction.followup.send(f"Response failed: {e}")
    
    @gpt.command(name="clear", description="Clear ChatGPT chat history.")
    async def gptClearHistory(self, interaction):
        self.history[:] = self.history[:1]
        await interaction.response.send_message("History cleared.")

    @gpt.command(name="img", description="Generate an image.")
    async def gptImage(self, interaction, prompt: str):
        await interaction.response.defer()
        try:
            image = self.AI.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1024"
            )
            await interaction.followup.send(file=discord.File(BytesIO(base64.b64decode(image))))
        except Exception as e:
            await interaction.followup.send(f"Response failed: {e}")
        finally:
            await interaction.followup.send("Feature abandoned (costs money)")

async def setup(bot):
    await bot.add_cog(ChatGPT(bot))
