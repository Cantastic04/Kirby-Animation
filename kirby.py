print("LOADING...")

# Imports
import pygame
import math
import random


# Screen settings
WIDTH = 1280
HEIGHT = 720
TITLE = "Clifford's Awesome Drawing (featuring Kirby)"
FPS = 60


# Initialize game engine
pygame.init()


# Make the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Colors
RED = (255, 0, 0)
GREEN = (5, 230, 35)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (252, 151, 204)
YELLOW = (255, 201, 54)
SKYBLUE = (98, 159, 245)
DARKPURPLE = (52, 0, 90)
CLOUDYNITE = (173, 189, 219)


# Fonts
FONT_SM = pygame.font.Font(None, 48)
FONT_MD = pygame.font.Font('fonts/mario_word.ttf', 64)
FONT_LG = pygame.font.Font(None, 96)


# Images
flower_img = pygame.image.load('images/flower.png').convert_alpha()
ministar_img = pygame.image.load('images/ministar.png').convert_alpha()
bfly_img = pygame.image.load('images/bfly.png').convert_alpha()
sungrass_img = pygame.image.load('images/sungrass.png').convert_alpha()
nightgrass_img = pygame.image.load('images/nightgrass.png').convert_alpha()
starrod_img = pygame.image.load('images/starrod.png').convert_alpha()
milk_img = pygame.image.load('images/milk.png').convert_alpha()
angry_img = pygame.image.load('images/angry.png').convert_alpha()
tomato_img = pygame.image.load('images/maxim_tomato.png').convert_alpha()
cookie_img = pygame.image.load('images/cookie.png').convert_alpha()


# Sounds
warpstar_snd = pygame.mixer.Sound('sounds/warpstar.mp3')
boing_snd = pygame.mixer.Sound('sounds/boing.ogg')

# Text
def write_kirby(text, color, x, y):
    text1 = FONT_MD.render(text, True, color)
    screen.blit(text1, [x, y])


# Sounds
def play_boing():
    boing_snd.play()


def play_hi():
    kirby_hi_snd = pygame.mixer.Sound('sounds/kirby_hi.mp3')


# Music
rainbow_mus = 'bg_music/rain_bow.mp3'
veggietime_mus = 'bg_music/vegg_valley.mp3'


def play_night_day(is_daytime):
    if is_daytime:
        pygame.mixer.music.load(veggietime_mus)
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load(rainbow_mus)
        pygame.mixer.music.play(-1)
    

# Drawing Functions
def upload_flowers(x, y):
    y = y
    for x in range (x, WIDTH, 100):
        screen.blit(flower_img, [x, y])


def upload_ministars(ministar_locs):
    for loc in ministar_locs:
        x, y = loc
        screen.blit(ministar_img, [x, y])


def upload_bfly(x, y):
    screen.blit(bfly_img, [x, y])
       

def draw_sky(is_daytime):
    if is_daytime:
        screen.fill(SKYBLUE)
    else:
        screen.fill(DARKPURPLE)


def draw_cloud(x, y):
    if is_daytime:
        cloud_color = WHITE
    else:
        cloud_color = CLOUDYNITE
        
    pygame.draw.ellipse(screen, cloud_color, [x, y+10, 60, 30],)
    pygame.draw.ellipse(screen, cloud_color, [x+30, y, 40, 30],)
    pygame.draw.ellipse(screen, cloud_color, [x+40, y+15, 90, 30],)
    pygame.draw.ellipse(screen, cloud_color, [x+60, y, 40, 30],)


def draw_grass(x, y):
    if is_daytime:
        screen.blit(sungrass_img, [x, y])
    else:
        screen.blit(nightgrass_img, [x, y])


def draw_kirby(x, y):
    #StarRod / Milk
    if is_daytime:
        screen.blit(starrod_img, [x+130, y-240])
    else:    
        screen.blit(milk_img, [x+160, y-210])


    #Warp Star                              1   2A  3B  4C  5D  6   7D  8C  9B  10A
    pygame.draw.polygon(screen, YELLOW, [[x+mx,y+my],         [x+80+mx,y+80+my],   [x+230+mx,y+80+my],
                                         [x+110+mx,y+150+my], [x+170+mx,y+240+my], [x+mx,y+180+my],
                                         [x-170+mx,y+240+my], [x-110+mx,y+150+my], [x-230+mx,y+80+my],
                                         [x-80+mx,y+80+my]])


    #Kirby Body 
    pygame.draw.ellipse(screen, RED, [x+130, y+190, 90, 110],)
    pygame.draw.ellipse(screen, PINK, [x, y, 250, 250],)
    pygame.draw.ellipse(screen, RED, [x+20, y+150, 90, 110],)
    pygame.draw.ellipse(screen, PINK, [x-50, y+30, 100, 100],)
    pygame.draw.ellipse(screen, PINK, [x+150, y-30, 100, 100],)


    #Kirby Face
    if is_happy:
        pygame.draw.ellipse(screen, RED, [x+130, y+105, 50, 70],)
        pygame.draw.rect(screen, PINK, [x+130, y+105, 60, 30],)
        
        pygame.draw.ellipse(screen, BLACK, [x+115, y+50, 25, 70],)     
        pygame.draw.ellipse(screen, BLACK, [x+165, y+50, 25, 70],)
        pygame.draw.ellipse(screen, BLUE, [x+118, y+53, 18, 60],)
        pygame.draw.ellipse(screen, BLUE, [x+168, y+53, 18, 60],)
        
        pygame.draw.ellipse(screen, BLACK, [x+117, y+50, 20, 50],)
        pygame.draw.ellipse(screen, BLACK, [x+167, y+50, 20, 50],)
        pygame.draw.ellipse(screen, BLACK, [x+117, y+80, 20, 20],)
        pygame.draw.ellipse(screen, BLACK, [x+167, y+80, 20, 20],)
        
        pygame.draw.ellipse(screen, WHITE, [x+120, y+59, 15, 30],)
        pygame.draw.ellipse(screen, WHITE, [x+170, y+58, 15, 30],)
    else:
        screen.blit(angry_img, [x + 55, y - 55])        


    #Tomato / Cookie
    if is_daytime:
        screen.blit(tomato_img, [x-130, y-50])
    else:
        screen.blit(cookie_img, [x-130, y-50])




