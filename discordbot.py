from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send("草")
    
@bot.event
async def on_message(message):
    if message.content == '$summon':
        await message.channel.send("おはよう！！")
        #voicechannelを取得
        voich = message.author.voice.channel
        #voicechannelに接続
        await voich.connect()
    if message.content == '$dc':
        await message.channel.send("さよなら...")
        voich = message.author.voice.channel
        await voich.disconnect()

    if message.content.startswith('!'):
        pass
    elif message.content == '$summon':
        pass
    else:
        if message.guild.voice_client:
            print(message.content)
            creat_WAV(message.content)
            source = discord.FFmpegPCMAudio("output.wav")
            message.guild.voice_client.play(source)
        else:
            pass


bot.run(token)
