import matplotlib.pyplot as plt
from numpy import mod

def listaComunasUsuario():
    with open("Datos.csv","r",encoding="utf-8") as f:
        comunasListadoUsuario= []
        for i in f.readlines():
            linea = i.split(",")
            if linea[2] != "Comuna" and len(linea[9])>0:
                comunaFormato = linea[2] + "(" + linea[3] + ")"
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
    with open("Datos.csv","r",encoding="utf-8") as f:
        listaParaValidacionComunas = []
        for i in f.readlines():
            linea = i.split(",")
            if linea[2] != "Comuna" and len(linea[3])>0:
                listaParaValidacionComunas.append(linea[2])
                listaParaValidacionComunas.append(linea[3])
    return listaParaValidacionComunas

def filtroDatosComuna(comuna):
    with open("Datos.csv","r",encoding="utf-8") as f:
        for i in f.readlines():
            linea = i.split(",")
            if comuna in linea:
                datoFiltrado = []
                for count in range(len(linea)-9,len(linea)-1):
                    datoFiltrado.append(int(float(linea[count])))
    return datoFiltrado