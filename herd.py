
class Herd:

    def __init__(self, player):
        self.herd = player
        self.health = self.player.health * 1.1
        self.attack_power = self.player.attack_power * .9
        