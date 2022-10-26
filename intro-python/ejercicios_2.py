# Multiplicar un número sin usar el operador de multiplicación
a = 8
b = 4
c = 0
for x in range (b):
    c += a
print(c)

# Ingresar nombre y apellidos e imprmirlos al revés
nombre = input('Deme su nombre: ')
apellido = input('Deme su primer apellido: ')
concatenacion = nombre + ' ' + apellido
print(concatenacion[::-1]) # Impirme de atrás a adelente

# Escribir una función que encuentre el elemento menor de una lista
def get_min(lista):
    resultado = min(lista)
    return print(resultado)
get_min([2,6,3,6548,346,98,346])

# Escribir una función que devuelve el volúmen de una esfera por su radio
# 4/3 * pi * r ** 3
def get_volume(radio):
    return 4/3*3.14*radio**3

calculo = get_volume(6)
print(calculo)

# Escribir una función que indique si el usuario es mayor de edad
age = int(input('Introduzca su edad: '))
def get_age(age):
    if age < 18:
        print('No puedes pasar, eres menor')
    else:
        print('Bienvenido')
get_age(age)

# Escribir una función que indique si el número es par o impar.
def get_even():
    number = int(input('Introduzca número: '))
    if number % 2 == 0:
        print('El número es par')
    else:
        print('El número es impar')
get_even()

# Escribir una función cuantas vocales tiene una palabra
def get_number_vowels():
    word_to_count = input('Introduzca palabra a contar vocales: ')
    word_to_count = word_to_count.lower()
    a = word_to_count.count('a')
    b = word_to_count.count('e')
    c = word_to_count.count('i')
    d = word_to_count.count('o')
    e = word_to_count.count('u')
    all_vowels = a + b + c + d + e
    return print('El número de vocales es: ', all_vowels)
get_number_vowels()

# Escribir un aplicacion que reciba un cantidad infinita de numeros hasta decir basta y que luego devuelva la suma de los numeros ingresados.
def get_infinite_sum():
    lst = []
    while True:
        number_str = input("Introduce un número o escribe \"break\" para parar y sumar los números: ")
        if number_str in {"break"}:
            break
        lst.append(int(number_str))

    print(lst)
    print("La cantidad de números a sumar es:", len(lst))
    print("La suma total de los números es: ", sum(lst))

get_infinite_sum()

# Escribir una función que reciba nombre y apellido y los agregue a un archivo
def agrega_nombre_a_archivo(nombre, apellido):
    with open ('nombrecompleto.txt', 'a') as c:
        c.write(nombre + ' ' + apellido + '\n')
agrega_nombre_a_archivo('Silvia', 'Perez')