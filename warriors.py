class Warrior:
    hp = 50
    attack = 5
    is_alive = True
    
class Defender(Warrior):
    health = 60
    attack = 3
    defense = 2

class Knight(Warrior):
    attack = 7
    
class Army:
    def __init__(self):
        self.warriors = []
        
    def add_units(self, objects, count):
        for i in range(count):
            self.warriors.append(objects())


class Battle:
    def fight(self, object1, object2):
        while len(object1.warriors) != 0 or len(object2.warriors) != 0:
            if fight(object1.warriors[0], object2.warriors[0]):
                object2.warriors.pop(0)
                if len(object2.warriors) == 0:
                    return True
            else:
                object1.warriors.pop(0)
                if len(object1.warriors) == 0:
                    return False
                

def fight(unit_1, unit_2):
    while unit_1.is_alive == True or unit_2.is_alive == True:
        unit_2.hp -= unit_1.attack
        if unit_2.hp <= 0:
            unit_2.is_alive = False
            return True
        unit_1.hp -= unit_2.attack
        if unit_1.hp <= 0:
            unit_1.is_alive = False
            return False
