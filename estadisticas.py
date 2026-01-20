import os
import random

from busqueda import (busqueda_secuencial, busqueda_indexada, crear_indice, ARCHIVO_INDICE)

DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
RUTA_DATOS = os.path.join(DIRECTORIO_BASE, "datos")
ARCHIVO_INDICE = os.path.join(RUTA_DATOS, "index.txt")

def obtener_carnes_aleatorios(num_carnes=10):
    """Obtiene carnés aleatorios del conjunto de datos existente"""
    carnes = []
    archivos = sorted(
        f for f in os.listdir(RUTA_DATOS)
        if f.startswith("estudiantes_")
    )
    
    todos_carnes = []
    for nombre_archivo in archivos:
        ruta = os.path.join(RUTA_DATOS, nombre_archivo)
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                carne = linea.split("|")[0]
                todos_carnes.append(carne)
    
    if len(todos_carnes) > 0:
        num_seleccionar = min(num_carnes, len(todos_carnes))
        carnes = random.sample(todos_carnes, num_seleccionar)
    
    return carnes

def comparar_busquedas(num_pruebas=10):
    """
    Ejecuta ambos tipos de búsqueda con carnés aleatorios y genera una tabla comparativa.
    
    Args:
        num_pruebas: Número de carnés diferentes a buscar
    """
    print("=" * 100)
    print("COMPARACIÓN DE MÉTODOS DE BÚSQUEDA")
    print("=" * 100)
    
    if not os.path.exists(ARCHIVO_INDICE):
        print("\nCreando índice...")
        crear_indice()
        print("Índice creado exitosamente.\n")
    
    print(f"Obteniendo {num_pruebas} carnés aleatorios...")
    carnes = obtener_carnes_aleatorios(num_pruebas)
    print(f"Se seleccionaron {len(carnes)} carnés para las pruebas.\n")
    
    resultados = []
    
    for i, carne in enumerate(carnes, 1):
        print(f"Ejecutando prueba {i}/{len(carnes)} - Carné: {carne}")
        
        res_sec = busqueda_secuencial(carne)
        res_idx = busqueda_indexada(carne)
        
        resultados.append({
            "carne": carne,
            "sec": res_sec,
            "idx": res_idx
        })
    
    print("\n" + "=" * 100)
    print("TABLA COMPARATIVA DE RESULTADOS")
    print("=" * 100)
    
    print(f"\n{'Carné':<15} {'Método':<15} {'Archivos':<12} {'Líneas':<12} {'Tiempo (ms)':<15}")
    print("-" * 100)
    
    for res in resultados:
        carne = res["carne"]
        
        print(f"{carne:<15} {'Secuencial':<15} {res['sec']['archivos_abiertos']:<12} "
              f"{res['sec']['lineas_leidas']:<12} {res['sec']['tiempo_ms']:<15.4f}")
        
        print(f"{'':<15} {'Indexada':<15} {res['idx']['archivos_abiertos']:<12} "
              f"{res['idx']['lineas_leidas']:<12} {res['idx']['tiempo_ms']:<15.4f}")
        
        print("-" * 100)
    
    print("\n" + "=" * 100)
    print("ESTADÍSTICAS PROMEDIO")
    print("=" * 100)
    
    prom_arch_sec = sum(r["sec"]["archivos_abiertos"] for r in resultados) / len(resultados)
    prom_lin_sec = sum(r["sec"]["lineas_leidas"] for r in resultados) / len(resultados)
    prom_tiempo_sec = sum(r["sec"]["tiempo_ms"] for r in resultados) / len(resultados)
    
    prom_arch_idx = sum(r["idx"]["archivos_abiertos"] for r in resultados) / len(resultados)
    prom_lin_idx = sum(r["idx"]["lineas_leidas"] for r in resultados) / len(resultados)
    prom_tiempo_idx = sum(r["idx"]["tiempo_ms"] for r in resultados) / len(resultados)
    
    print(f"\n{'Método':<15} {'Archivos':<12} {'Líneas':<12} {'Tiempo (ms)':<15}")
    print("-" * 100)
    print(f"{'Secuencial':<15} {prom_arch_sec:<12.2f} {prom_lin_sec:<12.2f} {prom_tiempo_sec:<15.4f}")
    print(f"{'Indexada':<15} {prom_arch_idx:<12.2f} {prom_lin_idx:<12.2f} {prom_tiempo_idx:<15.4f}")
    
    print("\n" + "=" * 100)
    print("MEJORA DE LA BÚSQUEDA INDEXADA")
    print("=" * 100)
    mejora_tiempo = ((prom_tiempo_sec - prom_tiempo_idx) / prom_tiempo_sec) * 100
    mejora_lineas = ((prom_lin_sec - prom_lin_idx) / prom_lin_sec) * 100
    
    print(f"\nReducción en tiempo: {mejora_tiempo:.2f}%")
    print(f"Reducción en líneas leídas: {mejora_lineas:.2f}%")
    print(f"Factor de velocidad: {prom_tiempo_sec / prom_tiempo_idx:.2f}x más rápida")
    print("=" * 100)
    
    return resultados