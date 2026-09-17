import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d


plt.rcParams.update({'font.size': 12})

def cargar_datos(nombre_archivo:str)->pd.DataFrame:
    """ Carga los datos de los exoplanetas en un archivo csv y retorna el DataFrame con la informacion.
    Parametros:
        nombre_archivo (str): El nombre del archivo de los exoplanetas en CSV que se debe cargar
    Retorno:
        (DataFrame) : DataFrame con todos los datos contenidos en el archivo
    """
        
    df = pd.read_csv(nombre_archivo)
    return df
    
    


def histograma_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula el histograma con 30 grupos en el que debe
        aparecer la cantidad de planetas descubiertos por anho.
    Parametros:
        datos (DataFrame): DataFrame con la informacion de los  exoplanetas
    """

    data = datos.loc[(datos["DESCUBRIMIENTO"] >= 1988) & (datos["DESCUBRIMIENTO"] <= 2018)]
    print(data)

    max_year = data["DESCUBRIMIENTO"].max()
    min_year = data["DESCUBRIMIENTO"].min()


    plt.hist(data["DESCUBRIMIENTO"], bins=30)

    plt.xlabel("Años",fontsize=8)
    plt.ylabel("Cantidad de planetas descubiertos")
    plt.title("Cantidad de planetas descubiertos entre 1988 y 2018")
    plt.tick_params(axis='x', labelsize=8)
    plt.tight_layout()
    margen = 0
    plt.xlim(min_year - margen, max_year + margen)

    plt.show()
    
   
def estado_publicacion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de publicacion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    
    datos.boxplot(column='DESCUBRIMIENTO', by='ESTADO_PUBLICACION', figsize=(7,7), rot="90")
    plt.xlabel('Tipo de Publicación')
    plt.ylabel('Año de Descubrimiento')
    plt.title('Tipo de Publicación vs Año de descubrimiento')
    plt.show()
    

    

def deteccion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de deteccion
    Parametros:
        datos (DataFrame): DataFrame con la informacion de los exoplanetas
        
    """
    
    datos.boxplot(column='DESCUBRIMIENTO', by='TIPO_DETECCION', figsize=(7,7), rot="90")
    plt.xlabel('Tipo de detección')
    plt.ylabel('Año de Descubrimiento')
    plt.title('Tipo de detección vs Año de descubrimiento')
    plt.show()

    
def deteccion_y_descubrimiento(datos:pd.DataFrame,anho:int)->None:
    """ Despliega un diagrama de pie donde aparecen la cantidad de
        planetas descubiertos en un anho particular, clasificados de acuerdo
        con el tipo de publicacion.
        Si el anho es 0, se muestra la información para todos los planetas.
    Parametros:
        datos (DataFrame): DataFrame con la informacion de los exoplanetas
        anho (int): El anho para el que se quieren analizar los planetas descubiertos
                    o 0 para indicar que deben ser todos los planetas.
    """
    opcion = int(anho)
      
    if opcion == 0:
      
        tipos_deteccion = datos['TIPO_DETECCION'].value_counts()
        
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 6)
        plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8)
        ax.pie(tipos_deteccion, labels=tipos_deteccion.index, autopct='%1.0f%%', startangle=0, colors=['#7e5baf', '#9c9c9c','#eb9927','#2ed80f','#f089e4'])
        ax.set_title("Tipos de detección para todos los años")
        plt.show()
        
    elif opcion > 1000:
        year = int(opcion)
        
        tipos_deteccion = datos.loc[datos['DESCUBRIMIENTO'] == year]['TIPO_DETECCION'].value_counts()
        
        fig, ax = plt.subplots()
        ax.pie(tipos_deteccion, labels=tipos_deteccion.index, autopct='%1.0f%%', startangle=0,colors=['#7e5baf', '#9c9c9c','#eb9927','#2ed80f','#f089e4'])
        ax.set_title("Tipos de detección en todo el año " + str(year))
        plt.tight_layout()
        plt.show()
        
    else:
        print("Opción no válida")
    
def cantidad_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Despliega un diagrama de lineas donde aparece una linea por
        cada tipo de deteccion y se muestra la cantidad de planetas descubiertos
        en cada anho para esta deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    print(datos)
   
    
    df=datos
     
    table = pd.pivot_table(df, values='NOMBRE', index=['DESCUBRIMIENTO'], columns=['TIPO_DETECCION'], aggfunc='count')

    ax = table.plot(kind='line', figsize=(10,6), title="Cantidad de planetas descubiertos segun el tipo de detección")
    ax.set_xlabel("Año de descubrimiento")
    ax.set_ylabel("Cantidad de planetas")
    ax.legend(title='')
    margen = 0
    max_year = df["DESCUBRIMIENTO"].max()
    min_year = df["DESCUBRIMIENTO"].min()
    plt.xlim(min_year - margen, max_year + margen)
    plt.show()
    
    

