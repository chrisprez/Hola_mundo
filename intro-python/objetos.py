class Usuario:
    def __init__(self, nombre, apellido):
        '''
        Esta funcion se ejecuta la primera, por que la iniciliza la clase
        '''
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("hola mi nombre es:", self.nombre, self.apellido)


class Admin(Usuario):   # Creamos otra clase que heredará los métodos de la superclase o clase init

    def supersaludo(self):  # Se crea su propia función, con paramétro self para referirse a los métdos de la superclase
        print('hola me llamo', self.nombre, 'soy administrador')


usuario = Usuario("juan", "perez")
#usuario2 = Usuario("cristian", "perez")

#print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

usuario.nombre = "Chanchito"    #Modificar valor de la instancia
usuario.saludo()
# del usuario.nombre              # Borrar dato de la instnacia
# #usuario.saludo()
# del usuario                     # Borramos la propia instancia
# print(usuario)

admin = Admin("Crsitian", "Pérez") # Se pasan los parámetros a la clase hija a una varibale. La clase ha de escribirse en mayusc
admin.saludo()                      # Se invoca a la clase con la función padre, pero los parámetros anteriormente definidos.
admin.supersaludo()                 # Se invoca a la clase con la función hijo, y los parámetros definodos para esta.

#usuario.supersaludo()               # No se puede isntanciar desde padre a la clase hijo

