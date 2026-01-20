from busqueda import busqueda_secuencial, busqueda_indexada, crear_indice, ARCHIVO_INDICE
from estadisticas import comparar_busquedas
import os

def main():
    """Función principal del programa"""
    print("\n" + "=" * 100)
    print(" " * 30 + "SISTEMA DE BÚSQUEDA DE ESTUDIANTES")
    print("=" * 100)
    
    while True:
        print("\n" + "-" * 100)
        print("MENÚ PRINCIPAL")
        print("-" * 100)
        print("1. Crear/Actualizar índice")
        print("2. Búsqueda secuencial (un carné)")
        print("3. Búsqueda indexada (un carné)")
        print("4. Comparar métodos de búsqueda")
        print("5. Salir")
        print("-" * 100)
        
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n" + "=" * 100)
            print("CREANDO/ACTUALIZANDO ÍNDICE")
            print("=" * 100)
            try:
                crear_indice()
                print("\nÍndice creado exitosamente.")
                print(f"Ubicación: {ARCHIVO_INDICE}")
            except Exception as e:
                print(f"\nError al crear el índice: {e}")
            
        elif opcion == "2":
            print("\n" + "=" * 100)
            print("BÚSQUEDA SECUENCIAL")
            print("=" * 100)
            carne = input("\nIngrese el carné a buscar: ").strip()
            
            if not carne:
                print("Error: Debe ingresar un carné válido.")
                continue
            
            try:
                print(f"\nBuscando carné '{carne}'...")
                resultado = busqueda_secuencial(carne)
                
                print("\n" + "-" * 100)
                if resultado['registro']:
                    print(f"REGISTRO ENCONTRADO:")
                    print(f"  {resultado['registro']}")
                else:
                    print(f"No se encontró el carné '{carne}'")
                
                print(f"\nESTADÍSTICAS DE BÚSQUEDA:")
                print(f"  • Archivos abiertos: {resultado['archivos_abiertos']}")
                print(f"  • Líneas leídas: {resultado['lineas_leidas']}")
                print(f"  • Tiempo transcurrido: {resultado['tiempo_ms']:.4f} ms")
                print("-" * 100)
            except Exception as e:
                print(f"\nError durante la búsqueda: {e}")
            
        elif opcion == "3":
            print("\n" + "=" * 100)
            print("BÚSQUEDA INDEXADA")
            print("=" * 100)
            
            if not os.path.exists(ARCHIVO_INDICE):
                print("\n✗ Error: El archivo índice no existe.")
                print("  Por favor, cree el índice primero (opción 1).")
                continue
            
            carne = input("\nIngrese el carné a buscar: ").strip()
            
            if not carne:
                print("Error: Debe ingresar un carné válido.")
                continue
            
            try:
                print(f"\nBuscando carné '{carne}'...")
                resultado = busqueda_indexada(carne)
                
                print("\n" + "-" * 100)
                if resultado['registro']:
                    print(f"REGISTRO ENCONTRADO:")
                    print(f"  {resultado['registro']}")
                else:
                    print(f"No se encontró el carné '{carne}'")
                
                print(f"\nESTADÍSTICAS DE BÚSQUEDA:")
                print(f"  • Archivos abiertos: {resultado['archivos_abiertos']}")
                print(f"  • Líneas leídas: {resultado['lineas_leidas']}")
                print(f"  • Tiempo transcurrido: {resultado['tiempo_ms']:.4f} ms")
                print("-" * 100)
            except Exception as e:
                print(f"\n✗ Error durante la búsqueda: {e}")
            
        elif opcion == "4":
            print("\n" + "=" * 100)
            print("CONFIGURACIÓN DE COMPARACIÓN")
            print("=" * 100)
            
            try:
                num_input = input("\n¿Cuántas pruebas desea ejecutar? [10]: ").strip()
                num = int(num_input) if num_input else 10
                
                if num <= 0:
                    print("Error: El número de pruebas debe ser mayor a 0.")
                    continue
                
                print(f"\nEjecutando {num} pruebas comparativas...\n")
                comparar_busquedas(num_pruebas=num)
                
            except ValueError:
                print("Error: Número inválido. Usando 10 pruebas por defecto.")
                comparar_busquedas(num_pruebas=10)
            except Exception as e:
                print(f"\nError durante la comparación: {e}")
                
        elif opcion == "5":
            print("\n" + "=" * 100)
            print(" " * 40 + "¡Hasta luego!")
            print("=" * 100 + "\n")
            break
            
        else:
            print("\nOpción inválida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()