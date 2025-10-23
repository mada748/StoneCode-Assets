import discord
from discord import app_commands
from discord.ext import commands
CHANNEL_ID = 1405999930849493122
SEVEN_DAYS_IN_SECONDS = 604800

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)



intents.message_content = True

channel = bot.get_channel(CHANNEL_ID)
        

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        # Get the channel object
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            # Send a message to the specified channel
            await channel.send("Bot online")
            print(f"Message sent to channel {channel.name}.")
        else:
            print(f"Channel with ID {CHANNEL_ID} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


LOG_CHANNEL_ID = 1406387760847392798  # Replace with your actual log channel ID

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent a loop
    if message.author == bot.user:
        return

    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(
            title="Message Log",
            description=f"**Message sent by {message.author.mention} in {message.channel.mention}**\n\n"
                        f"**Content:**\n```{message.content}```",
            color=discord.Color.blue()
        )
        await log_channel.send(embed=embed)
        delete_after=SEVEN_DAYS_IN_SECONDS

    await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel and before.content != after.content:
        embed = discord.Embed(
            title="Message Edited",
            description=f"**Message from {after.author.mention} in {after.channel.mention} was edited**\n\n"
                        f"**Original Content:**\n```{before.content}```\n\n"
                        f"**New Content:**\n```{after.content}```",
            color=discord.Color.orange()
        )
        await log_channel.send(embed=embed)
        delete_after=SEVEN_DAYS_IN_SECONDS

@bot.event
async def on_message_delete(message):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(
            title="Message Deleted",
            description=f"**Message from {message.author.mention} in {message.channel.mention} was deleted**\n\n"
                        f"**Content:**\n```{message.content}```",
            color=discord.Color.red()
        )
        await log_channel.send(embed=embed)
        delete_after=SEVEN_DAYS_IN_SECONDS

bot.run('BOT TOKEN (yeah im gonna put here a placeholder)')