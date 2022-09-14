from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('The Slicer', 50)
        self.active_weapon_list = [Weapon('The Slicer', 20), Weapon('Robo Mace', 22), Weapon('Robo sword', 24)]
        self.is_alive = True

    # Need to put this in the code so they can choose
    def choose_attack_weapon(self):
        robot_weapon = input("Please choose the weapon of choice, between: 1) 'The Slicer', 2) 'Robo Mace', and 3)'Robo Sword'")
        if robot_weapon == "1":
            self.active_weapon = self.active_weapon_list[0]
        elif robot_weapon == "2":
            self.active_weapon = self.active_weapon_list[1]
        elif robot_weapon == "3":
            self.active_weapon = self.active_weapon_list[2]    

    def attack(self, dinosaur):
        print(f'{self.name} attacked {dinosaur.name} for {str(self.active_weapon.attack_power)} damage!')
        dinosaur.health -= self.active_weapon.attack_power
        if dinosaur.health > 0:
            print(f'{dinosaur.name} has {str(dinosaur.health)} health reamining!')
        else:
            print(f'{dinosaur.name} has 0 health reamining!')
        
    