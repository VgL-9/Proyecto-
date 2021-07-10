import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import mod, true_divide
from matplotlib import pyplot as plt

listaDeDatos = []
def leer_archivo():
    with open("Datos.csv","r",encoding="utf-8") as f:
        for i in f.readlines():
            datos = i.split(",")
            listaDeDatos.append(datos)

def listaComunasUsuario():
    comunasListadoUsuario= []
    for i in listaDeDatos:
        if i[2] != "Comuna" and len(i[9])>0:
            comunaFormato = i[2] + "(" + i[3] + ")"
            comunasListadoUsuario.append(comunaFormato)
    formato = ""
    count = 0
    for i in range(len(comunasListadoUsuario)):
        if count < 2 and i != len(comunasListadoUsuario)-1:
            formato = formato + comunasListadoUsuario[i] + "\t\t"
            count += 1
        else:
            formato = formato + comunasListadoUsuario[i] + "\t\t"
            count = 0
            print(formato)
            formato = ""

def listaComunasValidacion():
    listaParaValidacionComunas = []
    for i in listaDeDatos:
        if i[2] != "Comuna" and len(i[3])>0:
            listaParaValidacionComunas.append(i[2])
            listaParaValidacionComunas.append(i[3])
    return listaParaValidacionComunas

def filtroDatosComuna(comuna):
    for i in listaDeDatos:
        if comuna in i:
            datoFiltrado = []
            for count in range(len(i)-9,len(i)-1):
                datoFiltrado.append(int(float(i[count])))
    return datoFiltrado

def datoComunaNoAcumulado(datoFiltrado):
    listaDatoNoAcumulado = []
    for i in range(1,len(datoFiltrado)):
        operacion = datoFiltrado[i] - datoFiltrado[i-1]
        listaDatoNoAcumulado.append(int(operacion))
    return listaDatoNoAcumulado        

def listaRegionesUsuario():
    regionListadoUsuario = []
    for i in listaDeDatos:
        formato = i[0] + "[" + i[1] + "]"
        if formato not in regionListadoUsuario and i[0] != "Region":
            regionListadoUsuario.append(formato)
    for region in regionListadoUsuario:
        print(f"-{region}")

def listaRegionValidacion():
    listaParaValidacionRegion = []
    for i in listaDeDatos:
        if i[0] not in listaParaValidacionRegion and i[0] != "Region":
            listaParaValidacionRegion.append(i[0])
            listaParaValidacionRegion.append(i[1])
    return listaParaValidacionRegion

def filtroRegion(region):
    filtrada = []
    for i in listaDeDatos:
        if region in i:   # Compruebo si el datodefiltro el cual seria region esta en la lista para asi solo obtener las que coincidan
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

def datosGraficoNoAcumuladoRegion(listaDatosRegion):
    listaNoAcumulada = []
    for i in range(1 , len(listaDatosRegion)): # Este for empieza en 1 ya que para obtener los casos totales de una region seria el valor anterior menos el nuevo
        listaNoAcumulada.append(listaDatosRegion[i] - listaDatosRegion[i-1]) # Aqui hago la operacion y la ingreso a una lista
    return listaNoAcumulada

def listadoRegionesAnalisis():
    listaRegionesAnalisis = []
    for i in listaDeDatos:
        if i[0] not in listaRegionesAnalisis and i[0] != "Region":
            listaRegionesAnalisis.append(i[0])
    return listaRegionesAnalisis

def tasaRegion():
    listaRegionesAnalisis = listadoRegionesAnalisis()
    tasas = []
    for region in listaRegionesAnalisis:
        poblacion = 0
        acumulado = 0
        with open("Datos.csv","r",encoding="utf-8") as f:
            for i in f.readlines():
                linea = i.split(",")
                if region in linea and len(linea[3])>0:
                    poblacion += int(float(linea[4]))
                    acumulado += int(float(linea[len(linea)-2]))
        tasa = (acumulado/poblacion) * 100000
        tasas.append(round(tasa,1))
    return tasas,listaRegionesAnalisis
    
def graficoTasas():
    datos = tasaRegion()
    tasas = datos[0]
    regiones = datos[1]
    mayortasa = max(tasas)
    menortasa = min(tasas)
    regionMayor = regiones[tasas.index(mayortasa)]
    regionMenor = regiones[tasas.index(menortasa)]
    plt.ion()
    plt.bar(regiones,tasas)
    plt.title("Regiones con mayor tasa de contagio y menor tasa de contagios", fontsize= 25)
    plt.xticks(rotation = 90)
    plt.tight_layout(pad=1, w_pad= 0, h_pad=0)
    plt.margins(y= 0.2)
    plt.annotate('Mayor tasa',fontsize= 15, xy=(regionMayor, mayortasa), xytext=(regionMayor, mayortasa+1000),
                arrowprops=dict(facecolor='red', shrink=0.04),
                )
    plt.annotate('Menor tasa', fontsize= 15, xy=(regionMenor, menortasa), xytext=(regionMenor, menortasa+3000),
                arrowprops=dict(facecolor='red', shrink=0.04),
                )
    mng = plt.get_current_fig_manager()    
    plt.show()

