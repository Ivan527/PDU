# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt
import copy

#Уравнение:
# дu/дt = a^2*(д2u/дx2 + д2u/дy2) + f(x,t)

#a температуропроводность
a = 1

#пространственный интервал: 0 <= x <= lx и 0 <= y <= ly
lx = 1
ly = 1
#число точек разбиения пространственного интервала
Nx = 20
Ny = 20
#пространственный шаг сетки
hx = (lx-0) / Nx
hy = (ly-0) /Ny

#временной интервал (время расчета)
T = 0.2
#временной шаг сетки
dt = 0.8 * 1 / (2*a**2*(hx**(-2)+hy**(-2)) )
print('dt=',dt)
#число точек разбиения временного интервала
Nt = int(T/dt)
print('Nt=',Nt)

#начальное условие u0(x,y)
def u0(x,y):
    return 1

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
def f(x,y,t):
    return 32*(x*(1-x)+y*(1-y))

#кооррдината x
x = []
for j in range(0,Nx+1):
    x.append(0+hx*j)    
#кооррдината y
y = []
for i in range(0,Ny+1):
    y.append(0+hy*i)    

#u_old - начальное условие на расчетной сетке
u_old = [[u0(x[j],y[i]) for i in range(Ny+1)] for j in range(Nx+1)]
#заполняем нулями (заготавливаем пустой массив)
u_new = [[0 for i in range(Ny+1)] for j in range(Nx+1)]
#аналитическое решение
u_anal = [[16*x[j]*(1-x[j])*y[i]*(1-y[i]) for i in range(Ny+1)] for j in range(Nx+1)]
#аналитическое решение при y = 0.5
u_an = [4*x[j]*(1-x[j]) for j in range(Nx+1)]
#график
plt.plot(x,u_an,label='anal y=0.5')
	

#===========================================================================
#основной цикл по времени (для t=0 решение уже известно - u_old)
for k in range(1,Nt+1):
    t = k*dt #время на текущем шаге
    
    #краевые условия левая и правая границы
    for i in range(1,Ny):
        u_new[0][i] = psi1(y[i],t)
        u_new[Nx][i] = psi2(y[i],t)
    #краевые условия нижняя и верхняя границы
    for j in range(1,Nx):
        u_new[j][0] = psi3(x[j],t)
        u_new[j][Ny] = psi4(x[j],t)

    #внутренняя область прямоугольника
    for j in range(1,Nx):
        for i in range (1,Ny):
            u_new[j][i] = u_old[j][i] +dt*a**2 * (  \
                    (u_old[j+1][i]-2*u_old[j][i]+u_old[j-1][i])/hx**2  + \
                    (u_old[j][i+1]-2*u_old[j][i]+u_old[j][i-1])/hy**2  ) + \
                    dt * f(x[j],y[i],t+dt/2)
    
    u_old = copy.deepcopy(u_new)
    
    #отображение результатов
    tt = str(round(t,5))
    if k == 1:
        plt.plot(x,u_new[:][int(Ny/2)], label='t='+tt,ls='dashed')
    if k == int(Nt/2):
        plt.plot(x,u_new[:][int(Ny/2)],label='t='+tt,ls='dashed')
    if k == Nt:
        plt.plot(x,u_new[:][int(Ny/2)],label='t='+tt,ls='dashed')

plt.legend(fontsize=10) 
#============================================================================
