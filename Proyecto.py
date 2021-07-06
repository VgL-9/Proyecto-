import matplotlib.pyplot as plt
from numpy import mod, true_divide

def leer_archivo():
    listaDeDato = []

    with open("Datos.csv","r",encoding="utf-8") as f:
        for i in f.readlines():
            datos = i.split(",")
            listaDeDato.append(datos)

    return listaDeDato

listaDeDato = leer_archivo()

def listaComunasUsuario():
    comunasListadoUsuario= []
    for i in listaDeDato:
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
    for i in listaDeDato:
        if i[2] != "Comuna" and len(i[3])>0:
            listaParaValidacionComunas.append(i[2])
            listaParaValidacionComunas.append(i[3])
    return listaParaValidacionComunas

def filtroDatosComuna(comuna):
    for i in listaDeDato:
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
    with open("Datos.csv","r",encoding="utf-8") as f:
        regionListadoUsuario = []
        for i in f.readlines():
            linea = i.split(",")
            formato = linea[0] + "[" + linea[1] + "]"
            if formato not in regionListadoUsuario and linea[0] != "Region":
                regionListadoUsuario.append(formato)
    for region in regionListadoUsuario:
        print(f"-{region}")

def listaRegionValidacion():
    with open("Datos.csv","r",encoding="utf-8") as f:  
        listaParaValidacionRegion = []
        for i in f.readlines():
            linea = i.split(",") 
            if linea[0] not in listaParaValidacionRegion and linea[0] != "Region":
                listaParaValidacionRegion.append(linea[0])
                listaParaValidacionRegion.append(linea[1])
    return listaParaValidacionRegion

def filtroRegion(region):
    with open("Datos.csv","r",encoding="utf-8") as f:
        filtrada = []
        for i in f.readlines():
            linea = i.split(",")
            if region in linea:   # Compruebo si el datodefiltro el cual seria region esta en la lista para asi solo obtener las que coincidan
                filtrada.append(linea)
    return filtrada