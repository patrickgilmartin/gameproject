import random
import uvage
import pygame
from time import time
from gameREVISED import TESTER
import sys
sys.path.append("/Users/Patrick Gilmartin/Downloads/gameREVISED/TESTER.py")

LevelsScreen_images = uvage.load_sprite_sheet("LevelsScreen.png", 1, 1)  #Mario's fireball
LevelsScreen = uvage.from_image(400, 300, LevelsScreen_images[0])
LevelsScreen.width = 800
LevelScreen.height = 600

camera = uvage.Camera(800, 600)

start_game = True
facing_right = not False
game_on = False
game_over = False
win = False
press_space = False


wall = uvage.from_color(-200, 200, "sky blue", 200, 700)
walls = [uvage.from_color(-200, 200, "sky blue", 200, 700)]
frame = 0
frame1 = 0
frame2 = 0
count = 7
floors = []

time = 220
countdown = 0

Loading_screen_image = uvage.load_sprite_sheet("snes-super-mario-world-1-h.png",1,1)
Loading_screen = uvage.from_image(400, 310, Loading_screen_image[0])
Loading_screen.width = 800
Loading_screen.height = 715

Mario_icon_image = uvage.load_sprite_sheet("MarioIcon.png",1,1)
Mario_icon = uvage.from_image(200, 700, Mario_icon_image[0])
Mario_icon.width = 200
Mario_icon.height = 200

Loading_screen_displayed = True

title_screen_image = uvage.load_sprite_sheet("Super-Mario-Bros-Title-Screen.png", 1, 1)
title_screen = uvage.from_image(400, 200, title_screen_image[0])
title_screen.width = 200
title_screen.height = 200

background_images = uvage.load_sprite_sheet("wp7619435.png", 1, 1)
background = uvage.from_image(400, 200, background_images[0])
background.width = 600
background.height = 800

bowser_icon_images = uvage.load_sprite_sheet("Bowser_back3.png", 1, 1)
bowser_icon = uvage.from_image(700, 423, bowser_icon_images[0])
bowser_icon.width = 150
bowser_icon.height = 210

mario_images = uvage.load_sprite_sheet('Mario.2.png', 1, 4)
mario = uvage.from_image(70, 550, mario_images[-1])
mario.width = 30
mario.height = 60

bowser_icon_images1 = uvage.load_sprite_sheet("Bowser_back3.png", 1, 1)
bowser_icon1 = uvage.from_image(mario.x, 423, bowser_icon_images[0])
bowser_icon1.width = 150
bowser_icon1.height = 210

background_images1 = uvage.load_sprite_sheet("wp7619435.png", 1, 1)
background1 = uvage.from_image(mario.x, 200, background_images[0])
background1.width = 600
background1.height = 800

title_screen_image1 = uvage.load_sprite_sheet("Super-Mario-Bros-Title-Screen.png", 1, 1)
title_screen1 = uvage.from_image(mario.x, 200, title_screen_image[0])
title_screen1.width = 200
title_screen1.height = 200

fireb_images = uvage.load_sprite_sheet("Fireball.png", 1, 1)
fireb = uvage.from_image(4390, 485, fireb_images[0])
fireb.width = 50
fireb.height = 50

fireballs = [fireb]

mario_bullet_images = uvage.load_sprite_sheet("Bullet.png", 1, 1)
mario_bullet = uvage.from_image(1700, 515, mario_bullet_images[0])
mario_bullet.width = 45
mario_bullet.height = 45

mario_bullet2 = uvage.from_image(2700, 310, mario_bullet_images[0])
mario_bullet2.width = 45
mario_bullet2.height = 45

mario_bullet3 = uvage.from_image(3000, 515, mario_bullet_images[0])
mario_bullet3.width = 45
mario_bullet3.height = 45

mario_bullet4 = uvage.from_image(10000, 460, mario_bullet_images[0])
mario_bullet4.width = 45
mario_bullet4.height = 45

mario_bullet5 = uvage.from_image(12000, 515, mario_bullet_images[0])
mario_bullet5.width = 45
mario_bullet5.height = 45

