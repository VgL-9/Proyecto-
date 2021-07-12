import matplotlib.pyplot as plt
from numpy import mod, true_divide
listaDeDatos = []
def leer_archivo():
    with open("Covid-19.csv","r",encoding="utf-8") as f:    # Abro el archivo en modo de lectura con encoding utf-8 para leer bien los caracteres espaciales
        for i in f.readlines(): # Recorro cada seldilla del excel
            datos = i.split(",")    #Convierto cada seldilla en una lista
            listaDeDatos.append(datos)  # introduzco la lista creada en la lista de datos
        listaDeDatos.pop(0) # elimino la primera lista ya que esta contiene las regiones

def listaComunasValidacion():
    listaParaValidacionComunas = []
    for i in listaDeDatos:  # Recorre la lista con los datos
        if len(i[3])>0: # esta condicion es para eliminar las listas que no tengan codigo de comuna ya que no serian comunas
            listaParaValidacionComunas.append(i[2]) # A la nueva lista le introduzco el dato de la lista en el indice 2 el que seria la comuna
            listaParaValidacionComunas.append(i[3]) # A la nueva lista le introduzco el dato de la lista en el indice 3 el que seria el codigo de region
    if len(listaParaValidacionComunas)%2 == 0:  # Veo si la lista es par o impar para darle un formato distinto en caso de que sea uno o lo otro
        print("/"*69)
        print("/"+" "*25+"Listado de Comunas"+" "*24+"/")
        print("/"+" "*67+"/")
        for i in range(0,len(listaParaValidacionComunas)-1,4):  # si es par recorro cada 4 para imprimir 2 comunas a la vez, cada una junto a su codigo
            espaciosFaltante  = " " * (25-len(listaParaValidacionComunas[i]))
            espaciosFaltante2 = " " * (25-len(listaParaValidacionComunas[i+2]))
            print("/ {}{}[{}] {}{}[{}] /".format(listaParaValidacionComunas[i],espaciosFaltante,listaParaValidacionComunas[i+1]
            ,listaParaValidacionComunas[i+2],espaciosFaltante2,listaParaValidacionComunas[i+3]))
        print("/"*69)
    else:
        for i in range(0,len(listaParaValidacionComunas)-1,6):  # si es impar recorro cada 6 para imprimir 3 comunas a la vez, cada junto a su codigo
            espaciosFaltante = 20-len(listaParaValidacionComunas[i])
            espaciosFaltante2 = 20-len(listaParaValidacionComunas[i+2])
            espaciosFaltante3 = 20-len(listaParaValidacionComunas[i+4])
            print("{}{}[{}] {}{}[{}] {}{}[{}]".format(listaParaValidacionComunas[i],
            espaciosFaltante,listaParaValidacionComunas[i+1],
            listaParaValidacionComunas[i+2],espaciosFaltante2,listaParaValidacionComunas[i+3],
            listaParaValidacionComunas[i+4],espaciosFaltante3,listaParaValidacionComunas[i+5]))
    return listaParaValidacionComunas   # Retorno la lista de validacion para ocuparla

def filtroDatosComuna(comuna):  # Ingresa la comuna que eligio el usuario
    for lista in listaDeDatos:  # recorre la lista con los datos
        if comuna in lista: # pregunto si la comuna ingresa por el usuario esta en la lista ya que si lo esta, deberia ser los datos que buscamos
            datoFiltrado = []
            for count in range(len(lista)-9,len(lista)-1):  # ocupo las longitudes de las lista -1 y -9 para recorrer los indices de la lista y no llegar al ultimo
                datoFiltrado.append(int(float(lista[count])))   # que es donde estaria la tasa y no la necesito, tambien al estar en -9 obtengo 8 datos
    return datoFiltrado # el octavo nos servira en caso de que necesitemos los no acumulado

def datoNoAcumulado(datoFiltrado):    # Aqui ingresa el dato de comuna Acumulado obtenido en los datos filtrados
    listaDatoNoAcumulado = []
    for i in range(1,len(datoFiltrado)):    # Recorro los datos iniciando en el 1 ya que para obtener los datos no acumulados es la resta del anterior al sucesor
        operacion = datoFiltrado[i] - datoFiltrado[i-1] 
        listaDatoNoAcumulado.append(int(operacion)) # Guardo en la lista el dato obtenido
    return listaDatoNoAcumulado

