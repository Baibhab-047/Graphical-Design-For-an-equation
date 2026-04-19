import pygame as pg
import numpy as np
import sympy as sp
import sys
from Dummy import Grapher


pg.init()
WIDTH, HEIGHT = 700, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Script")
clock = pg.time.Clock()

my_plot=Grapher(WIDTH, HEIGHT)
x=sp.symbols('x')
equation=x**4 + x**3 + x**2 + x + 1
math_x=np.linspace(-1000, 1000, 1000001)
fast_function=sp.lambdify(x, equation, modules=['numpy'])
math_y=fast_function(math_x)

running=True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        my_plot.movement(event)

    my_plot.conversion(math_x, math_y)
    screen.fill('white')
    my_plot.draw_grid(screen)
    my_plot.rendering(screen)
    pg.display.flip()
    clock.tick(60)