floor_images = uvage.load_sprite_sheet('BLOCKS.png', 1, 1)
floor = uvage.from_image(20, 581, floor_images[0])
floor.width = 2
floor.height = 60
floor2 = uvage.from_image(60, 581, floor_images[0])
floor2.width = 2
floor2.height = 60
floor3 = uvage.from_image(100, 581, floor_images[0])
floor3.width = 2
floor3.height = 60
floor4 = uvage.from_image(140, 581, floor_images[0])
floor4.width = 2
floor4.height = 60
floor5 = uvage.from_image(180, 581, floor_images[0])
floor5.width = 2
floor5.height = 60
floor6 = uvage.from_image(220, 581, floor_images[0])
floor6.width = 2
floor6.height = 60
floor7 = uvage.from_image(260, 581, floor_images[0])
floor7.width = 2
floor7.height = 60
floor8 = uvage.from_image(300, 581, floor_images[0])
floor8.width = 2
floor8.height = 60
floor9 = uvage.from_image(340, 581, floor_images[0])
floor9.width = 2
floor9.height = 60
floor10 = uvage.from_image(380, 581, floor_images[0])
floor10.width = 2
floor10.height = 60
floor11 = uvage.from_image(420, 581, floor_images[0])
floor11.width = 2
floor11.height = 60
floor12 = uvage.from_image(460, 581, floor_images[0])
floor12.width = 2
floor12.height = 60
floor13 = uvage.from_image(500, 581, floor_images[0])
floor13.width = 2
floor13.height = 60
floor14 = uvage.from_image(540, 581, floor_images[0])
floor14.width = 2
floor14.height = 60
floor15 = uvage.from_image(580, 581, floor_images[0])
floor15.width = 2
floor15.height = 60
floor16 = uvage.from_image(620, 581, floor_images[0])
floor16.width = 2
floor16.height = 60
floor17 = uvage.from_image(660, 581, floor_images[0])
floor17.width = 2
floor17.height = 60
floor18 = uvage.from_image(700, 581, floor_images[0])
floor18.width = 2
floor18.height = 60
floor19 = uvage.from_image(740, 581, floor_images[0])
floor19.width = 2
floor19.height = 60
floor20 = uvage.from_image(780, 581, floor_images[0])
floor20.width = 2
floor20.height = 60
floor_negative1 = uvage.from_image(-260, 581, floor_images[0])
floor_negative1.width = 2
floor_negative1.height = 2
floor_negative2 = uvage.from_image(-220, 581, floor_images[0])
floor_negative2.width = 2
floor_negative2.height = 2
floor_negative3 = uvage.from_image(-180, 581, floor_images[0])
floor_negative3.width = 2
floor_negative3.height = 2
floor_negative4 = uvage.from_image(-140, 581, floor_images[0])
floor_negative4.width = 2
floor_negative4.height = 2
floor_negative5 = uvage.from_image(-100, 581, floor_images[0])
floor_negative5.width = 2
floor_negative5.height = 2
floor_negative6 = uvage.from_image(-60, 581, floor_images[0])
floor_negative6.width = 2
floor_negative6.height = 2
floor_negative7 = uvage.from_image(-20, 581, floor_images[0])
floor_negative7.width = 2
floor_negative7.height = 2

random_x1 = random.randint(50, int(800)) #helps randomize coin position
random_x2 = random.randint(50, int(800))

mario_coin_images = uvage.load_sprite_sheet("Coins16.png", 1, 1) #coin image
mario_coin = uvage.from_image(random_x1 or random_x2, 500, mario_coin_images[0])  #Coin position is randomized
mario_coin.width = 10
mario_coin.height = 35

bowser_images = uvage.load_sprite_sheet("Bowser4.png", 1, 8)  #Bowser sprite
bowser = uvage.from_image(4500, 470, bowser_images[0])
bowser.height = 20
bowser.width = 200

power_box_images = uvage.load_sprite_sheet("Power Box.png", 1, 1)  #Box with question box, mystery box
power_box = uvage.from_image(300, 420, power_box_images[0])
power_box.width = 20
power_box.height = 60
power_box2 = uvage.from_image(2600, 420, power_box_images[0])
power_box2.width = 20
power_box2.height = 60
power_box3 = uvage.from_image(3950, 520, power_box_images[0])
power_box3.width = 20
power_box3.height = 60

power_boxes = [
    power_box, power_box2
]

long_blocks_images = uvage.load_sprite_sheet("long_blocks.png", 1, 1)  # Platforms that are hoisted in the air
long_blocks = uvage.from_image(1415, 450, long_blocks_images[0])
long_blocks.width = 100
long_blocks.height = 25
long_blocks2 = uvage.from_image(1615, 400, long_blocks_images[0])
long_blocks2.width = 100
long_blocks2.height = 25
long_blocks3 = uvage.from_image(2700, 500, long_blocks_images[0])
long_blocks3.width = 100
long_blocks3.height = 25

longblocks = [long_blocks]

smasher_images = uvage.load_sprite_sheet("Thwomp.png", 1, 1) #Smasher image
smasher = uvage.from_image(3120, 112, smasher_images[0])
smasher.width = 100
smasher.height = 150
smasher2 = uvage.from_image(3350, 112, smasher_images[0])
smasher2.width = 100
smasher2.height = 150
smasher3 = uvage.from_image(3580, 112, smasher_images[0])
smasher3.width = 100
smasher3.height = 150
smasher4 = uvage.from_image(3810, 112, smasher_images[0])
smasher4.width = 100
smasher4.height = 150

smashers = [smasher, smasher2, smasher3, smasher4]

tube_images = uvage.load_sprite_sheet("TUBE.png", 1, 1) #tube image
tube2 = uvage.from_image(450, 515, tube_images[0])
tube2.width = 1
tube2.height = 100
tube3 = uvage.from_image(600, 515, tube_images[0])
tube3.width = 1
tube3.height = 100
tube4 = uvage.from_image(750, 515, tube_images[0])
tube4.width = 1
tube4.height = 100
tube5 = uvage.from_image(900, 515, tube_images[0])
tube5.width = 1
tube5.height = 100
tube6 = uvage.from_image(900, 515, tube_images[0])
tube6.width = 1
tube6.height = 100

