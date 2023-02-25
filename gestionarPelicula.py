from cargaTexto import cargarTexto


class gestion:
    def __init__(self,name, actor):
        self.name=name
        self.actor=actor
    def showInfoMovie(self):
        print("\nNOMBRE PELICULA: ",self.name) 
    
def mostrarPelicula(lista):
    for i in lista:
        

