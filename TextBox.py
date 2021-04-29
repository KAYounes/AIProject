import pygame
from pygame import Vector2

clock = pygame.time.Clock()
class TextBox:
    def __init__(self, x, y):
        self.center = Vector2(x, y)
        self.text = '1'
        self.width = 45
        self.hight = 28
        self.color = (255, 255, 255)

        self.rect = pygame.Rect(self.center.x, self.center.y, self.width, self.hight)
        self.rect.center = self.center
        self.font = pygame.font.Font(None, 30)
        

    def takeInput(self, surface, screen):
        self.color = (162, 237, 50)
        loop = True
        while(loop):
            
            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    loop = False
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if not(self.rect.collidepoint(pygame.mouse.get_pos())):
                        self.color = (255, 255, 255)
                        print(int(self.text) + 1, self.text)
                        return int(self.text)
                if (event.type == pygame.KEYDOWN):

                    if(event.key == pygame.K_RETURN):
                        self.color = (255, 255, 255)
                        print(int(self.text) + 1, self.text)
                        return int(self.text)
                        loop = False

                    elif(event.key == pygame.K_BACKSPACE):
                        self.text = self.text[:-1]

                    elif(event.key >= pygame.K_0 and event.key <= pygame.K_9 and len(self.text) < 3):

                        if (len(self.text) == 0 and event.key == pygame.K_0):
                            continue
                        self.text += event.unicode

            self.render(surface)
            clock.tick(50)
            screen.blit(surface, (0,0))
            pygame.display.update()

    def render(self, surface):
        font_surface = self.font.render(self.text, True, (0, 0, 0))
        font_rect = font_surface.get_rect()
        font_rect.left = self.rect.left + 5
        font_rect.centery = self.rect.centery
        pygame.draw.rect(surface, self.color, self.rect) #206, 219, 221
        pygame.draw.rect(surface, (0,0,0), self.rect, 3)
        surface.blit(font_surface, font_rect)