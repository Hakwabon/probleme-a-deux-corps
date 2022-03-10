import matplotlib.pyplot as plt
from numpy import *
import math
from fractions import Fraction
import numpy as np
import numpy as np
from sympy import *
from sympy.interactive import printing
use_unicode = True
printing.init_printing(pretty_print=True,use_latex=True)
pi = math.pi


global m,M,G

M_S = 1.9891e30
tho = 24*3600*365
L = 1.5e11

M = 1.9891*10**30/M_S
m = 5.9722*10**24/M_S
G = 6.67*10**-11*M_S*tho**2/L**3

def Gravi(Position,vitesse):
	x_1 = Position[0]
	v_x_1 = vitesse[0]
	y_1 = Position[1]
	v_y_1 = vitesse[1]
	
	x_2 = Position[2]
	v_x_2 = vitesse[2]
	y_2 = Position[3]
	v_y_2 = vitesse[3]
	
	rx = x_1-x_2
	ry = y_1-y_2
	r = math.sqrt((rx)**2+(ry)**2)
	
	g = -G/r**3
	
	a_x_1 = m*rx*g
	a_y_1 = m*ry*g
	a_x_2 = -M*rx*g
	a_y_2 = -M*ry*g
	
	a = [a_x_1,a_y_1,a_x_2,a_y_2]
	v = [v_x_1,v_y_1,v_x_2,v_y_2]
	
	return a,v

x_1 = 0
y_1 = 0
x_2 = 152097701000/L
y_2 = 0

v_x_1 = 0
v_y_1 = 0
v_x_2 = 0
v_y_2 = sqrt(G*M/x_2)

y1 = [x_1,y_1,x_2,y_2]
d_y1 = [v_x_1,v_y_1,v_x_2,v_y_2]
y2 = []
d_y2 = []
y3 = []
d_y3 = []
y4 = []
d_y4 = []

for i in range(len(y1)):
	y2.append(0)
	d_y2.append(0)
	y3.append(0)
	d_y3.append(0)
	y4.append(0)
	d_y4.append(0)
	


dt = 0.05 #ne marche pas si dt >= 0.1
t = 0
temps = [0]
corps_1_x = [x_1]
corps_1_y = [y_1]
corps_2_x = [x_2]
corps_2_y = [y_2]

while t < 10 :
	
	p1 = Gravi(y1,d_y1)
	for i in range(len(y1)):
		y2[i] = y1[i] + dt/2*d_y1[i]
		d_y2[i] = d_y1[i] + dt/2*p1[0][i]
	
	p2 = Gravi(y2,d_y2)
	for i in range(len(y1)):
		y3[i] = y1[i] + dt/2*d_y1[i] + dt**2/4*p1[0][i]
		d_y3[i] = d_y1[i] + dt/2*p2[0][i]
	
	p3 = Gravi(y3,d_y3)
	for i in range(len(y1)):
		y4[i] = y1[i] +dt*d_y1[i] + dt**2/2*p2[0][i]
		d_y4[i] = d_y1[i] +dt*p3[0][i]
	
	p4 = Gravi(y4,d_y4)
	for i in range(len(y1)):
		y1[i] = y1[i] + dt*d_y1[i] +dt**2*(p1[0][i]+p2[0][i]+p3[0][i])/6
		d_y1[i] = d_y1[i] + dt*(p1[0][i]+2*p2[0][i]+2*p3[0][i]+p4[0][i])/6
	
	t = t + dt
	
	temps.append(t)
	
	corps_1_x.append(y1[0])
	corps_1_y.append(y1[1])
	corps_2_x.append(y1[2])
	corps_2_y.append(y1[3])

plt.plot(corps_1_x,corps_1_y,corps_2_x,corps_2_y)
plt.show()

