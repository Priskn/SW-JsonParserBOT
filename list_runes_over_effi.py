import csv
import json

import effi_rune


def list_runes(json_f, csv_filename, effi_asked):
    with open(csv_filename, 'w', newline='', encoding='utf8') as csv_f:
        with open('data_xzandro.json', encoding='utf8') as data_xzandro_f:
            data = json.load(json_f)
            data_xzandro = json.load(data_xzandro_f)
            writer = csv.writer(csv_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(
                ['Rune ID', 'Set', 'Slot', 'Monster Equipped', 'Efficiency', 'Max Efficiency', 'Gains', 'Main Stat', 'Innate',
                 'Innate Value', 'first_sub', 'first_sub_value', 'second_sub', 'second_sub_value', 'third_sub',
                 'third_sub_value', 'fourth_sub', 'fourth_sub_value'])

            for rune in data["runes"]:
                if rune["upgrade_curr"] >= 12:
                    if effi_rune.calcul_effi_rune(rune) < int(effi_asked) < effi_rune.calcul_effi_max(rune):
                        row = get_row_effi(rune, data_xzandro, "None")
                        writer.writerow(row)

            for monster in data["unit_list"]:

                if isinstance(monster["runes"], dict):
                    runes = list(monster["runes"].values())
                else:
                    runes = monster["runes"]

                for rune in monster["runes"]:
                    if rune["upgrade_curr"] >= 12:
                        if effi_rune.calcul_effi_rune(rune) < int(effi_asked) < effi_rune.calcul_effi_max(rune):
                            row = get_row_effi(rune, data_xzandro, monster["unit_master_id"])
                            writer.writerow(row)


def get_row_effi(rune, data_xzandro, monster):
    row = []

    row.append(rune["rune_id"])
    row.append(data_xzandro["rune"]["sets"][str(rune["set_id"])])
    row.append(rune["slot_no"])
    row.append("Inventory" if monster == "None" else data_xzandro["monster"]["names"][str(monster)])
    row.append(effi_rune.calcul_effi_rune(rune))
    row.append(effi_rune.calcul_effi_max(rune))
    row.append(effi_rune.calcul_effi_max(rune) - effi_rune.calcul_effi_rune(rune))
    row.append(data_xzandro["rune"]["effectTypes"][str(rune["pri_eff"][0])])
    row.append(data_xzandro["rune"]["effectTypes"][str(rune["prefix_eff"][0])])
    row.append(rune["prefix_eff"][1])

    for sub in rune["sec_eff"]:
        row.append(data_xzandro["rune"]["effectTypes"][str(sub[0])])
        row.append(sub[1] + sub[3])

    return row
