import matplotlib.pyplot as plt
from numpy import mod

def listaComunasUsuario():
    with open("Datos\Datos.csv","r",encoding="utf-8") as f:
        comunasListadoUsuario= []
        for i in f.readlines():
            linea = i.split(",")
            if linea[2] != "Comuna" and len(linea[9])>0:
                comunaFormato = linea[2] + "(" + linea[3] + ")"
                comunasListadoUsuario.append(comunaFormato)
    menuComunas = str(comunasListadoUsuario)
    menuComunas = menuComunas.replace("'","").replace("[","").replace("]","")
    print(menuComunas)