print("------------- TIENDA -------------------")


productos = []
precio_producto = []
cant_produc = []


nombre_producto = input("ingrese el nombre del producto:  ")
productos.append(nombre_producto)

precio_unitario = int(input( "ingrese el precio del producto:  "))

while precio_unitario<0:
    print("dato erroneo")
    precio_unitario = int(input( "ingrese el precio del producto:  "))
precio_producto.append(precio_unitario)

cantidad_producto = int(input("ingrese la cantidad que va llevar de este producto: "))

while cantidad_producto<0:
    print("dato erroneo")
    cantidad_producto = int(input("ingrese la cantidad que va llevar de este producto: "))
cant_produc.append(cantidad_producto)

#---------------------------------------------------------------------------------------

mas_producto = input("desea agregar otro producto diferente? (si/no)")


#------------------------------------------------------------------------------------------

while mas_producto == "si":

    nombre_producto = input("ingrese el nombre del producto:  ")
    productos.append(nombre_producto)

    precio_unitario = int(input( "ingrese el precio del producto:  "))

    while precio_unitario<0:
        print("dato erroneo")
        precio_unitario = int(input( "ingrese el precio del producto:  "))
    precio_producto.append(precio_unitario)

    cantidad_producto = int(input("ingrese la cantidad que va llevar de este producto: "))

    while cantidad_producto<0:
        print("dato erroneo")
        cantidad_producto = int(input("ingrese la cantidad que va llevar de este producto: "))
    cant_produc.append(cantidad_producto)

    mas_producto = input("desea agregar otro producto diferente? (si/no)\n")

print("**"*30)





""""
for pro in productos:
    print("el nombre del producto es: ", pro)
        
            
for pre in precio_producto:
    print(f"el precio del {nombre_producto} ", pre)



for ca in cant_produc:
    print("la cantidad total de los  productos son: ", ca)

"""


productos = [["arroz",2000,3],["platanos",1000,3]]
total = 0
for valor in productos:
     
     print(valor[0],valor[1],valor[2])
     total = total + (valor[1] * valor[2])

print(total)