tubes = [tube2, tube3, tube4, tube5, tube6]

castle_images = uvage.load_sprite_sheet("castle_final.png", 1, 1) #Castle image
castle = uvage.from_image(5200, 388, castle_images[0]) # 5000
castle.width = 200
castle.height = 350

stair_images = uvage.load_sprite_sheet('BLOCKS.png', 1, 1)

stair_block1 = uvage.from_image(4720, 540, floor_images[0])  # top
stair_block1.width = 40
stair_block1.height = 60
stair_block2 = uvage.from_image(4760, 540, floor_images[0])
stair_block2.width = 40
stair_block2.height = 60
stair_block3 = uvage.from_image(4760, 500, floor_images[0])  # top
stair_block3.width = 40
stair_block3.height = 60
stair_block4 = uvage.from_image(4800, 540, floor_images[0])
stair_block4.width = 40
stair_block4.height = 60
stair_block5 = uvage.from_image(4800, 500, floor_images[0])
stair_block5.width = 40
stair_block5.height = 60
stair_block6 = uvage.from_image(4800, 460, floor_images[0]) # top
stair_block6.width = 40
stair_block6.height = 60
stair_block7 = uvage.from_image(4840, 540, floor_images[0])
stair_block7.width = 40
stair_block7.height = 60
stair_block8 = uvage.from_image(4840, 500, floor_images[0])
stair_block8.width = 40
stair_block8.height = 60
stair_block9 = uvage.from_image(4840, 460, floor_images[0])
stair_block9.width = 40
stair_block9.height = 60
stair_block10 = uvage.from_image(4840, 420, floor_images[0]) # top
stair_block10.width = 40
stair_block10.height = 60
stair_block11 = uvage.from_image(4880, 540, floor_images[0])
stair_block11.width = 40
stair_block11.height = 60
stair_block12 = uvage.from_image(4880, 500, floor_images[0])
stair_block12.width = 40
stair_block12.height = 60
stair_block13 = uvage.from_image(4880, 460, floor_images[0])
stair_block13.width = 40
stair_block13.height = 60
stair_block14 = uvage.from_image(4880, 420, floor_images[0])
stair_block14.width = 40
stair_block14.height = 60
stair_block15 = uvage.from_image(4880, 380, floor_images[0]) # top
stair_block15.width = 40
stair_block15.height = 60
stair_block16 = uvage.from_image(4920, 540, floor_images[0])
stair_block16.width = 40
stair_block16.height = 60
stair_block17 = uvage.from_image(4920, 500, floor_images[0])
stair_block17.width = 40
stair_block17.height = 60
stair_block18 = uvage.from_image(4920, 460, floor_images[0])
stair_block18.width = 40
stair_block18.height = 60
stair_block19 = uvage.from_image(4920, 420, floor_images[0])
stair_block19.width = 40
stair_block19.height = 60
stair_block20 = uvage.from_image(4920, 380, floor_images[0])
stair_block20.width = 40
stair_block20.height = 60
stair_block21 = uvage.from_image(4920, 340, floor_images[0]) #top
stair_block21.width = 40
stair_block21.height = 60

peach_images = uvage.load_sprite_sheet("Peach6.png", 1, 1) #Peach image
peach = uvage.from_image(5500, 514, peach_images[0])
peach.width = 20
peach.height = 100

plant_images = uvage.load_sprite_sheet("PLANTS_NEW.png", 1, 12) #Plant images
plant = uvage.from_image(1950, 532, plant_images[-1])
plant.width = 20
plant.height = 110
plant2 = uvage.from_image(2150,  532, plant_images[-1])
plant2.width = 20
plant2.height = 110
plant3 = uvage.from_image(2350, 532, plant_images[-1])
plant3.width = 20
plant3.height = 110

shooter_images = uvage.load_sprite_sheet("Fireball2.png", 1, 1)  #Mario's fireball
shooter = uvage.from_image(3950, -10, shooter_images[0])
shooter.width = 20
shooter.height = 20

MapImage_images = uvage.load_sprite_sheet("MarioMap2.png", 1, 1)  #Mario's fireball
MapImage = uvage.from_image(400, 300, MapImage_images[0])
MapImage.width = 800
MapImage.height = 600

press_x_images = uvage.load_sprite_sheet("PressX-PhotoRoom.png-PhotoRoom.png", 1, 1)  #Mario's fireball
press_x = uvage.from_image(380, 400, press_x_images[0])
press_x.width = 20
press_x.height = 50

shooters = [shooter]

health_bar_height = 10
health_bar_width = 255
health_bar = uvage.from_color(4450, 280, "red", health_bar_width, health_bar_height)  #Physical healthbar

health = uvage.from_text(4450, 250, "Health: 300", 30, "red")  #Textual healthbar

coins = [
    mario_coin
]

