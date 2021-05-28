# Imports
import pygame
import random
import json

import os
import sys

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS + '/'
else:
    application_path = os.path.dirname(__file__) + '/'


# Window settings
GRID_SIZE = 64
WIDTH = 28 * GRID_SIZE
HEIGHT = 15 * GRID_SIZE
TITLE = "Minibot"
FPS = 60


# Create window
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (0, 150, 255)
GRAY = (175, 175, 175)
DARK_GRAY = (105,105,105)
# Stages
START = 0
PLAYING = 1
LOSE = 2
LEVEL_COMPLETE = 3
WIN = 4


# Load fonts
font_xs = pygame.font.Font(application_path + 'assets/fonts/Dinomouse-Regular.otf',14)
font_xl = pygame.font.Font(application_path + 'assets/fonts/Dinomouse-Regular.otf',96)
font_lg = pygame.font.Font(application_path + 'assets/fonts/Dinomouse-Regular.otf',64)
font_md = pygame.font.Font(application_path + 'assets/fonts/Dinomouse-Regular.otf',32)
font_sm = pygame.font.Font(application_path + 'assets/fonts/Dinomouse-Regular.otf',24)

#Load Images
#Tiles
plantPurple_img = pygame.image.load(application_path + 'assets/images/tiles/plantPurple.png').convert_alpha()
cactus_img = pygame.image.load(application_path + 'assets/images/tiles/cactus.png').convert_alpha()
bush_img = pygame.image.load(application_path + 'assets/images/tiles/bush.png').convert_alpha()
grass_img = pygame.image.load(application_path + 'assets/images/tiles/grass.png').convert_alpha()
dirt_img = pygame.image.load(application_path + 'assets/images/tiles/grassdirt.png').convert_alpha()
greenplatform_img = pygame.image.load(application_path + 'assets/images/tiles/greenblock.png').convert_alpha()
blueplatform_img = pygame.image.load(application_path + 'assets/images/tiles/blueblock.png').convert_alpha()
brownplatform_img = pygame.image.load(application_path + 'assets/images/tiles/brownblock.png').convert_alpha()
greyplatform_img = pygame.image.load(application_path + 'assets/images/tiles/greyblock.png').convert_alpha()
orangeplatform_img = pygame.image.load(application_path + 'assets/images/tiles/orangeblock.png').convert_alpha()
spring_img = pygame.image.load(application_path + 'assets/images/tiles/spring.png').convert_alpha()
pole_img = pygame.image.load(application_path + 'assets/images/tiles/flagpole.png').convert_alpha()
flagblue_img = pygame.image.load(application_path + 'assets/images/tiles/flagBlue1.png').convert_alpha()
shroomdirt_img = pygame.image.load(application_path + 'assets/images/tiles/dirt.png').convert_alpha()
dirtdirt_img = pygame.image.load(application_path + 'assets/images/tiles/dirtdirt.png').convert_alpha()
mushroombrown_img = pygame.image.load(application_path + 'assets/images/tiles/mushroomBrown.png').convert_alpha()
mushroomred_img = pygame.image.load(application_path + 'assets/images/tiles/mushroomRed.png').convert_alpha()
planetdirt_img = pygame.image.load(application_path + 'assets/images/tiles/planetdirt.png').convert_alpha()
planet_img = pygame.image.load(application_path + 'assets/images/tiles/planet.png').convert_alpha()
sand_img = pygame.image.load(application_path + 'assets/images/tiles/sand.png').convert_alpha()
sanddirt_img = pygame.image.load(application_path + 'assets/images/tiles/sanddirt.png').convert_alpha()
chain_img = pygame.image.load(application_path + 'assets/images/tiles/chain.png').convert_alpha()


#Enemies
spikes_img = pygame.image.load(application_path + 'assets/images/characters/spikes.png').convert_alpha()
upside_down_spikes_img =  pygame.image.load(application_path + 'assets/images/characters/spikes_upsidedown.png').convert_alpha()
barnacle_imgs = [pygame.image.load(application_path + 'assets/images/characters/barnacle.png').convert_alpha(),
                 pygame.image.load(application_path + 'assets/images/characters/barnacle_attack.png').convert_alpha()]
