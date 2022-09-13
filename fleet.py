

class Fleet:

    def __init__(self, dinosaur):
        self.name = dinosaur.name
        self.attack_power = dinosaur.attack_power
        self.health = dinosaur.health



    def update_stats(self):
        self.health = self.dinosaur.health * 0.9
        self.attack_power = self.dinosaur.attack_power * 1.2
