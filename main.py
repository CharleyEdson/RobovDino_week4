from battlefield import Battlefield
from weapon import Weapon
from robot import Robot
from dinosaur import Dinosaur

weapon_one = Weapon('The almighty', 30)
robo_one = Robot('Barthalemew', weapon_one)
dino_one = Dinosaur('Big Bertha', 20)

battlefield_one = Battlefield()
battlefield_one.run_game()

#Need to figure out how to pass in parameters into robot to give him the weapon_one.