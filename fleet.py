from robot import Robot
from herd import Herd

class Fleet:
    def __init__(self):
        self.fleet = []
        self.create_fleet()
            
    def create_fleet(self):
        """
        was trying to automate the creation of robos
        list = []
        for num in range(0,2):
        """
        fleet_of_robos_1 = Robot('Robo 1')
        fleet_of_robos_2 = Robot('Robo 2')
        fleet_of_robos_3 = Robot('Robo 3')
        self.fleet.append(fleet_of_robos_1)
        self.fleet.append(fleet_of_robos_2)
        self.fleet.append(fleet_of_robos_3)

    def fleet_attack(self, herd):
        
        #for num in self.fleet:
            #self.fleet[num]
       
        for robo in self.fleet:
            #first dino being attacked           
            if herd.herd[0].is_alive == True:
                herd.herd[0].health -= robo.active_weapon.attack_power
                print(f'{robo.name} attacked {herd.herd[0].name} for {str(robo.active_weapon.attack_power)} damage!')
                if herd.herd[0].health <= 0:
                    herd.herd[0].is_alive = False
                    if herd.herd[0].is_alive == False:
                        print(f'{herd.herd[0].name} perished')
                else:
                    print(f'{herd.herd[0].name} has {str(herd.herd[0].health)} health reamining!')
            #second dino being attacked
            elif herd.herd[1].is_alive == True:
                herd.herd[1].health -= robo.active_weapon.attack_power
                print(f'{robo.name} attacked {herd.herd[1].name} for {str(robo.active_weapon.attack_power)} damage!')
                if herd.herd[1].health <= 0:
                    herd.herd[1].is_alive = False
                    if herd.herd[1].is_alive == False:
                        print(f'{herd.herd[1].name} perished')
                else:
                    print(f'{herd.herd[1].name} has {str(herd.herd[1].health)} health reamining!')
            #third dino being attacked
            elif herd.herd[2].is_alive == True:
                herd.herd[2].health -= robo.active_weapon.attack_power
                print(f'{robo.name} attacked {herd.herd[2].name} for {str(robo.active_weapon.attack_power)} damage!')
                if herd.herd[2].health <= 0:
                    herd.herd[2].is_alive = False
                    if herd.herd[2].is_alive == False:
                        print(f'{herd.herd[0].name} perished')
                else:
                    print(f'{herd.herd[2].name} has {str(herd.herd[2].health)} health reamining!')


            """if herd.herd[0].health > 0:
                robo.attack(herd.herd[0])
            elif herd.herd[1].health > 0:
                robo.attack(herd.herd[1])
            elif herd.herd[2].health > 0:
                robo.attack(herd.herd[2])
            else:
                print('The Herd of Dinos are dead')"""
            




        #This worked in printing out print(f'{self.fleet[counter].name} attacked {herd.herd[counter].name} for {str(self.fleet[counter].active_weapon.attack_power)} damage!')
        #herd.herd[0].health -= self.fleet[counter].active_weapon.attack_power
        
       
    ##Next steps are to create a fleet attack against a herd of dino's. need to create the herd


