t = input().split()

t = [int(x) if x.isdigit() else x for x in t]

#Transformo en lista y utilizo reversed para invertirla
t_inverso = list(reversed(t))

#utilizo tuple para transformarlo en tupla
t_tupla = tuple(t_inverso)

print(t_tupla)