def listaRegionUsuario_Validacion(): 
    listaParaValidacionRegion = []
    for i in listaDeDatos: # Recorre la lista con los datos
        if i[0] not in listaParaValidacionRegion: 
            listaParaValidacionRegion.append(i[0]) # a la lista nueva le introduzco el dato de la lista en el indice 0 que seria la region
            listaParaValidacionRegion.append(i[1]) # a la lista nueva le introduzco el dato de la lista en el indice 1 que seria el codigo
    if len(listaParaValidacionRegion)%2 == 0: # Verifico si la lista es par o impar para darle un formato distinto en caso de que sea uno o lo otro
        print("/"*63)
        print("/"+" "*22+"Listado de Comunas"+" "*21+"/")
        print("/"+" "*61+"/")
        for i in range(0,len(listaParaValidacionRegion)-1,4): # si es par recorro cada 4 para imprimir 2 comunas a la vez, cada una junto a su codigo
            espaciosFaltante  = " " * (25-len(listaParaValidacionRegion[i]))
            espaciosFaltante2 = " " * (25-len(listaParaValidacionRegion[i+2]))
            print("/ {}{}[{}] {}{}[{}] /".format(listaParaValidacionRegion[i],espaciosFaltante,listaParaValidacionRegion[i+1]
            ,listaParaValidacionRegion[i+2],espaciosFaltante2,listaParaValidacionRegion[i+3]))
        # print(f"{listaParaValidacionRegion[i]}[{listaParaValidacionRegion[i+1]}]")
        print("/"+" "*61+"/")
        print("/"*63)
    else:
        print("/"*33)
        print("/"+" "*6+"Listado de Comunas"+" "*7+"/")
        print("/"+" "*31+"/")
        for i in range(0,len(listaParaValidacionRegion)-1,2):
            espaciosFaltante  = " " * (25-len(listaParaValidacionRegion[i]))
            print("/ {}{}[{}] /".format(listaParaValidacionRegion[i],espaciosFaltante,listaParaValidacionRegion[i+1]))
        # print(f"{listaParaValidacionRegion[i]}[{listaParaValidacionRegion[i+1]}]")
        print("/"+" "*31+"/")
        print("/"*33)
    return listaParaValidacionRegion # Retorno la lista de validacion para ocuparla

def filtroRegion(region):
    filtrada = []
    for i in listaDeDatos:  # Recorro la lista de datos
        if region in i:   # Compruebo de la region se encuentra en la lista para guardarla en caso de que sea asi
            filtrada.append(i)
    return filtrada

def datosRegionAcumulado(filtrada):
    listaDatosRegion = [0,0,0,0,0,0,0,0] # lista creada solo para ir sumando con los indices
    for comuna in filtrada:
        contador = 0 # es ocupado para obetener el indice de la lista donde estaran las sumas de todo
        for i in range(len(comuna)-9,len(comuna)-1,1):  # Este for obtiene 8 datos ya que son necesario 8 datos para obtener el no acumulado si es necesario
            listaDatosRegion[contador] = int(listaDatosRegion[contador] + float(comuna[i])) # voy sumando lo que ya estaba en la lista y el nuevo valor obtenido de la otra comuna
            contador += 1
        contador = 0 # reinicio valor para seguir con otra comuna
    return listaDatosRegion

def listadoRegionesAnalisis():
    listaRegionesAnalisis = []
    for i in listaDeDatos:  # recorro los datos
        if i[0] not in listaRegionesAnalisis:   # obtengo las regions, el not es para que no se repitan los datos
            listaRegionesAnalisis.append(i[0])
    return listaRegionesAnalisis

def tasaRegion():
    listaRegionesAnalisis = listadoRegionesAnalisis()   # Invoco a el listado de regionesAnalisis
    tasas = []
    for region in listaRegionesAnalisis:    # recorro el listado de regiones
        poblacion = 0
        acumulado = 0
        for i in listaDeDatos:  # recorro la lista de datos
            if region in i and len(i[3])>0: # region in i esta para ver si en la lista de datos se encuentra la region y ademas el len(i[3])>0 es para verificar que sea una comuna
                poblacion += int(float(i[4]))   # se obtienen las poblaciones de las comunas
                acumulado += int(float(i[len(i)-2]))    # se obtienen los ultimos datos acumulados de las comunas
        tasa = (acumulado/poblacion) * 100000   # formula para obtener una tasa
        tasas.append(round(tasa,1)) # redonde la tasa y la dejo en la lista de tasas
    return tasas,listaRegionesAnalisis

