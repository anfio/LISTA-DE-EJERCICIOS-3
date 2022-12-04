#5). imprimir el nombre del archivo ejecutado
import os
ruta=r'C:\Users\Usuario\Desktop\PYTHON Visual Studio Code\LISTA_DE_EJERCICIOS_3\P6.py'
nombre_archivo= os.path.basename(ruta)
print(nombre_archivo)