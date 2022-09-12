from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    
    def __init__(self):
        self.robot = Robot('Barthalemew', Weapon('Rusty Saw', 20))
        self.dinosaur = Dinosaur('Big Bertha', 30)
        self.winner = ''

       

    def run_game(self):
        
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages! \nOnly one side can win!\n')

    def battle_phase(self):
        self.winner = ''
        while self.robot.health >= 0 and self.dinosaur.health >= 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                self.winner = self.dinosaur.name
                return self.winner
                break
            if self.dinosaur.health <= 0:
                self.winner = self.robot.name
                return self.winner 
                break

    def display_winner(self):
        if self.winner == self.robot.name:
            print(f'{self.robot.name} made {self.dinosaur.name} extinct!')
            print(f'{self.robot.name} wins!')
        if self.winner == self.dinosaur.name:
            print(f'{self.dinosaur.name} discontinued {self.robot.name} permanently!')
            print(f'{self.dinosaur.name} wins!')