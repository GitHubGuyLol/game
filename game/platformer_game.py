import pygame, json

from pygame import key
from pygame.constants import RESIZABLE

clock = pygame.time.Clock()# set up the clock

pygame.display.set_caption("Slime Adventure")# window name
WINDOW_WIDTH, WINDOW_HEIGHT = (600, 400)# set up window size
real_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), RESIZABLE)# initiate screen
screen = real_screen.copy()

def load_map(path):
    with open(path + ".json", "r") as f:
        game_map = json.load(f)
    return game_map

PLAYER_WIDTH, PLAYER_HEIGHT = (50,50)
player_img = pygame.transform.scale(pygame.image.load("mygame/player.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
TILE_SIZE = 25
player_img.set_colorkey((213, 201, 255))
grass_img = pygame.transform.scale(pygame.image.load("mygame/grass.png"), (TILE_SIZE, TILE_SIZE))
dirt_img = pygame.transform.scale(pygame.image.load("mygame/dirt.png"), (TILE_SIZE, TILE_SIZE))

spd = 4
gravity = 0
gravity_acceleration = 0.5
def load_map():
    with open("mygame/map.json", "r") as f:
        game_map = json.load(f)
    return game_map
def draw(player):
    screen.fill((255,255,255))
    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == "1":
                screen.blit(dirt_img, (x*TILE_SIZE, y*TILE_SIZE))
            if tile == "2":
                screen.blit(grass_img, (x*TILE_SIZE, y*TILE_SIZE))
            if tile != "0":
                tile_rects.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    screen.blit(player_img, (player.x, player.y))
    pygame.display.update()
    return tile_rects
def handle_player_movement(keys, gravity, tiles):
    if keys_pressed[pygame.K_d]:
        player.x += spd
    if keys_pressed[pygame.K_a]:
        player.x -= spd
    if keys_pressed[pygame.K_SPACE]:
        gravity = -10
    player.y += gravity
    gravity += gravity_acceleration
    if gravity > 10:
        gravity = 10

    for tile in tiles:
        if player.colliderect(tile):
            if abs(tile.top - player.bottom) < 10:
                gravity = 0
    return gravity

game_map = load_map()
run = True
player = pygame.Rect(300-PLAYER_WIDTH/2, 50, PLAYER_WIDTH, PLAYER_HEIGHT)
while run:# game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    keys_pressed = pygame.key.get_pressed()
    tile_rects = draw(player)
    gravity = handle_player_movement(keys_pressed, gravity, tile_rects)
    real_screen.blit(pygame.transform.scale(screen, real_screen.get_rect().size), (0, 0))
    clock.tick(60)# maintain 60 fps