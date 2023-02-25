from cargaTexto import cargarTexto, grafica, filtradoPorActor
from cargaTexto import ruta
movieList=[]
listaPelis=[]
ruta=""

print("Lenguajes formales y de programacion")
print("Seccion B-")
print("202000353")
print("Billy David Must Ochoa")
input()
opcion=0
opGestion=0
contador=1
opFiltro=0

while opcion!=5:
    print("--------------")
    print("Menu principal")
    print("1)Carga")
    print("2)Gestion")
    print("3)Filtro")
    print("4)Grafico")
    print("5)Salir")
    print("--------------")
    print("Ingrese una opcion para continuar")
    opcion=int(input())
    if opcion==1:
        #cargar archivos
        print("cargar archivo")
        ruta=cargarTexto(movieList)
        print("CARGO EXITOSAMENTE\n")
        pass
    elif opcion==2:
        while opGestion!=3:
            print("--------------")
            print("Gestion de peliculas")
            print("1)Mostrar Películas")
            print("2)Mostrar Actores")
            print("3)Regresar")
            print("Ingrese una opcion para continuar")
            opGestion=int(input())
            if opGestion==1:
             for i in movieList:
                i.showInfo()
             break   
              
            if opGestion==2:
               for i in movieList:                
                    print(str(contador) , " ", str(i.showPeliculasEnum()))
                    contador+=1
            contadorActor=1    
            print("ingrese un numero para mostrar actores en la pelicula")
            opcionPelicula=int(input())
            for k in movieList:
                if opcionPelicula==contadorActor:
                    k.showActoresPeli()
                    break
                else:
                    contadorActor+=1
                pass

            if opGestion==3:
                
                pass
        #gestionar archvos
        pass
    elif opcion==3:
        #filtrar datos
        while opFiltro!=3:
            print("-------------")
            print("1)Filtrado por actor")
            print("2)Filtrado por año")
            print("3)Filtrado por genero")
            print("4)Regresar")
            print("---------------")
            print("ingrese una opcion para continuar")
            opFiltro=int(input())
            if opFiltro==1:
                print("ingrese un nombre para buscar")
                nombre=str(input())
                filtradoPorActor(movieList, nombre,ruta)
                for i in movieList:
                    i.showPeliculasActor()

                pass
            if opFiltro==2:
                pass
            if opFiltro==3:
                pass
            if opFiltro==4:
                pass              
            pass##pass de el while


        input()#input que espera una instruccion
        pass #pass de elif
    elif opcion==4:
        grafica(movieList)


        #graficar
        input()
        pass
    elif opcion==5:
        #terminar ejecución´
        print("ejecucion terminada por el usuario")
        break 






