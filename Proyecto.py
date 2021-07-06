import matplotlib.pyplot as plt
from numpy import mod, true_divide

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


leer_archivo()