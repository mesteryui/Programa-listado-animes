import xml.etree.ElementTree as ET

# Cargamos el archivo XML
arbol = ET.parse("lista-animes.xml")
raiz = arbol.getroot()

# Obtenemos el nombre del anime a buscar
genero = input("Dime el genero por el que quieres buscar:")

# Indicamos que queremos desde la etiqueta anime nos vamos a la etiqueta nombre que esta dentro de esta ultima y buscamos el contenido
animes = raiz.find("anime[generp='" + genero + "']")

print("\nNombre del Anime: " + animes.find('nombre').text)
print("Estado: " + animes.find('estado').text)
print("Episodios Vistos: " + animes.find('episodiosVistos').text)