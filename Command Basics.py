import discord
from discord.ext import commands
import random

client = discord.Client()
bot = commands.Bot(command_prefix="!", help_command=None)


@bot.event
async def on_ready():
    print("BOT IS ONLINE")
    print("봇이 작동중입니다")


"""command example (!ping)"""


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


"""coinFlip command example"""


@bot.command()
async def 코인던지기(ctx, coin):
    coins = ["앞면", "뒷면"]
    selected = random.choice(coins)

    if selected == "앞면":
        await ctx.send("(앞면이 나왔습니다)")
        if coin == "앞면":
            await ctx.send("와우! 주인님께서 말씀하신대로 앞면이 나왔군요! 축하드립니다~")
        elif coin == "뒷면":
            await ctx.send("이런.. 앞면이 나왔군요.. 다시 해보시겠어요?")
    if selected == "뒷면":
        await ctx.send("(뒷면이 나왔습니다)")
        if coin == "뒷면":
            await ctx.send("와우! 주인님께서 말씀하신대로 뒷면이 나왔군요! 축하드립니다~")
        elif coin == "앞면":
            await ctx.send("이런.. 뒷면이 나왔군요.. 다시 해보시겠어요?")


"""rock scissor paper game example"""


@bot.command()
async def 가위바위보(ctx, hand):
    hands = ["바위", "가위", "보"]
    bothand = random.choice(hands)

    if bothand == "바위":
        await ctx.send("👊")
    elif bothand == "가위":
        await ctx.send("✌")
    elif bothand == "보":
        await ctx.send("✋")

    if hand == bothand:
        await ctx.send("후훗 비겼네요 다음번에는 제가 꼭 이길꺼에요!")
    elif hand == "가위":
        if bothand == "바위":
            await ctx.send("제가 이겼네요 하핫! 포상을.. 주실건가요..? ")
        if bothand == "보":
            await ctx.send("주인님이 이기셨네요! 축하드립니다~")
    elif hand == "바위":
        if bothand == "보":
            await ctx.send("제가 이겼네요 하핫! 포상을.. 주실건가요..? ")
        if bothand == "가위":
            await ctx.send("주인님이 이기셨네요! 축하드립니다~")
    elif hand == "보":
        if bothand == "가위":
            await ctx.send("제가 이겼네요 하핫! 포상을.. 주실건가요..? ")
        if bothand == "바위":
            await ctx.send("주인님이 이기셨네요! 축하드립니다~")


"""explanation list commands"""


@bot.command(aliases=["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title="유이카의 명령어 모음집", description="뭐든지 시켜만 주세요 주인님.. 원하신다면 후훗.. 다 해드릴게요",
                            color=discord.Colour.dark_blue())
    MyEmbed.set_thumbnail(url="https://i.pinimg.com/736x/9f/67/3a/9f673ac438b765bae43f24f44e53d8a6.jpg")
    MyEmbed.add_field(name="!ping", value="this Commands replies back with Pong whenever you write !ping.",
                      inline=False)
    MyEmbed.add_field(name="!코인던지기", value="!코인던지기 (앞면/뒷면) 으로 유이카와 함께 도박을 하실 수 있어요.", inline=False)
    MyEmbed.add_field(name="!가위바위보", value="!가위바위보 (가위/바위/보) 로 유이카와 함께 가위바위보를 하실 수 있어요.", inline=False)
    MyEmbed.add_field(name="!edit servername (원하는 서버이름)", value="원하시는 서버 이름으로 바꿀 수 있어요", inline=False)
    MyEmbed.add_field(name="!edit region (음성채널지역)",
                      value="음성 채널을 원하시는 지역으로 바꿀 수 있어요 ('us-west', 'newark', 'santiago', 'st-pete', 'brazil', 'stockholm', 'us-east', 'vip-amsterdam', 'eu-west', 'sydney', 'deprecated', 'india', 'southafrica', 'finland', 'hongkong', 'amsterdam', 'frankfurt', 'vip-us-west', 'rotterdam', 'vip-us-east', 'japan', 'eu-central', 'singapore', 'madrid', 'europe', 'us-central', 'montreal', 'us-south', 'london', 'seattle', 'milan', 'santa-clara', 'south-korea', 'dubai', 'buenos-aires', 'bucharest', 'atlanta', 'russia') (",
                      inline=False)
    await ctx.send(embed=MyEmbed)


@bot.group()
async def edit(ctx):
    pass


@edit.command()
async def servername(ctx, *, input):
    await ctx.guild.edit(name=input)


@edit.command()
async def region(ctx, input):
    await ctx.guild.edit(region=input)


"""링크방지프로그램"""


# @bot.event
# async def on_message(message):
#    if 'https://' in message.content:
#       await message.delete()
#       await message.channel.send(f"{message.author.mention} Don't send links!")
#    else:
#       await bot.process_commands(message)


# @bot.event
# async def on_message(msg):
#     PEPList = []
#     x = 100
#     while x >= 0:
#         PEPList.append("PEP-" + str(x))
#         x -= 1
#
#     if msg.author == bot.user:
#         return
#     else:
#         for i in PEPList:
#             if i in msg.content:
#                 return await msg.channel.send("https://minta.atlassian.net/browse/" + i)



bot.run("")
