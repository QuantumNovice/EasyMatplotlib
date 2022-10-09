from anim import ParametricAnim
from numpy import *



def f1(x, t):
    return x**2+t

xrange = linspace(-10, 10, 100)
a = ParametricAnim(f1, xrange, lw=2)
a.ax.set_xlim(-10, 10)
a.ax.set_ylim(-200,200)
a.anim()

a.save("test")