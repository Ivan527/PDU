# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt

#Уравнение:
# д2u/dt2 = a^2*d2u/dx2 + f(x,t)

#a - фазовая скорость волны
a = 1

#пространственный интервал: 0 <= x <= l
l = 1
#число точек разбиения пространственного интервала
N = 50
#пространственный шаг сетки
h = (l-0) / N

#временной интервал (l/a - время прохождения волной системы)
T = 5 * l / a
print('T=',T)
#временной шаг сетки (h/a - время прохождения волной шага h)
dt = 0.5 * h / a
print('dt=',dt)
#число точек разбиения временного интервала
Nt = int(T/dt)
print('Nt=',Nt)

#начальное условие для самой функции
def mu1(x):
    return 0
#вторая производная по x от краевого условия
def mu1_xx(x):
    return 0
#начальное условие для первой производной
def mu2(x):
    return pi*a/l *sin(pi*x/l)
#краевое условие на левой границе
def mu3(t):
    return 0
#краевое условие на правой границе
def mu4(t):
    return 0

#источник-сток поглощение-возбуждение колебаний в среде
def f(x,t):
   return 0

def uanal(x,t):
    return sin(pi*x/l)*sin(pi*a*t/l)

x = []
u_old = []
u_curr = []
u_new = []
u_anal = []
#начальное условие
for j in range(0,N+1):
    x.append(0+h*j)    
    u_old.append(mu1(x[j]))
    u_curr.append( mu1(x[j]) + dt*mu2(x[j]) + dt**2/2*a**2*mu1_xx(x[j]) )
    u_anal.append( uanal(x[j],0))
#график начальное условие и аналитическое решение
#plt.plot(x,u_old, 'o', label='u0')
#plt.plot(x,u_anal, 'x', label='u_anal0')


b = 2*h**2/(a*dt)**2
sigma = 2+b
g = [0]*(N+1)
Xi = [0]*(N+1)
Eta = [0]*(N+1)
u_new = [0]*(N+1)
#===========================================================================
#основной цикл по времени
#значения при t=0: u(0)=u_old, а также при t=0+dt: u(dt)=u_curr уже известны
for m in range(2,Nt):
    t = m*dt #время на текущем шаге

    #вычисляем g[j]    
    for j in range(1,N):
        g[j] = -2*b*u_curr[j] - (u_old[j+1]-sigma*u_old[j]+u_old[j-1])

    #прямой ход прогонки
    Xi[1] = 0
    Eta[1] = mu3(t)
    for j in range(1,N):
        Xi[j+1] = 1/(sigma-Xi[j])
        Eta[j+1] = (Eta[j]-g[j])*Xi[j+1]

    #обратный ход прогонки
    u_new[N] = mu4(t)
    for j in range(N-1,-1,-1):
        u_new[j] = Xi[j+1]*u_new[j+1] + Eta[j+1]
    
    u_old[:] = u_curr[:]
    u_curr[:] = u_new[:]
    #аналитическое решение на текущем временном шаге
    for j in range(0,N+1):
        u_anal[j] = uanal(x[j],t)

    #вывод результатов
    if m == 10:
       plt.plot(x,u_new, 'o', label='t='+str(t))
       plt.plot(x,u_anal, label='anal t='+str(t))
    if m == 20:
        plt.plot(x,u_new, 'x', label='t='+str(t))
        plt.plot(x,u_anal, label='anal t='+str(t))
    if m == 30:
        plt.plot(x,u_new, 's', label='t='+str(t))
        plt.plot(x,u_anal, label='anal t='+str(t))
    if m == 50:
        plt.plot(x,u_new, 'd', label='t='+str(t))
        plt.plot(x,u_anal, label='anal t='+str(t))
#============================================================================
plt.legend()       
