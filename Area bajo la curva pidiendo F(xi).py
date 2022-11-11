
from math import *
from matplotlib import pyplot
from sympy import *
import numpy as np



def trapecio(n,x,y,numerotrapecios):
    suma=0
    for i in range(1,n):
        suma=suma+y[i]
    Rta=(x[n]-x[0])*(y[0]+2*suma+y[n])/(2*numerotrapecios)     #Funcion para encontrar el area bajo la curva con los valores dados anteriormente
    return Rta




a = float(input("Cuál es el intervalo inferior de la integral: "))
b = float(input("Cuál es el intervalo superior de la integral: "))
n = int(input("Cuál es el valor de n:  "))
h = (b-a)/n #calcular h BASE 



xi= np.linspace(a,b,n+1)
yi=np.zeros(n+1)  #(Datos de ejes para la grafica)


x= np.linspace(a,b,n+1)  #crea un array con los valores ya dados desde el lim inferior, hasta el limite superior
print("Valores de X: ",x)
y=np.zeros(n+1)  #crear un array para los valores de Y desde index cero hasta numero n+1
 


for i in range(0,n+1):
    y[i]=float(input(f"Valor de y{i}: "))  #ciclo for para pedir los valroes de Y

Num_Trapecios=n-1 

#INTEGRAL
respuesta=trapecio(n,x,y,n)   #llamar la funcion
print("respuesta de la integral: ",respuesta)


#GRaficar los puntos de f(x) para ver como es la funcion
pyplot.axhline(0, 
color="black")
pyplot.axvline(0, 
color="Black")


pyplot.plot(x,y)
pyplot.plot(xi,y,"ro")

pyplot.show()



#Grafica el area bajo la cruva sombreada de color verde mostrando los trapecios, cortando cada punto f(X) de color blanco para darle la forma

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








