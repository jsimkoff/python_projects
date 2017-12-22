# small class and method example
# make an object class called apple that has a method
# called seeds that generates a random number of
# new apple objects
import scipy as sp
import numpy as np


class Apple(object):

    def __init__(self,color):
        self.color = color

    def printargs(self):
        print(self.color)

    def seed(self):
        g = 0;
        if self.color == 'red':
            g = 1.2*sp.rand(1,1);
        elif self.color == 'blue':
            g = 1.6*sp.rand(1,1);
        else:
            print('error: invalid color')


        if np.round(g) >= 1:
            print (self.color,"apple spawned new blue apple")
            return Apple('blue')

        else:
            print (self.color, 'apple spawned new red apple')
            return Apple('red')


app1 = Apple('red')
app2 = app1.seed()
app3 = app2.seed();
app4 = Apple('green')
app5 = app4.seed()
