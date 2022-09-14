


class Raptor:

    def __init__(self):
        self.name = ''
        self.attack_power = 20
        self.health = 100
        self.type = 'Raptor'
        self.update_stats()



    def update_stats(self):
        self.health = self.health * 0.9
        self.attack_power = self.attack_power * 1.2


    def attack(self, robot):
        
        print(f'{self.name} attacked {robot.name} for {str(self.attack_power)} damage!')
        robot.health -= self.attack_power
        if robot.health > 0:
            print(f'{robot.name} has {str(robot.health)} health reamining!')
        else:
            print(f'{robot.name} has 0 health reamining!')