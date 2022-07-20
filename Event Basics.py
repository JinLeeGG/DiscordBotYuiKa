import discord


intents = discord.Intents.all()
bot = discord.Client(intents=intents)

"""when the bot is online"""


@bot.event
async def on_ready():
    print("BOT IS ONLINE")
    print("봇이 작동중입니다")


"""bot event lines"""


@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        if msg.content == "유이카 안녕":
            await msg.channel.send("안녕하세요 " + username + " 주인님 오늘 하루는 어떠셨나요?")


"""when a player joins the channel, it prints welcome message in the private messenger"""


@bot.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"안녕하세요 {member} 주인님~ 기다리고 있었습니다. {guildname}에 오신걸 환영해요~ 필요하신게 있으시면 언제든 불러주세요.")


"""Adding role when you reacted with certain emoji in the specific message."""


@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    member = payload.member
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)

    if emoji == "🕸️" and message_id == 979979326218985482:
        role = discord.utils.get(guild.roles, name="Marvel Fan")
        await member.add_roles(role)

    if emoji == "🦇" and message_id == 979979366522040360:
        role = discord.utils.get(guild.roles, name="DC Fan")
        await member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    user_id = payload.user_id
    emoji = payload.emoji.name
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    member = guild.get_member(user_id)

    if emoji == "🕸️" and message_id == 979979326218985482:
        role = discord.utils.get(guild.roles, name="Marvel Fan")
        await member.remove_roles(role)

    if emoji == "🦇" and message_id == 979979366522040360:
        role = discord.utils.get(guild.roles, name="DC Fan")
        await member.remove_roles(role)



bot.run("")

