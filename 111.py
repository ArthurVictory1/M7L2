import discord
from discord.ext import comands
from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents = discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            file_name =attachments.filename
            file_url = attachments.url
            await attachments.save(f'./{attachments.filename}')
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachments.filename}"))
    else:
        await ctx.send('Вы забыли загрузить картинку')

bot.run('MTExNzM1NjY5MjI0NjY0MjcwOA.GkIrJQ.v9q92PL390GXFUTMmW6vMVLT32WkeaYcysHXFk')
