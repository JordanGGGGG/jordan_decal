'''To do:
    -create graphics for walls, platforms, the player, and three different backgrounds for each level (maybe each level will have a different planet in the back)
    -create graphic and feature of a coin or some collectible that if you collect one in each level, something good happens at the end
    -create goal flag and graphic
    '''

import pygame
from sys import exit

pygame.init()

#Important Variables
screen = pygame.display.set_mode((1500,800))
pygame.display.set_caption('Gravity')
clock = pygame.time.Clock()
game_state = 0
t_font = pygame.font.Font('C:/Users/Jgome/python_decal/jordan_decal/final_project/fonts/slkscre.ttf', 100)
small_font = pygame.font.Font('C:/Users/Jgome/python_decal/jordan_decal/final_project/fonts/slkscre.ttf', 50)

#Surfaces
title_background_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/backgrounds/TitleScreen.png').convert()
level1_background_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/backgrounds/level1background.png').convert()
level1_background_surface = pygame.transform.scale(level1_background_surface, (1500, 800))

title_surface = t_font.render('Gravity', False, (224, 224, 224))
press_start_surface = small_font.render('Press Space to Start', False, (224, 224, 224))
bad_ending_surface = t_font.render('Bad Ending', False, (224, 224, 224))
bad_ending_message = small_font.render('Try Collecting All Coins', False, (224, 224, 224))
good_ending_surface = t_font.render('Good Ending', False, (224, 224, 224))
good_ending_message = small_font.render('Yippee!!!', False, (224, 224, 224))
thanks = t_font.render('Thanks!', False, (224, 224, 224))
#coins_collected_surface = small_font.render(f'Coins = {coins_collected}', False, (224, 224, 224)) #This needs to go inside the game loop so that it can be changed when collecting a coin

ground_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/ground.png').convert()
ground_surface = pygame.transform.scale(ground_surface, (1500, 100))
wall_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/ground.png').convert()
wall_surface = pygame.transform.scale(wall_surface, (100, 800))
wall_left_rect = wall_surface.get_rect(topleft = (0,0))
wall_right_rect = wall_surface.get_rect(topright = (1500, 0))

#Player variables

def player_animation():
    global player_surface, player_index, player_velocity#, player_rect, obstacle_rects_level1, platform_data_level1
    if player_velocity == 1:
    #for obstacle in obstacle_rects_level1:
        #if player_rect.colliderect(obstacle["rect"]):
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]
        #and platform in platform_data_level1:
        #or player_rect.bottom.colliderect(platform["rect"]):
        #else:
           # player_surface = player_fall
    else:
        player_index += 0.1
        if player_index >= len(reverse_player_walk):
            player_index = 0
        player_surface = reverse_player_walk[int(player_index)]
    #play walking animation when on floor
    #play fall animation when not on floor
    #play reverse walk animation when x_velocity < 0
    #play reverse fall animation when x_velocity < 0

player_walk_1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/playerwalk1.png').convert()
player_walk_1 = pygame.transform.scale(player_walk_1, (50,50))
player_walk_2 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/playerwalk2.png').convert()
player_walk_2 = pygame.transform.scale(player_walk_2, (50, 50))
reverse_player_walk_1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/reverseplayerwalk1.png').convert()
reverse_player_walk_1 = pygame.transform.scale(reverse_player_walk_1, (50,50))
reverse_player_walk_2 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/reverseplayerwalk2.png').convert()
reverse_player_walk_2 = pygame.transform.scale(reverse_player_walk_2, (50,50))
player_walk = [player_walk_1, player_walk_2]
reverse_player_walk = [reverse_player_walk_1, reverse_player_walk_2]
player_index = 0 #This will handle animation
#player_fall = pygame.image.load('C:/Users/Jgome/python_decal/final_project/entity_textures/playerfall.png').convert() 
#player_fall = pygame.transform.scale(player_fall, (50,50))
#reverse_player_fall = pygame.image.load('C:/Users/Jgome/python_decal/final_project/backgrounds/TitleScreen.png').convert() 
#reverse_player_fall = pygame.transform.scale(reverse_player_fall, (50,50))

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (125, 700))
player_velocity = 1

