import json
import csv
import subprocess
import openpyxl
import shutil


result = subprocess.run(['node', 'mapping.js'], capture_output=True, text=True)

# Vérifier si l'exécution s'est bien passée
if result.returncode != 0:
    print("Erreur lors de l'exécution du fichier JavaScript:", result.stderr)
else:
    # Charger les données JSON en Python
    json_data = result.stdout
    data_xzandro = json.loads(json_data)




def parse_json(json_f, csv_filename):
# with open('~Priskn~-101331.json', encoding='utf8') as json_f:
    with open(csv_filename, 'w',  newline='', encoding='utf8') as csv_f:
        with open('artifact_attribute.json', encoding='utf8') as artifact_attributes_f:
            data = json.load(json_f)
            # print(data["artifact"])
            # print(data["guild"]["guild_info"]["name"])

            attribs = json.load(artifact_attributes_f)
            writer = csv.writer(csv_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # print(data['artifacts'])
            writer.writerow(['Artifact ID', 'Type', 'Attribute','Monster Equiped (TBI)','Level', 'Efficiency (TBI)', 'Main Stat', 'first_sub', 'first_sub_value', 'second_sub', 'second_sub_value', 'third_sub', 'third_sub_value', 'fourth_sub', 'fourth_sub_value'])
            for arti in data['artifacts']:
                if arti["level"]>=12:
                    print("attribute : " + str(arti['attribute']))
                    row = []
                    row.append(str(arti['rid']))
                    type = data_xzandro['artifact']['types'][str(arti['type'])]
                    row.append(type)
                    row.append(attribs[str(arti['type'])][str(arti['attribute'])] if str(arti['type'])=="1" else attribs[str(arti['type'])][str(arti["unit_style"])])
                    row.append("Inventory")
                    row.append(str(arti['level']))
                    row.append("")#artifact effi TBI
                    row.append(data_xzandro['artifact']['effectTypes']['main'][str(arti["pri_effect"][0])])# maybe needs to remove the "flat" word
                    for sub in arti["sec_effects"]:
                        row.append(data_xzandro['artifact']["effectTypes"]["sub"][str(sub[0])])
                        row.append(str(sub[1]))
                    writer.writerow(row)
            for monster in data["unit_list"]:
                for mon_arti in monster["artifacts"]:
                    row = []
                    row.append(str(mon_arti['rid']))
                    print(mon_arti["rid"])
                    row.append(data_xzandro['artifact']['types'][str(mon_arti['type'])])
                    row.append(attribs[str(mon_arti['type'])][str(mon_arti['attribute'])] if str(mon_arti['type'])=="1" else attribs[str(mon_arti['type'])][str(mon_arti["unit_style"])])
                    row.append(data_xzandro["monster"]["names"][str(monster["unit_master_id"])])  # monster equiped TBI
                    row.append(str(mon_arti['level']))
                    row.append("")#artifact effi TBI
                    row.append(data_xzandro['artifact']['effectTypes']['main'][str(mon_arti["pri_effect"][0])])# maybe needs to remove the "flat" word
                    for sub in mon_arti["sec_effects"]:
                        row.append(data_xzandro['artifact']["effectTypes"]["sub"][str(sub[0])])
                        row.append(str(sub[1]))
                    writer.writerow(row)
