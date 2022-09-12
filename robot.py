
class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.active_weapon = weapon
        
    def attack(self, dinosaur):
        print(f'{self.name} attacked {dinosaur.name} for {str(self.active_weapon.attack_power)} damage!')
        dinosaur.health -= self.active_weapon.attack_power
        if dinosaur.health > 0:
            print(f'{dinosaur.name} has {str(dinosaur.health)} health reamining!')
        else:
            print(f'{dinosaur.name} has 0 health reamining!')
        