score = 0
score_display = uvage.from_text(40, 40, str(score), 50, "black")

obstacles = [floor, floor2, floor3, floor4, floor5, floor6, floor7, floor8, floor9, floor10, floor11, floor12, floor13,  #List of things mario touches
             floor14, floor15, floor16, floor17, floor18, floor19, floor20, floor_negative1, floor_negative2,
             floor_negative3, floor_negative4, floor_negative5, floor_negative6, floor_negative7, tube2, tube3, tube4,
             tube5, tube6, long_blocks, long_blocks2, long_blocks3, stair_block1, stair_block3, stair_block6, stair_block10, stair_block15, stair_block16,
             stair_block17,stair_block18, stair_block19,stair_block20, stair_block21 ]

pygame.mixer.init()
jump_sound = pygame.mixer.Sound("smb_jump-small.wav")
win_sound = pygame.mixer.Sound("smb_world_clear.wav")
bowser_death = pygame.mixer.Sound("smb_bowserfalls.wav")
game_over_s = pygame.mixer.Sound("smb_gameover.wav")
coin_sound = pygame.mixer.Sound("smb_coin.wav")
power_box_sound = pygame.mixer.Sound("smb_powerup.wav")
fireball_sound = pygame.mixer.Sound("smb_fireball.wav")
b_fireball_sound = pygame.mixer.Sound("ssbm_bowser_21.wav")
mario_laugh = pygame.mixer.Sound("ssbm_dr_mario_20_mario_14.wav")
smasher_sound = pygame.mixer.Sound("sm64_thwomp.wav")
background_sound = pygame.mixer.Sound("SuperMarioBros.wav")

gravity = 0.65
jump_speed = 11
num = 0
smasher_speed = 2
smasher1_speed = 2.25
time1 = 0
smasher_rising = {}

smasher_states = [0] * len(smashers)  # 0 for rising, 1 for falling
rise_speeds = [-random.uniform(4, 7) for _ in smashers]
fall_speeds = [random.uniform(4, 8) for _ in smashers]
sound_playing = False
game_started = False

title_map_initialization = False
x_key_pressed = False

play_background_sound = True

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

circle_color1 = (128, 0, 0)  # Red
circle_radius1 = 5
circle_position1 = (148, 408)
circle_color2 = (64, 64, 64)  # Red
circle_radius2 = 6
circle_position2 = (148, 315)
circle_color3 = (64, 64, 64)  # Red
circle_radius3 = 6.5
circle_position3 = (148, 261)
circle_color4 = (64, 64, 64)  # Red
circle_radius4 = 5
circle_position4 = (102, 241)
circle_color5 = (64, 64, 64)  # Red
circle_radius5 = 6
circle_position5 = (239, 186)
circle_color6 = (64, 64, 64)  # Red
circle_radius6 = 6
circle_position6 = (285, 222)
circle_color7 = (64, 64, 64)  # Red
circle_radius7 = 6
circle_position7 = (355, 55)     # set colors to gray, then when the level is beaten, gray turns to red
circle_color8 = (64, 64, 64)  # Red
circle_radius8 = 6
circle_position8 = (490, 90)
circle_color9 = (64, 64, 64)  # Red
circle_radius9 = 6
circle_position9 = (560, 93)
circle_color10 = (64, 64, 64)  # Red
circle_radius10 = 6
circle_position10 = (675, 65)
circle_color11 = (64, 64, 64)  # Red
circle_radius11 = 6
circle_position11 = (678, 180)
circle_color12 = (64, 64, 64)  # Red
circle_radius12 = 6
circle_position12 = (679, 305)
circle_color12 = (64, 64, 64)  # Red
circle_radius12 = 6
circle_position12 = (679, 305)
circle_color13 = (64, 64, 64)  # Red
circle_radius13 = 5
circle_position13 = (588, 350)
circle_color14 = (64, 64, 64)  # Red
circle_radius14 = 6
circle_position14 = (583, 406)
circle_color15 = (64, 64, 64)  # Red
circle_radius15 = 6
circle_position15 = (514, 502)
circle_color16 = (64, 64, 64)  # Red
circle_radius16 = 6
circle_position16 = (468, 502)
circle_color17 = (64, 64, 64)  # Red
circle_radius17 = 6
circle_position17 = (400, 502)
circle_color18 = (64, 64, 64)  # Red
circle_radius18 = 6
circle_position18 = (308, 482)
circle_color19 = (64, 64, 64)  # Red
circle_radius19 = 9
circle_position19 = (353, 427)
circle_color_fillin = (160, 125, 85)
circle_radius_fillin = 5
circle_position_fillin = (377, 537)

