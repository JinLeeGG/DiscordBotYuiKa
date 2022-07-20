import discord


intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("BOT IS ONLINE")
    print("봇이 작동중입니다")


@bot.event
async def on_message(msg):
    PEPList = []
    x = 1000
    while x > 0:
        PEPList.append("PEP-" + str(x))
        x -= 1

    if msg.author == bot.user:
        return
    else:
        for i in PEPList:
            if i in msg.content:
                return await msg.channel.send("https://minta.atlassian.net/browse/" + i)





bot.run("")