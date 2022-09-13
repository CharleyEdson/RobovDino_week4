
class Herd:

    def __init__(self, dinosaur):
        self.name = dinosaur.name
        self.attack_power = dinosaur.attack_power
        self.health = dinosaur.health



    def update_stats(self):
        self.health = self.health * 1.1
        self.attack_power = self.attack_power * .9
        
    def attack(self, robot):
        
        print(f'{self.name} attacked {robot.name} for {str(self.attack_power)} damage!')
        robot.health -= self.attack_power
        if robot.health > 0:
            print(f'{robot.name} has {str(robot.health)} health reamining!')
        else:
            print(f'{robot.name} has 0 health reamining!')