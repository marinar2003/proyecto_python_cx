# Importar las funciones de los modulos creados
# Asegúrate de que las rutas 'src2' y los nombres de archivos 'data_procesos', 'estadisticas' sean correctos en tu proyecto
from src2.data_procesos import cargar_y_limpiar_datos
from src2.estadisticas import contar_cirugias_por_dia, obtener_cirugias_de_medico

if __name__ == "__main__":
    # ---Configuración de parámetros---
    # La 'r' convierte la cadena en un "raw string" para evitar errores con las barras invertidas.
    ruta_archivos = r'C:\Users\marin\OneDrive\Escritorio\DALTO\EJERCICIO PYTHON PRUEBA\proyecto_cirugias2\data2\prueba1.xlsx'
    
    # Carga y limpieza de datos
    df = cargar_y_limpiar_datos(ruta_archivos)
    print(df.head())# Muestra las primeras 5 filas para verificar que se cargó bien.
    
    # --- Parámetros a analizar ---
    medico_a_analizar = input("Ingrese el nombre del medico a consultar: ")
    fecha_inicio = input("Indique la fecha de inicio ej ('2025-08-01'): ")
    fecha_fin = input("Indique la fecha de finalización ej ('2025-08-12'): ")
    
    # ---Flujo de trabajo---
    print("--- 1. PROCESANDO DATOS ---")
    
    # Muestra estadisticas en consola
    if df is not None:
        
        print("\n--- 2. GENERANDO ESTADISTICAS ---")
        # Cuenta las cirugías por día para el médico
        cirugias_del_medico_por_dia = contar_cirugias_por_dia(df, medico_a_analizar, fecha_inicio, fecha_fin)
        print(f"\nEstadísticas del medico {medico_a_analizar}:\n{cirugias_del_medico_por_dia}")
        
        print("\n--- CIRUGÍAS REALIZADAS POR UN MÉDICO ---")
        # Obtiene los nombres y conteos de las cirugías
        cirugias_conteo = obtener_cirugias_de_medico(df, medico_a_analizar)
        
        if cirugias_conteo is not None and not cirugias_conteo.empty:
            print(f"\nCirugías realizadas por el Dr. {medico_a_analizar.upper()}:")
            
            # Recorre el resultado para imprimir cada cirugía y su cantidad
            for cirugia, cantidad in cirugias_conteo.items():
                print(f"- {cirugia}: {cantidad}")
        else:
            print(f"❌ No se encontraron cirugías para el Dr. {medico_a_analizar} o el nombre del médico no es válido.")
