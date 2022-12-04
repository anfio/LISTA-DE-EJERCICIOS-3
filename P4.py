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