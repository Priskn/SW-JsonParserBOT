import json
import csv
import subprocess
import openpyxl
import shutil
import check_excel
import effi_rune

result = subprocess.run(['node', 'mapping.js'], capture_output=True, text=True)

# Vérifier si l'exécution s'est bien passée
if result.returncode != 0:
    print("Erreur lors de l'exécution du fichier JavaScript:", result.stderr)
else:
    # Charger les données JSON en Python
    json_data = result.stdout
    data_xzandro = json.loads(json_data)
    print(data_xzandro)


def parse_json(json_f, destination_file, guild_name):
    with open('artifact_attribute.json', encoding='utf8') as artifact_attributes_f:
        data = json.load(json_f)

        source_file = "jsonanalysed.xlsx"

        shutil.copyfile(source_file, destination_file)
        workbook = openpyxl.load_workbook(destination_file)
        sheet = workbook[guild_name]

        for arti in data['artifacts']:
            for sub in arti["sec_effects"]:
                sheet = check_excel.check_excel(
                                        str(sub[0]),
                                        sub[1],
                                        sheet,
                                        str(arti['type']),
                                        str(arti['attribute']),
                                        str(arti['unit_style']),
                                        str(arti["pri_effect"][0]),
                                        guild_name
                )

        for monster in data["unit_list"]:
            for mon_arti in monster["artifacts"]:
                for sub in mon_arti["sec_effects"]:
                    sheet = check_excel.check_excel(
                        str(sub[0]),
                        sub[1],
                        sheet,
                        str(mon_arti['type']),
                        str(mon_arti['attribute']),
                        str(mon_arti['unit_style']),
                        str(mon_arti["pri_effect"][0]),
                        guild_name)

        nb_effi_vio = 0
        nb_effi_max_vio = 0
        nb_110_vio = 0
        nb_110_max_vio = 0

        nb_effi_will = 0
        nb_effi_max_will = 0
        nb_110_will = 0
        nb_110_max_will = 0

        nb_effi_destroy = 0
        nb_effi_max_destroy = 0
        nb_110_destroy = 0
        nb_110_max_destroy = 0

        nb_effi_seal = 0
        nb_effi_max_seal = 0
        nb_110_seal = 0
        nb_110_max_seal = 0

        max_swift_1 = 0
        max_swift_3 = 0
        max_swift_4 = 0
        max_swift_5 = 0
        max_swift_6 = 0

        max_despair_1 = 0
        max_despair_3 = 0
        max_despair_4 = 0
        max_despair_5 = 0
        max_despair_6 = 0

        for monster in data["unit_list"]:
            for mon_rune in monster["runes"]:
                if mon_rune["set_id"] == 13:
                    effi = effi_rune.calcul_effi_rune(mon_rune)
                    effi_purple = effi_rune.calcul_effi_max(mon_rune)
                    if effi >= 100:
                        nb_effi_vio += 1
                        if effi >= 110 :
                            nb_110_vio += 1

                    if effi_purple >= 100:
                        nb_effi_max_vio += 1
                        if effi_purple >= 110:
                            nb_110_max_vio += 1

                if mon_rune["set_id"] == 15:
                    effi = effi_rune.calcul_effi_rune(mon_rune)
                    effi_purple = effi_rune.calcul_effi_max(mon_rune)
                    if effi >= 100:
                        nb_effi_will += 1
                        if effi >= 110:
                            nb_110_will += 1

                    if effi_purple >= 100:
                        nb_effi_max_will += 1
                        if effi_purple >= 110:
                            nb_110_max_will += 1

                if mon_rune["set_id"] == 18:
                    effi = effi_rune.calcul_effi_rune(mon_rune)
                    effi_purple = effi_rune.calcul_effi_max(mon_rune)
                    if effi >= 100:
                        nb_effi_destroy += 1
                        if effi >= 110:
                            nb_110_destroy += 1

                    if effi_purple >= 100:
                        nb_effi_max_destroy += 1
                        if effi_purple >= 110:
                            nb_110_max_destroy += 1

                if mon_rune["set_id"] == 24:
                    effi = effi_rune.calcul_effi_rune(mon_rune)
                    effi_purple = effi_rune.calcul_effi_max(mon_rune)
                    if effi >= 100:
                        nb_effi_seal += 1
                        if effi >= 110:
                            nb_110_seal += 1

                    if effi_purple >= 100:
                        nb_effi_max_seal += 1
                        if effi_purple >= 110:
                            nb_110_max_seal += 1

                if mon_rune["set_id"] == 3:
                    if mon_rune["slot_no"] == 1:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_swift_1 = max(max_swift_1, sub[1] + sub[3])
                    if mon_rune["slot_no"] == 3:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_swift_3 = max(max_swift_3, sub[1] + sub[3])
                    if mon_rune["slot_no"] == 5:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_swift_5 = max(max_swift_5, sub[1] + sub[3])
                    if mon_rune["slot_no"] == 4:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_swift_4 = max(max_swift_4, sub[1] + sub[3])
                    if mon_rune["slot_no"] == 6:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_swift_6 = max(max_swift_6, sub[1] + sub[3])

                if mon_rune["set_id"] == 10:
                    if mon_rune["slot_no"] == 1:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_despair_1 = max(max_despair_1, sub[1] + sub[3])
                    if mon_rune["slot_no"] == 3:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_despair_3 = max(max_despair_3, sub[1] + sub[3])
                    if mon_rune["slot_no"] == 5:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_despair_5 = max(max_despair_5, sub[1] + sub[3])
                    if mon_rune["slot_no"] == 4:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_despair_4 = max(max_despair_4, sub[1] + sub[3])
                    if mon_rune["slot_no"] == 6:
                        for sub in mon_rune["sec_eff"]:
                            if sub[0] == 8:
                                max_despair_6 = max(max_despair_6, sub[1] + sub[3])

        for rune in data["runes"]:
            if rune["set_id"] == 13:
                effi = effi_rune.calcul_effi_rune(rune)
                effi_purple = effi_rune.calcul_effi_max(rune)
                if effi >= 100:
                    nb_effi_vio += 1
                    if effi >= 110 :
                        nb_110_vio += 1

                if effi_purple >= 100:
                    nb_effi_max_vio += 1
                    if effi_purple >= 110:
                        nb_110_max_vio += 1

            if rune["set_id"] == 15:
                effi = effi_rune.calcul_effi_rune(rune)
                effi_purple = effi_rune.calcul_effi_max(rune)
                if effi >= 100:
                    nb_effi_will += 1
                    if effi >= 110:
                        nb_110_will += 1

                if effi_purple >= 100:
                    nb_effi_max_will += 1
                    if effi_purple >= 110:
                        nb_110_max_will += 1

            if rune["set_id"] == 18:
                effi = effi_rune.calcul_effi_rune(rune)
                effi_purple = effi_rune.calcul_effi_max(rune)
                if effi >= 100:
                    nb_effi_destroy += 1
                    if effi >= 110:
                        nb_110_destroy += 1

                if effi_purple >= 100:
                    nb_effi_max_destroy += 1
                    if effi_purple >= 110:
                        nb_110_max_destroy += 1

            if rune["set_id"] == 24:
                effi = effi_rune.calcul_effi_rune(rune)
                effi_purple = effi_rune.calcul_effi_max(rune)
                if effi >= 100:
                    nb_effi_seal += 1
                    if effi >= 110:
                        nb_110_seal += 1

                if effi_purple >= 100:
                    nb_effi_max_seal += 1
                    if effi_purple >= 110:
                        nb_110_max_seal += 1

            if rune["set_id"] == 3:
                if rune["slot_no"] == 1:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_swift_1 = max(max_swift_1, sub[1] + sub[3])
                if rune["slot_no"] == 3:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_swift_3 = max(max_swift_3, sub[1] + sub[3])
                if rune["slot_no"] == 5:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_swift_5 = max(max_swift_5, sub[1] + sub[3])
                if rune["slot_no"] == 4:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_swift_4 = max(max_swift_4, sub[1] + sub[3])
                if rune["slot_no"] == 6:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_swift_6 = max(max_swift_6, sub[1] + sub[3])

            if rune["set_id"] == 10:
                if rune["slot_no"] == 1:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_despair_1 = max(max_despair_1, sub[1] + sub[3])
                if rune["slot_no"] == 3:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_despair_3 = max(max_despair_3, sub[1] + sub[3])
                if rune["slot_no"] == 5:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_despair_5 = max(max_despair_5, sub[1] + sub[3])
                if rune["slot_no"] == 4:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_despair_4 = max(max_despair_4, sub[1] + sub[3])
                if rune["slot_no"] == 6:
                    for sub in rune["sec_eff"]:
                        if sub[0] == 8:
                            max_despair_6 = max(max_despair_6, sub[1] + sub[3])

        sheet['BE4'] = nb_effi_vio
        sheet['BE5'] = nb_effi_max_vio
        sheet['BE6'] = nb_effi_will
        sheet['BE7'] = nb_effi_max_will
        sheet['BE8'] = nb_effi_destroy
        sheet['BE9'] = nb_effi_max_destroy
        sheet['BE10'] = nb_effi_seal
        sheet['BE11'] = nb_effi_max_seal
        sheet['BE13'] = nb_110_vio
        sheet['BE14'] = nb_110_max_vio
        sheet['BE15'] = nb_110_will
        sheet['BE16'] = nb_110_max_will
        sheet['BE17'] = nb_110_destroy
        sheet['BE18'] = nb_110_max_destroy
        sheet['BE19'] = nb_110_seal
        sheet['BE20'] = nb_110_max_seal

        sheet['BE25'] = max_swift_1
        sheet['BE26'] = max_swift_3
        sheet['BE27'] = max_swift_4
        sheet['BE28'] = max_swift_5
        sheet['BE29'] = max_swift_6

        sheet['BE34'] = max_despair_1
        sheet['BE35'] = max_despair_3
        sheet['BE36'] = max_despair_4
        sheet['BE37'] = max_despair_5
        sheet['BE38'] = max_despair_6

        workbook.save(destination_file)