#Initialize Variables
gravity_mag = 1
gravity_direction = 1 #separate the magnitude of gravity from the direction so I can manipulate them individually
x_gravity_direction = -1 #this is negative so that all platforms start on the left side when the level loads
x_gravity_mag = 1
object_gravity = 0 #initialize object_gravity
object_x_gravity = 0 #initialize horizontal object gravity
player_gravity = 0 #initialize player_gravity
enemy_gravity = 0
coins_collected = 0

'''When defining rectangles for platforms, always use same coordinate (i.e. topleft) when specifying its rectangle for every platform. This prevents misalignment 
errors and keeps everything standardized.'''

#Level 1 surfaces and Lists
wall_1_l1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/ground.png').convert() 
wall_1_l1 = pygame.transform.scale(wall_1_l1, (100, 200))
wall_1_l1_rect = wall_1_l1.get_rect(bottomleft = (275, 700))
wall_2_l1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/ground.png').convert()
wall_2_l1 = pygame.transform.scale(wall_2_l1, (100, 200))
wall_2_l1_rect = wall_2_l1.get_rect(bottomleft = (450, 650))
wall_3_l1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/ground.png').convert()
wall_3_l1 = pygame.transform.scale(wall_3_l1, (150, 50))
wall_3_l1_rect = wall_3_l1.get_rect(bottomright = (700, 500))
wall_4_l1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/ground.png').convert()
wall_4_l1 = pygame.transform.scale(wall_4_l1, (425, 50))
wall_4_l1_rect = wall_4_l1.get_rect(topleft = (275, 300))
wall_5_l1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/ground.png').convert()
wall_5_l1 = pygame.transform.scale(wall_5_l1, (100, 50))
wall_5_l1_rect = wall_5_l1.get_rect(topleft = (100, 300))
wall_6_l1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/ground.png').convert()
wall_6_l1 = pygame.transform.scale(wall_6_l1, (200, 250))
wall_6_l1_rect = wall_6_l1.get_rect(topleft = (950, 450))
wall_7_l1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/ground.png').convert()
wall_7_l1 = pygame.transform.scale(wall_7_l1, (175, 75))
wall_7_l1_rect = wall_7_l1.get_rect(topleft = (1225, 450))
object1_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/verticalplatform.png').convert()
object1_surface = pygame.transform.scale(object1_surface, (75, 100))
object1_rect = object1_surface.get_rect(topleft = (200, 700))
object2_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/verticalplatform.png').convert()
object2_surface = pygame.transform.scale(object2_surface, (75, 100))
object2_rect = object2_surface.get_rect(topleft = (375, 700))
object3_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/horizontalplatform.png').convert()
object3_surface = pygame.transform.scale(object3_surface,(50, 100))
object3_rect = object3_surface.get_rect(topleft = (500, 650))
object4_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/verticalplatform.png').convert()
object4_surface = pygame.transform.scale(object4_surface, (125, 125))
object4_rect = object4_surface.get_rect(topleft = (700, 700))
object5_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/horizontalplatform.png').convert()
object5_surface = pygame.transform.scale(object5_surface, (50, 100))
object5_rect = object5_surface.get_rect(topleft = (500, 350))
object6_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/verticalplatform.png').convert()
object6_surface = pygame.transform.scale(object6_surface, (75, 50))
object6_rect = object6_surface.get_rect(topleft = (825, 300))
object7_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/verticalplatform.png').convert()
object7_surface = pygame.transform.scale(object7_surface, (75, 50))
object7_rect = object7_surface.get_rect(topleft = (200, 300))
object8_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/level_textures/verticalplatform.png').convert()
object8_surface = pygame.transform.scale(object8_surface, (75, 75))
object8_rect = object8_surface.get_rect(topleft = (1150,450))
obstacle_rects_level1 = [
    {
        "surf": wall_surface,
        "rect": wall_left_rect,
    }, 
    { 
        "surf": wall_surface,
        "rect": wall_right_rect, 
    },
    {
        "surf": wall_1_l1,
        "rect": wall_1_l1_rect, 
    },
    {
        "surf": wall_2_l1,
        "rect": wall_2_l1_rect, 
    },
    {
        "surf": wall_3_l1,
        "rect": wall_3_l1_rect
    },
    {
        "surf": wall_4_l1,
        "rect": wall_4_l1_rect
    },
    {
        "surf": wall_5_l1,
        "rect": wall_5_l1_rect
    },
    {
        "surf": wall_6_l1,
        "rect": wall_6_l1_rect
    },
    {
        "surf": wall_7_l1,
        "rect": wall_7_l1_rect
    }
] #List of all walls, ceilings, grounds, etc. in level 1. Define a List for every wall so that I don't have to create a separate if statement for each collision

