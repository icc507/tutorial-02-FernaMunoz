#Problema 1  
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t1 = input("Ingrese la primera tupla:").split()
t2 = input("Ingrese la segunda tupla:").split()

orden_tupla = tuple(t2 + t1 + t2)
print(orden_tupla)
