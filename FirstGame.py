import pygame as pg
import sys, random
import pygame.locals

pg.init()
font=pg.font.Font(None, 32)


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf=pg.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect=self.surf.get_rect()
        self.score=0

    def update(self, pressed_keys):
        if pressed_keys[pg.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pg.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pg.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pg.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>screen_width:
            self.rect.right=screen_width
        if self.rect.top<=0:
            self.rect.top=0
        if self.rect.bottom>=screen_height:
            self.rect.bottom=screen_height


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf=pg.Surface((20, 10))
        self.surf.fill((255, 0, 255))
        self.rect=self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height)))
        self.speed=5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right<0:
            self.kill()
            player.score+=1


# Drwaing data on the screen
def drawdata(surface, score):
    text="Score:{0}"
    info=text.format(score)
    text=font.render(info, False, (255, 255, 255))
    textpos=text.get_rect(centerx = surface.get_width() - text.get_width(), top = 0)
    surface.blit(text, textpos)


# Draw Game Over
def gameOver(surface, score):
    text1="Game Score : {0}"
    text2="Press Space Bar to restart the game"
    info1=text1.format(score)
    text1=font.render(info1, True, (255, 0, 255))
    text1pos=text1.get_rect(centerx = screen_width/2, top = 50)
    text2pos=text1.get_rect(centerx = screen_width/2, top = 70)
    text=font.render(text2, True, (255, 0, 255))
    surface.blit(text1, text1pos)
    surface.blit(text, text2pos)


# Setting up screen
screen_width=800
screen_height=600
screen=pg.display.set_mode((screen_width, screen_height))

# Create a custom event for adding a new enemy
ADDENEMY=pg.USEREVENT + 1
pg.time.set_timer(ADDENEMY, 500)

# Creating Player
player=Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies=pg.sprite.Group()
all_sprites=pg.sprite.Group()
all_sprites.add(player)

run=True
isPlaying=True
while run:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
            sys.exit()

        # Add new Enemy
        elif event.type==ADDENEMY:
            new_enemy=Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # Get the set of keys pressed and check for user input
    keys=pg.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(keys)

    screen.fill((0, 0, 0))

    if isPlaying:
        # Update enemy positions
        enemies.update()

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Check if any enemies have collided with the player
        if pg.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            player.kill()
            isPlaying=False

        drawdata(screen, player.score)


    else:
        gameOver(screen, player.score)

    pg.display.update()
