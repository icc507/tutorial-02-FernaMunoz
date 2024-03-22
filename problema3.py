def arbolTrinario(numero):
	return [numero, [], [],[]]

def insertaEnArbolTrinario(arbol,numero):
  if arbol==[]:
    arbol+=arbolTrinario(numero)
  elif numero < arbol[0]:
    insertaEnArbolTrinario(arbol[1],numero)
  elif numero == arbol[0]:
    insertaEnArbolTrinario(arbol[2],numero)
  else:
    insertaEnArbolTrinario(arbol[3],numero)


lista = input().split()

lista1 = [int(x) if x.isdigit() else x for x in lista]

arbol =[]

for i in lista1:
  insertaEnArbolTrinario(arbol,i)
print(arbol)
