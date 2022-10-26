class Animal: # Clase padre
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal): # Clase hija
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya): # La extensión logramos que podemos agregar funciones específicas de la clase hija, y que no tiene que tener padre
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola soy la extensión de la clase init padre')


class Perro(Animal):    # Clase hija
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):    # Hay que tener cuidado a extender, pq podríamos estar ejecuntado solo las funciones de la clase hija.
        super().__init__(nombre, onomatopeya)
        print('Otro modo de instaciación y extensión')

class Canario(Animal): # Clase hija
    tipo = 'canario'


gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

