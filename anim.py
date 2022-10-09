import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class ParametricAnim:
   
    def __init__(self, func, xrange, *args, **kwargs):

        self.fig = plt.figure()
        self.ax = plt.axes()
        self.ax.set_xlim(min(xrange), max(xrange))
        
        _f = func(xrange, 100)
        self.ax.set_ylim(min(_f) - 0.1*abs(min(_f)), max(_f) + 0.1*abs(max(_f)) )

        self.xrange = xrange
        self.func = func

        self.line, = self.ax.plot([],[], *args, **kwargs)
        self.line.set_data([],[])
        
        ## params
        self.frames = 100
        self.interval = 10
        self.blit = True
        

    def animate(self, i):

     
        y1 = self.func(self.xrange,i)
        
        self.line.set_data(self.xrange, y1)
        return self.line,

    def anim(self):
        self.anim = FuncAnimation(self.fig, 
                                  self.animate, 
                                  frames=self.frames, 
                                  interval=self.interval, 
                                  blit=self.blit)
        plt.show()

