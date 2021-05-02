
###> Imports
import pygame, sys, random


class Button:
    """
     #$ can change font type and size
     #$ change button text
     #$ change text color
     #$ change button bg color
     #$ change button coordinates, measured from top left
     #$ change button size
     #$ change border color
     #$ change border width, border width must be > 0 to apply
     #$ change button radius, affects border as well
     #$ change padding, could change left, right, top, and bottom padding independently

     #$ call render after any change or a group of changes to apply changes, called once only after a change(s)
     #$ call draw_btn() to draw button on screen, border is drawn in this function not in render()
     #$ call change_padding() to change padding, padding is applied in the render function

     #$ does not support transparent buttons
    """
    surfaceX = 0
    surfaceY = 0

    def __init__(self, font_size = 18):
    #$ text
        self.font_size = font_size
        self.bold_font = pygame.font.Font("RobotoCondensed-Bold.ttf", font_size)  #$ font object        
        self.regular_font = pygame.font.Font("RobotoCondensed-Regular.ttf", font_size)  #$ font object        
        self.btn_text = "Text"                  #$ text shown on button
        self.txt_color = (0, 0, 0)        #$ text color
        self.bold = False

    #$ Button color/coordinates/Size
        self.btn_bg = (227, 227, 227)               #$ button background color
        self.cords = (0, 0)                   #$ button render coordinates
        self.size = (0,0)                       #$ button size (affects only the background not the text area)
        self.toggled = False
        self.clicked = False
        self.hover_bg = (0, 255, 0)
        self.hover = False
        self.trans = False

    #$ Outline
        self.border_color = (0, 0, 0)         #$ border color
        self.border_width = 0                   #$ border width, width = 0 turns borders off

    #$ Radius
        self.radius = 20                         #$ radius of button, set to 1 to remove pixlated edges
        self.top_left_radius = 0
        self.top_right_radius = 0
        self.bottom_left_radius = 0
        self.bottom_right_radius = 0

    #$ Padding
        self.padding = [8, 8, 8, 8]                #$ padding, left, right, top, bottom

    #$ Relative Mouse
        self.reMouseX = Button.surfaceX 
        self.reMouseY = Button.surfaceY 
    


    def render(self):
        if(self.bold):
            self.btn_surface = self.bold_font.render(self.btn_text, True, self.txt_color)
        else:
            self.btn_surface = self.regular_font.render(self.btn_text, True, self.txt_color)
        self.btn_rect = self.btn_surface.get_rect()
        self.btn_rect.topleft = self.cords
            

        self.bg_rect = self.btn_rect.copy()

        if(self.size[0] > 0 or self.size[1] > 0):
            self.bg_rect.width = self.size[0]
            self.bg_rect.height = self.size[1]

        self.bg_rect.center = self.btn_rect.centerx - self.padding[0], self.btn_rect.centery - self.padding[2]
        self.bg_rect.width += self.padding[0] + self.padding[1]
        self.bg_rect.height += self.padding[2] + self.padding[3]


    def change_padding(self, left = 0, right = 0, top = 0, down = 0):
        self.padding[0] = left
        self.padding[1] = right
        self.padding[2] = top
        self.padding[3] = down


    def draw(self, screen):

        if not(self.trans):
            if (self.toggled):
                pygame.draw.rect(screen, (72, 255, 36), self.bg_rect, 0, self.radius)
                pygame.draw.rect(screen, (0, 0, 0), self.bg_rect, 3, self.radius)
            elif (self.hover):
                pygame.draw.rect(screen, (255, 244, 128), self.bg_rect, 0, self.radius)
            else:
                pygame.draw.rect(screen, self.btn_bg, self.bg_rect, 0, self.radius)

            if(self.border_width > 0):
                self.outline_rect = self.bg_rect.copy()
                pygame.draw.rect(screen, self.border_color, self.outline_rect, self.border_width, self.radius)

            
        screen.blit(self.btn_surface, self.btn_rect)

    def detect_hover(self, mouse_cord):

        if (self.bg_rect.collidepoint(mouse_cord)):   
            self.hover = True                
            self.border_width = 3
        else:
            self.hover = False                
            self.border_width = 0

    def detect_toggle(self):
        if (self.hover):
            self.toggled = not self.toggled
            return self.toggled

    def detect_click(self):
        if (self.hover):
            return True

# class toggle:
#     def __init__():
#         font = pygame.font.Font(None, 35)
#         font2 = pygame.font.Font(None, 25)
#         sound = font.render("Sound", True, (0, 0, 0))
#         space_on = pygame.Rect(sound.get_width() + 100, 50, 50, sound.get_height())
#         space_off = pygame.Rect(space_on.topright[0] , 50, 50, sound.get_height())
#         slider = pygame.Rect(space_on.x, space_on.y, space_on.width, space_on.height)
#         ON = font2.render("ON", True, (0, 0, 0))
#         on_rect = ON.get_rect(center = slider.center)
#         OFF = font2.render("OFF", True, (0, 0, 0))
#         off_rect = OFF.get_rect(centerx = slider.centerx + slider.width, centery = slider.centery)
#         screen.blit(sound, (70, 50))
#         screen.blit(volume, (45, 150))
#         pygame.draw.rect(screen, (52, 201, 89), space_on)
#         pygame.draw.rect(screen, (201, 65, 52), space_off)
#         screen.blit(ON, on_rect)
#         screen.blit(OFF, off_rect)

#         pygame.draw.rect(screen, (255, 255, 255), slider)