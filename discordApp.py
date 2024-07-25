import csv
import io
import os

import discord
import json

import json_to_csv_artifacts

intents = discord.Intents.default()
intents.message_content = True

client= discord.Client(intents=intents)

@client.event
async def on_message(message):
    print(str(message.author) + " : " + message.content)

    if message.author == client.user:
        return

    if message.content.startswith('$upload'):
        if len(message.attachments) > 0:
            attachment = message.attachments[0]
            if attachment.filename.endswith('.json'):
                # Télécharger le fichier
                file_content = await attachment.read()
                json_data = json.loads(file_content.decode('utf-8'))

                with open('temp.json', 'w', encoding='utf8') as temp_json_f:
                    json.dump(json_data, temp_json_f)

                csv_filename = attachment.filename.split('.')[0] + ".csv"
                with open('temp.json', 'r', encoding='utf8') as temp_json_f:
                    json_to_csv_artifacts.parse_json(temp_json_f, csv_filename)





                await message.channel.send(
                    file=discord.File(csv_filename))
            else:
                await message.channel.send("Le fichier doit être au format JSON.")
        else:
            await message.channel.send("Aucun fichier attaché. Utilisez la commande `$upload` avec un fichier JSON.")


client.run(os.getenv("DISCORD_TOKEN"))
