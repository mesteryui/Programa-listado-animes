import xml.etree.ElementTree as ET

# Cargamos el archivo XML
arbol = ET.parse("lista-animes.xml")
raiz = arbol.getroot()

# Obtenemos el nombre del anime a buscar
nombre = input("Dime el nombre del anime:")

# Indicamos que queremos desde la etiqueta anime nos vamos a la etiqueta nombre que esta dentro de esta ultima y buscamos el contenido
anime = raiz.find("anime[nombre='" + nombre + "']")

print("\nNombre del Anime: " + anime.find('nombre').text)
print("Estado: " + anime.find('estado').text)
print("Episodios Vistos: " + anime.find('episodiosVistos').text)

