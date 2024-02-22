class Enemy:
    def __init__(self):
        self.collided = False

    def check_collision(self):
        self.collided = not self.collided
        return True


class Game:
    def update(self):
        enemy = Enemy()

        if enemy.check_collision():
            # render crash and exit the game
        else:
            # continue the normal processes
