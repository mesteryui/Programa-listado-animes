import xml.etree.ElementTree as ET

# Cargamos el archivo XML
arbol = ET.parse("lista-animes.xml")
raiz = arbol.getroot()

# Obtenemos el nombre del anime a buscar
genero = input("Dime el genero por el que quieres buscar:")


animes = raiz.findall("anime[genero='" + genero + "']")
for anime in animes:
    print("\nNombre del Anime: " + anime.find('nombre').text)
    print("Estado: " + anime.find('estado').text)
    print("Episodios Vistos: " + anime.find('episodiosVistos').text)