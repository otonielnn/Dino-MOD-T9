import pygame
import os

pygame.init()
pygame.mixer.init()

# Global Constants
TITLE = "Monster Hunter Adventures"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

SHIELD_SOUND= pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/dead.wav'))
HAMMER_SOUND= pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/HammerSound.wav'))
JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/jump.wav'))
END_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/dead.wav'))
HIT_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/hit.wav'))
BACKGROUND_SOUND = pygame.mixer.music.load(os.path.join(IMG_DIR, 'Sounds/moonleap.mp3'))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botrun1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botrun2.png")).convert_alpha(),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botrun1shield.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botrun2shield.png")).convert_alpha(),
]


RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botrun1hammer.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botrun2hammer.png")).convert_alpha(),
]


JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/botjump.png")).convert_alpha()
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/botjumpshield.png")).convert_alpha()
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/botjumphammer.png")).convert_alpha()

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botduck1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botduck2.png")).convert_alpha(),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botduck1shield.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botduck2shield.png")).convert_alpha(),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botduckhammer1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/botduckhammer2.png")).convert_alpha(),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/smallpig1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/smallpig2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/smallpig3.png")).convert_alpha(),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/largepig2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/largepig2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/largepig3.png")).convert_alpha(),
]

BIRD_SPRITE = pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird.png")).convert_alpha()
BIRD = []
for i in range(4):
    img = BIRD_SPRITE.subsurface((i * 45, 0),(45, 30))
    img = pygame.transform.scale(img, (45*2, 30*2))
    BIRD.append(img)

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png')).convert_alpha()
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png')).convert_alpha()
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png')).convert_alpha()
DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/botdead.png")).convert_alpha()

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png')).convert_alpha()
BG2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax.png')).convert_alpha()
BG3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax2.png')).convert_alpha()
BG4 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax3.png')).convert_alpha()
BG5 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax4.png')).convert_alpha()

MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/MenuGame.png')).convert_alpha()

DEFAULT_TYPE = "default"

FONT_STYLE = (os.path.join(IMG_DIR, 'Fonts\Pix.ttf'))

SHIELD_TYPE = 'Poder do Deuses'

HAMMER_TYPE = 'Martelo do Thor'
