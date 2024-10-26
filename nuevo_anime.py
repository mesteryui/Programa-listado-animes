import xml.etree.ElementTree as ET 

arbol = ET.parse("lista-animes.xml")
raiz = arbol.getroot()

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

arbol.write("lista-animes.xml", encoding="utf-8", xml_declaration=True)