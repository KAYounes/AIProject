
# ###> Imports
# import pygame, sys, random
# from pygame.constants import QUIT,KEYDOWN,K_UP, K_RIGHT, K_DOWN, K_LEFT, USEREVENT
# from pygame import init, quit, Vector2

# ###> Setting up pygame
# init()
# pygame.mixer.pre_init(44100, -16, 2, 512) #! handles a lot of things. Used here to remove delay before sound plays
# clock = pygame.time.Clock()

# hor, ver = 1000, 800
# pygame.display.set_caption("CAPTION")
# # pygame.display.set_icon(pygame.image.load(""))
# screen = pygame.display.set_mode((hor, ver))
# aFont = pygame.font.Font(None, 50)
# def mlt(text):
#     for i, line in enumerate(text):
#         surf = aFont.render(line, True, (255, 255, 255))
#         screen.blit(surf, (0, 100 * (i + 1)))
# #> Main Loop
# #>
# loop = True
# while(loop):
    
#     #$ Event Loop
#     for event in pygame.event.get():        
#         #$ QUIT event
#         if (event.type == QUIT):
#             loop = False
#     mlt(["abc", "123"])
#     #$ Update Display
#     pygame.display.update()
#     clock.tick(60)

# quit()
# sys.exit()

c = 1
d = 1
e = 3

b = c + d < e

print(b)