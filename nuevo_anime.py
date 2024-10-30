from obtener_arbol import *

def añadirNuevoAnime():
    raiz = accederArbol()

    nombre_anime = input("Introduzca el nombre del anime:")

    estado_anime = input("Introduzca el estado (Emision,Finalizado) del anime:")

    episodios_vistos = input("Episodios vistos:")

    anime = ET.SubElement(raiz,"anime")

    nombre_animeXML = ET.SubElement(anime,"nombre")

    nombre_animeXML.text = nombre_anime

    estado_animeXML = ET.SubElement(anime,"estado")
    estado_animeXML.text = estado_anime

    episodios_vistosXML = ET.SubElement(anime, "episodiosVistos")
    episodios_vistosXML.text = episodios_vistos

    arbol = ET.ElementTree(raiz)

    arbol.write("lista-animes.xml", encoding="UTF-8", xml_declaration=True)