bee_imgs_lt =  [pygame.image.load(application_path + 'assets/images/characters/bee.png').convert_alpha(),
                pygame.image.load(application_path + 'assets/images/characters/bee_move.png').convert_alpha()]
bee_imgs_rt = [pygame.transform.flip(img, True, False)for img in bee_imgs_lt]
wormGreen_imgs_lt =  [pygame.image.load(application_path + 'assets/images/characters/wormGreen.png').convert_alpha(),
                      pygame.image.load(application_path + 'assets/images/characters/wormGreen_move.png').convert_alpha()]
wormGreen_imgs_rt = [pygame.transform.flip(img, True, False)for img in wormGreen_imgs_lt]

wormPink_imgs_lt =  [pygame.image.load(application_path + 'assets/images/characters/wormPink.png').convert_alpha(),
                     pygame.image.load(application_path + 'assets/images/characters/wormPink_move.png').convert_alpha()]
wormPink_imgs_rt = [pygame.transform.flip(img, True, False)for img in wormPink_imgs_lt]

fly_imgs_lt =  [pygame.image.load(application_path + 'assets/images/characters/fly.png').convert_alpha(),
                pygame.image.load(application_path + 'assets/images/characters/fly_move.png').convert_alpha()]
fly_imgs_rt = [pygame.transform.flip(img, True, False)for img in fly_imgs_lt]

saw_imgs_lt =  [pygame.image.load(application_path + 'assets/images/characters/saw.png').convert_alpha(),
                pygame.image.load(application_path + 'assets/images/characters/saw_move.png').convert_alpha()]
saw_imgs_rt = [pygame.transform.flip(img, True, False)for img in saw_imgs_lt]

sawhalf_imgs_lt =  [pygame.image.load(application_path + 'assets/images/characters/sawHalf.png').convert_alpha(),
                    pygame.image.load(application_path + 'assets/images/characters/sawHalf_move.png').convert_alpha()]
sawhalf_imgs_rt = [pygame.transform.flip(img, True, False)for img in sawhalf_imgs_lt]

snail_imgs_lt =  [pygame.image.load(application_path + 'assets/images/characters/snail.png').convert_alpha(),
                  pygame.image.load(application_path + 'assets/images/characters/snail_move.png').convert_alpha()]
snail_imgs_rt = [pygame.transform.flip(img, True, False)for img in snail_imgs_lt]

slime_imgs_lt =  [pygame.image.load(application_path + 'assets/images/characters/slimePurple.png').convert_alpha(),
                  pygame.image.load(application_path + 'assets/images/characters/slimePurple_move.png').convert_alpha()]
slime_imgs_rt = [pygame.transform.flip(img, True, False)for img in slime_imgs_lt]

#Items
coinGold_img = pygame.image.load(application_path + 'assets/images/items/coinGold.png').convert_alpha()

#Heroes
hero_idle_imgs_rt = [pygame.image.load(application_path +'assets/images/characters/alienBlue_stand.png').convert_alpha()]
hero_walk_imgs_rt = [pygame.image.load(application_path + 'assets/images/characters/alienBlue_walk1.png').convert_alpha(),
                     pygame.image.load(application_path + 'assets/images/characters/alienBlue_walk2.png').convert_alpha()]
hero_jump_imgs_rt = [pygame.image.load(application_path + 'assets/images/characters/alienBlue_jump.png').convert_alpha()]
hero_idle_imgs_lt = [pygame.transform.flip(img, True, False)for img in hero_idle_imgs_rt]
hero_walk_imgs_lt = [pygame.transform.flip(img, True, False)for img in hero_walk_imgs_rt]
hero_jump_imgs_lt = [pygame.transform.flip(img, True, False)for img in hero_jump_imgs_rt]

#Hud
herohud_img = pygame.image.load(application_path + 'assets/images/hud/hudPlayer_blue.png').convert_alpha()
fullheart_img = pygame.image.load(application_path + 'assets/images/hud/heart.png').convert_alpha()
emptyheart_img = pygame.image.load(application_path + 'assets/images/hud/hudHeart_empty.png').convert_alpha()