#Initial State
is_daytime = True
is_happy = True


bfly_x, bfly_y = -100, 40
kirby_x, kirby_y = 600, 250
grass_x, grass_y = 0, 400
flowers_x, flowers_y = 5, 325
mx = 120
my = 120

show_bfly = False
show_hi = False

num_ministars = 30
ministar_locs = []

for _ in range(num_ministars):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, 250)
    ministar_locs.append([x, y])


cloud_locs = []
num_clouds = 4
cloudy_locs = []
num_cloudys = 5
cloudyy_locs = []
num_cloudyys = 6


for _ in range(num_clouds):
    x = random.randrange(0,WIDTH)
    y = random.randrange(0,222)
    cloud_locs.append([x,y])

for _ in range(num_cloudys):
    x = random.randrange(0,WIDTH)
    y = random.randrange(0,222)
    cloudy_locs.append([x,y])
    
for _ in range(num_cloudyys):
    x = random.randrange(0,WIDTH)
    y = random.randrange(0,222)
    cloudyy_locs.append([x,y])

# Game loop
play_night_day(is_daytime)


running = True


while running:
    # Event handling
    '''This is where we react to key presses, mouse clicks, etc.'''
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                is_happy = not is_happy


            elif event.key == pygame.K_SPACE:
                is_daytime = not is_daytime

                play_night_day(is_daytime)
                play_boing()


    #Movement
    if grass_x < -1280:
        grass_x = 0
    else:
        grass_x -=7


    if flowers_x < -84:
        flowers_x = 5
    else:
        flowers_x -=7


    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        kirby_x -= 10
    elif pressed[pygame.K_RIGHT]:
        kirby_x += 10
    if pressed[pygame.K_UP]:
        kirby_y -= 10
    elif pressed[pygame.K_DOWN]:
        kirby_y += 10
    

    # Game logic
    '''This is where we check for collisions, update coordinates of moving objects, etc.)''' 
    if kirby_x < 130:
        kirby_x = 130
    elif kirby_x > WIDTH - 370:
        kirby_x = WIDTH - 370
    if kirby_y < 60:
        kirby_y = 60
    elif kirby_y > 560 - 230:
        kirby_y = 560 - 230
        

    r = random.randrange(0, 500)
    if r == 0:
        show_bfly = True
        warpstar_snd.play()
        
        
    if show_bfly:
        bfly_x += random.choice([-5, 5, 15])
        bfly_y += random.choice([-5, 0, 5])
    else:
        show_bfly = False

    if bfly_x > WIDTH:
        warpstar_snd.stop()

    r = random.randrange(0, 1000)
    if r == 0:
        show_hi = False
    else:
        show_hi = False
    if show_hi:
        play_hi()


    for loc in cloud_locs:
        loc[0] -=3
        if loc[0] < -150:
            loc[0] = WIDTH
            loc[1] = random.randrange(10,180)

    for loc in cloudy_locs:
        loc[0] -=4   
        if loc[0] < -150:
            loc[0] = WIDTH
            loc[1] = random.randrange(20,190)
            
    for loc in cloudyy_locs:
        loc[0] -=5   
        if loc[0] < -150:
            loc[0] = WIDTH
            loc[1] = random.randrange(30,200)


    # Drawing code
    '''The picture is assembled in the computers memory'''
    
    draw_sky(is_daytime)

    if is_daytime:
        draw_sky(is_daytime)
    else:
        upload_ministars(ministar_locs)
    
    upload_flowers(flowers_x, flowers_y)
    draw_grass(grass_x, grass_y)

    for loc in cloud_locs:
        draw_cloud(loc[0], loc[1])
    for loc in cloudy_locs:
        draw_cloud(loc[0], loc[1])    
    for loc in cloudyy_locs:
        draw_cloud(loc[0], loc[1])

    write_kirby("KIRBY!", PINK, 575, 160)

    if show_bfly:
        upload_bfly(bfly_x, bfly_y)

    draw_kirby(kirby_x, kirby_y)


    # Update screen
    '''
    The update() function takes the picture from the computer's
    memory buffer and actually puts it on the screen.
    '''
    pygame.display.update()


    # Limit refresh rate of game loop
    '''
    The game loop will pause for a bit here so that the screen
    refreshes at the desired rate.
    '''
    clock.tick(FPS)


# Close window and quit
pygame.quit()
