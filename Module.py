import numpy as np
import pygame as pg
import sys

class Grapher:
    def __init__(self, width, height, scale=40):
        self.width=width
        self.height=height
        self.origin_x=width//2
        self.origin_y=height//2
        self.scale=scale
        self.points=np.array([])
        self.draw=True
        self.font=pg.font.SysFont('Bahnschrift', 20)

    def draw_grid(self, surface):
        offset_x=self.origin_x%self.scale
        offset_y=self.origin_y%self.scale
        y_positions=np.arange(offset_y, self.height, self.scale)
        x_positions=np.arange(offset_x, self.width, self.scale)
        for i in x_positions:
            pg.draw.line(surface, 'lightgrey', (i, 0), (i, self.height), 1)
        for i in y_positions:
            pg.draw.line(surface, 'lightgrey', (0,i), (self.width,i), 1)
        pg.draw.line(surface, 'black', (0, self.origin_y), (self.width, self.origin_y), 1)
        pg.draw.line(surface, 'black', (self.origin_x, 0), (self.origin_x, self.height), 1)

    def movement(self, event):
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEMOTION:
            mouse = pg.mouse.get_pressed()
            if mouse[0]:
                self.origin_x+=event.rel[0]
                self.origin_y+=event.rel[1]
                self.draw=True
        elif event.type == pg.MOUSEWHEEL:
            if event.y>0: self.scale+=5
            elif event.y<0: self.scale-=5
            self.scale=max(5, (min(self.scale, 500)))
            self.draw=True

    def conversion(self, math_x, math_y, buffer):
        if self.draw:
            l_bound = -self.origin_x / self.scale - buffer
            r_bound = (self.width - self.origin_x) / self.scale + buffer
            u_bound = self.origin_y / self.scale + buffer
            d_bound = (self.origin_y - self.height) / self.scale - buffer

            view_mask = (math_x >= l_bound - 1) & (math_x <= r_bound + 1) & (math_y <= u_bound - 1) & (math_y >= d_bound + 1)

            v_x = math_x[view_mask]
            v_y = math_y[view_mask]

            screen_x = self.origin_x + (v_x * self.scale)
            screen_y = self.origin_y - (v_y * self.scale)
            mask=np.isfinite(screen_y)
            self.points=np.column_stack((screen_x[mask], screen_y[mask]))

    def rendering(self, surface):
        if self.points.shape[0]>=2:
            pg.draw.aalines(surface, 'red', False, self.points)
            self.draw=False









