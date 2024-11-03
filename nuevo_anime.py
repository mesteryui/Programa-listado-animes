from obtener_arbol import *

def NuevoAnime():
    """Nos permite añadir un nuevo anime verficando primero si existe el archivo xml correspondiente
    si no existe lo crea y posteriormente añade el anime, si este existe solo añade el anime"""
    if not os.path.exists("lista-animes.xml"): # Comprobamos si existe el archivo XML
        crear_archivo_xml("lista-animes.xml", "animes") # Pasamos los parametros a una funcion XML
        añadirAnime()
    else:
        añadirAnime()

def añadirAnime():
    """Esta funcion añade un anime al XML primero obtenemos la informacion que queremos del anime y despues la escribimos
    en el fichero"""
    raiz = accederArbol() # Localizamos el elemento raiz

    nombre_anime = input("Introduzca el nombre del anime:")

    estado_anime = input("Introduzca el estado (Emision,Finalizado) del anime:")

    episodios_vistos = input("Episodios vistos:")

    anime = ET.SubElement(raiz,"anime") # Indica un subelemento dentro del elemento raiz donde escribiremos los datos, 
    # para añadir un anime nuevo tenemos que escribirlo dentro de este atributo cada vez añadiendolo otra vez para cada nuevo anime

    nombre_animeXML = ET.SubElement(anime,"nombre") #Indicamos que dentro del elemento anime añadiremos un subelemento nombre que sera el nombre de nuestro anime

    nombre_animeXML.text = nombre_anime # Igualamos el interior del elemento nombre como el nombre solicitado antes

    estado_animeXML = ET.SubElement(anime,"estado")
    estado_animeXML.text = estado_anime

    episodios_vistosXML = ET.SubElement(anime, "episodiosVistos")
    episodios_vistosXML.text = episodios_vistos

    arbol = ET.ElementTree(raiz)

    arbol.write("lista-animes.xml", encoding="UTF-8", xml_declaration=True) # Realiza el proceso de escribir en el XML