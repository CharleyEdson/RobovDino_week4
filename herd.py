
from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.herd = []
        self.create_herd()
            
    def create_herd(self):
        """
        was trying to automate the creation of robos
        list = []
        for num in range(0,2):
        """
        herd_of_dinos_1 = Dinosaur('Dino 1')
        herd_of_dinos_2 = Dinosaur('Dino 2')
        herd_of_dinos_3 = Dinosaur('Dino 3')
        self.herd.append(herd_of_dinos_1)
        self.herd.append(herd_of_dinos_2)
        self.herd.append(herd_of_dinos_3)

    def herd_attack(self, fleet):
                
        for dino in self.herd:
            #first dino being attacked           
            if fleet.fleet[0].is_alive == True:
                fleet.fleet[0].health -= dino.attack_power
                print(f'{dino.name} attacked {fleet.fleet[0].name} for {str(dino.attack_power)} damage!')
                if fleet.fleet[0].health <= 0:
                    fleet.fleet[0].is_alive = False
                    if fleet.fleet[0].is_alive == False:
                        print(f'{fleet.fleet[0].name} disintigrated')
                else:
                    print(f'{fleet.fleet[0].name} has {str(fleet.fleet[0].health)} health reamining!')
            #second dino being attacked
            elif fleet.fleet[1].is_alive == True:
                fleet.fleet[1].health -= dino.attack_power
                print(f'{dino.name} attacked {fleet.fleet[1].name} for {str(dino.attack_power)} damage!')
                if fleet.fleet[1].health <= 0:
                    fleet.fleet[1].is_alive = False
                    if fleet.fleet[1].is_alive == False:
                        print(f'{fleet.fleet[1].name} disintigrated')
                else:
                    print(f'{fleet.fleet[1].name} has {str(fleet.fleet[1].health)} health reamining!')
            #third dino being attacked
            elif fleet.fleet[1].is_alive == True:
                fleet.fleet[1].health -= dino.attack_power
                print(f'{dino.name} attacked {fleet.fleet[0].name} for {str(dino.attack_power)} damage!')
                if fleet.fleet[1].health <= 0:
                    fleet.fleet[1].is_alive = False
                    if fleet.fleet[1].is_alive == False:
                        print(f'{fleet.fleet[1].name} disintigrated')
                else:
                    print(f'{fleet.fleet[1].name} has {str(fleet.fleet[1].health)} health reamining!')

"""herd_one = Herd()

print(herd_one.herd[0].health)
for dino in herd_one.herd:
    print(dino.name)"""