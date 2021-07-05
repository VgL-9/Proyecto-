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