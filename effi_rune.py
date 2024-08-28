import json


def calcul_effi_rune(rune):
    with open('stats_runes.json', encoding='utf8') as stats_runes_f:
        stats_runes = json.load(stats_runes_f)

        if rune["upgrade_curr"] < 12 :
            return 0
        sum_eff = 1

        if rune["prefix_eff"][0]!=0:
            sum_eff += (rune["prefix_eff"][1] / stats_runes[str(rune["prefix_eff"][0])][0]) * stats_runes[str(rune["prefix_eff"][0])][2]

        for sub in rune["sec_eff"]:
            sum_eff += ((sub[1]+sub[3]) / stats_runes[str(sub[0])][0]) * stats_runes[str(sub[0])][3]
        return sum_eff*100/2.8


def calcul_effi_max(rune):
    with open('stats_runes.json', encoding='utf8') as stats_runes_f:
        stats_runes = json.load(stats_runes_f)

        if rune["upgrade_curr"] < 12 :
            return 0
        sum_eff = 1

        if rune["prefix_eff"][0] != 0:
            sum_eff += (rune["prefix_eff"][1] / stats_runes[str(rune["prefix_eff"][0])][0]) * stats_runes[str(rune["prefix_eff"][0])][2]

        for sub in rune["sec_eff"]:
            sum_eff += ((sub[1]+ max(sub[3],stats_runes[str(sub[0])][1])) / stats_runes[str(sub[0])][0]) * stats_runes[str(sub[0])][3]
        return sum_eff*100/2.8


