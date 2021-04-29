
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
        
        self.panel_surf = pygame.Surface((self.hor, self.ver))
        
        self.button_offset = 75
        self.algo_Title_y = 0
        self.algo_Title = Button(45)
        self.algo_Title.btn_text = "Algorithms"
        self.algo_Title.cords = (0, self.algo_Title_y)
        self.algo_Title.trans = True
        self.algo_Title.txt_color = (0,0,0)
        self.algo_Title.bold = True

        self.uninfored_title = Button(30)
        self.uninfored_title.btn_text = "• Uninformed"
        self.uninfored_title.cords = (30, self.algo_Title_y + 75)
        self.uninfored_title.trans = True
        self.uninfored_title.txt_color = (0,0,0)
        self.uninfored_title.bold = True
        self.uninfored_title.render()

        self.bfs_btn = Button()
        self.bfs_btn.btn_text = "BFS Algorithm"
        self.bfs_btn.cords = (self.button_offset, self.algo_Title_y + 125)
        self.bfs_btn.render()

        self.dfs_btn = Button()
        self.dfs_btn.btn_text = "DFS Algorithm"
        self.dfs_btn.cords = (self.button_offset, self.algo_Title_y + 175)
        self.dfs_btn.render()

        self.ucs_btn = Button()
        self.ucs_btn.btn_text = "UCS Algorithm"
        self.ucs_btn.cords = (self.button_offset, self.algo_Title_y + 225)
        self.ucs_btn.render()


        self.infored_title = Button(30)
        self.infored_title.btn_text = "• Informed"
        self.infored_title.cords = (30, self.algo_Title_y + 275)
        self.infored_title.trans = True
        self.infored_title.txt_color = (0,0,0)
        self.infored_title.bold = True
        self.infored_title.render()

        self.greedy_btn = Button()
        self.greedy_btn.btn_text = "GREEDY Algorithm"
        self.greedy_btn.cords = (self.button_offset, self.algo_Title_y + 325)
        self.greedy_btn.render()

        self.aStar_btn = Button()
        self.aStar_btn.btn_text = "A* Algorithm"
        self.aStar_btn.cords = (self.button_offset, self.algo_Title_y + 375)
        self.aStar_btn.render()


        self.control_Title_y = self.algo_Title_y + 425
        self.control_Title = Button(45)
        self.control_Title.btn_text = "Control"
        self.control_Title.cords = (0, self.control_Title_y)
        self.control_Title.trans = True
        self.control_Title.txt_color = (0,0,0)
        self.control_Title.bold = True

        self.play_btn = Button()
        self.play_btn.btn_text = " Play Search "
        self.play_btn.cords = (self.button_offset, self.control_Title_y + 75)
        self.play_btn.render()

        self.stop_btn = Button()
        self.stop_btn.btn_text = " Stop Search "
        self.stop_btn.cords = (self.button_offset, self.control_Title_y + 125)
        self.stop_btn.render()


        self.graph_title_y = self.control_Title_y + 175
        self.graph_title = Button(45)
        self.graph_title.btn_text = "Graph"
        self.graph_title.cords = (0, self.graph_title_y)
        self.graph_title.trans = True
        self.graph_title.txt_color = (0,0,0)
        self.graph_title.bold = True

        self.directed_btn = Button()
        self.directed_btn.btn_text = "Directed Graph"
        self.directed_btn.cords = (self.button_offset, self.graph_title_y + 75)
        self.directed_btn.render()

        self.clear_btn = Button()
        self.clear_btn.btn_text = " Clear "
        self.clear_btn.cords = (self.button_offset, self.graph_title_y + 125)
        self.clear_btn.render()


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
        self.graph_title.draw(self.panel_surf)
        self.directed_btn.draw(self.panel_surf)
        self.clear_btn.draw(self.panel_surf)

    def btnDetect_hover(self, mouse):
        relMouse = (mouse[0] - self.cordX, mouse[1] - self.cordY)

        self.bfs_btn.detect_hover(relMouse)
        self.dfs_btn.detect_hover(relMouse)
        self.ucs_btn.detect_hover(relMouse)
        self.greedy_btn.detect_hover(relMouse)
        self.aStar_btn.detect_hover(relMouse)
        self.play_btn.detect_hover(relMouse)
        self.stop_btn.detect_hover(relMouse)
        self.directed_btn.detect_hover(relMouse)
        self.clear_btn.detect_hover(relMouse)

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
        return "no btn was pressed"

        return "no btn was pressed"
    def mouseOnPanel(self, mouse):
        relMouse = (mouse[0] - self.cordX, mouse[1] - self.cordY)
        return (self.panel_surf.get_rect().collidepoint(relMouse))

