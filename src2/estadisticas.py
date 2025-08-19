import pandas as pd 

def contar_cirugias_por_dia(df, medico, fecha_inicio, fecha_fin):
    """
    Filtra el DataFrame para un médico y un rango de fechas, y cuenta las cirugías por día.

    Args:
        df (pd.DataFrame): El DataFrame a procesar.
        medico (str): El nombre del médico a filtrar.
        fecha_inicio (str): La fecha de inicio del rango.
        fecha_fin (str): La fecha de fin del rango.

    Returns:
        pd.Series: Una Serie con el conteo de cirugías por fecha.
    """
    # Convertimos las fechas de filtro a tipo datetime.date para una comparación segura
    fecha_inicio_dt = pd.to_datetime(fecha_inicio).date()
    fecha_fin_dt = pd.to_datetime(fecha_fin).date()
    
    # Creamos una copia de la columna de fecha para evitar SettingWithCopyWarning
    df_con_fechas = df.copy()
    df_con_fechas['FECHA_DIA'] = df_con_fechas['FECHA'].dt.date
    
    # Aplicamos los filtros
    df_filtrado = df_con_fechas.loc[
        (df_con_fechas['FECHA_DIA'] >= fecha_inicio_dt) & 
        (df_con_fechas['FECHA_DIA'] <= fecha_fin_dt) & 
        (df_con_fechas['MEDICO'].str.upper() == medico.upper())
    ]
    
    if df_filtrado.empty:
        print(f"⚠️ No se encontraron cirugías para el Dr. {medico} en el rango de fechas especificado.")
        return pd.Series(dtype=int) # Retorna una serie vacía si no hay datos
        
    return df_filtrado.groupby('FECHA_DIA').size()

def obtener_cirugias_de_medico(df, medico):
    """
    Filtra y devuelve el conteo de cada cirugía que realizó un médico.

    Args:
        df (pd.DataFrame): El DataFrame con los datos de las cirugías.
        medico (str): El nombre del médico a buscar.

    Returns:
        pd.Series: Una Serie con el conteo de cada cirugía, o una Serie vacía si no se encuentra.
    """
    try:
        # Convertimos tanto la columna 'MEDICO' como el nombre del médico a mayúsculas para la comparación.
        df_filtrado = df[df['MEDICO'].str.upper() == medico.upper()]
        
        if df_filtrado.empty:
            print(f"⚠️ No se encontraron cirugías para el Dr. {medico}.")
            return pd.Series(dtype='object')
        
        # Devolvemos el conteo de cada cirugía en lugar de los nombres únicos
        return df_filtrado['CIRUGIA'].value_counts()
    except KeyError:
        print(f"❌ Error: La columna 'MEDICO' o 'CIRUGIA' no existe en el DataFrame.")
        return None
