import csv
import io
import os


import discord
import json

import effi_graph
import fill_excel

import json_to_csv_artifacts
import list_runes_over_effi

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

rune_set_list = [
    "Energy",
    "Guard",
    "Swift",
    "Blade",
    "Rage",
    "Focus",
    "Endure",
    "Fatal",
    "Despair",
    "Vampire",
    "Violent",
    "Nemesis",
    "Will",
    "Shield",
    "Revenge",
    "Destroy",
    "Fight",
    "Determination",
    "Enhance",
    "Accuracy",
    "Tolerance",
    "Seal",
    "Intangible",
    "Immemorial"
]
# async def rename_player(json_f, message):
#     if message.author.mention != discord.Permissions.administrator:
#         player_data = json.load(json_f)
#         player_name = player_data["wizard_info"]["wizard_name"]
#         await message.author.edit(nick=player_name)


@client.event
async def on_message(message):
    print(str(message.author) + " : " + message.content)

    if message.author == client.user:
        return

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

    if message.content.startswith('$fill_doc'):
        if len(message.attachments) > 0:
            attachment = message.attachments[0]
            if attachment.filename.endswith('.json'):
                # Télécharger le fichier
                file_content = await attachment.read()
                json_data = json.loads(file_content.decode('utf-8'))

                guild_info = json_data['guild']['guild_info']

                if guild_info is None:
                    guild_name = "None"
                else:
                    guild_name = guild_info['name']
                print(guild_name)
                args = message.content.split(' ')[1:]
                if args:
                    guild_to_check = args[0] + " " + args[1]
                else:
                    guild_to_check = guild_name
                list_guildes = ["Rose Tattoo", "Rose Tattwo", "Little Rose", "Baby Rose"]
                if guild_name not in list_guildes:
                    await message.reply("Cet outil est réservé aux guildes du groupe Rose Tattoo (hors Lazy)")
                    return

                if guild_to_check not in list_guildes:
                    await message.reply("La guilde que vous avez entrée ne fait pas partie du groupe Rose Tattoo")
                    return

                with open(attachment.filename.split('.')[0] + '-temp.json', 'w', encoding='utf8') as temp_json_f:
                    json.dump(json_data, temp_json_f)
                destination_file = attachment.filename.split('.')[0] + ".xlsx"
                with open(attachment.filename.split('.')[0] + '-temp.json', 'r', encoding='utf8') as temp_json_f:
                    # await rename_player(temp_json_f, message)
                    # for guild in list_guildes:
                    fill_excel.parse_json(temp_json_f, destination_file, guild_to_check)

                # await message.channel.send(file=discord.File(csv_filename))
                await message.reply(
                    "Vous pourrez retrouver le contenu rempli dans l'onglet de la bonne guilde (" + guild_to_check + ")",
                    file=discord.File(destination_file))

                os.remove(destination_file)
                os.remove(attachment.filename.split('.')[0] + '-temp.json')

            else:
                await message.reply("Le fichier doit être au format JSON.")
        else:
            await message.reply("Aucun fichier attaché. Utilisez la commande `$fill_doc` avec un fichier JSON.")

    if message.content.startswith('$help'):
        await message.reply("- $fill_doc : Remplit le document Excel qui vous indiquera les contenus à farmer. Nécessite un fichier json en pièce jointe")

    if message.content.startswith('$efficheck'):
        if len(message.attachments) > 0:
            attachment = message.attachments[0]
            if attachment.filename.endswith('.json'):
                # Télécharger le fichier
                file_content = await attachment.read()
                json_data = json.loads(file_content.decode('utf-8'))

                args = message.content.split(' ')[1:]

                if args:
                    if args[0].isdigit():
                        with open(attachment.filename.split('.')[0] + '-temp.json', 'w',
                                  encoding='utf8') as temp_json_f:
                            json.dump(json_data, temp_json_f)
                        csv_filename = attachment.filename.split('.')[0] + "-effi-" + args[0] + ".csv"
                        with open(attachment.filename.split('.')[0] + '-temp.json', 'r',
                                  encoding='utf8') as temp_json_f:
                            # await rename_player(temp_json_f, message)
                            list_runes_over_effi.list_runes(temp_json_f, csv_filename, args[0])

                        await message.reply(file=discord.File(csv_filename))
                        os.remove(csv_filename)
                        os.remove(attachment.filename.split('.')[0] + '-temp.json')

                else:
                    await message.reply("Veuillez passer un argument à la fonction\n"
                                        "Usage : $efficheck x")

            else:
                await message.channel.send("Le fichier doit être au format JSON.")
        else:
            await message.channel.send("Aucun fichier attaché. Utilisez la commande `$efficheck` avec un fichier JSON.")



    if message.content.startswith('$graph'):
        if len(message.attachments) > 0:
            attachment = message.attachments[0]
            if attachment.filename.endswith('.json'):
                # Télécharger le fichier
                file_content = await attachment.read()
                json_data = json.loads(file_content.decode('utf-8'))

                args = message.content.split(' ')[1:]


                if args:
                    if args[0] in rune_set_list:
                        with open(attachment.filename.split('.')[0] + '-temp.json', 'w', encoding='utf8') as temp_json_f:
                            json.dump(json_data, temp_json_f)
                        image_filename = attachment.filename.split('.')[0] + "-effi-graph-" + args[0] + ".png"
                        with open(attachment.filename.split('.')[0] + '-temp.json', 'r', encoding='utf8') as temp_json_f:
                            # await rename_player(temp_json_f, message)
                            effi_graph.effi_graph_with_set(temp_json_f, image_filename, args[0])

                        await message.reply(file=discord.File(image_filename))
                        os.remove(image_filename)
                        os.remove(attachment.filename.split('.')[0] + '-temp.json')
                    else:
                        await message.reply("Argument non reconnu veuillez entrer un set de rune")

                else:
                    with open(attachment.filename.split('.')[0] + '-temp.json', 'w', encoding='utf8') as temp_json_f:
                        json.dump(json_data, temp_json_f)
                    image_filename = attachment.filename.split('.')[0] + "-effi-graph.png"
                    with open(attachment.filename.split('.')[0] + '-temp.json', 'r', encoding='utf8') as temp_json_f:
                        # await rename_player(temp_json_f, message)
                        effi_graph.effi_graph_without_set(temp_json_f, image_filename)

                    await message.reply(file=discord.File(image_filename))
                    os.remove(image_filename)
                    os.remove(attachment.filename.split('.')[0] + '-temp.json')

            else:
                await message.reply("Le fichier doit être au format JSON.")
        else:
            await message.reply("Aucun fichier attaché. Utilisez la commande `$efficheck` avec un fichier JSON.")


print(os.getenv("DISCORD_TOKEN"))
client.run(os.getenv("DISCORD_TOKEN"))