#Define a list of dictionaries to contain dy info, rectangle info, and surface info, and y-value limits for each moving platforms
'''As of 4/23, I realize that this section of the code is a less efficient way of doing a class as this list basically functions as a class. However since I already
typed all this out I won't go back now to change it. If I were to start the project over I would create a platform class with all these traits'''
platform_data_level1= [
        {
            "rect": object1_rect, 
            "surf": object1_surface, 
            "dy": 0, 
            "min_y" : 500,
            "max_y" : 700
         }, 
         {
             "rect": object2_rect, 
             "surf": object2_surface,
             "dy": 0,
             "min_y": 500,
             "max_y": 700
        },
        {
            "rect": object3_rect,
            "surf": object3_surface,
            "dx" : 0,
            "min_x": 500,
            "max_x": 900
        },
        {
            "rect": object4_rect,
            "surf": object4_surface,
            "dy": 0,
            "min_y": 300,
            "max_y": 700
        },
        {
            "rect": object5_rect,
            "surf": object5_surface,
            "dx" : 0,
            "min_x": 500,
            "max_x": 900
        },
        {
            "rect": object6_rect,
            "surf": object6_surface,
            "dy": 0,
            "min_y": 250,
            "max_y": 300,
            "invert_gravity": True #I only need this in this single platform because just like a Class, unspecified tags will default to normal (False here)
        },
        {
            "rect": object7_rect,
            "surf": object7_surface,
            "dy" : 0,
            "min_y": 250,
            "max_y": 320
        },
        {
            "rect": object8_rect,
            "surf": object8_surface,
            "dy": 0,
            "min_y": 250,
            "max_y": 460
        }
    ]

#Dictionary for platforms in each level
level_platforms = {
    1: platform_data_level1,
    }

#Enemy Class
class Enemy:
    def __init__(self, surface, rect, max_x, min_x, max_y, min_y, invert_gravity, max_velocity):
        self.surface = surface
        self.rect = rect
        self.max_x = max_x
        self.min_x = min_x
        self.max_y = max_y
        self.min_y = min_y
        self.invert_gravity = invert_gravity
        self.max_velocity = max_velocity
        self.x_velocity = 1
        self.gravity = enemy_gravity
    def draw(self):
        screen.blit(self.surface, self.rect)
    def movement(self):
        self.rect.left += self.x_velocity
        if self.rect.right >= self.max_x:
            self.x_velocity *= -1
        if self.rect.left <= self.min_x:
            self.x_velocity *= -1
        if self.rect.bottom >= self.min_y:
            self.rect.bottom = self.min_y
        if self.rect.top <= self.max_y:
            self.rect.top = self.max_y
    def gravity_function(self):
        if self.invert_gravity == True:
            direction = -1
        else:
            direction = 1
        self.gravity +=  gravity_mag * gravity_direction * direction
        if self.gravity > self.max_velocity:
            self.gravity = self.max_velocity
        if self.gravity < -self.max_velocity:
            self.gravity = -self.max_velocity
        self.rect.y += self.gravity
    def kill_player(self):
        if self.rect.colliderect(player_rect):
            pygame.quit()
            exit()
    def walk_animation(self):
        global enemy_surface, enemy_index
        if self.gravity <= 0:
            enemy_index += 0.1
            if enemy_index >= len(upsidedown_enemy_walk):
                enemy_index = 0
            self.surface = upsidedown_enemy_walk[int(enemy_index)]
        if self.gravity >= 0:
            enemy_index += 0.1
            if enemy_index >= len(enemy_walk):
                enemy_index = 0
            self.surface = enemy_walk[int(enemy_index)]
        
