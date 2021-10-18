import math
from scipy.integrate import odeint
import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

#graphing the homogeneous equation of the undetermined coeffiencent equation
def homoEqu1 (x):
    #using IVP c1 = 3/4 and c2 = -3/4
    yhx= (3/4) - (3/4)*pow(math.e,-2*x)
    return yhx
xh = np.linspace(0, 20)
yh = []
for i in xh:
    yh.append(homoEqu1(i))

#graphing greens function
def greens(t):
    yt = integrate.quad(lambda s : gts(t, s)*rt(s), 0, t)
    return yt[0]
def gts (t, s):
    gts = (1 / 2) - (1 / 2) * pow(math.e, 2 * (s - t))
    return gts
def rt(s):
    rt = (2 * s) - 2
    return rt
t = np.linspace(0,20)
yg = []
for i in t:
    yg.append(greens(i))

#graphing undetermined coefficients/ variation of parameters
#I chose to graph the undetermined coefficients equation
def undCoe(x):
    # using IVP c1 = 3/4 and c2 = -3/4
    yhx = (3 / 4) - (3 / 4) * pow(math.e, -2 * x)
    # A1=1/2and A2=-3/2 were found on paper
    ypx = 1/2*x*x - 3/2*x
    yx = yhx + ypx
    return yx
xuc = np.linspace(0, 20)
yuc = []
for i in xuc:
    yuc.append(undCoe(i))

#graphing using ODE
def ODE(y, x):
    y1 = y[0]
    dy = y[1]
    dydx = [[], []]
    dydx[0] = dy
    dydx[1] = (-2*dy)+(2*x)-2
    return dydx
y0=[0,0] #y'(0)=y(0)=0
x = np.linspace(0, 20)
ys = odeint(ODE, y0, x)
y = ys[:,0]

def graphing():
    fig, axs = plt.subplots(3, 2)
    axs[0,0].plot(xh, yh,'r')
    axs[0, 0].set_title("Homogeneous Equation")
    axs[0,1].plot(t, yg)
    axs[0, 1].set_title("Green's Function")
    axs[1,0].plot(xuc, yuc)
    axs[1, 0].set_title("Undetermined Coefficients")
    axs[1,1].plot(x,y)
    axs[1, 1].set_title("ODEint")
    axs[2, 0].plot(x, y, label='ODE')
    axs[2, 0].plot(xh, yh, '.', label='Homo')
    axs[2, 0].plot(xuc, yuc, ':', label='Und Coe')
    axs[2, 0].plot(t, yg, label='Greens')
    axs[2, 0].legend()

    plt.show()


