
from math import *
from matplotlib import pyplot
from sympy import *
import numpy as np



def trapecio(n,x,y,numerotrapecios):
    suma=0
    for i in range(1,n):
        suma=suma+y[i]
    Rta=(x[n-1]-x[0])*(y[0]+2*suma+y[n-1])/(2*numerotrapecios)
    return Rta




a = float(input("Cuál es el intervalo inferior de la integral: "))
b = float(input("Cuál es el intervalo superior de la integral: "))
n = int(input("Cuál es el valor de n:  "))
h = (b-a)/n #calcular h BASE 



xi= np.linspace(a,b,n)
yi=np.zeros(n)


x= np.linspace(a,b,n)
print("Valores de X: ",x)
y=np.zeros(n)



for i in range(0,n):
    y[i]=float(input(f"Valor de y{i}: "))

Num_Trapecios=n-1

#INTEGRAL
respuesta=trapecio(n,x,y,n)
print("respuesta de la integral: ",respuesta)


#FUNCION
pyplot.axhline(0, 
color="black")
pyplot.axvline(0, 
color="Black")


pyplot.plot(x,y)
pyplot.plot(xi,y,"ro")

pyplot.show()



#TABLA RELLENA DE VERDE

print("TABLA RELLENA")
pyplot.axhline(0, 
color="black")
pyplot.axvline(0, 
color="Black")

pyplot.plot(x,y)
pyplot.plot(xi,y,"ro")
pyplot.fill_between(xi,y,color='g')            #pyplot.fill_between(xi,0,fi,color='g')

for i in range(0,n-1,1):
    #ciclo for para poner unas lineas en el eje x por cada punto, (se ponen de color blanco para que se vean como recuadros)
    pyplot.axvline(xi[i], color='w')

pyplot.show()








