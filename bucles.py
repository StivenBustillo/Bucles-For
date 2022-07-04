"""for num in range (0,150):
    print (num)""" #Solamente el # sirve para una linea
    # Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000. 

"""for num in range (5, 1001):
    if num % 5 == 0: #módulo % arroja el residuo de la división
        print (num) """

"""from ast import Return


for num in range (5, 1001, 5):
    print (num)"""

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
#Range: es para recorrer un interválo, 
"""for x in range (1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else: 
        print (x)"""

"""Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final."""
"""for x in range (1,11,2):
    print(x)"""

"""for x in range(1,11):
    if x % 2 != 0:
        print(x)"""

"""sum = 0
for x in range (1, 500, 2):
    sum = x+sum
print(sum)"""
#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.


"""for x in range(2018, 0, -4):
    print(x)"""

#Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

"""
lowNum = 10
highNum = 100
mult = 10

for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)"""
    
#Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

"""Num = input("Ingrese un número mi perro!")
N = int(Num) #convierte un dato en número entero
list = [1, N ,Num]
list.append(N) #append es útil para agregar elementos en la lista
print(list)
"""
"""def miPrimeraFuncion(S):
    list = []
    for p in range(S, -1, -1):
        list.append(p)
    return list
k = miPrimeraFuncion(5)
print(k)"""
#Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
"""from re import X


def imprimir_y_devolver(o):
    print(o[0])
    return o[1]
x = imprimir_y_devolver([4,8])
print(x)
"""
#Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
"""
import re


def crear_lista(listar):
    listadevuelta = []
    segundo_elemento = listar[1]
    for elemento in listar:
        if elemento > segundo_elemento:
            listadevuelta.append(elemento)
    return listadevuelta


x = [7,6,18, 98, 1, 78, 10]
print(crear_lista(x))
    """
def crear_lista(listar):
    listadevuelta = []
    
    if len(listar) < 2:
        print(False)
    else:    
        segundo_elemento = listar[1]
        for elemento in listar:
            if elemento > segundo_elemento:
                listadevuelta.append(elemento)
        print(len(listadevuelta))           #la funcion solo se va a ejecutar hasta  un return
        return listadevuelta 


x = [3]

(crear_lista(x))  
def longitud_valor(tamaño, valor):
    lista = []                        #1) [2,2,2]--
    for numemro in range(0,tamaño):    # rango(0,6)-- 1) numero = 0 -- nun = 2 -- num = 3 -- 
         lista.append(valor)          #  
    return(lista)

lista = longitud_valor(6,2)
print(lista)


    








