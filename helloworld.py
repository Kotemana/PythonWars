import die
import monster_desc

monster = monster_desc.Monster("Orc", 100, 2, 2, 6)
hero = monster_desc.Monster("Paladin", 50, 5, 2, 8)



while(True):
    if(monster_desc.fight(hero, monster)):
        break
    if (monster_desc.fight(monster, hero)):
        break





