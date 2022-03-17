import discord
from discord.commands import Option
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


guilds = [770287021347569676]


@bot.slash_command(guild_ids=guilds)
async def t(ctx):
    await ctx.respond("test", ephemeral=True)


@bot.slash_command(guild_ids=guilds)
async def translateadd(ctx, channelfrom: discord.TextChannel, channelto: discord.TextChannel,
                       langto: Option(str, autocomplete=discord.utils.basic_autocomplete(
                           ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque',
                            'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa',
                            'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish',
                            'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian',
                            'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa',
                            'hawaiian',
                            'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish',
                            'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'kinyarwanda', 'korean',
                            'kurdish', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian',
                            'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar',
                            'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi',
                            'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi',
                            'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish',
                            'tajik', 'tamil', 'tatar', 'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu',
                            'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba',
                            'zulu'])) = "english"):
    with open("data.json") as f:
        data = json.load(f)
    data[str(channelfrom.id)] = [str(channelto.id), langto]
    with open("data.json", "w") as f:
        json.dump(data, f)
    await ctx.send(f"Alle Nachrichten aus dem Kanal {channelfrom.mention} werden nun in den Kanal {channelto.mention} in die Sprache `{langto}` übersetzt.", ephemeral=True)


@bot.slash_command(guild_ids=guilds)
async def translate_remove(ctx, channelfrom: discord.TextChannel):
    with open("data.json") as f:
        data = json.load(f)
    print(data)
    if not str(channelfrom.id) in data:
        await ctx.respond("Der angegebene Kanal wird bereits nicht übersetzt.", ephemeral=True)
        return
    del data[str(channelfrom.id)]
    with open("data.json", "w") as f:
        json.dump(data, f)
    await ctx.respond(f"Nachrichten aus dem Kanal {channelfrom} werden nun nicht mehr übersetzt.")


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
            em = discord.Embed(title=f"Nachricht von {msg.author}", description=f"*gesendet in {msg.channel.mention}*", color=msg.author.color)
            em.add_field(name="Original:", value=msg.content, inline=False)
            em.add_field(name="Übersetzung:", value=text, inline=False)
            em.set_thumbnail(url=msg.author.display_avatar.url)
            em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
            await channel.send(embed=em)


bot.run("ODUwNzk5MDg1NTE0NjUzNzM2.YLu-ZQ.E4P4lKNRgL7FATjpsZl1d5_oikQ")
