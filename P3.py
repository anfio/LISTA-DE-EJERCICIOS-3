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