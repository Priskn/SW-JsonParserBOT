
import os

import discord
import json

from discord.ext import commands



import json_to_csv_artifacts

import commands as comm

intents = discord.Intents.default()
intents.message_content = True


# async def rename_player(json_f, message):
#     if message.author.mention != discord.Permissions.administrator:
#         player_data = json.load(json_f)
#         player_name = player_data["wizard_info"]["wizard_name"]
#         await message.author.edit(nick=player_name)


bot = commands.Bot(command_prefix='$', intents=intents)

help_f = open("help.json")
data_help = json.load(help_f)


@bot.command(help=data_help["fill_doc"])
async def fill_doc(ctx):
    await comm.fill_doc(ctx)


@bot.command(help=data_help["efficheck"])
async def efficheck(ctx, arg="none"):
    await comm.efficheck(ctx, arg)

@bot.command(help=data_help["graph"])
async def graph(ctx, arg="None"):
    await comm.graph(ctx, arg)

# @bot.command()
# async def help(ctx, arg="none"):
#     await comm.help(ctx, arg)

@bot.event
async def on_message(message):
    print(str(message.author) + " : " + message.content)

    if message.author == bot.user:
        return

    await bot.process_commands(message)

    if message.content.startswith('Nephtys pue'):
        await message.reply("tro dakor")

    if 'Nephthys' in message.content:
        await message.add_reaction('🤮')

    if message.content.startswith('$upload'):
        if len(message.attachments) > 0:
            attachment = message.attachments[0]
            if attachment.filename.endswith('.json'):
                # Télécharger le fichier
                file_content = await attachment.read()
                json_data = json.loads(file_content.decode('utf-8'))

                with open(attachment.filename.split('.')[0] + '-temp.json', 'w', encoding='utf8') as temp_json_f:
                    json.dump(json_data, temp_json_f)

                csv_filename = attachment.filename.split('.')[0] + ".csv"
                with open(attachment.filename.split('.')[0] + '-temp.json', 'r', encoding='utf8') as temp_json_f:
                    # await rename_player(temp_json_f, message)
                    json_to_csv_artifacts.parse_json(temp_json_f, csv_filename)

                # await message.channel.send(file=discord.File(csv_filename))
                await message.reply(file=discord.File(csv_filename))

            else:
                await message.channel.send("Le fichier doit être au format JSON.")
        else:
            await message.channel.send("Aucun fichier attaché. Utilisez la commande `$upload` avec un fichier JSON.")




# client.run(os.getenv("DISCORD_TOKEN"))
bot.run(os.getenv("DISCORD_TOKEN"))
