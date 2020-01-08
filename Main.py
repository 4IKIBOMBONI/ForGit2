import pygame
import os
import random
import sys
pygame.init()
FPS = 10

pygame.init()
image = pygame.Surface([100, 100])
size = 1000, 800
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

def load_image(name, colorkey=0, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == 0:
            color_key = image.get_at((0, 0))
            pygame.display.flip()
        image.set_colorkey(color_key)
    elif colorkey == 2:
        pass
    else:
        image = image.convert_alpha()

    return image


def start_screen():
    WIDTH = 1000
    HEIGHT = 800
    curpos = [0, 0]
    cursor = load_image("arrow.png")
    cursor = pygame.transform.scale(cursor, (50, 50))
    intro_text = ["Здравствуйте!", "",
                  "Для начала игры",
                  "Нажмите любую клавишу"]

    fon = pygame.transform.scale(load_image('fon.jpg', 1), (WIDTH, HEIGHT))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    running = True
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


    while running:
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 388 and event.pos[0] < 577 and event.pos[1] < 711 and event.pos[1] > 431:
                return  # начинаем игру
            elif event.type == pygame.MOUSEMOTION:
                curpos = event.pos
        screen.blit(cursor, curpos)
        pygame.display.flip()
        clock.tick(FPS)


image = load_image("creature.png", 0)
image2 = load_image("crosh.png", 0)
image2 = pygame.transform.scale(image2, (200, 200))
running = True
pos = [100, 100]
pos2 = [500, 100]
motion = 0


def crosh2():
    global pos2
    ch = random.choice(['DOWN', 'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP', 'LEFT', 'RIGHT'])
    if pos2[0] < 1000 and pos2[1] < 500 and pos2[0] > 0 and pos2[1] > 0:
        if ch == 'DOWN':
            pos2 = [pos2[0], pos2[1] + 15]
            screen.blit(image2, pos2)

        elif ch == 'UP':
            pos2 = [pos2[0], pos2[1] - 15]
            screen.blit(image2, pos2)

        elif ch == 'LEFT':
            pos2 = [pos2[0] - 15, pos2[1]]
            screen.blit(image2, pos2)

        elif ch == 'RIGHT':
            pos2 = [pos2[0] + 15, pos2[1]]
            screen.blit(image2, pos2)


    elif pos2[0] >= 1000 or pos2[1] >= 500:
        pos2 = [pos2[0] - 20, pos2[1] - 20]
    elif pos2[0] <= 0 or pos2[1] <= 0:
        pos2 = [pos2[0] + 20, pos2[1] + 20]
    else:
        pos2 = [pos2[0] + 20, pos2[1] + 20]
    screen.blit(image2, pos2)
    clock.tick(FPS)



start_screen()
fon = pygame.transform.scale(load_image('secondfon.jpg', 1), (1000, 800))


while running:
    screen.blit(fon, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                motion = 'DOWN'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                motion = 'UP'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                motion = 'LEFT'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                motion = 'RIGHT'
        if event.type == pygame.KEYUP:
            motion = 0

    crosh2()

    if motion == 'DOWN':
        pos = [pos[0], pos[1] + 5]
    elif motion == 'UP':
        pos = [pos[0], pos[1] - 5]
    elif motion == 'LEFT':
        pos = [pos[0] - 5, pos[1]]
    elif motion == 'RIGHT':
        pos = [pos[0] + 5, pos[1]]

    screen.blit(image, pos)


    pygame.display.flip()