circles = {
    1: {'color': (128, 0, 0), 'radius': 5, 'position': (148, 408)},
    2: {'color': (64, 64, 64), 'radius': 6, 'position': (148, 315)},
    3: {'color': (64, 64, 64), 'radius': 6.5, 'position': (148, 261)},
    4: {'color': (64, 64, 64), 'radius': 5, 'position': (102, 241)},
    5: {'color': (64, 64, 64), 'radius': 6, 'position': (239, 186)},
    6: {'color': (64, 64, 64), 'radius': 6, 'position': (285, 222)},
    7: {'color': (64, 64, 64), 'radius': 6, 'position': (355, 55)},
    8: {'color': (64, 64, 64), 'radius': 6, 'position': (490, 90)},
    9: {'color': (64, 64, 64), 'radius': 6, 'position': (560, 93)},
    10: {'color': (64, 64, 64), 'radius': 6, 'position': (675, 65)},
    11: {'color': (64, 64, 64), 'radius': 6, 'position': (678, 180)},
    12: {'color': (64, 64, 64), 'radius': 6, 'position': (679, 305)},
    13: {'color': (64, 64, 64), 'radius': 5, 'position': (588, 350)},
    14: {'color': (64, 64, 64), 'radius': 6, 'position': (583, 406)},
    15: {'color': (64, 64, 64), 'radius': 6, 'position': (514, 502)},
    16: {'color': (64, 64, 64), 'radius': 6, 'position': (468, 502)},
    17: {'color': (64, 64, 64), 'radius': 6, 'position': (400, 502)},
    18: {'color': (64, 64, 64), 'radius': 6, 'position': (308, 482)},
    19: {'color': (64, 64, 64), 'radius': 9, 'position': (353, 427)}
}

def handle_mario_x_movement():
    global camera, mario, frame, facing_right, walls, is_moving
    is_moving = False
    if uvage.is_pressing("left arrow"):
        if facing_right:
            facing_right = False
            mario.flip()
        is_moving = True
        mario.x -= 5
        camera.x = mario.x + 318
    elif uvage.is_pressing("right arrow"):
        if not facing_right:
            facing_right = True
            mario.flip()
        is_moving = True
        mario.x += 5
        camera.x = mario.x + 318
    if not is_moving:
        mario.image = mario_images[3]
    else:
        frame += 0.3
        if frame >= 3:
            frame = 0
        mario.image = mario_images[int(frame)]
    mario.move_to_stop_overlapping(wall)
    if press_space is False:
        if uvage.is_pressing("right arrow"):
            mario.x -= 5
            mario.image = mario_images[-1]
            facing_right = True
    if press_space is False:
        if uvage.is_pressing("left arrow"):
            mario.x += 5
            mario.image = mario_images[3]
            facing_right = False

def handle_wall():
    global walls
    for i in walls:
        if mario.right_touches(i) or mario.left_touches(i):
            return True

def handle_plant_movement():
    global facing_right, is_moving, frame1
    frame1 += 0.2
    if frame1 >= 5:
        frame1 = 0
    plant.image = plant_images[int(frame1)]
    plant2.image = plant_images[int(frame1)]
    plant3.image = plant_images[int(frame1)]

def handle_bowser_movement():
    global frame2, game_over
    frame2 += 0.2
    if frame2 >= 5:
        frame2 = 0
    bowser.image = bowser_images[int(frame2)]

def move_smasher():
   global start_game, game_on, smashers, obstacles, gravity, smasher_speed, time1, smasher_rising, smasher_states, rise_speeds, fall_speeds, sound_playing

   if game_on and mario.x >= 2300:
       for i, smasher in enumerate(smashers):
           if smasher_states[i] == 0:
               smasher.speedy = rise_speeds[i]
               smasher.top += smasher.speedy
               if smasher.top <= 25:
                   smasher_states[i] = 1
           else:  # Falling state
               smasher.speedy = fall_speeds[i]
               smasher.top += smasher.speedy
               if smasher.top >= 410:
                   smasher_states[i] = 0
                   sound_playing = True
                   smasher_sound.play()

           mario.move_to_stop_overlapping(smasher)
   if game_on and mario.x >= 4000:
       smasher_sound.stop()

def handle_coins():
    global score, coins, score_display
    for coin in coins:
        if mario.touches(coin):
            score += 1
            random_x = random.randint(int(mario.x) + 100, 5500)
            coin.x = random_x
            coin_sound.play()
        camera.draw(coin)
    score_display = uvage.from_text(705 + mario.x, 25, str(score), 40, "black")
    camera.draw(score_display)

def handle_powerboxes():
    global countdown
    if mario.touches(power_box):
        mario.width = 50
        mario.height = 120
        power_box.x = -300
        countdown = 150
        power_box_sound.play()
    if mario.touches(power_box2):
        mario.width = 50
        mario.height = 120
        power_box2.x = -305
        countdown = 150
        power_box_sound.play()

def bullet():
    global start_game, game_on, game_over
    if game_on is True:
        mario_bullet.x -= 12.5
        mario_bullet.move_speed()
        mario_bullet2.x -= 8
        mario_bullet2.move_speed()
        mario_bullet3.x -= 8
        mario_bullet3.move_speed()
        if mario.x > 800:
            mario_bullet4.x -= 13
            mario_bullet4.move_speed()
        if mario.x > 900:
            mario_bullet4.x -= 10
            mario_bullet4.move_speed()
        if mario.x > 900:
            mario_bullet5.x -= 8
            mario_bullet5.move_speed()

