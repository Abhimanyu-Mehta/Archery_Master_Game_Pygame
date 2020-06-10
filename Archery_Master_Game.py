import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

background_img = pygame.image.load('grass_background.png')
background = pygame.transform.scale(background_img, (800, 600))


pygame.display.set_caption('Archery Master')

icon = pygame.image.load('icon_target.png')
pygame.display.set_icon(icon)

mixer.music.load('background.wav')
mixer.music.play(-1)

target = pygame.image.load('target.png')
targetx = 336
targety = 70
targetx_change = 3
targety_change = 0

bow = pygame.image.load('crossbow.png')
bowX = 336
bowy = 490
bowx_change = 0
bowy_change = 0

arrow = pygame.image.load('arrow.png')
arrowX = 0
arrowY = 490
arrowX_change = 0
arrowY_change = -6
arrow_state = "ready"


def print_target():
    screen.blit(target, (targetx, targety))


def print_bow():
    screen.blit(bow, (bowX, bowy))


def print_arrow(x, y):
    global arrow_state
    arrow_state = "fire"
    screen.blit(arrow, (x, y + 10))


def cheak_collision(targetX, targetY, arrowX, arrowY):
    distance = math.sqrt((math.pow(targetX - arrowX, 2) + (math.pow(targetY - arrowY, 2))))
    if distance <= 27:
        return True
    else:
        return False


score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def print_score(x, y):
    score_print = score_font.render("Score:" + str(score), True, (255, 255, 255))
    screen.blit(score_print, (x, y))


life = 3
life_font = pygame.font.Font('freesansbold.ttf', 32)
lifeX = 670
lifeY = 10


def print_life(x, y):
    life_print = score_font.render("Lives:" + str(life), True, (255, 255, 255))
    screen.blit(life_print, (x, y))


game_over = pygame.font.Font('freesansbold.ttf', 64)
fontX = 200
fontY = 270


def print_game_over():
    game_over_ = game_over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_, (fontX, fontY))


running = True

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bowx_change = 4
            elif event.key == pygame.K_LEFT:
                bowx_change = -4
            elif event.key == pygame.K_SPACE:
                if arrow_state == "ready":
                    bow_sound = mixer.Sound('bow_sound.wav')
                    bow_sound.play()
                    arrowX = bowX
                    print_arrow(arrowX, arrowY)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                bowx_change = 0
            elif event.key == pygame.K_LEFT:
                bowx_change = 0

    if targetx >= 736:
        targetx = 736
        targetx_change = -3

    elif targetx <= 0:
        targetx = 0
        targetx_change = 3

    if bowX >= 723:
        bowX = 723

    elif bowX <= 0:
        bowX = 0

    collision = cheak_collision(targetx, targety, arrowX, arrowY)

    if collision:
        arrowY = 490
        arrow_state = "ready"
        target_sound = mixer.Sound('target_hit.wav')
        target_sound.play()
        targetx = random.randint(0, 736)
        targety = random.randint(70, 140)
        score += 1

    elif life == 0:
        arrowY = 0
        print_game_over()

    elif arrowY <= 0:
        arrowY = 490
        arrow_state = "ready"
        life -= 1

    elif arrow_state is "fire":
        print_arrow(arrowX, arrowY)
        arrowY += arrowY_change

    print_life(lifeX, lifeY)
    print_score(textX, textY)
    targetx += targetx_change
    print_target()
    bowX += bowx_change
    print_bow()
    pygame.display.update()
