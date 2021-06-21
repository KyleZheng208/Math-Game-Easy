# A Button Class
# Modified code from Tech with Tim
class button():
    def __init__(self, sprite, value, x, y,):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.number = value

    def generate(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + 150:
            if pos[1] > self.y and pos[1] < self.y + 75:
                return True
            
        return False