#Create collectible class for coins
class Collectible:
    def __init__(self, surface, collected_surface, rect):
        self.surface = surface
        self.collected_surface = collected_surface
        self.rect = rect
        self.collected = False
    def draw(self):
        if self.collected == False:
            screen.blit(self.surface, self.rect)
        else:
            screen.blit(self.collected_surface, self.rect)
    def collect(self):
        global coins_collected #I want this variable to be accesible by things outside this class definition like my UI surface at the top left. Therefore I declare global
        if self.rect.colliderect(player_rect) and self.collected == False:
            coins_collected += 1
            self.collected = True

#Create Goal Class
class Goal:
    def __init__(self, surface, rect):
        self.surface = surface
        self.rect = rect
    def draw(self):
        screen.blit(self.surface, self.rect)
    def win(self):
        global game_state #put this here to ensure the following game_state is the same one that I defined at the top of this whole code I think
        global coins_collected #The statements with this condition are only necessary because this will be a one level game. These conditionals allow for a good and bad ending
        if self.rect.colliderect(player_rect) and coins_collected == 3:
            game_state += 2
        elif self.rect.colliderect(player_rect) and coins_collected != 3:
            game_state += 1
        

#Enemies
enemy_upsidedown_walk_1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/upsidedownenemywalk1.png').convert()
enemy_upsidedown_walk_1 = pygame.transform.scale(enemy_upsidedown_walk_1, (50,50))
enemy_upsidedown_walk_2 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/upsidedownenemywalk2.png').convert()
enemy_upsidedown_walk_2 = pygame.transform.scale(enemy_upsidedown_walk_2, (50,50))
upsidedown_enemy_walk = [enemy_upsidedown_walk_1, enemy_upsidedown_walk_2]
enemy_walk_1 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/enemywalk1.png').convert()
enemy_walk_1 = pygame.transform.scale(enemy_walk_1, (50, 50))
enemy_walk_2 = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/enemywalk2.png').convert()
enemy_walk_2 = pygame.transform.scale(enemy_walk_2, (50, 50))
enemy_walk = [enemy_walk_1, enemy_walk_2]
enemy_index = 0

enemy_surface = upsidedown_enemy_walk[enemy_index]

enemy1_rect = enemy_surface.get_rect(topleft = (275, 100))
enemy1 = Enemy(enemy_surface, enemy1_rect, 700, 275, 100, 300, True, 5)

#Coins
coin_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/coin.png').convert()
coin_surface = pygame.transform.scale(coin_surface, (25,25))
coin1_rect = coin_surface.get_rect(topleft = (475, 390))
coin2_rect = coin_surface.get_rect(topleft = (125, 250))
coin3_rect = coin_surface.get_rect(topleft = (1175, 200))
collected_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/coincollected.png').convert()
collected_surface = pygame.transform.scale(collected_surface, (25, 25))

coin1 = Collectible(coin_surface, collected_surface, coin1_rect)
coin2 = Collectible(coin_surface, collected_surface, coin2_rect)
coin3 = Collectible(coin_surface, collected_surface, coin3_rect)

#Goal
goal_surface = pygame.image.load('C:/Users/Jgome/python_decal/jordan_decal/final_project/entity_textures/flag.png').convert()
goal_surface = pygame.transform.scale(goal_surface, (50, 75))
goal1_rect = goal_surface.get_rect(topleft = (1300, 625))

