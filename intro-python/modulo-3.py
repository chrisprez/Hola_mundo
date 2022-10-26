from modulos import saludo, mascotas # Podemos importar funciones específicas del modulo que vayamos a usar
from camelcase import CamelCase # Este módulo se ha instalado con pip


print(mascotas)
saludo('Nicolas')   # Invocamos la funcion del otro modulo

c = CamelCase()
s = 'esta oracion necesita CamelCase'
camelcased = c.hump(s)
print(camelcased)