
#oop
# init is a dunder method and is a constructor
# self = this
class Player:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("run")

player = Player("Kris")

print(player.name)