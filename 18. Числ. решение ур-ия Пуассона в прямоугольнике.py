# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt
import copy

#Уравнение:
# (д2u/дx2 + д2u/дy2) = - f(x,y)

#пространственный интервал: 0 <= x <= lx и 0 <= y <= ly
lx = 1
ly = 1
#число точек разбиения пространственного интервала
Nx = 20
Ny = 20
#пространственный шаг сетки
hx = (lx-0) / Nx
hy = (ly-0) /Ny

#краевые условия в прямоугольнике
#левая граница
def psi1(y,t):
    return 0
#правая граница
def psi2(y,t):
    return 0
#нижняя граница
def psi3(x,t):
    return 0
#верхняя граница
def psi4(x,t):
    return 0

#источник-сток тепла
def f(x,y):
    return 0

#кооррдината x
x = []
for j in range(0,Nx+1):
    x.append(0+hx*j)    
#кооррдината y
y = []
for i in range(0,Ny+1):
    y.append(0+hy*i)    

#u_old - начальное приближение (1)
u_old = [[1 for i in range(Ny+1)] for j in range(Nx+1)]
#заполняем нулями (заготавливаем пустой массив)
u_new = [[0 for i in range(Ny+1)] for j in range(Nx+1)]
delta_u = [[0 for i in range(Ny+1)] for j in range(Nx+1)]

#===========================================================================
eps = 0.00001
d = 2*(hx**(-2)+hy**(-2))
#основной итерационный цикл
norm=1
itern = 0
while (norm > eps):
       
    #краевые условия левая и правая границы
    for i in range(1,Ny):
        u_new[0][i] = psi1(y[i],t)
        u_new[Nx][i] = psi2(y[i],t)
    #краевые условия нижняя и верхняя границы
    for j in range(1,Nx):
        u_new[j][0] = psi3(x[j],t)
        u_new[j][Ny] = psi4(x[j],t)

    #внутренняя область прямоугольника
    max_du = 0    
    for j in range(1,Nx):
        for i in range (1,Ny):
            u_new[j][i] = 1/d *(  hx**(-2) * (u_old[j+1][i]+u_new[j-1][i]) +\
                                  hy**(-2) * (u_old[j][i+1]+u_new[j][i-1]) +\
                                  f(x[j],y[i]) )
            delta_u = abs(u_new[j][i] - u_old[j][i])
            if delta_u > max_du:
                max_du = delta_u

    #вычисление нормы    
    norm = max_du
    print('itern=',itern)
    print('norm=',norm)
    u_old = copy.deepcopy(u_new)
    
    #отображение результатов (диагональ прямоугольника)
    if itern == 0:
        plt.plot(x,u_new[:][int(Ny/2)], label='itern='+str(itern),ls='dashed')
    if itern == 10:
        plt.plot(x,u_new[:][int(Ny/2)],label='itern='+str(itern),ls='dashed')
    if itern == 200:
        plt.plot(x,u_new[:][int(Ny/2)],label='itern='+str(itern),ls='dashed')
    itern += 1
plt.legend(fontsize=10) 
#============================================================================
