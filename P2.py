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