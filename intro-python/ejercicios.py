# dato = input('Ingrese dato: ')
#
#lista = ["hola", " mundo", "Chanchito", "Feliz"]
#if lista.count(dato) > 0:
#    print("EL dato existe", dato)
#else:
#    print("El dato no existe :( ", dato)

primero = input("Ingrese primer numero: ")
try:
    primero = int(primero)
except:
    primero = "a"

segundo = input('Ingrese segundo número: ')
try:
    segundo = int(segundo)
except:
    segundo = "a"

simbolo = input('Ingrese símbolo: ')

if primero == 'a' or segundo == 'a':
    print ('Ingresaste mal un dato, trata de ingresar solo numeros')
elif simbolo == "+":
    print('Suma: ', primero + segundo)
elif simbolo == '*':
    print('Multiplicación: ', primero * segundo)
elif simbolo == '/':
    print('División: ', primero / segundo)
elif simbolo == '-':
    print('Resta: ', primero - segundo)
else:
    print('El simbolo ingresado no es válido.')
