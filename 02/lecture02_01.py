import csv

def lecture02_01_printHeroStatus() -> None:
    with open('lecture02_Hero.csv') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダー行をスキップ
        for row in reader:
            if row[0] == '1':  # idが1の行を探す
                hero_name = row[1]
                hero_hp = int(row[2])
                hero_mp = int(row[3])
                hero_atk = int(row[4])
                hero_def = int(row[5])
                hero_age = int(row[6])
                print(f"{hero_name}のステータスはHP:{hero_hp},MP:{hero_mp},Atk:{hero_atk},Def:{hero_def},Age:{hero_age}")
                break

def lecture02_01_printWeaponStatus() -> None:
    with open('lecture02_Weapon.csv') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダー行をスキップ
        for row in reader:
            if row[0] == '1':  # idが1の行を探す
                weapon_name = row[1]
                weapon_hp = int(row[2])
                weapon_mp = int(row[3])
                weapon_atk = int(row[4])
                weapon_def = int(row[5])
                weapon_age = int(row[6])
                print(f"{weapon_name}のステータスはHP:{weapon_hp},MP:{weapon_mp},Atk:{weapon_atk},Def:{weapon_def},Age:{weapon_age}")
                break

def lecture02_01_printHeroStatusWithWeapon() -> None:
    # Heroのデータを読み込む
    with open('lecture02_Hero.csv') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダー行をスキップ
        for row in reader:
            if row[0] == '1':  # idが1の行を探す
                hero_name = row[1]
                hero_hp = int(row[2])
                hero_mp = int(row[3])
                hero_atk = int(row[4])
                hero_def = int(row[5])
                hero_age = int(row[6])
                hero_weapon = row[7]
                break
    
    # Weaponのデータを読み込む
    with open('lecture02_Weapon.csv') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダー行をスキップ
        for row in reader:
            if row[0] == hero_weapon:  # hero_weaponと一致する行を探す
                weapon_name = row[1]
                weapon_hp = int(row[2])
                weapon_mp = int(row[3])
                weapon_atk = int(row[4])
                weapon_def = int(row[5])
                weapon_age = int(row[6])
                break
    
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