goal1 = Goal(goal_surface, goal1_rect)

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

while True:
    current_platforms = level_platforms.get(game_state, []) #define variable so that I can easily access different level dictionaries depending on the level
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSLASH: #Debugging Each Game_State by pressing \
                game_state += 1
            elif event.key == pygame.K_w:
                gravity_direction *= -1
                object_gravity = 0
                enemy_gravity = 0
            elif event.key == pygame.K_d:
                x_gravity_direction *= -1
                object_x_gravity = 0
            
            '''This actually doesn't work because it doesn't reset the game state, just goes back one. When you go forward again to the state you were on, all the 
            positions remain how they were when you left it. If I wanted to reset a state, I would need to define a function that would place not only my player back 
            to their starting positon but also the platforms. This would be easily done if I had defined a platform class where I specified not only the info I did
            in the list below but also the starting position of the platform.'''
            #elif event.key == pygame.K_BACKSPACE: #Easily debug by going back a state
                #game_state -= 1




    keys = pygame.key.get_pressed() #global variable to detect key presses
    
    

    #Title Screen
    if game_state == 0:
        screen.blit(title_background_surface,(0,0))
        screen.blit(title_surface,(450,200))
        screen.blit(press_start_surface, (350, 600))
        if keys[pygame.K_SPACE]:
            game_state += 1

    #Level 1        
    elif game_state == 1:
        #Level Layout (REMEMBER THAT THE ORDER MATTERS!! THE FIRST SURFACE WILL GO IN THE VERY BACK AND THE REST OVERLAP)
        coins_collected_surface = small_font.render(f'Coins = {coins_collected}', False, (224, 224, 224))
        screen.blit(level1_background_surface, (0,0))
        screen.blit(ground_surface, (0,700))
        screen.blit(ground_surface,(0,0))
        for wall in obstacle_rects_level1:
            screen.blit(wall["surf"], wall["rect"])
        screen.blit(coins_collected_surface, (0, 0))
        

        #Gravity Set Up
        object_gravity += gravity_mag * gravity_direction
        max_velocity = 2 #Set a cap for gravity velocity so that it doesn't accumulate to super high levels
        if object_gravity > max_velocity:
            object_gravity = max_velocity
        if object_gravity < -max_velocity:
            object_gravity = -max_velocity

        object_x_gravity += x_gravity_mag * x_gravity_direction
        max_x_velocity = 2
        if object_x_gravity > max_x_velocity:
            object_x_gravity = max_x_velocity
        if object_x_gravity < -max_x_velocity:
            object_x_gravity = -max_x_velocity
        
        #Gravity Affected Obstacles
        for platform in current_platforms:
            if "dy" in platform: #Separate veritcal moving platforms from horizontal ones
                platform_gravity = object_gravity
                if platform.get("invert_gravity"): #The .get command functions similarly to using if "dy" in platform and then checking 
                    #what the value is. Also if there is no invert_gravity attribute (like all the rest of my platforms, the .get() wont crash while the other syntax will)
                    platform_gravity *= -1
                
                platform["dy"] = platform_gravity
                platform["rect"].y += platform["dy"]

                #Lock position between min_y and max_y
                if platform["rect"].top >= platform["max_y"]:
                    platform["rect"].top = platform["max_y"]
                if platform["rect"].top <= platform["min_y"]:
                    platform["rect"].top = platform["min_y"]
            if "dx" in platform:
                platform["dx"] = object_x_gravity
                platform["rect"].x += platform["dx"]
                #Same thing for min_x and max_x for horizontally moving platforms
                if platform["rect"].left >= platform["max_x"]:
                    platform["rect"].left = platform["max_x"]
                if platform["rect"].left <= platform["min_x"]:
                    platform["rect"].left = platform["min_x"]

            #Draw each platform on the screen
            screen.blit(platform["surf"], platform["rect"])

        #Putting the enemy in
        enemy1.draw()
        enemy1.walk_animation()
        enemy1.movement()
        enemy1.gravity_function()
        enemy1.kill_player()
        
        #Implementing the coins (3)
        coin1.draw()
        coin1.collect()
        coin2.draw()
        coin2.collect()
        coin3.draw()
        coin3.collect()

        #Implementing the Goal
        goal1.draw()
        goal1.win()

        #Player Manipulation
        
        player_animation()
        screen.blit(player_surface, player_rect)
        player_rect.left += player_velocity #Player is always moving
        
        player_on_platform = False #check if player is on platform
        
        for object in obstacle_rects_level1:
            if player_rect.colliderect(object["rect"]):
                player_velocity *= -1 #change direction when player hits a wall
            if (
                player_rect.bottom <= object["rect"].top 
                and player_rect.bottom + player_gravity >= object["rect"].top 
                and player_rect.right > object["rect"].left 
                and player_rect.left < object["rect"].right
                ):
                player_rect.bottom = object["rect"].top
                player_on_platform = True
                player_gravity = 0
        
        for platform in current_platforms:
            if "dx" in platform:
                rect = platform["rect"]
                dx = platform["dx"]
                rect.x += dx

                if (
                    player_rect.right >= rect.left
                    and player_rect.left < rect.left
                    and player_rect.bottom > rect.top
                    and player_rect.top < rect.bottom
                    ): #the first two conditions check if the player's right edge is touching any rect's left edge
                    #the second two conditions ensure the player is on the same horizontal plane as the rect, this will prevent the player from colliding with it when they are above or below it
                    player_rect.right = rect.left
                    player_velocity *= -1
                elif (
                    player_rect.left <= rect.right
                    and player_rect.right > rect.left
                    and player_rect.bottom > rect.top
                    and player_rect.top < rect.bottom
                    ):
                    player_rect.left = rect.right
                    player_velocity *= -1
            if "dy" in platform:
                rect = platform["rect"]
                dy = platform["dy"]

                rect.y += dy

                if (
                    abs(player_rect.bottom - rect.top) <= 8 
                    and player_rect.right > rect.left 
                    and player_rect.left < rect.right
                    ):
                    player_on_platform = True
                    player_gravity = 0
                    player_rect.bottom = rect.top
                    player_rect.y += dy  #carry the player with the platform
                elif (
                    player_rect.right >= rect.left
                    and player_rect.left < rect.left
                    and player_rect.bottom > rect.top
                    and player_rect.top < rect.bottom
                    and abs(player_rect.bottom - rect.top) > 10 #relax condition by ten pixels to allow for a tiny bit of colllision so player can walk over these platforms
                    ): 
                    player_rect.right = rect.left
                    player_velocity *= -1
                elif (
                    player_rect.left <= rect.right
                    and player_rect.right > rect.left
                    and player_rect.bottom > rect.top
                    and player_rect.top < rect.bottom
                    and abs(player_rect.bottom - rect.top) > 10
                    ):
                    player_rect.left = rect.right
                    player_velocity *= -1
            
        if not player_on_platform:
            player_gravity += gravity_mag

        
        if player_gravity > max_velocity:
            player_gravity = max_velocity
        if player_gravity < -max_velocity:
            player_gravity = -max_velocity
        
        player_rect.y += player_gravity

        if player_rect.bottom >= 700:
            player_rect.bottom = 700 #Player doesnt fall below screen
        if player_rect.top <= 100:
            player_rect.top = 100 #Player Doesnt fall above screen
       

        

        

    #bad ending        
    elif game_state == 2:
        screen.blit(title_background_surface,(0,0))
        screen.blit(bad_ending_surface,(300,200))
        screen.blit(bad_ending_message, (350, 600))
    #good ending   
    elif game_state == 3:
        screen.blit(title_background_surface,(0,0))
        screen.blit(good_ending_surface,(300,200))
        screen.blit(good_ending_message, (350, 600))

    #thanks   
    else:
        screen.blit(title_background_surface,(0,0))
        screen.blit(thanks,(450,200))
        
        
    pygame.display.update()
    clock.tick(60)


