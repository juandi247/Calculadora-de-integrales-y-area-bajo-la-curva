from math import *
from matplotlib import pyplot
from sympy import *
import numpy as np
from tabulate import tabulate


                              
funcion_input = input("Escribe la funcion f(X): ") #convertimos a lista para menejarla mejor
def funcion(x):
    return  eval(funcion_input)



a=float(input("escribe el limite inferior: "))
b=float(input("escribe el limite superior: "))
Numero_puntos = int(input("escribe el numero (n) de puntos: ")) 


# PROCEDIMIENTO

Tramos = Numero_puntos   #numero (n) de puntos

#Para mostrar integral
xi = np.linspace(a,b,Tramos) #desde a hasta b con paso en el numero de (tramos)
fi = funcion(xi)   #evalua cada punto xi en la funcion



#para mostrar cada punto de la integral
matefacil=Tramos*10   #se multiplica por 10 para que salga una linea continua
xk = np.linspace(a,b,matefacil)  #puntos pero unidos como funcion desde a hasta b
fk = funcion(xk)




#establecer el color de los ejes
pyplot.axhline(0,     
color="black")
pyplot.axvline(0,    #axVline, como es V es vertical
color="Black")






x = range(-5, 10)  #rango para la funcion
print("Estas viendo la grafica de la funcion")
#Graficar la funcion COMPLETA solo con puntos
pyplot.plot(x, [funcion(i) for i in x])   #imprimir la funcion recorriendo eje x (Rango), y un ciclo for para que transforme los valores de X en la funcion como i
                                                        
pyplot.plot(xi,fi,"ro")     #imprimir los puntos rojos "ro" significa rojo
pyplot.fill_between(xi,0,fi,color='g')  #rellenar entre xi y fi (rellena de verde el espacio entre los limites de integracion)
pyplot.show()   #comando show para mostrar la grafica

print("---------- \n")




pyplot.axhline(0, 
color="black")
pyplot.axvline(0, 
color="Black")
print("Ahora estas viendo el area bajo la curva sombreada")
#los punticos de la funcion
pyplot.plot(xi,fi,"ro")
#esta es la funcion con los limites ya puestos
pyplot.plot(xk,fk)


#rellenar desde el primerp punto hasta el ultimo
pyplot.fill_between(xi,fi,color='g')            #pyplot.fill_between(xi,0,fi,color='g')

for i in range(0,Tramos,1):
    #ciclo for para poner unas lineas en el eje x por cada punto, (se ponen de color blanco para que se vean como recuadros)
    pyplot.axvline(xi[i], color='w')
    




pyplot.show()




#mostrar respuesta de la integral por calculadora
x=symbols("x")
respuesta_integral=integrate(funcion_input,(x,a,b))
print(f"--la respusta de la integral por calculadora es: {respuesta_integral}--")


#metodo trapecios
suma=0
xi=a #es igual al limite inferior porque ahi empieza el primer intervalo
h=(b-a)/Numero_puntos    # valor de la base(h) de cada trapecio 
for i in range (0,Numero_puntos,1):
    print("y= ",funcion(xi))
    Area_trapecios=h*(funcion(xi)+funcion(xi+h))/2   #coge el xi que es el primer valor del intervalo y lo suma al siguiente intervalo el cual seria xi+h porque h es lo que mide la base
    suma=suma+Area_trapecios #acumular en la variable suma cada area de trapecio, se van sumando
    xi=xi+h  #al sumar este h pasa al siguiente intervalo para el ciclo for
    print("valor:   ",xi)
integracion_trapecio=suma   

print("\n")
print(f"Numero de tramos o trapecios: {Numero_puntos} ")
print(f"la integral por regla de trapecios es: {integracion_trapecio} ")



print(" \n --BONUS--") #aca hallamos el porcentje de error con respecto a la calculadora

porcentaje_error=(integracion_trapecio*100/respuesta_integral)-100
print(" el porcentaje de error de la regla de trapecios con respecto a la de integracion por calculadora es de: ")
print(porcentaje_error," %")



#hacer una tabla con la importada del TABULATE
tabla = [['Metodo de Trapecios', integracion_trapecio],
         ["integral por calculadora", respuesta_integral]]
        
#mostrar tabla
print(tabulate(tabla, headers = ["Metodo", "Resultado"]))







#comandos explicados
#pyltot.linspace()   genera un array (una lista) de los numeros entre dos puntos, en este caso entre los limites y entre la funcion para los recuadros
#pylot.plot()  provee una interfaz y la grafica pero no la muestra
#pylot.show() es como un print pero con la interfaz 
#pylot.fill_between()    rellenar entre dos puntos 







 
