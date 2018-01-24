from die import *

def fight(attacker, receiver):
    if(attacker.check_hit_another(receiver)):
        print(attacker.name, "hits", receiver.name, "for", attacker.hit_another(receiver), "hp. Now", \
              receiver.name, "is", receiver.hp)
    else:
        print(attacker.name, "misses", receiver.name)
    if (receiver.is_dead):
        print(receiver.name, "is dead!", attacker.name, "wins")
        return True
    return False

class Monster:

    def __init__(self, name, hp, armor, ap_throws, ap_sides):
        self.attack_power = AttackPower(ap_throws, ap_sides)
        self.name=name
        self.hp=hp
        self.armor=armor

    @property
    def is_dead(self):
        return self.hp<0

    def check_hit_another(self, another):
        """
        :param another: is monster
        :returns bool
        """


        die=Die(20)
        return die.roll(1)>5+another.armor

    def hit_another(self, another):
        """
        :param another: is monster
        :returns bool
        """


        die=Die(self.attack_power.sides)
        result=die.roll(self.attack_power.throws)
        another.hp-=result
        return result



class AttackPower:
    def __init__(self, ap_throws, ap_sides):
        self.sides = ap_sides
        self.throws = ap_throws