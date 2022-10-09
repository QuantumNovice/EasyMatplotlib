from anim import ParametricAnim
import numpy as np 
from numpy import *

def func(x,t):
    return 10*np.sin(x-t/10)

xrange = np.linspace(0, 2*np.pi, 100)
a = ParametricAnim(lambda x,t: t*np.sin(x), xrange, lw=2)
a.anim()
#a.save("reee")

xrange = np.linspace(0, 2*np.pi, 100)
a = ParametricAnim(lambda x,t: np.sin(x*t/10), xrange, lw=2)
#a.anim()
a.save("re2")
