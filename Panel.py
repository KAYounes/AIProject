
import pygame
from buttons import Button

class Panel:


    def __init__(self, x_cord, y_cord, horizontal, vertical, color):
        # self.surfaceX = x_cord
        # self.surfaceY = y_cord
        # print(horizontal, vertical)
        # self.relativeMouse = 
        self.cordX = x_cord
        self.cordY = y_cord
        self.hor = horizontal
        self.ver = vertical
        self.panel_color = color

        self.speed = 2000

        self.font = pygame.font.Font("RobotoCondensed-Light.ttf", 20)
        
        self.panel_surf = pygame.Surface((self.hor, self.ver))
        
        self.button_offset_x = 45
        self.button_offset_y = 45
        self.algo_Title_y = 0
        self.algo_Title = Button(30)
        self.algo_Title.btn_text = "Algorithms"
        self.algo_Title.cords = (0, self.algo_Title_y)
        self.algo_Title.trans = True
        self.algo_Title.txt_color = (0,0,0)
        self.algo_Title.bold = True

        self.uninfored_title = Button(25)
        self.uninfored_title.btn_text = "• Uninformed"
        self.uninfored_title.cords = (30, self.algo_Title_y + self.button_offset_y)
        self.uninfored_title.trans = True
        self.uninfored_title.txt_color = (0,0,0)
        self.uninfored_title.bold = True
        self.uninfored_title.render()

        self.bfs_btn = Button()
        self.bfs_btn.btn_text = "BFS Algorithm"
        self.bfs_btn.cords = (self.button_offset_x, self.algo_Title_y + self.button_offset_y * 2)
        self.bfs_btn.render()

        self.dfs_btn = Button()
        self.dfs_btn.btn_text = "DFS Algorithm"
        self.dfs_btn.cords = (self.button_offset_x, self.algo_Title_y + self.button_offset_y * 3)
        self.dfs_btn.render()

        self.ucs_btn = Button()
        self.ucs_btn.btn_text = "UCS Algorithm"
        self.ucs_btn.cords = (self.button_offset_x, self.algo_Title_y + self.button_offset_y * 4)
        self.ucs_btn.render()


        self.infored_title = Button(25)
        self.infored_title.btn_text = "• Informed"
        self.infored_title.cords = (30, self.algo_Title_y + self.button_offset_y * 5)
        self.infored_title.trans = True
        self.infored_title.txt_color = (0,0,0)
        self.infored_title.bold = True
        self.infored_title.render()

        self.greedy_btn = Button()
        self.greedy_btn.btn_text = "GREEDY Algorithm"
        self.greedy_btn.cords = (self.button_offset_x, self.algo_Title_y + self.button_offset_y * 6)
        self.greedy_btn.render()

        self.aStar_btn = Button()
        self.aStar_btn.btn_text = "A* Algorithm"
        self.aStar_btn.cords = (self.button_offset_x, self.algo_Title_y + self.button_offset_y * 7)
        self.aStar_btn.render()


        self.control_Title_y = self.algo_Title_y + self.button_offset_y * 8
        self.control_Title = Button(30)
        self.control_Title.btn_text = "Control"
        self.control_Title.cords = (0, self.control_Title_y)
        self.control_Title.trans = True
        self.control_Title.txt_color = (0,0,0)
        self.control_Title.bold = True

        self.play_btn = Button()
        self.play_btn.btn_text = " Play "
        self.play_btn.cords = (self.button_offset_x, self.control_Title_y + self.button_offset_y)
        self.play_btn.render()

        self.stop_btn = Button()
        self.stop_btn.btn_text = " Stop "
        self.stop_btn.cords = (self.button_offset_x + self.play_btn.bg_rect.width * 1.25, self.control_Title_y + self.button_offset_y)
        self.stop_btn.render()

        self.speed_btn = Button()
        self.speed_btn.btn_text = "Search Speed: " + str(self.speed  * 100 / 2000) + "%"
        self.speed_btn.cords = (self.button_offset_x, self.control_Title_y + self.button_offset_y * 2)
        self.speed_btn.render()

        self.graph_title_y = self.control_Title_y + self.button_offset_y * 3
        self.graph_title = Button(30)
        self.graph_title.btn_text = "Graph"
        self.graph_title.cords = (0, self.graph_title_y)
        self.graph_title.trans = True
        self.graph_title.txt_color = (0,0,0)
        self.graph_title.bold = True

        self.directed_btn = Button()
        self.directed_btn.btn_text = "Directed Graph"
        self.directed_btn.cords = (self.button_offset_x, self.graph_title_y + self.button_offset_y)
        self.directed_btn.render()

        self.clear_btn = Button()
        self.clear_btn.btn_text = " Clear "
        self.clear_btn.cords = (self.button_offset_x + self.directed_btn.btn_rect.width * 1.25, self.graph_title_y + self.button_offset_y)
        self.clear_btn.render()
        
        self.showH_btn = Button()
        self.showH_btn.btn_text = "Show Heuristic"
        self.showH_btn.cords = (self.button_offset_x, self.graph_title_y + self.button_offset_y * 2)
        self.showH_btn.render()

        self.showC_btn = Button()
        self.showC_btn.btn_text = "Show Edge Cost"
        self.bottom = (self.graph_title_y + self.button_offset_y * 3)
        self.showC_btn.cords = (self.button_offset_x, self.bottom)
        self.showC_btn.render()

        self.algo_Title.render()

        self.control_Title.render()

        self.graph_title.render()  


    def fill(self):
        self.panel_surf.fill(self.panel_color)

    def draw_btns(self):
        self.algo_Title.draw(self.panel_surf)
        self.uninfored_title.draw(self.panel_surf)
        self.bfs_btn.draw(self.panel_surf)
        self.dfs_btn.draw(self.panel_surf)
        self.ucs_btn.draw(self.panel_surf)
        self.infored_title.draw(self.panel_surf)
        self.greedy_btn.draw(self.panel_surf)
        self.aStar_btn.draw(self.panel_surf)
        self.control_Title.draw(self.panel_surf)
        self.play_btn.draw(self.panel_surf)
        self.stop_btn.draw(self.panel_surf)
        self.speed_btn.draw(self.panel_surf)
        self.graph_title.draw(self.panel_surf)
        self.directed_btn.draw(self.panel_surf)
        self.clear_btn.draw(self.panel_surf)
        self.showH_btn.draw(self.panel_surf)
        self.showC_btn.draw(self.panel_surf)


    def btnDetect_hover(self, mouse):
        relMouse = (mouse[0] - self.cordX, mouse[1] - self.cordY)

        self.bfs_btn.detect_hover(relMouse)
        self.dfs_btn.detect_hover(relMouse)
        self.ucs_btn.detect_hover(relMouse)
        self.greedy_btn.detect_hover(relMouse)
        self.aStar_btn.detect_hover(relMouse)
        self.play_btn.detect_hover(relMouse)
        self.stop_btn.detect_hover(relMouse)
        self.speed_btn.detect_hover(relMouse)
        self.directed_btn.detect_hover(relMouse)
        self.clear_btn.detect_hover(relMouse)
        self.showH_btn.detect_hover(relMouse)
        self.showC_btn.detect_hover(relMouse)


    def btnDetect_click(self, mouse):
        self.btnDetect_hover(mouse)

        if self.bfs_btn.detect_click() : return "BFS"
        if self.dfs_btn.detect_click() : return "DFS"
        if self.ucs_btn.detect_click() : return "UCS"
        if self.greedy_btn.detect_click() : return "GRD"
        if self.aStar_btn.detect_click() : return "AST"
        if self.play_btn.detect_click() : return "PLY"
        if self.stop_btn.detect_click() : return "STP"
        if self.directed_btn.detect_click() : return "DIR"
        if self.clear_btn.detect_click() : return "CLR"
        if self.showH_btn.detect_click() : return "SHW"
        return None

    def mouseOnPanel(self, mouse):
        relMouse = (mouse[0] - self.cordX, mouse[1] - self.cordY)
        return self.panel_surf.get_rect().collidepoint(relMouse)


    def displayMessage(self, message):
        pygame.draw.line(self.panel_surf, (0, 0, 0), (0, self.bottom + 45), (self.ver, self.bottom + 45), 2)
        tokens = message.split(" ")
        message = tokens[0]
        new_line = False
        messages = []
        offset = 0
        for token in tokens[1:]:
            message += " " + token

            msg_surf = self.font.render(message, True, (0, 0, 0))
            msg_rect = msg_surf.get_rect()

            if (message[0] == " "):
                message = message[1:]

            if (msg_rect.width > self.hor):
                # print(">", message)
                message = message[:-len(token) - 1]
                # print(">", message + ".")

                messages.append(message)
                message = token
            
            if (token == tokens[-1]):
                messages.append(message)
            elif (token == "nl"):
                # print(">>" + message, ">>" + message + ">",token)
                if (message != "nl"):
                    messages.append(message[:-2])
                messages.append(token)
                message = ""
        
        for line in (messages):
            surf = self.font.render(line, True, (0,0,0))

            if line == "nl":
                offset += 1
                continue

            self.panel_surf.blit(surf, (0, self.bottom + 60 + 25 * offset))
            offset += 1

    def speed_control(self):
        if (self.speed == 250):
            self.speed = 2000

        self.speed -= 250
        self.speed_btn.btn_text = "Search Speed: " + str(2 - (self.speed) / 1000) + "X"
        self.speed_btn.render()
        return self.speed
            