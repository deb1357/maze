from pygame import *
import sys

game = True
Finish = True

WINDOW_SIZE = (700, 500)


window = display.set_mode(WINDOW_SIZE)
display.set_caption('Jungle maze')

clock = time.Clock()
FPS = 60



mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, Image, SIZE, x=0, y=0):
        super().__init__()

        self.image = transform.scale(
            image.load(Image),
            SIZE
        )
        self.rect = self.image.get_rect()
        self.Speed = 0

        self.x = x
        self.y = y

        self.rect.x = self.x
        self.rect.y = self.y
    
    def show(self, Window):
        self.update()
        self.rect.x = self.x
        self.rect.y = self.y
        Window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, Image, SIZE, x=0, y=0):
        super().__init__(Image, SIZE,x,y)

        self.Speed = 5

    def Control(self, Keys):
        if Keys[K_UP]:
            if self.y > 0:
                self.y-=self.Speed
        if Keys[K_DOWN]:
            if self.y < WINDOW_SIZE[1]-100:
                self.y+=self.Speed
        if Keys[K_RIGHT]:
            if self.x < WINDOW_SIZE[0]-100:
                self.x+=self.Speed
        if Keys[K_LEFT]:
            if self.x > 0:
                self.x-=self.Speed

class Enemy(GameSprite):
    def __init__(self, Image, SIZE, x=0, y=0):
        super().__init__(Image, SIZE,x,y)
    
        self.offset = 0
        self.Speed = 3

    def check_collide(self, Target):
        collide = sprite.collide_rect(self, Target)
        if collide:
            sys.exit()

    def automatic_move(self):
        if self.offset <= -60:
            self.Speed = 3
        elif self.offset >= 60:
            self.Speed = -3
        self.offset += self.Speed
        self.x += self.Speed


Background = GameSprite('background.jpg', WINDOW_SIZE)
Main_Character = Player('hero.png', (100,100), 100,250)
Cyborg = Enemy('cyborg.png', (100,100), 200, 150)

while game:
    Background.show(window)

    KeysPressed = key.get_pressed() 
    Main_Character.show(window)
    Cyborg.show(window)

    for Event in event.get():
        if Event.type == QUIT:
            game = False

    Main_Character.Control(KeysPressed)
    Cyborg.automatic_move()

    Cyborg.check_collide(Main_Character)

    clock.tick(FPS)
    display.update()
