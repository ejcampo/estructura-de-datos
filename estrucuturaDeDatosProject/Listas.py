#Listas
lista = []#Definir una lista vacia
print(lista)
lista1 = [1,2,3,4,5,"hola",4.5]#Una lista heterogenea
print(lista1)

print("")
#Enlazar las listas
lista2 = [0,1,2,3]
lista3 = ["A", "B", "C"]
lista4 = [lista2,lista3]
print(lista4)
print(lista4[1][1])

print("")
# Definición de una lista
lista = []  # lista vacía
lista1 = ["Este es un texto"]  # Una lista con un elemento.
lista2 = ['Una cadena', 123]  # Una lista de dos elementos
lista3 = [1, 2, 3, 4.5, 'hola', 'a']  # Una lista de seis elementos
print(lista)
print(lista1)
print(lista2)
print(lista3)

print("")
#Listas enlazadas
lista5 = [0, 1, 2, 3]
lista6 = ["A", "B", "C"]
lista7 = [lista5, lista6]
print(lista7)
print(lista7[0])  # Muestra solo lista5
print(lista7[1])  # Muestra solo lista6
print(lista7[1][0])  # Muestra de la lista6 el elemento en el índice 0

print("")
#Operaciones con listas
# Concatenacion
lista8 = ["A", "B", "C", "E"]
lista9 = [1, 2, 3, 4, 5]
lista10 = lista8 + lista9
print(lista10)
print(lista10[2])

print("")
# El metodo extend agrega una lista al final de otra lista, la operación afecta la lista invocante
nombres1 = ["Antonio", "Maria", "Mabel"]
nombres2 = ["Barry", "John", "Guttag"]
# nombres3 = ["Barry", "John", "Guttag"]
nombres1.extend(nombres2)
print(nombres1)
print(nombres2)

print("")
# Repetir
lista1 = [1, 2, 3, 4, 5]
lista2 = lista1 * 3
print(lista2)

print("")
# Comparación
# Usando los operadores convencionales (<, <=, >, >=, ==, !=)
print(["Rojas", 123] < ["Rosas", 123])
print(["Rosas", 123] == ["rosas", 123])
print(["Rosas", 123] > ["Rosas", 23])

print("")
#Es posible determinar si un elemento se encunetra en una lista
lista12 = ['cien', 'años', 'de', 'soledad']
if 'de' in lista12:
    print('Si esta en la lista')
else:
    print('No esta en la lista')

print("")
#Iterando una lista
lista13 = ['hola', 'amigos', 'mios']
for palabra in lista13: #para cada palabra de la lista
    print(palabra, end=',') # end evita salto de linea
