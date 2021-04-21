import pygame
from pygame import Vector2

clock = pygame.time.Clock()
class TextBox:
    def __init__(self, x, y, width = 30, hight = 30):
        self.center = Vector2(x, y)
        self.text = '1'
        self.width = width
        self.hight = hight

        self.rect = pygame.Rect(self.center.x, self.center.y, width, hight)
        self.rect.center = self.center
        self.font = pygame.font.Font(None, 30)
        

    def takeInput(self, screen, g):
        loop = True
        while(loop):
            
            screen.fill( (255, 255, 255))

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    loop = False
                # print(event)
                if (event.type == pygame.KEYDOWN):
                    # print("KEYFDOWN")
                    if(event.key == pygame.K_RETURN):
                        # print("ENTER")
                        loop = False
                    elif(event.key == pygame.K_BACKSPACE):
                        self.text = self.text[:-1]
                    elif(event.key >= pygame.K_0 and event.key <= pygame.K_9 and len(self.text) < 3):
                        if (len(self.text) == 0 and event.key == pygame.K_0):
                            continue
                        self.text += event.unicode

            self.render(screen)
            g.draw_nodes()
            # print(self.text)
            clock.tick(50)
            pygame.display.update()

    def render(self, screen):
        font_surface = self.font.render(self.text, True, (0, 0, 255))
        font_rect = font_surface.get_rect()
        font_rect.left = self.rect.left + 5
        font_rect.centery = self.rect.centery
        pygame.draw.rect(screen, (255,0,0), self.rect)
        self.rect.width = max(font_surface.get_width() + 10, self.width)
        screen.blit(font_surface, font_rect)