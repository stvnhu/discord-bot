
from pathlib import Path
import discord
from discord.ext import commands
from discord import app_commands
import yt_dlp

ROOT_DIR = Path(__file__).parent.parent.parent
AUDIO_DIR = ROOT_DIR / "audio"

yt_options = {
    "format": "bestaudio/best",
    "outtmpl": str(AUDIO_DIR / "%(title)s.%(ext)s"),
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
}

class Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    yt = app_commands.Group(name="yt", description="Youtube related commands.")

    @yt.command(name="join", description="The bot will join your channel")
    async def ytJoin(self, interaction):
        await interaction.response.defer(ephemeral=True)

        if not interaction.user.voice:
            await interaction.followup.send("You are not in a voice channel.")

        voiceChannel = interaction.user.voice.channel
        voiceClient = interaction.guild.voice_client

        try:
            if not voiceClient:
                voiceClient = await voiceChannel.connect(reconnect=False)
            elif voiceClient.channel != voiceChannel:
                await voiceClient.move_to(voiceChannel)
        except Exception as e:
            await interaction.followup.send("Failed to join voice channel: {e}.")

        await interaction.followup.send(f"Joined {voiceChannel}.")

    @yt.command(name="play", description="Play a youtube link.")
    async def ytPlay(self, interaction, url: str):
        await interaction.response.defer()
        try:
            with yt_dlp.YoutubeDL(yt_options) as ydl:
                info = ydl.extract_info(url, download=True)
                file = Path(ydl.prepare_filename(info)).with_suffix(".mp3")
                audio = discord.FFmpegPCMAudio(file)
                voice_client = interaction.guild.voice_client
                voice_client.play(audio)
        except Exception as e:
            await interaction.followup.send(f"Error playing audio: {e}.")
        await interaction.followup.send(f"Now playing: {url}.")

    @yt.command(name="leave", description="Make the bot leave the voice channel.")
    async def leave(self, interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.guild.voice_client.disconnect()
        await interaction.followup.send("Voice channel left.")

async def setup(bot):
    await bot.add_cog(Youtube(bot))