def graficoTasas():
    datos = tasaRegion()    # Invoco a la funcion tasa ragion
    mayortasa = max(datos[0])   # busco con la funcion max la mayor tasa de la lista
    menortasa = min(datos[0])   # busco con la funcion min la menor tasa de la lista
    regionMayor = datos[1][datos[0].index(mayortasa)]   # las tasas se sacaron en el orden que se encontraron las region de los datos por lo tanto
    regionMenor = datos[1][datos[0].index(menortasa)]   # el indice de las tasas y la regiones coincidira
    plt.ion()                                           # por eso busco el inice del mayor dato en la lista de datos y ocupo ese indice para buscar
    plt.bar(datos[1],datos[0])                          # la region en la lista de regiones
    plt.title("Regiones con mayor tasa de contagio y menor tasa de contagios", fontsize= 25)
    plt.xticks(rotation = 90)
    plt.tight_layout(pad=1, w_pad= 0, h_pad=0)
    plt.margins(y= 0.2)
    plt.annotate('Mayor tasa',fontsize= 15, xy=(regionMayor, mayortasa), xytext=(regionMayor, mayortasa+1000),
                arrowprops=dict(facecolor='red', shrink=0.04),)
    plt.annotate('Menor tasa', fontsize= 15, xy=(regionMenor, menortasa), xytext=(regionMenor, menortasa+3000),
                arrowprops=dict(facecolor='red', shrink=0.04),)
    mng = plt.get_current_fig_manager()    
    mng.window.showMaximized()
    plt.show()

