# Graphical-Design-For-an-equation
Hi, I am a 14 year old programmer( or a coder you can say) , As you can see I have made a graph plotting software for simple or maybe a little complex equation that you give. Please try this file out. I made this out of boredom. It uses numpy vectorization, and several sympy functions such implicit_multiplication, etc.
# Ultra-Fast Graphical Representation Engine

A high-performance 2D graphing tool built with **Python**, **Pygame**, and **NumPy**. This project uses **SymPy** to parse complex mathematical equations and vectorizes the coordinates for smooth, real-time rendering.

## Features
* **Real-time Parsing:** Enter equations like `sin(x) * x` or `x^2` and see them instantly.
* **Vectorized Math:** Uses NumPy for $N \times 2$ array processing, making it capable of handling thousands of points without lag.
* **Interactive UI:** Supports zooming with the scroll wheel and panning by dragging the mouse.

##  Installation
1. Install the dependencies:
   ```bash
   pip install pygame numpy sympy

##  Module
I have added the module file for using graphical viewing in your program. You can use the following functions in this module(For more info watch out for the Dummy_Script file):
* **Importing** Use `from Module import Grapher` at the top while making sure that your script and the module are in the same folder and dont forget to set a variable `{name_of_your_variable}=Grapher(WIDTH, HEIGHT)
* **Movement of Graph** Use the events or the mouse inputs to zoom in, zoom out or move the graph ; syntax: `{name_of_your_variable}.movement(event)`
* **Conversion(Main Function)** Uses high level culling so your graph doesnt freeze and converts your math coordinates into screen coordinates using several numpy calculations making sure it filters/masks non-finite values
* **Drawing the Graphical Grid** Use the `{name_of_your_variable}.draw_grid(surface)` to draw the graphical grid. This uses modulo and a few numpy vectorizations.
* **Rendering the Equation** Use the `{name of your variable}.rendering(screen)` to render the equation in your grid. This uses pygame's anti-aliasing line line drawing features.

Start example:
`# Quick Start Example
from Module import Grapher
import numpy as np

 #setting up the equations, width and height
plot = Grapher(800, 800)
x_math = np.linspace(-10, 10, 1000)
y_math = x_math ** 2

 #In your loop:
plot.conversion(x_math, y_math)
plot.draw_grid(screen)
plot.rendering(screen)`

This program can handle millions of points using the culling system with freezing, crashing, or lagging.
PROOF is in the dummy script file

