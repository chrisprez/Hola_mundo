# Esto es un comentario.
#if 5 > 3: # Esto es un comentario.
 #   print("Esto se va a imprimir")

x = 5
y = "palabra"
print (x, y)

email = "prueba@feliz.com"
print(email)

mi_variable = "prueba"

a, b, c = "lala", "llele", "lili"
print(a,b,c)

inicio = "hola"
final = " mundo"
print (inicio + final)

# Listas
lista = [1, 2, 3, 3]   # Se crea lista
lista2 = lista.copy() # Se copia la lista, sin valor de 4, ya que eso es una actualizacion de la varibale posterior
lista.append(5)     # Se añade elemento al final de lista
#lista.clear()       # Se borra la lista


print(lista, lista2, lista2.count(3)) # El métodoo "count" cuenta le n veces de repeticion de un elemento de la lista.
print(len(lista), len(lista2)) # Cuenta el n de valores de la lista

print(lista[0]) # Imprime el primer elemento, es el índice
print(lista[4]) # Para el ultimo elemento, es el total -1

lista.pop()     # Se elemina el ultimo elemento
print(lista)
lista.remove(2) # Borramos el valor deseado
print(lista)

lista.append(4) # Para pode seguir con ejemplos
lista.append(9) # Para pode seguir con ejemplos
lista.append(6) # Para pode seguir con ejemplos


lista.reverse()       # Se invierte el orden de la lista
print(lista)

lista.sort()    # Se ordena la lista, por defecto de menoar a mayor, si la lista tuviera distinto tipos de datos, no se puede ordenar
print(lista)
print()
# Tuplas
print('Tuplas:\n')
print('Las tuplas funcionan de la misma manera que las listas, pero no son modificables\n')
tupla = ('a', 'b', 'c', 'd')
print ('Esto es una tupla, fijate en los paratesis: ', tupla)
# tupla.append('f') # Dará error por lo dicho anteriormente
lista_de_tupla = list(tupla)
print('Esto es una lista, fiajte en los corchetes: ', lista_de_tupla)
lista_de_tupla.append('e')
print('Añadimos un elemento ahora que es una lista')
print(lista_de_tupla)
print()

# Range
print('Rangos:\n')
rango = range(6)
print('Imprimirá los limites del rango: ', rango)
print('Esto nos sera útil cuando trabajemos con las iteraciones')
print()

# Diccionarios
print('Introducción a los diccionarios:\n')

diccionario = { #Se aplica este formato por mayor legibilidad del codigo, se podría hacer seguido.
    'nombre': 'pepito',
    'edad': 45,
    'pais':'España'
}

print('Este es el diccionario creado: ', diccionario)
print('Así accedemos al indice del diccionario (edad): ', diccionario['edad']) # Hay que hacerlo con el mismo tipo y valor de la key del diccionario.
print('Otra forma es hacerlo con el metodo get, aplicado en "nombre": ', diccionario.get('nombre'))

diccionario['nombre'] = 'Juan Luis'
print('Se ha cambiado la "key" de nombre: ', diccionario['nombre'])
print('Longitud del diccionario: ', len(diccionario), ' Es el numero de elementos que pueblan el diccionario.\n')

diccionario['Sexo'] = 'Varon' # Se agrega una nuevb Key con un valor
print('Se ha agregado un nuevo elemento :', diccionario)
diccionario.pop('Sexo') # del diccionario['Sexo'] hace lo mismo
# También funciona con poptitem, que elimina la ultima key del diccionario
print('Se eleminado la key agrega anteriormente: ', diccionario)

copia_diccionario = diccionario.copy() # Tambien se puede hacer con copia_diccionario = ditc(diccionario)
print('Se ha copiado el diccionario.\n', diccionario, '\n', copia_diccionario)

copia_diccionario.clear()
print('Se ha borrado la copia_diccionario: ', copia_diccionario)
print()

# Diccionarios anidados y constructor dict
print('Diccionario anidado y manejo del constructor dict:\n')
personas = {
    'Cristian':{
        'nombre': 'Cristian',
        'edad': 41,
        'altura': 1.8,
        'sexo': 'Varon'
    }, # OJO, hay que poner coma para separar los diccionarios internos
    'Julia':{
        'nombre': 'Julia',
        'edad': 43,
        'altura': 1.73,
        'sexo': 'Mujer'
    }
}

print('Diccionarios de personas anidado: ', personas, '\n')

# Con el constructor

perros = dict(nombre='Dama', edad=12, sexo='Hembra')
print('Diccionario de perros: ', perros)