def masa_promedio_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Despliega un diagrama de lineas donde aparece una linea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): DataFrame con la informacion de los exoplanetas
    """
    
    
    df = datos

    df_grouped = df.groupby(['TIPO_DETECCION', 'DESCUBRIMIENTO']).mean()['MASA'].reset_index()

    print(df_grouped)

 
    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_title('Masa promedio de los planetas por tipo de detección', fontsize=16)
    ax.set_xlabel('Año de descubrimiento', fontsize=14)
    ax.set_ylabel('Masa promedio ', fontsize=14)

    
    for tipo_det in df_grouped['TIPO_DETECCION'].unique():
        df_tipo_det = df_grouped[df_grouped['TIPO_DETECCION'] == tipo_det]
        ax.plot(df_tipo_det['DESCUBRIMIENTO'], df_tipo_det['MASA'], label=tipo_det)


    ax.legend()
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98))
    plt.show()
    
    

def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame)->None:
    """ Despliega un diagrama de dispersión donde en el eje x se
        encuentra la masa de los planetas y en el eje y se encuentra el logaritmo
        de la masa de las estrellas. Cada punto en el diagrama correspondera
        a un planeta y estara ubicado de acuerdo con su masa y la masa de la
        estrella más cercana.
    Parametros:
        datos (DataFrame): DataFrame con la informacion de los exoplanetas
    """
    
    

    data = pd.read_csv('exoplanetas.csv')


    plt.yscale('log')

    plt.scatter(data['MASA'], data['MASA_ESTRELLA'],s=8)

   
    plt.xlabel('Masa del planeta')
    plt.ylabel('Masa de la estrella (log)')
    plt.title('Masa del planeta vs. Masa de la estrella más cercana')

    plt.show()
    

def graficar_cielo(datos:pd.DataFrame)->list:
    """ Despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección utilizado.
    Parametros:
        datos (DataFrame): DataFrame con la informacion de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representacion del cielo
    """
 
    df = datos

    
    img = np.zeros((100, 200, 3))

    
    colors = {
        'Astrometry': [0.94, 0.65, 0.10],
        'Imaging': [0.34, 0.94, 0.10],
        'Microlensing': [0.94, 0.10, 0.10],
        'Other': [0.94, 0.10, 0.85],
        'Primary Transit': [0.10, 0.94, 0.85],
        'Radial Velocity': [0.1, 0.5, 0.94],
        'TTV': [1.0, 1.0, 1.0],
    }

    
    for i, row in df.iterrows():
       
        color = colors.get(row['TIPO_DETECCION'], [0.0, 0.0, 0.0])
        ra = row['RA']
        dec = row['DEC']
        row_idx = 99 - np.abs(int((np.sin(ra) * np.cos(dec) * 100)))
        
        col_idx = int((np.cos(ra) * np.cos(dec) * 100)) + 100
       
        img[row_idx, col_idx] = color

    
    plt.imshow(img)
    plt.show()
    

def filtrar_imagen_cielo(imagen:list)->None:
    """ Le aplica a la imagen un filtro de convolucion basado en la matriz
        [[-1,-1,-1],
         [-1,9,-1],
         [-1,-1,-1]]
    Parametros:
        imagen (list): Matriz con la imagen del cielo
    """
    df = pd.read_csv('exoplanetas.csv')

    img = np.zeros((100, 200, 3))

    
    colors = {
        'Astrometry': [0.94, 0.65, 0.10],
        'Imaging': [0.34, 0.94, 0.10],
        'Microlensing': [0.94, 0.10, 0.10],
        'Other': [0.94, 0.10, 0.85],
        'Primary Transit': [0.10, 0.94, 0.85],
        'Radial Velocity': [0.1, 0.5, 0.94],
        'TTV': [1.0, 1.0, 1.0],
    }

    
    for i, row in df.iterrows():
        color = colors.get(row['TIPO_DETECCION'], [0.94, 0.10, 0.85])
        ra = row['RA']
        dec = row['DEC']
        row_idx = 99 - np.abs(int((np.sin(ra) * np.cos(dec) * 100)))
        col_idx = int((np.cos(ra) * np.cos(dec) * 100)) + 100
        img[row_idx, col_idx] = color

    
    mask = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    img_conv = np.zeros_like(img)
    for i in range(3):
        img_conv[..., i] = convolve2d(img[..., i], mask, mode='same')


    plt.imshow(img_conv)
    plt.show()
    