# Load sounds
coin_snd = pygame.mixer.Sound(application_path + 'assets/sounds/collect_point.wav')
jump_snd = pygame.mixer.Sound(application_path + 'assets/sounds/jump.wav')
spring_snd = pygame.mixer.Sound(application_path + 'assets/sounds/spring.ogg')
oof_snd = pygame.mixer.Sound(application_path + 'assets/sounds/oof.ogg')
goal_snd = pygame.mixer.Sound(application_path + 'assets/sounds/victory.ogg')

# Music
win_music = application_path + 'assets/music/winmusic.ogg'
playing_music = application_path + 'assets/music/playingmusic.ogg'
lose_music = application_path + 'assets/music/losemusic.ogg'

#end_music =
# Levels
levels = ['assets/levels/level-1.json',
          'assets/levels/level-2.json',
          'assets/levels/level-3.json',
          'assets/levels/level-4.json',
          'assets/levels/level-5.json',]

# Game classes
class Entity(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x * GRID_SIZE + GRID_SIZE //2
        self.rect.centery = y * GRID_SIZE + GRID_SIZE //2

        self.vx = 0
        self.vy = 0
        
    def apply_gravity(self):
        self.vy += gravity
        if self.vy > terminal_velocity:
            self.vy = terminal_velocity

class AnimatedEntity(Entity):

    def __init__ (self,x, y, images):
        super().__init__(x,y, images[0])

        self.images = images
        self.image_index = 0
        self.ticks = 0
        self.animation_speed = 10

    def set_images_list(self):
        self.images = self.images
        
    def animate(self):
        self.set_images_list()
        self.ticks += 1

        if self.ticks % self.animation_speed == 0:
            self.image_index += 1

            if self.image_index >= len(self.images):
                self.image_index = 0
            self.image = self.images[self.image_index]

        
class Hero(AnimatedEntity):
    
    def __init__(self, x, y, image):
        super().__init__(x,y,image)

        self.speed = 5
        self.jump_power = 22
        self.vx = 0
        self.vy = 0
        self.hurt_timer = 0
        self.facing_right = True
        self.jumping = False
        
        self.hearts = 3
        self.maxhearts = 3
        self.coins = 0
        self.score = 0

    def move_to(self, x ,y):
        self.rect.centerx = x * GRID_SIZE + GRID_SIZE //2
        self.rect.centery = y * GRID_SIZE + GRID_SIZE //2

    def move_right(self):
    	self.vx = self.speed
    	self.facing_right = True

    def move_left(self):
    	self.vx = -1 * self.speed
    	self.facing_right = False

    def stop(self):
        self.vx = 0
        
    def jump(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 1

        if len(hits) > 0:
            self.vy = -1 * self.jump_power
            jump_snd.play()
            self.jumping = True

    def move_and_check_blocks(self):
        self.rect.x +=self.vx
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for block in hits:
            if self.vx > 0:
                self.rect.right = block.rect.left
            elif self.vx < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.vy
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for block in hits:
            if self.vy > 0:
                self.rect.bottom = block.rect.top
                self.jumping = False
            elif self.vy <0:
                self.rect.top = block.rect.bottom

            self.vy = 0

    def check_world_edges (self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > world_width:
            self.rect.right = world_width
        elif self.rect.top > world_height:
            hero.hearts = 0
        
    def check_items(self):
        hits = pygame.sprite.spritecollide(self, items, True, pygame.sprite.collide_mask)

        for item in hits :
            item.apply(self)
    
    def check_enemies(self):
        hits = pygame.sprite.spritecollide(self, enemies, False, pygame.sprite.collide_mask)

        for enemy in hits :
            if self.hurt_timer == 0:
                self.hearts -= 1
                self.hurt_timer = 1.0 * FPS
                oof_snd.play()
                
# Bumping of enemies
#            if self.rect.centerx < enemy.rect.centerx:
 #               self.rect.right = enemy.rect.left
#            elif self.rect.centerx > enemy.rect.centerx:
#                self.rect.left = enemy.rect.right

#            if self.rect.centery < enemy.rect.centery:
#                self.rect.bottom = enemy.rect.top
#            elif self.rect.centery > enemy.rect.centery:
#                self.rect.top = enemy.rect.bottom

        else:
            self.hurt_timer -= 1

            if self.hurt_timer < 0:
                self.hurt_timer = 0
                
    def check_spikes (self):
        hits = pygame.sprite.spritecollide(self, spikes, False, pygame.sprite.collide_mask)

        for enemy in hits :
            if self.hurt_timer == 0:
                self.hearts -= 1
                self.hurt_timer = 1.0 * FPS
                oof_snd.play()

            if self.rect.x < enemy.rect.x:
                self.vx = 0
            elif self.rect.x > enemy.rect.x:
                self.vx = 0

            if self.rect.y < enemy.rect.y:
                self.vy = -15
                
        else:
            self.hurt_timer -= 1

            if self.hurt_timer < 0:
                self.hurt_timer = 0

    def check_barnacles (self):
        hits = pygame.sprite.spritecollide(self, barnacles, False, pygame.sprite.collide_mask)

        for enemy in hits :
            if self.hurt_timer == 0:
                self.hearts -= 1
                self.hurt_timer = 1.0 * FPS
                oof_snd.play()

            if self.rect.x < enemy.rect.x:
                self.vx = 0
            elif self.rect.x > enemy.rect.x:
                self.vx = 0

            if self.rect.y < enemy.rect.y:
                self.vy = -15
                
        else:
            self.hurt_timer -= 1

            if self.hurt_timer < 0:
                self.hurt_timer = 0

    def check_upside_down_spikes (self):
        hits = pygame.sprite.spritecollide(self, upside_down_spikes, False, pygame.sprite.collide_mask)

        for enemy in hits :
            if self.hurt_timer == 0:
                self.hearts -= 1
                self.hurt_timer = 1.0 * FPS
                oof_snd.play()

                    
            if self.rect.x < enemy.rect.x:
                self.vx = 0
            elif self.rect.x > enemy.rect.x:
                self.vx = 0

            if self.rect.y < enemy.rect.y:
                self.vy = -5
                
            elif self.rect.y < enemy.rect.y:
                self.vy = 5
                
        else:
            self.hurt_timer -= 1

            if self.hurt_timer < 0:
                self.hurt_timer = 0 

    def check_springs (self):
        hits = pygame.sprite.spritecollide(self, springs, False, pygame.sprite.collide_mask)

        for spring in hits :
            spring_snd.play()
                   
            if self.rect.x < spring.rect.x:
                self.vx = 0
            elif self.rect.x > spring.rect.x:
                self.vx = 0

            if self.rect.y < spring.rect.y:
                self.vy = -30
                
    def check_mushroomsprings (self):
        hits = pygame.sprite.spritecollide(self, mushroomsprings, False, pygame.sprite.collide_mask)

        for mushroomspring in hits :
            spring_snd.play()
                   
            if self.rect.x < mushroomspring.rect.x:
                self.vx = 0
            elif self.rect.x > mushroomspring.rect.x:
                self.vx = 0

            if self.rect.y < mushroomspring.rect.y:
                self.vy = -30
                
    def reached_goal(self):
        return pygame.sprite.spritecollideany(self, goal)

    def set_images_list(self):
        if self.facing_right:
            if self.jumping :
                self.images = hero_jump_imgs_rt
            elif self.vx == 0:
                self.images = hero_idle_imgs_rt
            else:
                self.images = hero_walk_imgs_rt
        else:
            if self.jumping :
                self.images = hero_jump_imgs_lt
            elif self.vx == 0:
                self.images = hero_idle_imgs_lt
            else:
                self.images = hero_walk_imgs_lt

            
    def update(self):
        self.apply_gravity()
        self.check_world_edges()
        self.check_items()
        self.check_enemies()
        self.check_spikes()
        self.check_upside_down_spikes()
        self.move_and_check_blocks()
        self.check_springs()
        self.check_mushroomsprings()
        self.check_barnacles()
        self.animate()


    	
class Coin(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x,y,image)
        
    def apply(self, character):
        character.coins += 1
        character.score += 10
        if character.coins == 10:
            character.hearts = min(character.hearts + 1, character.maxhearts)
            character.coins = 0

        print (character.coins)
        coin_snd.play()
        
class Platform(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x,y,image)

class Flag(Entity):

    def __init__(self, x, y, image):
        super().__init__(x,y,image)

class FakePlatform(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x,y,image)
    

class Enemy_Bee(AnimatedEntity):
    
    def __init__(self, x, y, images):
        super().__init__(x,y,images)
        self.animation_speed = 8

        self.speed = 2
        self.vx = -1 * self.speed
        self.vy = 0
        self.killable = True

    def set_images_list(self):
        if self.vx > 0:
            self.images = bee_imgs_rt
        else:
            self.images = bee_imgs_lt
            
    def reverse(self):
        self.vx *= -1
        
    def move_and_check_blocks(self):
        self.rect.x += self.vx
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            if self.vx > 0:
                self.rect.right = hit.rect.left
                self.reverse()
            elif self.vx < 0:
                self.rect.left = hit.rect.right
                self.reverse()

        self.rect.y += self.vy
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            if self.vy > 0:
                self.rect.bottom = hit.rect.top
            elif self.vy <0:
                self.rect.top = hit.rect.bottom

            self.vy = 0

    def check_platform_edges(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self,platforms, False)
        self.rect.y -= 2

        must_reverse = True

        for platform in hits:
            if self.vx < 0 and platform.rect.left <= self.rect.left:
                must_reverse = False
            elif self.vx > 0 and platform.rect.right >= self.rect.right:
                must_reverse = False
                
        if must_reverse:
            self.reverse()
            
    def check_world_edges (self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.reverse()
        elif self.rect.right > world_width:
            self.rect.right = world_width
            self.reverse()
    
    def update(self):
        self.move_and_check_blocks()
        self.check_world_edges()
        self.animate()
        
class Enemy_Fly(Enemy_Bee):
    def __init__(self, x, y, images):
        super().__init__(x,y,images)
        self.animation_speed = 8

    def set_images_list(self):
        if self.vx > 0:
            self.images = fly_imgs_rt
        else:
            self.images = fly_imgs_lt
            
    def update(self):
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_platform_edges()
        self.animate()

class Enemy_Saw(Enemy_Bee):
    def __init__(self, x, y, images):
        super().__init__(x,y,images)
        self.animation_speed = 8

    def set_images_list(self):
        if self.vx > 0:
            self.images = saw_imgs_rt
        else:
            self.images = saw_imgs_lt
            
    def update(self):
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_platform_edges()
        self.animate()

class Enemy_Halfsaw(Enemy_Bee):
    def __init__(self, x, y, images):
        super().__init__(x,y,images)
        self.animation_speed = 8

    def set_images_list(self):
        if self.vx > 0:
            self.images = sawhalf_imgs_rt
        else:
            self.images = sawhalf_imgs_lt
            
    def update(self):
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_platform_edges()
        self.animate()
        
class Enemy_Greenworm(Enemy_Bee):
    def __init__(self, x, y, images):
        super().__init__(x,y,images)
        self.animation_speed = 8

    def set_images_list(self):
        if self.vx > 0:
            self.images = wormGreen_imgs_rt
        else:
            self.images = wormGreen_imgs_lt
            
    def update(self):
        self.apply_gravity()
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_platform_edges()
        self.animate()

class Enemy_Pinkworm(Enemy_Bee):
    def __init__(self, x, y, images):
        super().__init__(x,y,images)
        self.animation_speed = 7

    def set_images_list(self):
        if self.vx > 0:
            self.images = wormPink_imgs_rt
        else:
            self.images = wormPink_imgs_lt
            
    def update(self):
        self.apply_gravity()
        self.move_and_check_blocks()
        self.check_world_edges()
        self.animate()

class Enemy_Snail(Enemy_Bee):
    def __init__(self, x, y, images):
        super().__init__(x,y,images)
        self.animation_speed = 6

    def set_images_list(self):
        if self.vx > 0:
            self.images = snail_imgs_rt
        else:
            self.images = snail_imgs_lt
            
    def update(self):
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_platform_edges()
        self.animate()

class Enemy_Slime(Enemy_Bee):
    def __init__(self, x, y, images):
        super().__init__(x,y,images)
        self.animation_speed = 10

    def set_images_list(self):
        if self.vx > 0:
            self.images = slime_imgs_rt
        else:
            self.images = slime_imgs_lt
            
    def update(self):
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_platform_edges()
        self.animate()
        
class Spike (pygame.sprite.Sprite):

    def __init__(self,x,y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE + 32

    def apply(self,character):
        character.health -= 1



class Upside_Down_Spike (pygame.sprite.Sprite):

    def __init__(self,x,y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE

    def apply(self,character):
        character.health -= 1


class Spring (pygame.sprite.Sprite):

    def __init__(self,x,y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE + 31

class MushroomSpring (pygame.sprite.Sprite):

    def __init__(self,x,y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE + 101

class Barnacle (AnimatedEntity):
    def __init__(self, x, y, images):
        super().__init__(x,y,images)

    def update(self):
        self.animate()

# Helper functoins

def show_start_screen():
    text = font_xl.render(TITLE, True, GRAY)
    rect = text.get_rect()
    rect.midbottom = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_md.render("Press Any Key to Start", True, GRAY)
    rect = text.get_rect()
    rect.midtop = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

def show_lose_screen():
    text = font_xl.render("Game Over", True, GRAY)
    rect = text.get_rect()
    rect.midbottom = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_md.render("Press 'R' to Restart", True, GRAY)
    rect = text.get_rect()
    rect.midtop = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)
    
def show_win_screen():
    text = font_xl.render("You Won!", True, GRAY)
    rect = text.get_rect()
    rect.midbottom = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_md.render("Press 'R' to Restart", True, GRAY)
    rect = text.get_rect()
    rect.midtop = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)
    
def show_level_complete_screen():
    text = font_xl.render("Level Complete", True, GRAY)
    rect = text.get_rect()
    rect.midbottom = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)


def draw_grid(offset_x=0, offset_y=0):
    for x in range(0, WIDTH + GRID_SIZE, GRID_SIZE):
        adj_x = x - offset_x % GRID_SIZE
        pygame.draw.line(screen, GRAY, [adj_x, 0], [adj_x, HEIGHT], 1)

    for y in range(0, HEIGHT + GRID_SIZE, GRID_SIZE):
        adj_y = y - offset_y % GRID_SIZE
        pygame.draw.line(screen, GRAY, [0, adj_y], [WIDTH, adj_y], 1)

    for x in range(0, WIDTH + GRID_SIZE, GRID_SIZE):
        for y in range(0, HEIGHT + GRID_SIZE, GRID_SIZE):
            adj_x = x - offset_x % GRID_SIZE + 4
            adj_y = y - offset_y % GRID_SIZE + 4
            disp_x = x // GRID_SIZE + offset_x // GRID_SIZE
            disp_y = y // GRID_SIZE + offset_y // GRID_SIZE
            
            point = '(' + str(disp_x) + ',' + str(disp_y) + ')'
            text = font_xs.render(point, True, DARK_GRAY)
            screen.blit(text, [adj_x, adj_y])


def show_hud():
    text = font_md.render(str(hero.score), False, WHITE)
    rect = text.get_rect()
    rect.midtop = WIDTH //2, 16
    screen.blit(text,rect)

    screen.blit(coinGold_img, [WIDTH - 99,16])
    text = font_sm.render('x'+ str(hero.coins), False, WHITE)
    rect = text.get_rect()
    rect.topleft = WIDTH - 64, 24
    screen.blit(text,rect)

    for i in range(hero.maxhearts):
        if i < hero.hearts:
            x = i * 32 + 48
            y = 8
            screen.blit(fullheart_img,[x,y])
        else:
            x = i * 32 + 48
            y = 8
            screen.blit(emptyheart_img,[x,y])

    screen.blit(herohud_img, herohud_locs)

# Setup
def start_game():
    global hero, stage, current_level
    
    hero = Hero (0,0, hero_idle_imgs_rt)
    stage = START
    current_level = 0
    
    
def start_level():
    global player, world_width, world_height, platforms, mushroomsprings, all_sprites, barnacles, fakeplatforms, background_img
    global items, start, herohud, hero, spikes, upside_down_spikes, springs, gravity, terminal_velocity, goal, herohud_locs, enemies
    
    platforms = pygame.sprite.Group()
    fakeplatforms = pygame.sprite.Group()
    items = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    player = pygame.sprite.GroupSingle()
    spikes = pygame.sprite.Group()
    barnacles = pygame.sprite.Group()
    upside_down_spikes = pygame.sprite.Group()
    springs = pygame.sprite.Group()
    mushroomsprings = pygame.sprite.Group()
    goal = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    with open(levels[current_level]) as f:
        data = json.load(f)

    world_width = data['width'] * GRID_SIZE
    world_height = data['height'] * GRID_SIZE
    background_img = pygame.image.load(data['background_img']).convert()
    herohud_locs = [1,6]
    hero.move_to(data['start'][0], data['start'][1])
    player.add(hero)
    
    for i, loc in enumerate (data['flagblue_locs']):
        if i == 0:
            goal.add( Flag(loc[0],loc[1], flagblue_img))
        else:
            goal.add( Flag(loc[0],loc[1], pole_img))

    for loc in data ['bush_locs']:
        fakeplatforms.add( FakePlatform(loc[0],loc[1], bush_img))
        
    for loc in data ['chain_locs']:
        platforms.add( Platform(loc[0],loc[1], chain_img))

    for loc in data ['cactus_locs']:
        fakeplatforms.add( FakePlatform(loc[0],loc[1], cactus_img))

    for loc in data ['plantPurple_locs']:
        fakeplatforms.add( FakePlatform(loc[0],loc[1], plantPurple_img))

    for loc in data ['mushroomRed_locs']:
        fakeplatforms.add( FakePlatform(loc[0],loc[1], mushroomred_img))
        
    for loc in data ['dirt_locs']:
        platforms.add( Platform(loc[0],loc[1], dirt_img))

    for loc in data ['shroomdirt_locs']:
        platforms.add( Platform(loc[0],loc[1], shroomdirt_img))

    for loc in data ['dirtdirt_locs']:
        platforms.add( Platform(loc[0],loc[1], dirtdirt_img))

    for loc in data ['grass_locs']:
        platforms.add( Platform(loc[0],loc[1], grass_img))

    for loc in data ['planet_locs']:
        platforms.add( Platform(loc[0],loc[1], planet_img))

    for loc in data ['planetdirt_locs']:
        platforms.add( Platform(loc[0],loc[1], planetdirt_img))

    for loc in data ['sanddirt_locs']:
        platforms.add( Platform(loc[0],loc[1], sanddirt_img))

    for loc in data ['sand_locs']:
        platforms.add( Platform(loc[0],loc[1], sand_img))

    for loc in data ['blueplatform_locs']:
        platforms.add( Platform(loc[0],loc[1], blueplatform_img))

    for loc in data ['greyplatform_locs']:
        platforms.add( Platform(loc[0],loc[1], greyplatform_img))

    for loc in data ['orangeplatform_locs']:
        platforms.add( Platform(loc[0],loc[1], orangeplatform_img))

    for loc in data ['brownplatform_locs']:
        platforms.add( Platform(loc[0],loc[1], brownplatform_img))

    for loc in data ['greenplatform_locs']:
        platforms.add( Platform(loc[0],loc[1], greenplatform_img))
    
    for loc in data ['coin_locs']:
        items.add( Coin(loc[0],loc[1], coinGold_img))

    for loc in data ['enemy_bee_locs']:
        enemies.add( Enemy_Bee(loc[0], loc[1], bee_imgs_lt))

    for loc in data ['enemyfly_locs']:
        enemies.add( Enemy_Fly(loc[0], loc[1], fly_imgs_lt))

    for loc in data ['enemysaw_locs']:
        enemies.add( Enemy_Saw(loc[0], loc[1], saw_imgs_lt))

    for loc in data ['enemysawhalf_locs']:
        enemies.add( Enemy_Halfsaw(loc[0], loc[1], sawhalf_imgs_lt))

    for loc in data ['enemy_greenworm_locs']:
        enemies.add( Enemy_Greenworm(loc[0], loc[1], wormGreen_imgs_lt))

    for loc in data ['enemy_pinkworm_locs']:
        enemies.add( Enemy_Pinkworm(loc[0], loc[1], wormPink_imgs_lt))

    for loc in data ['enemy_snail_locs']:
        enemies.add( Enemy_Snail(loc[0], loc[1], snail_imgs_lt))

    for loc in data ['enemy_slime_locs']:
        enemies.add( Enemy_Slime(loc[0], loc[1], slime_imgs_lt))
        
    for loc in data ['spikes_locs']:
        spikes.add( Spike(loc[0], loc[1], spikes_img))
        
    for loc in data ['barnacle_locs']:
        barnacles.add( Barnacle(loc[0], loc[1], barnacle_imgs))

    for loc in data ['upside_down_spikes_locs']:
        upside_down_spikes.add( Upside_Down_Spike(loc[0], loc[1], upside_down_spikes_img))

    for loc in data ['spring_locs']:
        springs.add( Spring(loc[0],loc[1], spring_img))

    for loc in data ['mushroomBrown_locs']:
        mushroomsprings.add( MushroomSpring(loc[0],loc[1], mushroombrown_img))
        
    gravity = data['gravity']
    terminal_velocity = data['terminal_velocity']

    all_sprites.add(player, platforms, items, enemies, goal, fakeplatforms, spikes, barnacles, upside_down_spikes, springs, mushroomsprings)

    pygame.mixer.music.load(playing_music)
    pygame.mixer.music.play(-1)
    
# Game loop
running = True
grid_on = False
start_game()
start_level()


while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                grid_on = not grid_on
            elif stage == START:
                stage = PLAYING
                    
            elif stage == PLAYING:
                if event.key == pygame.K_w:
                    hero.jump()
                
            elif stage == LOSE or stage == WIN:
                if event.key == pygame.K_r:
                    start_game()
                    start_level()

    pressed = pygame.key.get_pressed()

    if stage == PLAYING:
        if pressed[pygame.K_a]:
            hero.move_left()
        elif pressed[pygame.K_d]:
            hero.move_right()

        else:
            hero.stop()

    
    # Game logic
    if stage == PLAYING:
        all_sprites.update()
        
        if hero.hearts == 0:
            stage = LOSE
            pygame.mixer.music.stop
            pygame.mixer.music.load(lose_music)
            pygame.mixer.music.play(0)
            
        elif hero.reached_goal():
            pygame.mixer.music.stop()
            hero.score += 100
            goal_snd.play()
            stage = LEVEL_COMPLETE
            countdown = 4 * FPS
    elif stage == LEVEL_COMPLETE:
        countdown -= 1
        if countdown <= 0:
            current_level += 1

            if current_level < len(levels):
                start_level()
                stage = PLAYING
                
            else:
                stage = WIN
                pygame.mixer.music.stop
                pygame.mixer.music.load(playing_music)
                pygame.mixer.music.play(0)

    if hero.rect.centerx < WIDTH // 2:
        offset_x = 0
    elif hero.rect.centerx > world_width - WIDTH // 2:
        offset_x = world_width - WIDTH 
    else:
        offset_x = hero.rect.centerx - WIDTH // 2

    background_offset_x = -1 * (.75 * offset_x % background_img.get_width())
                                
    # Drawing code
    screen.blit(background_img, [background_offset_x,0])
    screen.blit(background_img, [background_offset_x + background_img.get_width(),0])

    for sprite in all_sprites:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y])

    if stage == START:
        show_start_screen()
    elif stage == LOSE:
        show_lose_screen()
    elif stage == LEVEL_COMPLETE:
        show_level_complete_screen()
    elif stage == WIN:
        show_win_screen()
    if grid_on:
        draw_grid(offset_x)
    show_hud()
    
    # Update screen
    pygame.display.update()


    # Limit refresh rate of game loop 
    clock.tick(FPS)


# Close window and quit
pygame.quit()

