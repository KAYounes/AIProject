import pygame
from pygame import Vector2

clock = pygame.time.Clock()
class TextBox:
    def __init__(self, x, y, width = 42, hight = 28, color = (255, 255, 255), active = ((162, 237, 50)), allowZero = False, border = True):
        self.center = Vector2(x, y)
        self.text = '1'
        self.width = width
        self.hight = hight
        self.main_color = color
        self.active_color = active
        self.color = color
        self.allowZero = allowZero
        self.border = border

        self.rect = pygame.Rect(self.center.x, self.center.y, self.width, self.hight)
        self.rect.center = self.center
        self.font = pygame.font.Font(None, 30)
        

    def takeInput(self, surface, screen, font):
        #> BUG
            #solved #$ if textbox is empty (no text) and then deactivated, program crashes since int("") is not valid
        self.color = self.active_color
        loop = True
        while(loop):
            
            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    self.color = self.main_color
                    loop = False
                    return int(self.text)

                if(event.type == pygame.MOUSEBUTTONDOWN and self.text != ""):
                    if not(self.rect.collidepoint(pygame.mouse.get_pos())):
                        self.color = self.main_color
                        # print(int(self.text) + 1, self.text)
                        loop = False
                        return int(self.text)

                if (event.type == pygame.KEYDOWN):

                    if(event.key == pygame.K_RETURN and self.text != ""):
                        self.color = self.main_color
                        # print(int(self.text) + 1, self.text)
                        loop = False
                        return int(self.text)

                    elif(event.key == pygame.K_BACKSPACE):
                        self.text = self.text[:-1]

                    elif(event.key >= pygame.K_0 and event.key <= pygame.K_9 and len(self.text) < 3):
                        if not(self.allowZero):
                            if (len(self.text) == 0 and event.key == pygame.K_0):
                                continue
                        self.text += event.unicode

            self.render(surface, font)

            clock.tick(50)
            screen.blit(surface, (0,0))
            pygame.display.update()

    def render(self, surface, font):
        font_surface = font.render(self.text, True, (0, 0, 0))

        font_rect = font_surface.get_rect()
        # font_rect.left = self.rect.left + 5
        font_rect.center = self.rect.center

        pygame.draw.rect(surface, self.color, self.rect) #206, 219, 221
        if(self.border):
            pygame.draw.rect(surface, (0,0,0), self.rect, 3)
        surface.blit(font_surface, font_rect)