def Analisis(graficoY,tipoDeContagio):
    if tipoDeContagio == "no acumulativo":

        mediana = graficoY.sort()
        mediana = graficoY[len(graficoY)//2]
        promedio = 0

        for valor in graficoY:
            promedio += valor

        promedio = round(promedio/len(graficoY),2)
        mayorDato = max(graficoY)
        mayorDato = graficoY[graficoY.index(mayorDato)]

        modaDato = 0
        contador = 0
        for dato in graficoY:
            repit = graficoY.count(dato)    
            if repit > contador and repit > 1:
                contador = repit
                modaDato = dato
        if modaDato == 0:
            return mediana,promedio,mayorDato
        else:
            return mediana,promedio,mayorDato,modaDato

    elif tipoDeContagio == "acumulativo":
        mediana = graficoY.sort()
        mediana = graficoY[len(graficoY)//2]
        promedio = 0

        for valor in graficoY:
            promedio += valor

        promedio = round(promedio/len(graficoY),2)
        print(mediana)
        print(promedio)
        return mediana,promedio

def graficoGeneral(graficoY,tipoDeContagio,analisis):
    x = ["Dia 1","Dia 2","Dia 3","Dia 4","Dia 5","Dia 6","Dia 7"]

    plt.xlabel("Datos cada 3 dias.")
    plt.ylabel("Contagios "+tipoDeContagio)
    plt.title("Grafico de contagos "+ tipoDeContagio+" en las ultimas 7 fechas")
    plt.tight_layout(pad=1, w_pad= 3, h_pad=0)
    plt.suptitle('Fuente: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto1', fontsize=10)
    if len(analisis) == 3:
        plt.xlabel("aaaaaaaaaaaaaaaa")
    else:
        plt.xlabel("Analisis Grafico: Media: "+str(analisis[0])+"\nMediana: "+str(analisis[1]),color="red",loc="left")
    mng = plt.get_current_fig_manager()   
    plt.plot(x,graficoY)
    plt.show()
    print(analisis)
    print(analisis[1])

accion = "0"

TipoNoAcumulado = "Grafico de datos no acumulado"
TipoAcumulado = "Grafico de datos acumulado"

while accion != "4":
    print("¿Que desea hacer?")
    print("(1) filtrar Datos por Comuna")
    print("(2) filtrar Datos por Region")
    print("(3) Ver Region con mayor tasa de contagios y menor")
    print("(4) Salir del programa")
    accion = input("Ingrese accion: ")

    while accion not in ["1","2","3","4"]:  # Validacion para que el usuario ingrese una opcion valida
        accion = input("Ingrese accion: ")

    if accion == "1":
        validacionComuna = listaComunasValidacion()
        listaComunasUsuario()
        print("El menu contiene Comuna(Codigo)")
        comuna = input("Ingrese el nombre de la comuna o su codigo: ")

        while comuna not in validacionComuna:
            comuna = input("Ingrese el nombre de la comuna o su codigo: ")
        
        datos = filtroDatosComuna(comuna)

        print("¿Que desea hacer?")
        print("(1) Mostrar un gráfico de contagiados no acumulativos de la comuna")
        print("(2) Mostrar un gráfico de contagiados acumulativos de la comuna")
        print("Los graficos se haran en base a las 7 ultimas fechas")
        graficoAccion = input("Ingrese eleccion: ")

        while graficoAccion not in ["1","2"]:
            graficoAccion = input("Ingrese eleccion: ")  

        if graficoAccion == "1":
            tipoDeContagio = "no acumulativo"
            graficoY = datoComunaNoAcumulado(datos)
            analisis = Analisis(graficoY,tipoDeContagio)
            graficoGeneral(graficoY,tipoDeContagio,analisis)
        else:
            tipoDeContagio = "acumulativo"
            datos.remove(datos[0])
            graficoY = datos
            analisis = Analisis(graficoY,tipoDeContagio,analisis)           
            graficoGeneral(graficoY,tipoDeContagio,analisis)

    elif accion == "2":
        validacionRegion = listaRegionValidacion()
        listaRegionesUsuario()
        print("El menu contiene Region[Codigo]")
        region = input("Ingrese el codigo de region o Nombre: ")

        while region not in validacionRegion:
            region = input("Ingrese el codigo de region o nombre: ") 

        datos = filtroRegion(region)  

        print("¿Que desea hacer?")
        print("(1) Mostrar un gráfico de contagiados no acumulativos de la Region")
        print("(2) Mostrar un gráfico de contagiados acumulativos de la Region")
        print("Los graficos se haran en base a las 7 ultimas fechas")
        graficoAccion = input("Ingrese eleccion: ")
leer_archivo()