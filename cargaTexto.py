class movie:
    def __init__(self,name, actor, year, genre):
        self.name=name
        self.actor=actor
        self.year=year
        self.genre=genre

    def showInfo(self):
        print("\nNOMBRE PELICULA: ",self.name, "\nAUTORES: ", self.actor,"\nAÑO ESTRENO: ", self.year,"\nGENERO: ", self.genre)
    
    def showPeliculasEnum(self):
        print("\nNOMBRE PELICULA: ",self.name)
    
    def showActoresPeli(self):
        print("AUTORES: ", self.actor)





ruta=None
def grafica(list):
    ruta=input("Ingrese la ruta del .lfp a leer: ")
    textoLfp=open(ruta, "r")
    lines= textoLfp.readlines()
    for i in lines:
        i=i.replace('\n', '')
        i=i.split(";")
        x={"Pelicula": i[0], "Autores": i[1], "Año": i[2], "Genero": i[3]}
        list.append(x)

    print(list)
    textoLfp.close
    textoDOT=open("imagen.dot","w")
    textoDOT.write("digraph{  \n")
    textoDOT.write('rankdir=LR \n')
    textoDOT.write('node[shape=record, fontname="Arial Black", fontsize=16] \n')
    for i in list:
        textoDOT.write(i["Pelicula"]+'->'+i["Autores"]+"\n")
    textoDOT.write(" } \n" )
    textoDOT.close

def filtradoPorActor(list,nombre):
    ruta=input("Ingrese la ruta del .lfp a leer: ")
    textoLfp=open(ruta, "r")
    lines= textoLfp.readlines()
    temp_name=None
    pelisEncontradas=0
    for i in lines:
        if nombre==temp_name:
            pelisEncontradas+=1
    if pelisEncontradas==0:
        None
    peliPorActor=[pelisEncontradas]
    pelisEncontradas=0
    for i in lines:
        if nombre==temp_name:
            peliPorActor[pelisEncontradas]
            pelisEncontradas+=1
        
    



def cargarTexto(list):
    ruta=input("Ingrese la ruta del .lfp a leer: ")
    textoLfp=open(ruta, "r")
    lines= textoLfp.readlines()

    for i in lines:
        i=i.split(";")
        contador=1
        tempo_name=None
        tempo_actor=None
        tempo_year=None
        tempo_genre=None
        
        for j in i:
            if contador==1:
                tempo_name=j
            elif contador==2:
                j=j.split(",")
                tempo_actor=j
            elif contador==3:
                tempo_year=j
            elif contador==4:
                tempo_genre=j
            contador+=1
        
        cine=movie(tempo_name, tempo_actor, tempo_year, tempo_genre)
        list.append(cine)



