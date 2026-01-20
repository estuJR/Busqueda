import os
import time

DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
RUTA_DATOS = os.path.join(DIRECTORIO_BASE, "datos")
ARCHIVO_INDICE = os.path.join(RUTA_DATOS, "index.txt")


def busqueda_secuencial(carne):
    inicio = time.perf_counter()

    archivos = sorted(
        f for f in os.listdir(RUTA_DATOS)
        if f.startswith("estudiantes_")
    )

    archivos_abiertos = 0
    lineas_leidas = 0

    for nombre_archivo in archivos:
        archivos_abiertos += 1
        ruta = os.path.join(RUTA_DATOS, nombre_archivo)

        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                lineas_leidas += 1
                campos = linea.strip().split("|")
                if campos[0] == carne:
                    fin = time.perf_counter()
                    return {
                        "registro": linea.strip(),
                        "archivos_abiertos": archivos_abiertos,
                        "lineas_leidas": lineas_leidas,
                        "tiempo_ms": (fin - inicio) * 1000
                    }

    fin = time.perf_counter()
    return {
        "registro": None,
        "archivos_abiertos": archivos_abiertos,
        "lineas_leidas": lineas_leidas,
        "tiempo_ms": (fin - inicio) * 1000
    }


    
# parten 2

def crear_indice():
    archivos = sorted(
        f for f in os.listdir(RUTA_DATOS)
        if f.startswith("estudiantes_")
    )

    with open(ARCHIVO_INDICE, "w", encoding="utf-8") as indice:
        for nombre_archivo in archivos:
            ruta = os.path.join(RUTA_DATOS, nombre_archivo)
            with open(ruta, "r", encoding="utf-8") as archivo:
                while True:
                    posicion = archivo.tell()
                    linea = archivo.readline()
                    if not linea:
                        break
                    carne = linea.split("|")[0]
                    indice.write(f"{carne}|{nombre_archivo}|{posicion}\n")


#funcion para la parte 3 
def busqueda_indexada(carne):
    inicio = time.perf_counter()

    archivos_abiertos = 0
    lineas_leidas = 0

    with open(ARCHIVO_INDICE, "r", encoding="utf-8") as indice:
        archivos_abiertos += 1
        for linea in indice:
            lineas_leidas += 1
            c, archivo_datos, posicion = linea.strip().split("|")
            if c == carne:
                ruta = os.path.join(RUTA_DATOS, archivo_datos)
                with open(ruta, "r", encoding="utf-8") as archivo:
                    archivos_abiertos += 1
                    archivo.seek(int(posicion))
                    registro = archivo.readline().strip()
                    fin = time.perf_counter()
                    return {
                        "registro": registro,
                        "archivos_abiertos": archivos_abiertos,
                        "lineas_leidas": lineas_leidas + 1,
                        "tiempo_ms": (fin - inicio) * 1000
                    }

    fin = time.perf_counter()
    return {
        "registro": None,
        "archivos_abiertos": archivos_abiertos,
        "lineas_leidas": lineas_leidas,
        "tiempo_ms": (fin - inicio) * 1000
    }