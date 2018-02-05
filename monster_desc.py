from die import *
from enum import Enum


def fight(attacker, receiver):
    if not attacker.isStunned:
        if attacker.check_hit_another(receiver):
            print(attacker.name, "hits", receiver.name, "for", attacker.hit_another(receiver), "hp with his ",
                  attacker.weapon.name, ". Now",
                  receiver.name, "is", receiver.hp)
        else:
            print(attacker.name, "misses", receiver.name)
    else:
        print(attacker.name, "is stunned and misses his chance to attack")
        attacker.isStunned = False
    if receiver.is_dead:
        print(receiver.name, "is dead!", attacker.name, "wins")
        return True
    return False


class Monster:
    def __init__(self, name, hp, armor, weapon=None):
        if weapon is None:
            self.weapon = Weapon(1, 2, "bare hands", WeaponType.BLUNT)
        else:
            self.weapon = weapon
        self.name = name
        self.hp = hp
        self.armor = armor
        self.isStunned = False

    @property
    def is_dead(self):
        return self.hp < 0

    def check_hit_another(self, another):
        """
        :param another: is monster
        :returns bool
        """

        die = Die(20)
        to_hit = 5 + another.armor
        if to_hit > 10 and self.weapon.weaponType == WeaponType.PIERCE:
            to_hit = 10
        return die.roll(1) > to_hit

    def hit_another(self, another):
        """
        :param another: is monster
        :returns bool
        """
        die = Die(self.weapon.attack_power.sides)
        result = die.roll(self.weapon.attack_power.throws)
        another.hp -= result
        if self.weapon.weaponType == WeaponType.BLUNT:
            stun_die = Die(5)
            if stun_die.roll(1) == 5:
                another.isStunned = True
                print(another.name, "is stunned by mighty blow of", self.weapon.name)
        return result


class AttackPower:
    def __init__(self, ap_throws, ap_sides):
        self.sides = ap_sides
        self.throws = ap_throws


class Weapon:
    def __init__(self, ap_throws, ap_sides, name, weapon_type):
        self.attack_power = AttackPower(ap_throws, ap_sides)
        self.name = name
        self.weaponType = weapon_type


class WeaponType(Enum):
    PIERCE = 1
    BLUNT = 2
    SLASH = 3
