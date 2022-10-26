# c = open('chanchito.txt') # Abrimos todo el archivo
# print(c.read()) # Visualizamos el archivo abierto
#
# for x in c: # Al iterar cada linea podemos trabajar con cada una de ellas # por separado
#     print(x)
#
# c.close()

# OJO con los permisos con lo que se abre, w sobreescribe todo el archivo, "a" añade al final del archivo, "r" solo es lectura, "x" crea el archivo si no existiera

import os # Se podrán ejecutar comandos de SO

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
    print('El archivo ha sido eliminado')
else:
    print('El archivo no existe')

# os.rmdir('') borra directorio