def Analaisis(graficoY,tipoDeContagio): # En la funcion analisis ingresaran los datos de GraficoY y el tipo de contagio
    if tipoDeContagio == "no acumulativo":
        media = graficoY.sort() # Ordeno la lista para sacar la media
        media = graficoY[len(graficoY)//2]  # Parto la longitud de la lista en 2 para obtener el indice del dato del medio
        promedio = 0
        for valor in graficoY:  # recorro graficoY para sumar todos los datos de la lista
            promedio += valor
        promedio = round(promedio/len(graficoY),2)  # ocupo la funcion roun para obtener datos con menos decimales
        mayorDato = max(graficoY)
        modaDato = 0
        contador = 0
        for dato in graficoY:
            repit = graficoY.count(dato)  # cuento cuantas veces se repite el dato en la lista  
            if repit > contador and repit > 1: # la condicion repit > contador esta para verificar que la repeticion del dato sea mayor al que se asigno anteriormente
                contador = repit    # la condicion de repit > 1 esta para evitar que asigne una moda si es que no se repite mas de una vez ya que
                modaDato = dato     # si todas se repiten una vez no tendria moda
        if modaDato == 0:   # si moda dato es 0 significa que no tiene moda el dato por lo tanto no es necesario mostrar el dato
            return media,promedio,mayorDato
        else:
            return media,promedio,mayorDato,modaDato
    elif tipoDeContagio == "acumulativo":   # este no tiene moda ya que al ser acumulativo no deberia repetirse los datos como para decir que tiene moda
        media = graficoY.sort()
        media = graficoY[len(graficoY)//2]
        promedio = 0

        for valor in graficoY:
            promedio += valor

        promedio = round(promedio/len(graficoY),2)
        return media,promedio

def graficoGeneral(tipoDeContagio,datos,accion):    # A la funcion grafico general deberan ingresar los datos de tipo de contagio, datos,accion
    if tipoDeContagio == "no acumulativo":  # pregunto que tipo de dato necesita el usuario
        if accion == "1":   # Pregunto que tipo de grafico necesita el usuario          
            graficoY = datoNoAcumulado(datos) # Invoco a la funcion datoComunaNoAcumulado
            analisis = Analaisis(graficoY,tipoDeContagio)   # Invoco a la funcion Analisis
        else:
            graficoY = datosRegionAcumulado(datos)
            graficoY = datoNoAcumulado(graficoY)  # invoco a la funcion de Datos no acumulados
            analisis = Analaisis(graficoY,tipoDeContagio)
    elif tipoDeContagio == "acumulativo":
        if accion == "1":
            datos.remove(datos[0])  # Se remueve el dato 0 ya que este solo nos sirve en el no acumulativos
            graficoY = datos
            analisis = Analaisis(graficoY,tipoDeContagio)
        else:
            graficoY = datosRegionAcumulado(datos)  # Invoco a la funcion de deatos acumulado
            graficoY.remove(graficoY[0])
            analisis = Analaisis(graficoY,tipoDeContagio)
    x = ["1° Fecha","2° Fecha","3° Fecha","4° Fecha","5° Fecha","6° Fecha","7° Fecha"]
    plt.xlabel("Datos cada 3 dias.")
    plt.ylabel("Contagios "+tipoDeContagio)
    plt.title("Grafico de contagos "+ tipoDeContagio+" en las ultimas 7 fechas")
    plt.tight_layout(pad=1, w_pad= 3, h_pad=0)
    plt.suptitle('Fuente: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto1', fontsize=10)
    if len(analisis) == 3:
        plt.xlabel("Analisis Grafico\nMedia: "+str(analisis[0])+"\nMediana: "+str(analisis[1])+
        "\nMayor dato: "+str(analisis[2]),color="red",loc="left")
    elif len(analisis) == 4:
        plt.xlabel("Analisis Grafico\nMedia: "+str(analisis[0])+"\nMediana: "+str(analisis[1])+
        "\nMayor dato: "+str(analisis[2])+"\nModa: "+str(analisis[3]),color="red",loc="left")       
    else:
        plt.xlabel("Analisis Grafico\nMedia: "+str(analisis[0])+"\nMediana: "+str(analisis[1]),color="red",loc="left")
    mng = plt.get_current_fig_manager()    
    mng.window.showMaximized()
    plt.plot(x,graficoY)    # Ingreso los datos finales del ejeY y la variable X
    plt.show()

accion = "0"
leer_archivo()
TipoNoAcumulado = "Grafico de datos no acumulado"
TipoAcumulado = "Grafico de datos acumulado"
arribaAbajoMenu = "/"*80
espaciosMenu = "/"+" "*78+"/"
preguntaMenu = "/"+" "*31+"¿Que desea hacer?"+" "*30+"/"

while accion != "4":    # Estructura repetitiva para que no se cierre el programa a menos que el usuario ponga la opcion
    print(arribaAbajoMenu)
    print(preguntaMenu)
    print(espaciosMenu)
    print("/ (1) filtrar Datos por Comuna"+" "*49+"/")
    print("/ (2) filtrar Datos por Region"+" "*49+"/")
    print("/ (3) Ver Region con mayor tasa de contagios y menor"+" "*27+"/")
    print("/ (4) Salir del programa"+" "*55+"/")
    print(espaciosMenu)
    print(arribaAbajoMenu)
    accion = input("Ingrese alguna de las alternativas: ")
    while accion not in ["1","2","3","4"]:# Validacion para que el usuario ingrese una opcion valida
        accion = input("Ingrese alguna de las alternativas validas: ")

    if accion == "1":
        validacionComuna = listaComunasValidacion() # Invoco a la funcion de listaComunasValidacion y guardo lo que retorna
        print("El menu contiene Comuna(Codigo)")
        comuna = input("Ingrese el nombre de la comuna o su codigo: ")
        while comuna not in validacionComuna:   # verifico que la comuna ingresada por el usuario este en la lista
            comuna = input("Ingrese el nombre de la comuna o su codigo: ")
        datos = filtroDatosComuna(comuna)   # Invoco a la funcion filtro comuna

        print(arribaAbajoMenu)
        print(preguntaMenu)
        print(espaciosMenu)
        print("/ (1) Mostrar un gráfico de contagiados no acumulativos de la comuna"+" "*11+"/")
        print("/ (2) Mostrar un gráfico de contagiados acumulativos de la comuna"+" "*14+"/")
        print(espaciosMenu)
        print(arribaAbajoMenu)
        graficoAccion = input("Ingrese eleccion: ")

        while graficoAccion not in ["1","2"]:   # Validacion para que el usuario ingrese alguna de las disponibles
            graficoAccion = input("Ingrese eleccion: ")  

        if graficoAccion == "1":
            tipoDeContagio = "no acumulativo"
            graficoGeneral(tipoDeContagio,datos,accion) # invoco a la funcion grafico general
        else:
            tipoDeContagio = "acumulativo"          
            graficoGeneral(tipoDeContagio,datos,accion)

    elif accion == "2":
        validacionRegion = listaRegionUsuario_Validacion()  # Invoco a la funcion
        print("El menu contiene Region[Codigo]")
        region = input("Ingrese el codigo de region o Nombre: ")
        while region not in validacionRegion:   # compruebo que lo ingresado por el usuario sea valido
            region = input("Ingrese el codigo de region o nombre: ") 
        datos = filtroRegion(region)  # Llamo a la funcion filtro region

        print(arribaAbajoMenu)
        print(preguntaMenu)
        print(espaciosMenu)
        print("/ (1) Mostrar un gráfico de contagiados no acumulativos de la Region"+" "*11+"/")
        print("/ (2) Mostrar un gráfico de contagiados acumulativos de la Region"+" "*14+"/")
        print(espaciosMenu)
        print(arribaAbajoMenu)
        graficoAccion = input("Ingrese eleccion: ")
        while graficoAccion not in ["1","2"]:   # Validacion para que el usuario ingrese una opcion valida
            graficoAccion = input("Ingrese eleccion: ")

        if graficoAccion == "1":
            tipoDeContagio = "no acumulativo"
            graficoGeneral(tipoDeContagio,datos,accion)
        else:
            tipoDeContagio = "acumulativo"
            graficoGeneral(tipoDeContagio,datos,accion) 
    elif accion == "3":
        graficoTasas()  #   Invoco a la funcion grafico tasas