def jump():
    for obstacle in obstacles:
        if mario.bottom_touches(obstacle):
            if uvage.is_pressing('up arrow'):
                mario.speedy = -jump_speed
                jump_sound.play()
    mario.speedy += gravity
    mario.move_speed()
    for obstacle in obstacles:
        mario.move_to_stop_overlapping(obstacle)

def move_floors():
    global floor_negative1, floor_negative2, floor_negative3, floor_negative4, floor_negative5, floor_negative6, floor_negative7, floor, floor2, floor3, floor4, floor5, floor6, floor7, floor8, floor9, floor10, floor11,floor12, floor13, floor14, floor15, floor16, floor17, floor18, floor19, floor20
    if floor_negative1 in obstacles:
        floor_negative1.x = mario.x - 260
    if floor_negative2 in obstacles:
        floor_negative2.x = floor_negative1.x + 40
    if floor_negative3 in obstacles:
        floor_negative3.x = floor_negative2.x + 40
    if floor_negative4 in obstacles:
        floor_negative4.x = floor_negative3.x + 40
    if floor_negative5 in obstacles:
        floor_negative5.x = floor_negative4.x + 40
    if floor_negative6 in obstacles:
        floor_negative6.x = floor_negative5.x + 40
    if floor_negative7 in obstacles:
        floor_negative7.x = floor_negative6.x - 40
    if floor in obstacles:
        floor.x = floor_negative7.x + 40
    if floor2 in obstacles:
        floor2.x = floor.x + 40
    if floor3 in obstacles:
        floor3.x = floor2.x + 40
    if floor4 in obstacles:
        floor4.x = floor3.x + 40
    if floor5 in obstacles:
        floor5.x = floor4.x + 40
    if floor6 in obstacles:
        floor6.x = floor5.x + 40
    if floor7 in obstacles:
        floor7.x = floor6.x + 40
    if floor8 in obstacles:
        floor8.x = floor7.x + 40
    if floor9 in obstacles:
        floor9.x = floor8.x + 40
    if floor10 in obstacles:
        floor10.x = floor9.x + 40
    if floor11 in obstacles:
        floor11.x = floor10.x + 40
    if floor12 in obstacles:
        floor12.x = floor11.x + 40
    if floor13 in obstacles:
        floor13.x = floor12.x + 40
    if floor14 in obstacles:
        floor14.x = floor13.x + 40
    if floor15 in obstacles:
        floor15.x = floor14.x + 40
    if floor16 in obstacles:
        floor16.x = floor15.x + 40
    if floor17 in obstacles:
        floor17.x = floor16.x + 40
    if floor18 in obstacles:
        floor18.x = floor17.x + 40
    if floor19 in obstacles:
        floor19.x = floor18.x + 40
    if floor20 in obstacles:
        floor20.x = floor19.x + 40

def touching_tubes():
    for tube in tubes:
        mario.move_to_stop_overlapping(tube, padding2=-150)

def touching_long_blocks():
    for block in longblocks:
        mario.move_to_stop_overlapping(block)

def touching_castle():
    global win,time, game_over,jump_speed,is_moving,facing_right,facing_left, mario_images

    if mario.touches(castle, padding=1, padding2=-72):   ## FIXXX !!!!
        win = True
        time = 1
        mario.x = 5070
        mario.image = mario_images[-1]
        mario.speedy = 0.5
        mario.speedx = 0
        if uvage.is_pressing ("left arrow") or uvage.is_pressing ("right arrow"):
            is_moving = False
            facing_right = False
            facing_left = False
            mario.image = mario_images[-1]

def fireball_generation():
    global fireb, fireballs, game_over, jump_speed, count

    if mario.x > 3700:
        jump_speed = 12
        fireb.x -= 5
        fireb.move_speed()
    if fireb.x < 3650:
        fireb.x = 4450
        fireb.speedx = -5
    if count == 0:
        fireb.x = -200
        jump_speed = 11

def mario_fireball():
    global shooter, facing_right, count
    if mario.x >= 3950 and  not count == 0:
        shooter.y = mario.y + 13
        if mario.touches(power_box3):
            power_box3.x = -200
            shooter.x = 3800
        if facing_right is True:
            if uvage.is_pressing("d"):
                shooter.x = mario.x
                shooter.speedx = 5
                fireball_sound.play()
        shooter.move_speed()
        if facing_right is False:
            if uvage.is_pressing("d"):
                shooter.speedx = -5
                shooter.x = mario.x
                fireball_sound.play()
        shooter.move_speed()

