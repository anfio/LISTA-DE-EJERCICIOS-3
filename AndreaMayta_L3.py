#1.Definir la siguiente clases con sus métodos iniciales y su método __str__
def clase():
    class prueba:
        def __init__(self) -> None:
            pass
        def __str__(self) -> str:
            pass

#2. Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
#clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
#tener un método para agregar productos y otra para mostrar toda la lista de productos.

class producto:
    def __init__(self, producto, marca, año):
        self.producto = producto
        self.marca = marca
        self.año = año
        print('El producto: ', self.producto)
    def __str__(self):
        return '{} de la marca {} y del año ({})'.format(self.producto,self.marca, self.año) 

class Catalogo:

    listaProductos = []  

    def __init__(self, producto):
        self.listaProductos.append(producto)

    def agregar(self, p):  
        self.listaProductos.append(p)

    def mostrar(self):
        for p in self.listaProductos:
            print(p)  

p=producto("aro","toyota",2019)
p1=producto("luces","kia",2021)
p2=producto("motor","hyundai",2022)

c1=Catalogo(p)
c1.agregar(p1)
c1.agregar(p2)
print("LISTA DE PRODUCTOS EN LA AUTOPARTE")
c1.mostrar()

#3.Crear una clase Animal ,luego una clase Perro y gato que sean hijos de Animal ,el método
#de Sonido debe ser diferente

class Animal:
    def __init__(self,sexo):
            self.sexo=sexo
    def __str__(self):
            pass
class perro(Animal):
    def sonidoanimal(self,sonido):
            print("El perro dice: ",sonido)
class gato(Animal):
    def sonidoanimal(self,sonido):
            print("El gato dice: ",sonido)
hijo1=perro('hembra')
hijo2=gato('macho')
print("El sexo del hijo 1 es: ",hijo1.sexo)
print("El sexo del hijo 2 es: ",hijo2.sexo)
hijo1.sonidoanimal("guau")
hijo2.sonidoanimal("miau")

#4).Con la librería os (import os ) usar 3 funciones de la libreria e imprimir su resultado
# referencia: https://docs.python.org/3/library/os.html

import os
print(os.getcwd())
print(os.listdir())
#Lista del archivo
print(os.listdir('CLASE_06_11'))
#Unir dos rutas
print(os.path.join(os.getcwd(),'CLASE_06_11'))
#Para crear una nueva carpeta
os.mkdir('NUEVA CARPETA')

#5). imprimir el nombre del archivo ejecutado
import os
ruta=r'C:\Users\Usuario\Desktop\PYTHON Visual Studio Code\LISTA_DE_EJERCICIOS_3\P6.py'
nombre_archivo= os.path.basename(ruta)
print(nombre_archivo)

#6). Generar un número aleatorio entre 1 y 100.

import random
print (random.randint(1,100)) 


# 7).Hacer un programa que consulte el valor del dolar (compra y venta ) de la fecha actual
#segun sunat (url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat')

    #import requests 
url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' 

    #response = requests.get(url)
    #response.json() 
    #res=response.json()

    #print(res)

#8.Buscar si existe la palabra python en el siguiente texto 

import re
texto ="Python es uno de los lenguajes de programación dinámicos más populares que existen entre los que se encuentran Java,Javascript, Go y C#. Aunque es considerado a menudo como un lenguaje scripting, es realmente un lenguaje de propósito general. En la actualidad, Python es usado para todo, desde simples scripts, hasta grandes servidores web que proveen servicio ininterrumpido 24×7. Es utilizado para la programación de interfaces gráficas y bases de datos, programación web tanto en el cliente como en el servidor (véase Django o Flask) y testing de aplicaciones"
re.search('Python', texto)
palabra = "Python"

encontrado = re.search(palabra,  texto)

if encontrado:
    print("Se ha encontrado la palabra:", palabra)
else:
    print("No se ha encontrado la palabra:", palabra)

#9) .Obtener todas las ocurrencias de la palabra python en el texto anterior.
import re
texto= "Python es uno de los lenguajes de programación dinámicos más populares que existen entre los que se encuentran Java,Javascript, Go y C#. Aunque es considerado a menudo como un lenguaje scripting, es realmente un lenguaje de propósito general. En la actualidad, Python es usado para todo, desde simples scripts, hasta grandes servidores web que proveen servicio ininterrumpido 24×7. Es utilizado para la programación de interfaces gráficas y bases de datos, programación web tanto en el cliente como en el servidor (véase Django o Flask) y testing de aplicaciones"
print(re.findall(r"Python", texto))