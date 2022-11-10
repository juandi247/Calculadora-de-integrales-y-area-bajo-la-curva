from math import *
from matplotlib import pyplot
from sympy import *
import numpy as np
from tabulate import tabulate



print ("Calculadora de integrales por distintos metdoos")

#INGRESAR LOS DATOS
funcion_input = input("Escribe la funcion f(X): ") 
x=symbols("x")

def funcion(x):
    return  eval(funcion_input)



a = float(input("Cuál es el intervalo inferior de la integral: "))
b = float(input("Cuál es el intervalo superior de la integral: "))
n = int(input("Cuál es el valor de n:  "))
r=a


#integral por calculadora normal
x=symbols("x")
respuesta_integral=integrate(funcion_input,(x,a,b))



h = (b-a)/n #calcular h BASE 
total= 0   

#FORMULA: f(x)=h/3[f(limite inferior)+4f(xi)+f[limite superior]] xi son los limites de adentro

# IMPORTANTE metodo 1/3 las funciones desde x0 hasta x n-1 van a valer 2 o 4, si es par por 2 y si es impar por 4


for i in range(1,n): #para evaluar la funcion en x (x0, x1. xn)
    x=a+(i*h)  #valor de xn si el numero de tramos es par se multiplica por 2 y si es impar por 4
       #para calcular xn - limite inferior + multiplicacion de n por h
    if(i%2==0):
        total+=2*funcion(x)
    else:
        total+=4*funcion(x)

total+=funcion(a)+funcion(b)
Integral_simpson = total*((1/3)*h)  #primero va a multiplicar 1/3 por h y multiplicado a la suma de todas las funciones evaluadas

print(f"\nResultado integacion por simpson: {Integral_simpson}")






#TRAPECIOS
suma=0
for i in range (0,n,1):
    
    Area_trapecios=h*(funcion(a)+funcion(a+h))/2#coge el a que es el primer valor del intervalo y lo suma al siguiente intervalo el cual seria a+h porque h es lo que mide la base
    suma=suma+Area_trapecios #acumular en la variable suma cada area de trapecio, se van sumando las areas en cada iteracion del ciclo for
    
    a=a+h #se suma h para seguir al siguiente intervalo en el ciclo for 
integracion_trapecio=suma #guardar la variable al final y listo 


print(f"resultado integracion trapcio: {integracion_trapecio}")








#riemman


print("-------------------------")

def RiemannInf(f, xi, xf, n):   
  
  x = np.linspace(xi, xf, n)            #Valores de 'x' en los 'n' intervalos hace un array o lista de los valores
  A = 0                                 #Aproximacion del area bajo la curva. Inicia en cero
  area = []                             #Vector que guarda el area del rectangulo en cada Subintervalo
  f1 = []                               #Valor de la funcion a la izquierda de cada subintervalo, osea coge la altura de la parte izq hasta la curva
  f2 = []                               #Valor de la funcion a la derecha de cada subintervalo, aca coge la altura de la parte derecha 
                 
                

  for i in range (1, n):
    #Suma de Riemman
        f1.append(f(x[i-1]))               #Evalua la funcion a la izquierda de cada subintervalo y lo agrega a la lista f1
        f2.append(f(x[i]))                  #Evalua la funcion a la derecha de cada subintervalo y lo agrega a la lista f2
        fx = np.min([f(x[i-1]), f(x[i])])  #amin significa escoger el minimo #Escoge al Menor de los dos valores de 'f(x)' en el subintervalo  f(x(i-1 es izquierda)  y f(x(i) es derecha))      
        area.append(fx*h)                 #Area del rectangulo del subintervalo y lo agrega el vector 'a'

        A += fx*h     #guarda el area de cada intervalo en la lista o el array fx y los va sumando para que de el area final total
        #print(A)
                
  return A

Integral_riemman = RiemannInf(funcion, r, b, n)
print("respuesta riemman: ",Integral_riemman,"\n")


#TABLAA
porcentaje_error_Trapecio=(integracion_trapecio*100/respuesta_integral)-100
porcentaje_error_Trapecio=abs(porcentaje_error_Trapecio)

porcentaje_error_Simpson=(Integral_simpson*100/respuesta_integral)-100
porcentaje_error_Simpson=abs(porcentaje_error_Simpson)


porcentaje_error_Riemman=(Integral_riemman*100/respuesta_integral)-100
porcentaje_error_Riemman=abs(porcentaje_error_Riemman)



tabla = [["Metodo Simpson 1/3",Integral_simpson,porcentaje_error_Simpson],
        ['Metodo de Trapecios', integracion_trapecio,porcentaje_error_Trapecio],
         ["Metodo Riemman (INFERIOR)",Integral_riemman,porcentaje_error_Riemman],
         ["Calculadora normal", respuesta_integral,0]
         ]         
print(tabulate(tabla, headers = ["Metodo", "Resultado","porcentaje de error%"]))










