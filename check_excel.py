import json


def check_excel(sub_type, value, sheet, art_type, attribute, unit_type, main_stat, guild_name):
    with open('guildes_arte_values.json', encoding='utf8') as guild_values_f:
        guild_values = json.load(guild_values_f)
        # Damage dealt on water
        if sub_type == "301":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "101":
                        sheet['H4'] = int(sheet['H4'].value) + 1
                    elif main_stat == "100":
                        sheet['H11'] = int(sheet['H11'].value) + 1
                    elif main_stat == "102":
                        sheet['H18'] = int(sheet['H18'].value) + 1

                elif attribute == "2":
                    if main_stat == "101":
                        sheet['I4'] = sheet['I4'].value + 1
                    elif main_stat == "100":
                        sheet['I11'] = sheet['I11'].value + 1

                elif attribute == "3":
                    if main_stat == "101":
                        sheet['J4'] = sheet['J4'].value + 1
                    elif main_stat == "100":
                        sheet['J11'] = sheet['J11'].value + 1
                    if main_stat == "102":
                        sheet['J18'] = sheet['J18'].value + 1

                elif attribute == "4":
                    if main_stat == "101":
                        sheet['K4'] = sheet['K4'].value + 1
                    elif main_stat == "100":
                        sheet['K11'] = sheet['K11'].value + 1
                    if main_stat == "102":
                        sheet['K18'] = sheet['K18'].value + 1

                elif attribute == "5":
                    if main_stat == "101":
                        sheet['L4'] = sheet['L4'].value + 1
                    elif main_stat == "100":
                        sheet['L11'] = sheet['L11'].value + 1
                    if main_stat == "102":
                        sheet['L18'] = sheet['L18'].value + 1

        # Damage dealt on fire
        elif sub_type == "300":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "101":
                        sheet['H5'] = sheet['H5'].value + 1
                    elif main_stat == "100":
                        sheet['H12'] = sheet['H12'].value + 1
                    elif main_stat == "102":
                        sheet['H19'] = sheet['H19'].value + 1

                elif attribute == "2":
                    if main_stat == "101":
                        sheet['I5'] = sheet['I5'].value + 1
                    elif main_stat == "100":
                        sheet['I12'] = sheet['I12'].value + 1
                    if main_stat == "102":
                        sheet['I19'] = sheet['I19'].value + 1

                elif attribute == "3":
                    if main_stat == "101":
                        sheet['J5'] = sheet['J5'].value + 1
                    elif main_stat == "100":
                        sheet['J12'] = sheet['J12'].value + 1

                elif attribute == "4":
                    if main_stat == "101":
                        sheet['K5'] = sheet['K5'].value + 1
                    elif main_stat == "100":
                        sheet['K12'] = sheet['K12'].value + 1
                    if main_stat == "102":
                        sheet['K19'] = sheet['K19'].value + 1

                elif attribute == "5":
                    if main_stat == "101":
                        sheet['L5'] = sheet['L5'].value + 1
                    elif main_stat == "100":
                        sheet['L12'] = sheet['L12'].value + 1
                    if main_stat == "102":
                        sheet['L19'] = sheet['L19'].value + 1

        # Damage dealt on wind
        elif sub_type == "302":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "101":
                        sheet['H6'] = sheet['H6'].value + 1
                    elif main_stat == "100":
                        sheet['H13'] = sheet['H13'].value + 1

                elif attribute == "2":
                    if main_stat == "101":
                        sheet['I6'] = sheet['I6'].value + 1
                    elif main_stat == "100":
                        sheet['I13'] = sheet['I13'].value + 1
                    if main_stat == "102":
                        sheet['I20'] = sheet['I20'].value + 1

                elif attribute == "3":
                    if main_stat == "101":
                        sheet['J6'] = sheet['J6'].value + 1
                    elif main_stat == "100":
                        sheet['J13'] = sheet['J13'].value + 1
                    if main_stat == "102":
                        sheet['J20'] = sheet['J20'].value + 1

                elif attribute == "4":
                    if main_stat == "101":
                        sheet['K6'] = sheet['K6'].value + 1
                    elif main_stat == "100":
                        sheet['K13'] = sheet['K13'].value + 1
                    if main_stat == "102":
                        sheet['K20'] = sheet['K20'].value + 1

                elif attribute == "5":
                    if main_stat == "101":
                        sheet['L6'] = sheet['L6'].value + 1
                    elif main_stat == "100":
                        sheet['L13'] = sheet['L13'].value + 1
                    if main_stat == "102":
                        sheet['L20'] = sheet['L20'].value + 1

    # Damage dealt on light
        elif sub_type == "303":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "101":
                        sheet['H7'] = sheet['H7'].value + 1
                    elif main_stat == "100":
                        sheet['H14'] = sheet['H14'].value + 1
                    elif main_stat == "102":
                        sheet['H21'] = sheet['H21'].value + 1

                elif attribute == "2":
                    if main_stat == "101":
                        sheet['I7'] = sheet['I7'].value + 1
                    elif main_stat == "100":
                        sheet['I14'] = sheet['I14'].value + 1
                    if main_stat == "102":
                        sheet['I21'] = sheet['I21'].value + 1

                elif attribute == "3":
                    if main_stat == "101":
                        sheet['J7'] = sheet['J7'].value + 1
                    elif main_stat == "100":
                        sheet['J14'] = sheet['J14'].value + 1
                    if main_stat == "102":
                        sheet['J21'] = sheet['J21'].value + 1

                elif attribute == "4":
                    if main_stat == "101":
                        sheet['K7'] = sheet['K7'].value + 1
                    elif main_stat == "100":
                        sheet['K14'] = sheet['K14'].value + 1
                    if main_stat == "102":
                        sheet['K21'] = sheet['K21'].value + 1

                elif attribute == "5":
                    if main_stat == "101":
                        sheet['L7'] = sheet['L7'].value + 1
                    elif main_stat == "100":
                        sheet['L14'] = sheet['L14'].value + 1
                    if main_stat == "102":
                        sheet['L21'] = sheet['L21'].value + 1

        # Damage dealt on dark
        elif sub_type == "304":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "101":
                        sheet['H8'] = sheet['H8'].value + 1
                    elif main_stat == "100":
                        sheet['H15'] = sheet['H15'].value + 1
                    elif main_stat == "102":
                        sheet['H22'] = sheet['H22'].value + 1

                elif attribute == "2":
                    if main_stat == "101":
                        sheet['I8'] = sheet['I8'].value + 1
                    elif main_stat == "100":
                        sheet['I15'] = sheet['I15'].value + 1
                    if main_stat == "102":
                        sheet['I22'] = sheet['I22'].value + 1

                elif attribute == "3":
                    if main_stat == "101":
                        sheet['J8'] = sheet['J8'].value + 1
                    elif main_stat == "100":
                        sheet['J15'] = sheet['J15'].value + 1
                    if main_stat == "102":
                        sheet['J22'] = sheet['J22'].value + 1

                elif attribute == "4":
                    if main_stat == "101":
                        sheet['K8'] = sheet['K8'].value + 1
                    elif main_stat == "100":
                        sheet['K15'] = sheet['K15'].value + 1
                    if main_stat == "102":
                        sheet['K22'] = sheet['K22'].value + 1

                elif attribute == "5":
                    if main_stat == "101":
                        sheet['L8'] = sheet['L8'].value + 1
                    elif main_stat == "100":
                        sheet['L15'] = sheet['L15'].value + 1
                    if main_stat == "102":
                        sheet['L22'] = sheet['L22'].value + 1

    # Damage received from water
        elif sub_type == "306":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "100":
                        sheet['U4'] = int(sheet['U4'].value) + 1
                    elif main_stat == "102":
                        sheet['U11'] = int(sheet['U11'].value) + 1
                    elif main_stat == "101":
                        sheet['U18'] = int(sheet['U18'].value) + 1

                elif attribute == "2":
                    if main_stat == "100":
                        sheet['V4'] = sheet['V4'].value + 1
                    elif main_stat == "102":
                        sheet['V11'] = sheet['V11'].value + 1
                    elif main_stat == "101":
                        sheet['V18'] = sheet['V18'].value + 1

                elif attribute == "3":
                    if main_stat == "100":
                        sheet['W4'] = sheet['W4'].value + 1
                    elif main_stat == "102":
                        sheet['W11'] = sheet['W11'].value + 1
                    elif main_stat == "101":
                        sheet['W18'] = sheet['W18'].value + 1

                elif attribute == "4":
                    if main_stat == "100":
                        sheet['X4'] = sheet['X4'].value + 1
                    elif main_stat == "102":
                        sheet['X11'] = sheet['X11'].value + 1
                    elif main_stat == "101":
                        sheet['X18'] = sheet['X18'].value + 1

                elif attribute == "5":
                    if main_stat == "100":
                        sheet['Y4'] = sheet['Y4'].value + 1
                    elif main_stat == "102":
                        sheet['Y11'] = sheet['Y11'].value + 1
                    elif main_stat == "101":
                        sheet['Y18'] = sheet['Y18'].value + 1

        # Damage dealt on fire
        elif sub_type == "305":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "100":
                        sheet['U5'] = sheet['U5'].value + 1
                    elif main_stat == "102":
                        sheet['U12'] = sheet['U12'].value + 1
                    elif main_stat == "101":
                        sheet['U19'] = sheet['U19'].value + 1

                elif attribute == "2":
                    if main_stat == "100":
                        sheet['V5'] = sheet['V5'].value + 1
                    elif main_stat == "102":
                        sheet['V12'] = sheet['V12'].value + 1
                    elif main_stat == "101":
                        sheet['V19'] = sheet['V19'].value + 1

                elif attribute == "3":
                    if main_stat == "100":
                        sheet['W5'] = sheet['W5'].value + 1
                    elif main_stat == "102":
                        sheet['W12'] = sheet['W12'].value + 1
                    elif main_stat == "101":
                        sheet['W19'] = sheet['W19'].value + 1

                elif attribute == "4":
                    if main_stat == "100":
                        sheet['X5'] = sheet['X5'].value + 1
                    elif main_stat == "102":
                        sheet['X12'] = sheet['X12'].value + 1
                    elif main_stat == "101":
                        sheet['X19'] = sheet['X19'].value + 1

                elif attribute == "5":
                    if main_stat == "100":
                        sheet['Y5'] = sheet['Y5'].value + 1
                    elif main_stat == "102":
                        sheet['Y12'] = sheet['Y12'].value + 1
                    elif main_stat == "101":
                        sheet['Y19'] = sheet['Y19'].value + 1

        # Damage received from wind
        elif sub_type == "307":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "100":
                        sheet['U6'] = sheet['U6'].value + 1
                    elif main_stat == "102":
                        sheet['U13'] = sheet['U13'].value + 1
                    elif main_stat == "101":
                        sheet['U20'] = sheet['U20'].value + 1

                elif attribute == "2":
                    if main_stat == "100":
                        sheet['V6'] = sheet['V6'].value + 1
                    elif main_stat == "102":
                        sheet['V13'] = sheet['V13'].value + 1
                    elif main_stat == "101":
                        sheet['V20'] = sheet['V20'].value + 1

                elif attribute == "3":
                    if main_stat == "100":
                        sheet['W6'] = sheet['W6'].value + 1
                    elif main_stat == "102":
                        sheet['W13'] = sheet['W13'].value + 1
                    elif main_stat == "101":
                        sheet['W20'] = sheet['W20'].value + 1

                elif attribute == "4":
                    if main_stat == "100":
                        sheet['X6'] = sheet['X6'].value + 1
                    elif main_stat == "102":
                        sheet['X13'] = sheet['X13'].value + 1
                    elif main_stat == "101":
                        sheet['X20'] = sheet['X20'].value + 1

                elif attribute == "5":
                    if main_stat == "100":
                        sheet['Y6'] = sheet['Y6'].value + 1
                    elif main_stat == "102":
                        sheet['Y13'] = sheet['Y13'].value + 1
                    elif main_stat == "101":
                        sheet['Y20'] = sheet['Y20'].value + 1

        # Damage dealt on light
        elif sub_type == "308":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "100":
                        sheet['U7'] = sheet['U7'].value + 1
                    elif main_stat == "102":
                        sheet['U14'] = sheet['U14'].value + 1
                    elif main_stat == "101":
                        sheet['U21'] = sheet['U21'].value + 1

                elif attribute == "2":
                    if main_stat == "100":
                        sheet['V7'] = sheet['V7'].value + 1
                    elif main_stat == "102":
                        sheet['V14'] = sheet['V14'].value + 1
                    if main_stat == "101":
                        sheet['V21'] = sheet['V21'].value + 1

                elif attribute == "3":
                    if main_stat == "100":
                        sheet['W7'] = sheet['W7'].value + 1
                    elif main_stat == "102":
                        sheet['W14'] = sheet['W14'].value + 1
                    if main_stat == "101":
                        sheet['W21'] = sheet['W21'].value + 1

                elif attribute == "4":
                    if main_stat == "100":
                        sheet['X7'] = sheet['X7'].value + 1
                    elif main_stat == "102":
                        sheet['X14'] = sheet['X14'].value + 1
                    if main_stat == "101":
                        sheet['X21'] = sheet['X21'].value + 1

                elif attribute == "5":
                    if main_stat == "100":
                        sheet['Y7'] = sheet['Y7'].value + 1
                    elif main_stat == "102":
                        sheet['Y14'] = sheet['Y14'].value + 1
                    if main_stat == "101":
                        sheet['Y21'] = sheet['Y21'].value + 1

        # Damage dealt on dark
        elif sub_type == "309":
            if value >= guild_values[str(sub_type)][guild_name]:
                if attribute == "1":
                    if main_stat == "100":
                        sheet['U8'] = sheet['U8'].value + 1
                    elif main_stat == "102":
                        sheet['U15'] = sheet['U15'].value + 1
                    elif main_stat == "101":
                        sheet['U22'] = sheet['U22'].value + 1

                elif attribute == "2":
                    if main_stat == "100":
                        sheet['V8'] = sheet['V8'].value + 1
                    elif main_stat == "102":
                        sheet['V15'] = sheet['V15'].value + 1
                    if main_stat == "101":
                        sheet['V22'] = sheet['V22'].value + 1

                elif attribute == "3":
                    if main_stat == "100":
                        sheet['W8'] = sheet['W8'].value + 1
                    elif main_stat == "102":
                        sheet['W15'] = sheet['W15'].value + 1
                    if main_stat == "101":
                        sheet['W22'] = sheet['W22'].value + 1

                elif attribute == "4":
                    if main_stat == "100":
                        sheet['X8'] = sheet['X8'].value + 1
                    elif main_stat == "102":
                        sheet['X15'] = sheet['X15'].value + 1
                    if main_stat == "101":
                        sheet['X22'] = sheet['X22'].value + 1

                elif attribute == "5":
                    if main_stat == "100":
                        sheet['Y8'] = sheet['Y8'].value + 1
                    elif main_stat == "102":
                        sheet['Y15'] = sheet['Y15'].value + 1
                    if main_stat == "101":
                        sheet['Y22'] = sheet['Y22'].value + 1



        elif sub_type == "219":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "101":
                    if attribute == "1":
                        sheet['H29'] = sheet['H29'].value + 1
                    elif attribute == "2":
                        sheet['I29'] = sheet['I29'].value + 1
                    elif attribute == "3":
                        sheet['J29'] = sheet['J29'].value + 1
                    elif attribute == "4":
                        sheet['K29'] = sheet['K29'].value + 1
                    elif attribute == "5":
                        sheet['L29'] = sheet['L29'].value + 1
                    elif unit_type == "1":
                        sheet['AR5'] = sheet['AR5'].value + 1
                    elif unit_type == "3":
                        sheet['AT5'] = sheet['AT5'].value + 1
                    elif unit_type == "4":
                        sheet['AU5'] = sheet['AU5'].value + 1


        elif sub_type == "225":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "101":
                    if attribute == "1":
                        sheet['H30'] = sheet['H30'].value + 1
                    elif attribute == "2":
                        sheet['I30'] = sheet['I30'].value + 1
                    elif attribute == "3":
                        sheet['J30'] = sheet['J30'].value + 1
                    elif attribute == "4":
                        sheet['K30'] = sheet['K30'].value + 1
                    elif attribute == "5":
                        sheet['L30'] = sheet['L30'].value + 1
                    elif unit_type == "1":
                        sheet['AR7'] = sheet['AR7'].value + 1

                elif main_stat == "102":
                    if unit_type == "2":
                        sheet['AS33'] = sheet['AS33'].value + 1

        elif sub_type == "226":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "101":
                    if attribute == "1":
                        sheet['H31'] = sheet['H31'].value + 1
                    elif attribute == "2":
                        sheet['I31'] = sheet['I31'].value + 1
                    elif attribute == "3":
                        sheet['J31'] = sheet['J31'].value + 1
                    elif attribute == "4":
                        sheet['K31'] = sheet['K31'].value + 1
                    elif attribute == "5":
                        sheet['L31'] = sheet['L31'].value + 1
                    elif unit_type == "1":
                        sheet['AR4'] = sheet['AR4'].value + 1
                    elif unit_type == "4":
                        sheet['AU4'] = sheet['AU4'].value + 1

                elif main_stat == "102":
                    if attribute == "2":
                        sheet['I38'] = sheet['I38'].value + 1
                    elif attribute == "3":
                        sheet['J38'] = sheet['J38'].value + 1
                    elif attribute == "5":
                        sheet['L38'] = sheet['L38'].value + 1
                    if unit_type == "2":
                        sheet['AS37'] = sheet['AS37'].value + 1
                    if unit_type == "3":
                        sheet['AT37'] = sheet['AT37'].value + 1

        elif sub_type == "210":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "101":
                    if attribute == "1":
                        sheet['H32'] = sheet['H32'].value + 1
                    elif attribute == "2":
                        sheet['I32'] = sheet['I32'].value + 1
                    elif attribute == "3":
                        sheet['J32'] = sheet['J32'].value + 1
                    elif attribute == "4":
                        sheet['K32'] = sheet['K32'].value + 1
                    elif attribute == "5":
                        sheet['L32'] = sheet['L32'].value + 1
                    elif unit_type == "1":
                        sheet['AR6'] = sheet['AR6'].value + 1

        elif sub_type == "223":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "101":
                    if attribute == "1":
                        sheet['H33'] = sheet['H33'].value + 1
                    elif attribute == "3":
                        sheet['J33'] = sheet['J33'].value + 1
                    elif unit_type == "1":
                        sheet['AR8'] = sheet['AR8'].value + 1
                    elif unit_type == "4":
                        sheet['AU8'] = sheet['AU8'].value + 1
                if main_stat == "102":
                    if unit_type == "3":
                        sheet['AT36'] = sheet['AT36'].value + 1
                    elif unit_type == "4":
                        sheet['AU36'] = sheet['AU36'].value + 1

        elif sub_type == "218":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if attribute == "1":
                        sheet['H35'] = sheet['H35'].value + 1
                    elif attribute == "2":
                        sheet['I35'] = sheet['I35'].value + 1
                    elif attribute == "3":
                        sheet['J35'] = sheet['J35'].value + 1
                    elif attribute == "4":
                        sheet['K35'] = sheet['K35'].value + 1
                    elif attribute == "5":
                        sheet['L35'] = sheet['L35'].value + 1
                    elif unit_type == "1":
                        sheet['AR17'] = sheet['AR17'].value + 1
                    elif unit_type == "2":
                        sheet['AS17'] = sheet['AS17'].value + 1
                    elif unit_type == "3":
                        sheet['AT17'] = sheet['AT17'].value + 1
                    elif unit_type == "4":
                        sheet['AU17'] = sheet['AU17'].value + 1
                if main_stat == "102":
                    if unit_type == "1":
                        sheet['AR30'] = sheet['AR30'].value + 1
                    elif unit_type == "2":
                        sheet['AS30'] = sheet['AS30'].value + 1
                    elif unit_type == "3":
                        sheet['AT30'] = sheet['AT30'].value + 1
                    elif unit_type == "4":
                        sheet['AU30'] = sheet['AU30'].value + 1

        elif sub_type == "220":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "1":
                        sheet['AR18'] = sheet['AR18'].value + 1
                    elif unit_type == "2":
                        sheet['AS18'] = sheet['AS18'].value + 1
                    elif unit_type == "3":
                        sheet['AT18'] = sheet['AT18'].value + 1
                    elif unit_type == "4":
                        sheet['AU18'] = sheet['AU18'].value + 1

                if main_stat == "102":
                    if attribute == "1":
                        sheet['H37'] = sheet['H37'].value + 1
                    elif attribute == "2":
                        sheet['I37'] = sheet['I37'].value + 1
                    elif attribute == "3":
                        sheet['J37'] = sheet['J37'].value + 1
                    elif attribute == "4":
                        sheet['K37'] = sheet['K37'].value + 1
                    elif attribute == "5":
                        sheet['L37'] = sheet['L37'].value + 1
                    elif unit_type == "1":
                        sheet['AR31'] = sheet['AR31'].value + 1
                    elif unit_type == "2":
                        sheet['AS31'] = sheet['AS31'].value + 1
                    elif unit_type == "3":
                        sheet['AT31'] = sheet['AT31'].value + 1
                    elif unit_type == "4":
                        sheet['AU31'] = sheet['AU31'].value + 1

        elif sub_type == "206":
            if value >= guild_values[str(sub_type)][guild_name]:

                if attribute == "1":
                    sheet['H40'] = sheet['H40'].value + 1
                elif attribute == "2":
                    sheet['I40'] = sheet['I40'].value + 1
                elif attribute == "3":
                    sheet['J40'] = sheet['J40'].value + 1
                elif attribute == "4":
                    sheet['K40'] = sheet['K40'].value + 1
                elif attribute == "5":
                    sheet['L40'] = sheet['L40'].value + 1

                elif main_stat == "100":
                    if unit_type == "1":
                        sheet['AG21'] = sheet['AG21'].value + 1
                    if unit_type == "2":
                        sheet['AH21'] = sheet['AH21'].value + 1
                    if unit_type == "3":
                        sheet['AI21'] = sheet['AI21'].value + 1
                    if unit_type == "4":
                        sheet['AJ21'] = sheet['AJ21'].value + 1
                elif main_stat == "101":
                    if unit_type == "1":
                        sheet['AG8'] = sheet['AG8'].value + 1
                    if unit_type == "2":
                        sheet['AH8'] = sheet['AH8'].value + 1
                    if unit_type == "3":
                        sheet['AI8'] = sheet['AI8'].value + 1
                    if unit_type == "4":
                        sheet['AJ8'] = sheet['AJ8'].value + 1
                elif main_stat == "102":
                    if unit_type == "1":
                        sheet['AG34'] = sheet['AG34'].value + 1
                    if unit_type == "2":
                        sheet['AH34'] = sheet['AH34'].value + 1
                    if unit_type == "3":
                        sheet['AI34'] = sheet['AI34'].value + 1
                    if unit_type == "4":
                        sheet['AJ34'] = sheet['AJ34'].value + 1

        elif sub_type == "221":
            if value >= guild_values[str(sub_type)][guild_name]:

                if attribute == "1":
                    sheet['H41'] = sheet['H41'].value + 1
                elif attribute == "2":
                    sheet['I41'] = sheet['I41'].value + 1
                elif attribute == "3":
                    sheet['J41'] = sheet['J41'].value + 1
                elif attribute == "4":
                    sheet['K41'] = sheet['K41'].value + 1
                elif attribute == "5":
                    sheet['L41'] = sheet['L41'].value + 1

                elif main_stat == "101":
                    if unit_type == "1":
                        sheet['AR11'] = sheet['AR11'].value + 1
                    elif unit_type == "2":
                        sheet['AS11'] = sheet['AS11'].value + 1
                    elif unit_type == "3":
                        sheet['AT11'] = sheet['AT11'].value + 1
                    elif unit_type == "4":
                        sheet['AU11'] = sheet['AU11'].value + 1

                elif main_stat == "100":
                    if unit_type == "1":
                        sheet['AR19'] = sheet['AR19'].value + 1
                    elif unit_type == "2":
                        sheet['AS19'] = sheet['AS19'].value + 1
                    elif unit_type == "3":
                        sheet['AT19'] = sheet['AT19'].value + 1
                    elif unit_type == "4":
                        sheet['AU19'] = sheet['AU19'].value + 1

                elif main_stat == "102":
                    if unit_type == "1":
                        sheet['AR32'] = sheet['AR32'].value + 1
                    elif unit_type == "2":
                        sheet['AS32'] = sheet['AS32'].value + 1
                    elif unit_type == "3":
                        sheet['AT32'] = sheet['AT32'].value + 1
                    elif unit_type == "4":
                        sheet['AU32'] = sheet['AU32'].value + 1
        elif sub_type == "411":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "101":
                    if unit_type == "1":
                        sheet['AR9'] = sheet['AR9'].value + 1
                    elif unit_type == "4":
                        sheet['AU9'] = sheet['AU9'].value + 1

                elif main_stat == "102":
                    if unit_type == "2":
                        sheet['AS34'] = sheet['AS34'].value + 1
                    elif unit_type == "3":
                        sheet['AT34'] = sheet['AT34'].value + 1
                    elif unit_type == "4":
                        sheet['AU34'] = sheet['AU34'].value + 1

        elif sub_type == "222":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "101":
                    if unit_type == "1":
                        sheet['AR10'] = sheet['AR10'].value + 1
                    elif unit_type == "4":
                        sheet['AU10'] = sheet['AU10'].value + 1

                elif main_stat == "102":
                    if unit_type == "2":
                        sheet['AS35'] = sheet['AS35'].value + 1
                    elif unit_type == "3":
                        sheet['AT35'] = sheet['AT35'].value + 1
                    elif unit_type == "4":
                        sheet['AU35'] = sheet['AU35'].value + 1

        elif sub_type == "407":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "1":
                        sheet['AG17'] = sheet['AG17'].value + 1
                    elif unit_type == "2":
                        sheet['AH17'] = sheet['AH17'].value + 1
                    elif unit_type == "3":
                        sheet['AI17'] = sheet['AI17'].value + 1
                    elif unit_type == "4":
                        sheet['AJ17'] = sheet['AJ17'].value + 1

                elif main_stat == "101":
                    if unit_type == "1":
                        sheet['AG4'] = sheet['AG4'].value + 1
                    elif unit_type == "2":
                        sheet['AH4'] = sheet['AH4'].value + 1
                    elif unit_type == "3":
                        sheet['AI4'] = sheet['AI4'].value + 1
                    elif unit_type == "4":
                        sheet['AJ4'] = sheet['AJ4'].value + 1

                elif main_stat == "102":
                    if unit_type == "1":
                        sheet['AG30'] = sheet['AG30'].value + 1
                    elif unit_type == "2":
                        sheet['AH30'] = sheet['AH30'].value + 1
                    elif unit_type == "3":
                        sheet['AI30'] = sheet['AI30'].value + 1
                    elif unit_type == "4":
                        sheet['AJ30'] = sheet['AJ30'].value + 1

        elif sub_type == "408":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "1":
                        sheet['AG18'] = sheet['AG18'].value + 1
                    elif unit_type == "2":
                        sheet['AH18'] = sheet['AH18'].value + 1
                    elif unit_type == "3":
                        sheet['AI18'] = sheet['AI18'].value + 1
                    elif unit_type == "4":
                        sheet['AJ18'] = sheet['AJ18'].value + 1

                elif main_stat == "101":
                    if unit_type == "1":
                        sheet['AG5'] = sheet['AG5'].value + 1
                    elif unit_type == "2":
                        sheet['AH5'] = sheet['AH5'].value + 1
                    elif unit_type == "3":
                        sheet['AI5'] = sheet['AI5'].value + 1
                    elif unit_type == "4":
                        sheet['AJ5'] = sheet['AJ5'].value + 1

                elif main_stat == "102":
                    if unit_type == "1":
                        sheet['AG31'] = sheet['AG31'].value + 1
                    elif unit_type == "2":
                        sheet['AH31'] = sheet['AH31'].value + 1
                    elif unit_type == "3":
                        sheet['AI31'] = sheet['AI31'].value + 1
                    elif unit_type == "4":
                        sheet['AJ31'] = sheet['AJ31'].value + 1

        elif sub_type == "409":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "1":
                        sheet['AG19'] = sheet['AG19'].value + 1
                    elif unit_type == "2":
                        sheet['AH19'] = sheet['AH19'].value + 1
                    elif unit_type == "3":
                        sheet['AI19'] = sheet['AI19'].value + 1
                    elif unit_type == "4":
                        sheet['AJ19'] = sheet['AJ19'].value + 1

                elif main_stat == "101":
                    if unit_type == "1":
                        sheet['AG6'] = sheet['AG6'].value + 1
                    elif unit_type == "2":
                        sheet['AH6'] = sheet['AH6'].value + 1
                    elif unit_type == "3":
                        sheet['AI6'] = sheet['AI6'].value + 1
                    elif unit_type == "4":
                        sheet['AJ6'] = sheet['AJ5'].value + 1

                elif main_stat == "102":
                    if unit_type == "1":
                        sheet['AG32'] = sheet['AG32'].value + 1
                    elif unit_type == "2":
                        sheet['AH32'] = sheet['AH32'].value + 1
                    elif unit_type == "3":
                        sheet['AI32'] = sheet['AI32'].value + 1
                    elif unit_type == "4":
                        sheet['AJ32'] = sheet['AJ32'].value + 1

        elif sub_type == "214":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "1":
                        sheet['AG20'] = sheet['AG20'].value + 1
                    elif unit_type == "2":
                        sheet['AH20'] = sheet['AH20'].value + 1
                    elif unit_type == "3":
                        sheet['AI20'] = sheet['AI20'].value + 1
                    elif unit_type == "4":
                        sheet['AJ20'] = sheet['AJ20'].value + 1

                elif main_stat == "102":
                    if unit_type == "1":
                        sheet['AG33'] = sheet['AG33'].value + 1
                    elif unit_type == "2":
                        sheet['AH33'] = sheet['AH33'].value + 1
                    elif unit_type == "3":
                        sheet['AI33'] = sheet['AI33'].value + 1
                    elif unit_type == "4":
                        sheet['AJ33'] = sheet['AJ33'].value + 1

        elif sub_type == "400":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "1":
                        sheet['AG22'] = sheet['AG22'].value + 1
                    elif unit_type == "2":
                        sheet['AH22'] = sheet['AH22'].value + 1
                    elif unit_type == "3":
                        sheet['AI22'] = sheet['AI22'].value + 1
                    elif unit_type == "4":
                        sheet['AJ22'] = sheet['AJ22'].value + 1

                elif main_stat == "101":
                    if unit_type == "1":
                        sheet['AG9'] = sheet['AG9'].value + 1
                    elif unit_type == "2":
                        sheet['AH9'] = sheet['AH9'].value + 1
                    elif unit_type == "3":
                        sheet['AI9'] = sheet['AI9'].value + 1
                    elif unit_type == "4":
                        sheet['AJ9'] = sheet['AJ9'].value + 1

                elif main_stat == "102":
                    if unit_type == "1":
                        sheet['AG35'] = sheet['AG35'].value + 1
                    elif unit_type == "2":
                        sheet['AH35'] = sheet['AH35'].value + 1
                    elif unit_type == "3":
                        sheet['AI35'] = sheet['AI35'].value + 1
                    elif unit_type == "4":
                        sheet['AJ35'] = sheet['AJ35'].value + 1

        elif sub_type == "401":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "1":
                        sheet['AG23'] = sheet['AG23'].value + 1
                    elif unit_type == "2":
                        sheet['AH23'] = sheet['AH23'].value + 1
                    elif unit_type == "3":
                        sheet['AI23'] = sheet['AI23'].value + 1
                    elif unit_type == "4":
                        sheet['AJ23'] = sheet['AJ23'].value + 1

                elif main_stat == "101":
                    if unit_type == "1":
                        sheet['AG10'] = sheet['AG10'].value + 1
                    elif unit_type == "2":
                        sheet['AH10'] = sheet['AH10'].value + 1
                    elif unit_type == "3":
                        sheet['AI10'] = sheet['AI10'].value + 1
                    elif unit_type == "4":
                        sheet['AJ10'] = sheet['AJ10'].value + 1

                elif main_stat == "102":
                    if unit_type == "1":
                        sheet['AG36'] = sheet['AG36'].value + 1
                    elif unit_type == "2":
                        sheet['AH36'] = sheet['AH36'].value + 1
                    elif unit_type == "3":
                        sheet['AI36'] = sheet['AI36'].value + 1
                    elif unit_type == "4":
                        sheet['AJ36'] = sheet['AJ36'].value + 1

        elif sub_type == "410" or sub_type == "402":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "1":
                        sheet['AG24'] = sheet['AG24'].value + 1
                    elif unit_type == "2":
                        sheet['AH24'] = sheet['AH24'].value + 1
                    elif unit_type == "3":
                        sheet['AI24'] = sheet['AI24'].value + 1
                    elif unit_type == "4":
                        sheet['AJ24'] = sheet['AJ24'].value + 1

                elif main_stat == "101":
                    if unit_type == "1":
                        sheet['AG11'] = sheet['AG11'].value + 1
                    elif unit_type == "2":
                        sheet['AH11'] = sheet['AH11'].value + 1
                    elif unit_type == "3":
                        sheet['AI11'] = sheet['AI11'].value + 1
                    elif unit_type == "4":
                        sheet['AJ11'] = sheet['AJ11'].value + 1

                elif main_stat == "102":
                    if unit_type == "1":
                        sheet['AG37'] = sheet['AG37'].value + 1
                    elif unit_type == "2":
                        sheet['AH37'] = sheet['AH37'].value + 1
                    elif unit_type == "3":
                        sheet['AI37'] = sheet['AI37'].value + 1
                    elif unit_type == "4":
                        sheet['AJ37'] = sheet['AJ37'].value + 1

        elif sub_type == "404":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "4":
                        sheet['AJ25'] = sheet['AJ25'].value + 1

                elif main_stat == "102":
                    if unit_type == "4":
                        sheet['AJ35'] = sheet['AJ35'].value + 1

        elif sub_type == "405":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "1":
                        sheet['AG26'] = sheet['AG26'].value + 1
                    elif unit_type == "2":
                        sheet['AH26'] = sheet['AH26'].value + 1
                    elif unit_type == "3":
                        sheet['AI26'] = sheet['AI26'].value + 1
                    elif unit_type == "4":
                        sheet['AJ26'] = sheet['AJ26'].value + 1

                elif main_stat == "101":
                    if unit_type == "4":
                        sheet['AJ13'] = sheet['AJ13'].value + 1

                elif main_stat == "102":
                    if unit_type == "2":
                        sheet['AH39'] = sheet['AH39'].value + 1
                    elif unit_type == "3":
                        sheet['AI39'] = sheet['AI39'].value + 1
                    elif unit_type == "4":
                        sheet['AJ39'] = sheet['AJ39'].value + 1

        elif sub_type == "406":
            if value >= guild_values[str(sub_type)][guild_name]:
                if main_stat == "100":
                    if unit_type == "2":
                        sheet['AH27'] = sheet['AH27'].value + 1
                    elif unit_type == "3":
                        sheet['AI27'] = sheet['AI27'].value + 1
                    elif unit_type == "4":
                        sheet['AJ27'] = sheet['AJ27'].value + 1

                elif main_stat == "102":
                    if unit_type == "2":
                        sheet['AH40'] = sheet['AH40'].value + 1
                    elif unit_type == "3":
                        sheet['AI40'] = sheet['AI40'].value + 1
                    elif unit_type == "4":
                        sheet['AJ40'] = sheet['AJ40'].value + 1

    return sheet
