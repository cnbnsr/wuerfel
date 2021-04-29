import pygame
# import sys
import random

pygame.init()
FELD = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Wuerfel")

BLAU = (0, 0, 255)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)

P1 = (160, 160)
P2 = (60, 60)
P3 = (60, 160)
P4 = (260, 60)
P5 = (60, 260)
P6 = (260, 160)
P7 = (260, 260)

mainloop = True
print("Beliebige Taste drücken zum Würfeln")
print("[ESC] beendet das Spiel")

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            mainloop = False
        if event.type == pygame.KEYDOWN:
            FELD.fill(SCHWARZ)
            ZAHL = random.randrange(1, 7)
            print(ZAHL)
            if ZAHL == 1:
                pygame.draw.circle(FELD, WEISS, P1, 40)
            if ZAHL == 2:
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)
            if ZAHL == 3:
                pygame.draw.circle(FELD, WEISS, P1, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
            if ZAHL == 4:
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)
            if ZAHL == 5:
                pygame.draw.circle(FELD, WEISS, P1, 40)
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)
            if ZAHL == 6:
                pygame.draw.circle(FELD, WEISS, P2, 40)
                pygame.draw.circle(FELD, WEISS, P3, 40)
                pygame.draw.circle(FELD, WEISS, P4, 40)
                pygame.draw.circle(FELD, WEISS, P5, 40)
                pygame.draw.circle(FELD, WEISS, P6, 40)
                pygame.draw.circle(FELD, WEISS, P7, 40)
    pygame.display.update()
pygame.quit()
