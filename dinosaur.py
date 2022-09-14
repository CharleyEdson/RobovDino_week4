

class Dinosaur:

    def __init__(self,name):
        self.name = name
        self.attack_power = 50
        self.health = 100
        self.is_alive = True
        
        
   
    def update_stats_trex(self):
        self.health = self.health * 1.1
        self.attack_power = self.attack_power * .9

    def update_stats_raptor(self):
        self.health = self.health * 0.9
        self.attack_power = self.attack_power * 1.2 

    def choose_type_of_dino(self):
        dino_type = input("Please choose the type of Dinosaur you want: 1) 'Regular', 2) 'Trex', and 3) 'Raptor'")
        if dino_type == '1':
            hello = 'nothing'
        if dino_type == '2':
            self.update_stats_trex()   
        if dino_type == '3':
            self.update_stats_raptor()
               

    def attack(self, robot):
        print(f'{self.name} attacked {robot.name} for {str(self.attack_power)} damage!')
        robot.health -= self.attack_power
        if robot.health > 0:
            print(f'{robot.name} has {str(robot.health)} health reamining!')
        else:
            print(f'{robot.name} has 0 health reamining!')

    

    

        
        
    