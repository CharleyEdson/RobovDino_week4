from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon
from fleet import Fleet
from herd import Herd

class Battlefield:
    
    def __init__(self):
        #self.robot = Robot('Barthalemew', Weapon('Rusty Saw', 20))
        #self.dinosaur = Dinosaur('Big Bertha', 30)
        self.robot = ''
        self.dinosaur = ''
        self.winner = ''
        self.fleet = Fleet()
        self.herd = Herd()
        
       

    def run_game(self):
        
        decision = input('Please choose 1) for a one v one battle, or 2) a fleet v herd battle')
        if decision == '1':
            self.regular_battle_display_welcome()
            self.battle_phase()
            self.display_winner()
    
        else:
            self.herd_v_fleet_display_welcome()
            self.herd_and_fleet_battle_phase()
            self.dispaly_winner_for_herd_v_robos()

    


    def regular_battle_display_welcome(self):
        print('Before we begin the game, you must pick the opponents who will face off,\n between the legend of the Dinosoar and the Robot!')
        robot_name = input("Please input the name of the Robot: ")
        
        self.robot = Robot(robot_name)
        self.robot.choose_attack_weapon()
        dino_name = input("Please input the name of the Dino: ")
        self.dinosaur = Dinosaur(dino_name)
        self.dinosaur.choose_type_of_dino() 
        
                
        print('\nWelcome to an epic battle for the ages! \nOnly one side can win!\n')

    def herd_v_fleet_display_welcome(self):
        print('The battle between the herd and the fleet will commence!') 
        print('\nWelcome to an epic battle for the ages! \nOnly one side can win!\n')


    def battle_phase(self):
                  
        
        while self.robot.health >= 0 and self.dinosaur.health >= 0:
            if self.dinosaur.health <= 0:
                self.winner = self.robot.name
                return self.winner
            if self.robot.health <= 0:
                self.winner = self.dinosaur.name
                return self.winner
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                self.winner = self.robot.name
                return self.winner
            if self.robot.health <= 0:
                self.winner = self.dinosaur.name
                return self.winner
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                self.winner = self.dinosaur.name
                return self.winner
                break
            if self.dinosaur.health <= 0:
                self.winner = self.robot.name
                return self.winner 
                break

    def herd_and_fleet_battle_phase(self):
        #Robos will attack first, check to see if dino's are dead.
        total_herd_health_list = []
        while self.herd.herd[0].is_alive is True or self.herd.herd[1].is_alive is True or self.herd.herd[2].is_alive is True:
            
            self.fleet.fleet_attack(self.herd)
            for dino in self.herd.herd:
                total_herd_health_list.append(dino.health)
            herd_health = 0
            for health in total_herd_health_list:
                herd_health += health
            if herd_health <= 0:
                print('This is finished, it Should end')
                self.winner = 'Robots'
                return self.winner
                
                break
               
            elif herd_health >0:
                total_herd_health_list.clear()
                total_fleet_health = []
                if self.fleet.fleet[0].is_alive is False or self.fleet.fleet[1].is_alive is False or self.fleet.fleet[2].is_alive is False:
                    self.winner = 'Dinosaurs'
                    return self.winner
                for robo in self.fleet.fleet:
                    total_fleet_health.append(robo.health)
                fleet_health = 0
                for health in total_fleet_health:
                    fleet_health += health
                if fleet_health <= 0:
                    self.winner = 'Dinosaurs'
                    return self.winner
                elif fleet_health > 0:
                    total_fleet_health.clear()
                    self.herd.herd_attack(self.fleet)

        


            
    def display_winner(self):
        if self.winner == self.robot.name:
            print(f'{self.robot.name} made {self.dinosaur.name} extinct!')
            print(f'{self.robot.name} wins!')
        elif self.winner == self.dinosaur.name:
            print(f'{self.dinosaur.name} discontinued {self.robot.name} permanently!')
            print(f'{self.dinosaur.name} wins!')
        elif self.winner == 'Dinosaurs':
            print('The herd of Dinosaurs are victorious')
        elif self.winner == 'Robots':
            print('The fleet of robots are victorious!')

    def dispaly_winner_for_herd_v_robos(self):
        if self.winner == 'Dinosaurs':
            print('The herd of Dinosaurs are victorious')
        elif self.winner == 'Robots':
            print('The fleet of robots are victorious!')


    