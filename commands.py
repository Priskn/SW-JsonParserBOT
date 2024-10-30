import json
import os

import discord

import effi_graph
import fill_excel
import list_runes_over_effi

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



async def fill_doc(ctx):
    if len(ctx.message.attachments) > 0:
        attachment = ctx.message.attachments[0]
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
            args = ctx.message.content.split(' ')[1:]
            if args:
                guild_to_check = args[0] + " " + args[1]
            else:
                guild_to_check = guild_name
            list_guildes = ["Rose Tattoo", "Rose Tattwo", "Little Rose", "Baby Rose"]
            if guild_name not in list_guildes:
                await ctx.message.reply("Cet outil est réservé aux guildes du groupe Rose Tattoo (hors Lazy)")
                return

            if guild_to_check not in list_guildes:
                await ctx.message.reply("La guilde que vous avez entrée ne fait pas partie du groupe Rose Tattoo")
                return

            with open(attachment.filename.split('.')[0] + '-temp.json', 'w', encoding='utf8') as temp_json_f:
                json.dump(json_data, temp_json_f)
            destination_file = attachment.filename.split('.')[0] + ".xlsx"
            with open(attachment.filename.split('.')[0] + '-temp.json', 'r', encoding='utf8') as temp_json_f:
                # await rename_player(temp_json_f, message)
                # for guild in list_guildes:
                fill_excel.parse_json(temp_json_f, destination_file, guild_to_check)

            # await message.channel.send(file=discord.File(csv_filename))
            await ctx.message.reply(
                "Vous pourrez retrouver le contenu rempli dans l'onglet de la bonne guilde (" + guild_to_check + ")",
                file=discord.File(destination_file))

            os.remove(destination_file)
            os.remove(attachment.filename.split('.')[0] + '-temp.json')

        else:
            await ctx.message.reply("Le fichier doit être au format JSON.")
    else:
        await ctx.message.reply("Aucun fichier attaché. Utilisez la commande `$fill_doc` avec un fichier JSON.")


async def efficheck(ctx, arg):
    if len(ctx.message.attachments) > 0:
        attachment = ctx.message.attachments[0]
        if attachment.filename.endswith('.json'):
            # Télécharger le fichier
            file_content = await attachment.read()
            json_data = json.loads(file_content.decode('utf-8'))

            if arg != "none":
                if arg.isdigit():
                    with open(attachment.filename.split('.')[0] + '-temp.json', 'w',
                              encoding='utf8') as temp_json_f:
                        json.dump(json_data, temp_json_f)
                    csv_filename = attachment.filename.split('.')[0] + "-effi-" + arg + ".csv"
                    with open(attachment.filename.split('.')[0] + '-temp.json', 'r',
                              encoding='utf8') as temp_json_f:
                        # await rename_player(temp_json_f, message)
                        list_runes_over_effi.list_runes(temp_json_f, csv_filename, arg)

                    await ctx.message.reply(file=discord.File(csv_filename))
                    os.remove(csv_filename)
                    os.remove(attachment.filename.split('.')[0] + '-temp.json')

            else:
                await ctx.message.reply("Veuillez passer un argument à la fonction\n"
                                        "Usage : $efficheck x")

        else:
            await ctx.message.channel.send("Le fichier doit être au format JSON.")
    else:
        await ctx.message.channel.send("Aucun fichier attaché. Utilisez la commande `$efficheck` avec un fichier JSON.")


async def graph(ctx, arg):
    if len(ctx.message.attachments) > 0:
        attachment = ctx.message.attachments[0]
        if attachment.filename.endswith('.json'):
            # Télécharger le fichier
            file_content = await attachment.read()
            json_data = json.loads(file_content.decode('utf-8'))

            if arg != "None":
                if arg in rune_set_list:
                    with open(attachment.filename.split('.')[0] + '-temp.json', 'w',
                              encoding='utf8') as temp_json_f:
                        json.dump(json_data, temp_json_f)
                    image_filename = attachment.filename.split('.')[0] + "-effi-graph-" + arg + ".png"
                    with open(attachment.filename.split('.')[0] + '-temp.json', 'r',
                              encoding='utf8') as temp_json_f:
                        # await rename_player(temp_json_f, message)
                        effi_graph.effi_graph_with_set(temp_json_f, image_filename, arg)

                    await ctx.message.reply(file=discord.File(image_filename))
                    os.remove(image_filename)
                    os.remove(attachment.filename.split('.')[0] + '-temp.json')
                else:
                    await ctx.message.reply("Argument non reconnu veuillez entrer un set de rune")

            else:
                with open(attachment.filename.split('.')[0] + '-temp.json', 'w', encoding='utf8') as temp_json_f:
                    json.dump(json_data, temp_json_f)
                image_filename = attachment.filename.split('.')[0] + "-effi-graph.png"
                with open(attachment.filename.split('.')[0] + '-temp.json', 'r', encoding='utf8') as temp_json_f:
                    # await rename_player(temp_json_f, message)
                    effi_graph.effi_graph_without_set(temp_json_f, image_filename)

                await ctx.message.reply(file=discord.File(image_filename))
                os.remove(image_filename)
                os.remove(attachment.filename.split('.')[0] + '-temp.json')

        else:
            await ctx.message.reply("Le fichier doit être au format JSON.")
    else:
        await ctx.message.reply("Aucun fichier attaché. Utilisez la commande `$graph` avec un fichier JSON.")


