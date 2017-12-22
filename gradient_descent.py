import numpy as np

class myFun(object):
    # Gradient descent using forward differences

    # could improve by adding backward / central differences, adjustable
    # step-size, ability to take in function string as a parameter

    def __init__(self,IC,h,alpha,tol):
        self.IC = IC
        self.h = h
        self.alpha = alpha
        self.tol = tol

    def evalF(self,x):
        return 3 * np.power(x,2) - x + 1

    def forward_diff(self,x):
        return (1 / self.h) * (self.evalF(x + self.h) - self.evalF(x))

    def step(self,x):
        dFdx = self.forward_diff(x)
        return x - self.alpha * dFdx

    def descend(self):
        x = self.IC
        num_iter = 0;
        # print(x)
        while self.forward_diff(x) > self.tol:
            x = self.step(x)
            num_iter += 1
        #    print(x)
        return x, num_iter

f = myFun(100,0.1,0.05,0.001)
xmin, num_iter = f.descend()
print("xmin is ", xmin)
print("fvalue at xmin is ", f.evalF(xmin))
print("number of iterations was ", num_iter)
