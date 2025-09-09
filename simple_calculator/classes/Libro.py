





class Libro:
    """ Clase libro chevere """
    def __init__(self, nombre):
        """
        Constructor de la clase libro

        Argumentos:
        que onda -- que onda


        """
        self.nombre = nombre


    def leer(self, a):
        print(f"{self.nombre} leo y {a}")






class Blue(Libro):
    def __init__(self, nombre, blueParam):
        Libro.__init__(self, nombre)
        self.blueParam = blueParam
