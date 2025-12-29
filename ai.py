import discord
from discord.ext import commands
from discord import app_commands

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True 
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot()

LOG_CHANNEL_NAME = "log-channel"  
SEVEN_DAYS_IN_SECONDS = 604800

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f'latency ({latency}ms)')

@bot.event
async def on_message(message):
    if message.author == bot.user or not message.guild:
        return

    log_channel = discord.utils.get(message.guild.text_channels, name=LOG_CHANNEL_NAME)

    if log_channel:
        embed = discord.Embed(
            title="Message Sent",
            description=f"**User:** {message.author.mention}\n**Channel:** {message.channel.mention}\n\n**Content:**\n{message.content}",
            color=discord.Color.blue()
        )
        await log_channel.send(embed=embed, delete_after=SEVEN_DAYS_IN_SECONDS)

    await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user or not before.guild:
        return

    if before.content != after.content:
        log_channel = discord.utils.get(after.guild.text_channels, name=LOG_CHANNEL_NAME)
        if log_channel:
            embed = discord.Embed(
                title="Message Edited",
                description=f"**User:** {after.author.mention}\n**Channel:** {after.channel.mention}",
                color=discord.Color.orange()
            )
            embed.add_field(name="Before", value=before.content or "None", inline=False)
            embed.add_field(name="After", value=after.content or "None", inline=False)
            
            await log_channel.send(embed=embed, delete_after=SEVEN_DAYS_IN_SECONDS)

@bot.event
async def on_message_delete(message):
    if message.author == bot.user or not message.guild:
        return

    log_channel = discord.utils.get(message.guild.text_channels, name=LOG_CHANNEL_NAME)
    if log_channel:
        embed = discord.Embed(
            title="Message Deleted",
            description=f"**User:** {message.author.mention}\n**Channel:** {message.channel.mention}\n\n**Content:**\n{message.content}",
            color=discord.Color.red()
        )
        await log_channel.send(embed=embed, delete_after=SEVEN_DAYS_IN_SECONDS)

bot.run('BOT TOKEN (yeah im gonna put here a placeholder)')
