import discord
import csv
import pprint

TOKEN = 'NzA1Nzc4NTIxNzQ1Nzg0OTE0.Xqy9IQ.04IeYo_dNa-In1BWgf4b0htECBg'

with open('/home/pi/DiscordBot/Schedule_FirstHalf.csv') as Schedule:
    reader = csv.reader(Schedule)
    data = [row for row in reader]

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    #テスト用
    if message.content == '/cat':
        await message.channel.send('にゃーん')

    #月曜1限
    if message.content == '/Mon-1':
        await message.channel.send(data[1][1])
        await message.channel.send(data[1][2])
        await message.channel.send(data[1][3])

    #月曜2限
    if message.content == '/Mon-2':
        await message.channel.send(data[2][1])
        await message.channel.send(data[2][2])
        await message.channel.send(data[2][3])

    #月曜3限
    if message.content == '/Mon-3':
        await message.channel.send(data[3][1])
        await message.channel.send(data[3][2])
        await message.channel.send(data[3][3])

    #月曜4限
    if message.content == '/Mon-4':
        await message.channel.send(data[4][1])
        await message.channel.send(data[4][2])
        await message.channel.send(data[4][3])

    #月曜5限
    if message.content == '/Mon-5':
        await message.channel.send(data[5][1])
        await message.channel.send(data[5][2])
        await message.channel.send(data[5][3])

    #月曜6限
    if message.content == '/Mon-6':
        await message.channel.send(data[6][1])
        await message.channel.send(data[6][2])
        await message.channel.send(data[6][3])

    if message.content == '/Mon-7':
        await message.channel.send(data[7][1])
        await message.channel.send(data[7][2])
        await message.channel.send(data[7][3])

    if message.content == '/Mon-8':
        await message.channel.send(data[8][1])
        await message.channel.send(data[8][2])
        await message.channel.send(data[8][3])

    if message.content == '/Tue-1':
        await message.channel.send(data[9][1])
        await message.channel.send(data[9][2])
        await message.channel.send(data[9][3])

    if message.content == '/Tue-2':
        await message.channel.send(data[10][1])
        await message.channel.send(data[10][2])
        await message.channel.send(data[10][3])

    if message.content == '/Tue-3':
        await message.channel.send(data[11][1])
        await message.channel.send(data[11][2])
        await message.channel.send(data[11][3])

    if message.content == '/Tue-4':
        await message.channel.send(data[12][1])
        await message.channel.send(data[12][2])
        await message.channel.send(data[12][3])

    if message.content == '/Tue-5':
        await message.channel.send(data[13][1])
        await message.channel.send(data[13][2])
        await message.channel.send(data[13][3])

    if message.content == '/Tue-6':
        await message.channel.send(data[14][1])
        await message.channel.send(data[14][2])
        await message.channel.send(data[14][3])

    if message.content == '/Wed-1':
        await message.channel.send(data[15][1])
        await message.channel.send(data[15][2])
        await message.channel.send(data[15][3])

    if message.content == '/Wed-2':
        await message.channel.send(data[16][1])
        await message.channel.send(data[16][2])
        await message.channel.send(data[16][3])

    if message.content == '/Wed-3':
        await message.channel.send(data[17][1])
        await message.channel.send(data[17][2])
        await message.channel.send(data[17][3])

    if message.content == '/Wed-4':
        await message.channel.send(data[18][1])
        await message.channel.send(data[18][2])
        await message.channel.send(data[18][3])

    if message.content == '/Wed-5':
        await message.channel.send(data[19][1])
        await message.channel.send(data[19][2])
        await message.channel.send(data[19][3])

    if message.content == '/Wed-6':
        await message.channel.send(data[20][1])
        await message.channel.send(data[20][2])
        await message.channel.send(data[20][3])

    if message.content == '/Wed-7':
        await message.channel.send(data[21][1])
        await message.channel.send(data[21][2])
        await message.channel.send(data[21][3])

    if message.content == '/Wed-8':
        await message.channel.send(data[22][1])
        await message.channel.send(data[22][2])
        await message.channel.send(data[22][3])

    if message.content == '/Thr-1':
        await message.channel.send(data[23][1])
        await message.channel.send(data[23][2])
        await message.channel.send(data[23][3])

    if message.content == '/Thr-2':
        await message.channel.send(data[24][1])
        await message.channel.send(data[24][2])
        await message.channel.send(data[24][3])

    if message.content == '/Thr-3':
        await message.channel.send(data[25][1])
        await message.channel.send(data[25][2])
        await message.channel.send(data[25][3])

    if message.content == '/Thr-4':
        await message.channel.send(data[26][1])
        await message.channel.send(data[26][2])
        await message.channel.send(data[26][3])

    if message.content == '/Thr-5':
        await message.channel.send(data[27][1])
        await message.channel.send(data[27][2])
        await message.channel.send(data[27][3])

    if message.content == '/Thr-6':
        await message.channel.send(data[28][1])
        await message.channel.send(data[28][2])
        await message.channel.send(data[28][3])

    if message.content == '/Fri-1':
        await message.channel.send(data[29][1])
        await message.channel.send(data[29][2])
        await message.channel.send(data[29][3])

    if message.content == '/Fri-2':
        await message.channel.send(data[30][1])
        await message.channel.send(data[30][2])
        await message.channel.send(data[30][3])

    if message.content == '/Fri-3':
        await message.channel.send(data[31][1])
        await message.channel.send(data[31][2])
        await message.channel.send(data[31][3])

    if message.content == '/Fri-4':
        await message.channel.send(data[32][1])
        await message.channel.send(data[32][2])
        await message.channel.send(data[32][3])

    if message.content == '/Fri-5':
        await message.channel.send(data[33][1])
        await message.channel.send(data[33][2])
        await message.channel.send(data[33][3])

    if message.content == '/Fri-6':
        await message.channel.send(data[34][1])
        await message.channel.send(data[34][2])
        await message.channel.send(data[34][3])

    if message.content == '/Fri-7':
        await message.channel.send(data[35][1])
        await message.channel.send(data[35][2])
        await message.channel.send(data[35][3])

    if message.content == '/Fri-8':
        await message.channel.send(data[36][1])
        await message.channel.send(data[36][2])
        await message.channel.send(data[36][3])

client.run(TOKEN)