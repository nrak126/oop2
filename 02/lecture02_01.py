import csv

def lecture02_01_printHeroStatus(weapon_data) -> None:
    # implement me

def lecture02_01_printWeaponStatus() -> None:
    # implement me

def lecture02_01_printHeroStatusWithWeapon() -> None:
    weapon_header = []
    weapon_data = []
    with open('lecture02_Weapon.csv') as f:
        reader = csv.reader(f)
    for row in reader:
        if len(weapon_header) == 0:
            weapon_header = row
        else :
            weapon_data.append(row)
    # ステータス情報を出力する
    print(f"{weapon_name}を装備した{hero_name}のステータスは" +
        f"HP:{hero_hp+weapon_hp}," +
        f"MP:{hero_mp+weapon_mp}," +
        f"Atk:{hero_atk+weapon_atk}," +
        f"Def:{hero_def+weapon_def}," +
        f"Age:{hero_age+weapon_age}")

if __name__ == '__main__':
    lecture02_01_printHeroStatus()
    lecture02_01_printWeaponStatus()
    lecture02_01_printHeroStatusWithWeapon()