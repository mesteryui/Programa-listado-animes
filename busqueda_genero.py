from obtener_arbol import *

# Obtenemos el nombre del anime a buscar
def BuscarGenero():
    genero = input("Introduzca genero:")
    animes = accederArbol().findall("anime[genero='" + genero + "']")
    return animes

def MostrarGenero(animes):
    # Usamos un bucle for para iterar cada etiqueta anime que contenga el genero deseado
    for anime in animes:
        print("\nNombre del Anime: ", anime.find('nombre').text)
        print("Estado: ", anime.find('estado').text)
        print("Episodios Vistos: ", anime.find('episodiosVistos').text)
