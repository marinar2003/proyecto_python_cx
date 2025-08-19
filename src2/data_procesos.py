# Importamos la libreria pandas
import pandas as pd

def cargar_y_limpiar_datos(ruta_archivos):
    """
    Carga un archivo Excel, limpia los valores vacíos y corrige nombres de materiales.
    
    Args:
        ruta_archivo (str): La ruta al archivo Excel.
    
    Returns:
        pd.DataFrame: Un DataFrame limpio y procesado, o None si el archivo no se encuentra.
    """
    try: 
        df = pd.read_excel(ruta_archivos)
        print("✅ Archivo cargado correctamente.")
        
        # Limpiar valores NaN con un guion.
        df = df.fillna('-')
        print("✅ Valores vacios reemplazados por '-'.")
        
        # Corregir nombres de las columnas "SIERRA" y "CIRUGIA".
        # ¡Corregido! Las modificaciones se aplican directamente a 'df' después de llenar NaN
        df['SIERRA'] = df['SIERRA'].str.replace('BOSH','SIERRA BOSH', regex=False)
        df['CIRUGIA'] = df['CIRUGIA'].str.replace('ARTO','ARTRO', regex=False)  
        
        # Asegurar que la columna "FECHA" sea del tipo datetime.   
        df['FECHA'] = pd.to_datetime(df['FECHA'])
        print("✅ Columna 'FECHA' convertida en formato fecha.") 
        
        return df

    except FileNotFoundError:
        print(f"❌ Error: El archivo '{ruta_archivos}' no fue encontrado.")
        print("Asegúrate de que el nombre y la ruta sean correctos.")
        return None