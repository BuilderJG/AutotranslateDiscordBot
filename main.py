import discord
from deep_translator import GoogleTranslator
import json

bot = discord.Bot(intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Under Development"))
    print("Bot by BuilderJG#4088\n")
    print("Bot running with:")
    print(f"Username: {bot.user.name}")
    print(f"User ID: {bot.user.id}")
    print(
        f"Invite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications"
        f".commands")


@bot.event
async def on_message(msg):
    with open("data.json") as f:
        data = json.load(f)
    if str(msg.channel.id) in data["translatechannels"] and msg.author.id != bot.user.id:
        try:
            text = GoogleTranslator(source="auto", target=data["translatechannels"][str(msg.channel.id)][1]).translate(
                msg.content)
        except Exception:
            pass
        else:
            channel = msg.guild.get_channel(int(data["translatechannels"][str(msg.channel.id)][0]))
            em = discord.Embed(title=f"Message by {msg.author}", description=f"*sent in {msg.channel.mention}*", color=msg.author.color)
            em.add_field(name="Original:", value=msg.content, inline=False)
            em.add_field(name="Translation:", value=text, inline=False)
            em.set_thumbnail(url=msg.author.display_avatar.url)
            em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
            await channel.send(embed=em)


bot.run("TOKEN")
