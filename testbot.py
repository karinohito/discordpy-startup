# coding:utf-8
import discord
from discord.ext import commands
import subprocess
import ffmpeg
from voice_gen import creat_WAV
bot = commands.Bot(command_prefix="$")
client = commands.Bot(command_prefix='.')
voice_client = None
global voich

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_message(message):
    if message.content == '$summon':
        await message.channel.send("おはよう！！")
        #voicechannelを取得
        voich = message.author.voice.channel
        #voicechannelに接続
        await voich.connect()
    if message.content == '$dc':
        await message.channel.send("さよなら...")
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


client.run("")
