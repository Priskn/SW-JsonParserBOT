import json

import matplotlib.pyplot as plt

import effi_rune


def effi_graph_with_set(json_f, image_filename, set):
    with open('data_xzandro.json', encoding='utf8') as data_xzandro_f:
        data = json.load(json_f)
        data_xzandro = json.load(data_xzandro_f)
        rune_array = []
        rune_max_array = []

        for rune in data["runes"]:
            if rune["upgrade_curr"] >= 12:
                set_id = data_xzandro["rune"]["reverse_sets"][set]
                print(set_id, type(set_id))
                print(rune["set_id"] , type(rune["set_id"]))
                if str(rune["set_id"]) == data_xzandro["rune"]["reverse_sets"][set]:
                    print("gne")
                    rune_array.append(effi_rune.calcul_effi_rune(rune))
                    rune_max_array.append((effi_rune.calcul_effi_max(rune)))

        for monster in data["unit_list"]:

            if isinstance(monster["runes"], dict):
                runes = list(monster["runes"].values())
            else:
                runes = monster["runes"]

            for rune in runes:
                if rune["upgrade_curr"] >= 12:
                    if str(rune["set_id"]) == data_xzandro["rune"]["reverse_sets"][set]:
                        rune_array.append(effi_rune.calcul_effi_rune(rune))
                        rune_max_array.append((effi_rune.calcul_effi_max(rune)))

        rune_sorted  = sorted(rune_array, reverse=True)[:300]
        rune_max_sorted  = sorted(rune_max_array, reverse=True)[:300]

        print(rune_sorted)
        print(rune_max_sorted)

        plt.figure(figsize=(10, 6))
        plt.plot(rune_sorted, marker='o', label='Rune effi', color='blue')
        plt.plot(rune_max_sorted, marker='x', label='Rune effi max', color='red')
        plt.title('Comparison of Top ' + str(len(rune_sorted)) + " " + set + ' Rune Values')
        plt.xlabel('Rune Index')
        plt.ylabel('Rune Value')
        plt.grid(True)
        plt.legend()
        plt.savefig(image_filename)


def effi_graph_without_set(json_f, image_filename):
    data = json.load(json_f)
    rune_array = []
    rune_max_array = []

    for rune in data["runes"]:
        if rune["upgrade_curr"] >= 12:
            rune_array.append(effi_rune.calcul_effi_rune(rune))
            rune_max_array.append((effi_rune.calcul_effi_max(rune)))

    for monster in data["unit_list"]:

        if isinstance(monster["runes"], dict):
            runes = list(monster["runes"].values())
        else:
            runes = monster["runes"]

        for rune in runes:
            if rune["upgrade_curr"] >= 12:
                rune_array.append(effi_rune.calcul_effi_rune(rune))
                rune_max_array.append((effi_rune.calcul_effi_max(rune)))

    rune_sorted = sorted(rune_array, reverse=True)[:300]
    rune_max_sorted = sorted(rune_max_array, reverse=True)[:300]

    print(rune_sorted)
    print(rune_max_sorted)

    plt.figure(figsize=(10, 6))
    plt.plot(rune_sorted, marker='o', label='Rune effi', color='blue')
    plt.plot(rune_max_sorted, marker='x', label='Rune effi max', color='red')
    plt.title('Comparison of Top ' + str(len(rune_sorted)) + ' Rune Values')
    plt.xlabel('Rune Index')
    plt.ylabel('Rune Value')
    plt.grid(True)
    plt.legend()
    plt.savefig(image_filename)