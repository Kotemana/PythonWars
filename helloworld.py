import monster_desc
dagger = monster_desc.Weapon(1, 6, "dagger", monster_desc.WeaponType.PIERCE)
warhammer = monster_desc.Weapon(1, 8, "warhammer", monster_desc.WeaponType.BLUNT)
monster = monster_desc.Monster("Orc", 100, 2, dagger)
hero = monster_desc.Monster("Paladin", 50, 10)

while True:
    if monster_desc.fight(hero, monster):
        break
    if monster_desc.fight(monster, hero):
        break