def tick():
    global levels_screen, game_on, start_game, press_space, mario, floor, time, smashers, game_over, countdown, power_box3, shooter, shooters, health_bar, health_bar_width, health_bar_height, count, health, bowser, game_state, score, game_started, Mario_icon, custom_font, MapImage, press_x, title_map_initialization, x_key_pressed, play_background_sound, play_background_sound_iterations, start_time_game, desired_iterations, circle_color, screen, circle_radius, circle_position, circles
    from gameREVISED import TESTER
    for shooter in shooters:
        if shooter.touches(bowser):
            count -= 1
            shooter.speedx = 1000
            if count == 6:
                health_bar = (uvage.from_color(4451, 280, "red", 255*0.7, health_bar_height))
                health = uvage.from_text(4450, 250, "Health: 255", 30, "red")
            if count == 5:
                health_bar = (uvage.from_color(4452, 280, "red", 181, health_bar_height))
                health = uvage.from_text(4450, 250, "Health: 210", 30, "red")
            if count == 4:
                health_bar = (uvage.from_color(4453, 280, "red", 144, health_bar_height))
                health = uvage.from_text(4450, 250, "Health: 165", 30, "red")
            if count == 3:
                health_bar = (uvage.from_color(4454, 280, "red", 107, health_bar_height))
                health = uvage.from_text(4450, 250, "Health: 120", 30, "red")
            if count == 2:
                health_bar = (uvage.from_color(4455, 280, "red", 70, health_bar_height))
                health = uvage.from_text(4450, 250, "Health: 75", 30, "red")
            if count == 1:
                health_bar = (uvage.from_color(4456, 280, "red", 33, health_bar_height))
                health = uvage.from_text(4450, 250, "Health: 30", 30, "red")
            if count == 0:
                health_bar = (uvage.from_color(4457, 280, "red", 0, health_bar_height))
                health = uvage.from_text(-200, 250, "Health: 100", 30, "red")
                bowser.x = -200
                fireb.x = -200
                bowser_death.play()
                mario_laugh.play()

    shooter.move_speed()

    if game_on is False:
        if start_game is True:
            if game_started is False and not x_key_pressed:
                camera.draw(Loading_screen)
                camera.draw(press_x)
                camera.draw(Mario_icon)
                camera.display()

                if uvage.is_pressing("x") and title_map_initialization is False:
                    x_key_pressed = True
                    background_sound.play()
                    pygame.draw.circle(screen, circle_color1, circle_position1, circle_radius1)
                    pygame.draw.circle(screen, circle_color2, circle_position2, circle_radius2)
                    pygame.draw.circle(screen, circle_color3, circle_position3, circle_radius3)
                    pygame.draw.circle(screen, circle_color4, circle_position4, circle_radius4)
                    pygame.draw.circle(screen, circle_color5, circle_position5, circle_radius5)
                    pygame.draw.circle(screen, circle_color6, circle_position6, circle_radius6)
                    pygame.draw.circle(screen, circle_color7, circle_position7, circle_radius7)
                    pygame.draw.circle(screen, circle_color8, circle_position8, circle_radius8)
                    pygame.draw.circle(screen, circle_color9, circle_position9, circle_radius9)
                    pygame.draw.circle(screen, circle_color10, circle_position10, circle_radius10)
                    pygame.draw.circle(screen, circle_color11, circle_position11, circle_radius11)
                    pygame.draw.circle(screen, circle_color12, circle_position12, circle_radius12)
                    pygame.draw.circle(screen, circle_color13, circle_position13, circle_radius13)
                    pygame.draw.circle(screen, circle_color14, circle_position14, circle_radius14)
                    pygame.draw.circle(screen, circle_color15, circle_position15, circle_radius15)
                    pygame.draw.circle(screen, circle_color16, circle_position16, circle_radius16)
                    pygame.draw.circle(screen, circle_color17, circle_position17, circle_radius17)
                    pygame.draw.circle(screen, circle_color18, circle_position18, circle_radius18)
                    pygame.draw.circle(screen, circle_color19, circle_position19, circle_radius19)
                    pygame.draw.circle(screen, circle_color_fillin, circle_position_fillin, circle_radius_fillin)
                    TESTER.run_game() and camera.draw(LevelsScreen)
                    camera.display()


                    if uvage.is_pressing("space") and not game_over and x_key_pressed is True :
                        press_space = True
                        game_on = True
        if uvage.is_pressing("r") and game_over:
            game_started = True
            press_space = False
            game_on = False
            start_game = True
            game_over = False
            mario.x = 70
            camera.x = mario.x + 320 # keep
            power_box.x = 300
            power_box2.x = 2600
            power_box3.x = 3950
            fireb.x = 4390
            mario_bullet.x = 1700
            mario_bullet2.x = 2700
            mario_bullet3.x = 3000
            mario_bullet4.x = 10000
            mario_bullet5.x = 12000
            camera.draw(background1)
            camera.draw(title_screen1)
            camera.draw(bowser_icon1)
            camera.draw("Bowser has kidnapped Princess Peach! Save her!", 30, "white", mario.x, 335)
            camera.draw("Press Space to Start", 30, "white", mario.x, 450)
            camera.draw(power_box)
            camera.draw(power_box2)
            camera.display()
            score = 0 # keep
            time = 220  # keep
    else:
        if game_on and press_space:
            mario.move_speed()
            time -= 0.1
            if time == 0:
                press_space = False
        camera.clear("sky blue")
        camera.draw(mario)
        camera.draw("Time: " + str(int(time)), 30, "black", 400, 30)
        if game_on is False and start_game is True:
            camera.draw("MARIO", 110, "red", 380, 270)
            camera.draw("Press Space to Start", 30, "red", 380, 330)
        if game_on is True and start_game is False:
            game_on = True
            start_game = True
            #if uvage.is_pressing("r"):
                #game_on = True
                #start_game = True
        for circle_sprite in circle_sprites.values():
            screen.blit(circle_sprite.image, circle_sprite.rect)
        for floor in floors:
            camera.draw(floor)
        if mario.touches(mario_bullet) or mario.touches(smasher2) or mario.touches(mario_bullet2) or mario.touches(mario_bullet3) or mario.touches(mario_bullet4) or mario.touches(mario_bullet5) or  mario.touches(
                smasher) or mario.touches(smasher3) or mario.touches(smasher4) or time <= 0 or \
                mario.touches(plant, padding=-60, padding2=-60) \
                or mario.touches(plant2, padding=-60, padding2=-60) or mario.touches(plant3, padding=-60, padding2=-60) or mario.touches(fireb, padding=-40, padding2=-10) or mario.touches(bowser):
            mario_bullet.x = -320
            mario_bullet2.x = -320
            mario_bullet3.x = -320
            mario_bullet4.x = -320
            mario_bullet5.x = -320
            game_on = False
            start_game = False
            game_over = True
            game_over_s.play()
        if game_over is True:
            camera.draw(uvage.from_text(mario.x + 300, 100, "Game Over", 150, "red"))
            camera.draw(uvage.from_text(mario.x + 300, 300, "Press r to Restart!", 50, "red"))
            camera.display()
        handle_mario_x_movement()
        handle_wall()
        handle_plant_movement()
        handle_bowser_movement()
        move_smasher()
        handle_coins()
        handle_powerboxes()

        if countdown > 0:
            countdown -= 1
        if countdown == 0:
            mario.width = 30
            mario.height = 60

        bullet()
        jump()
        move_floors()
        touching_tubes()
        touching_long_blocks()
        touching_castle()

        if win is True:
            camera.draw(uvage.from_text(5500, 300, "You Saved the Princess!", 50, "red"))
            time = 1
            mario.xspeed = 0
            mario.move_speed()
            win_sound.play()
            game_over = not True


        fireball_generation()
        mario_fireball()
        camera.draw(wall)
        handling_levels()
        TESTER.run_game()
        camera.draw(floor_negative1)
        camera.draw(floor_negative2)
        camera.draw(floor_negative3)
        camera.draw(floor_negative4)
        camera.draw(floor_negative5)
        camera.draw(floor_negative6)
        camera.draw(floor_negative7)
        camera.draw(floor)
        camera.draw(floor2)
        camera.draw(floor3)
        camera.draw(floor4)
        camera.draw(floor5)
        camera.draw(floor6)
        camera.draw(floor7)
        camera.draw(floor8)
        camera.draw(floor9)
        camera.draw(floor10)
        camera.draw(floor11)
        camera.draw(floor12)
        camera.draw(floor13)
        camera.draw(floor14)
        camera.draw(floor15)
        camera.draw(floor16)
        camera.draw(floor17)
        camera.draw(floor18)
        camera.draw(floor19)
        camera.draw(floor20)
        camera.draw(power_box2)
        camera.draw(power_box2)
        camera.draw(power_box)
        camera.draw(tube2)
        camera.draw(tube3)
        camera.draw(tube4)
        camera.draw(tube5)
        camera.draw(tube6)
        camera.draw(mario_bullet)
        camera.draw(mario_bullet2)
        camera.draw(mario_bullet3)
        camera.draw(mario_bullet4)
        camera.draw(mario_bullet5)
        camera.draw(long_blocks)
        camera.draw(long_blocks2)
        camera.draw(long_blocks3)
        camera.draw(plant)
        camera.draw(plant2)
        camera.draw(plant3)
        camera.draw(smasher)
        camera.draw(smasher2)
        camera.draw(smasher3)
        camera.draw(smasher4)
        camera.draw(power_box3)
        camera.draw(fireb)
        camera.draw(shooter)
        camera.draw(bowser)
        camera.draw(health_bar)
        camera.draw(castle)
        camera.draw(peach)
        camera.draw(health)
        camera.draw(stair_block1)
        camera.draw(stair_block2)
        camera.draw(stair_block3)
        camera.draw(stair_block4)
        camera.draw(stair_block5)
        camera.draw(stair_block6)
        camera.draw(stair_block7)
        camera.draw(stair_block8)
        camera.draw(stair_block9)
        camera.draw(stair_block10)
        camera.draw(stair_block11)
        camera.draw(stair_block12)
        camera.draw(stair_block13)
        camera.draw(stair_block14)
        camera.draw(stair_block15)
        camera.draw(stair_block16)
        camera.draw(stair_block17)
        camera.draw(stair_block18)
        camera.draw(stair_block19)
        camera.draw(stair_block20)
        camera.draw(stair_block21)
    camera.display()
uvage.timer_loop(30, tick)
