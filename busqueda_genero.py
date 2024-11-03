from obtener_arbol import *

# Obtenemos el nombre del anime a buscar
def BuscarGenero():
    genero = input("Introduzca genero:")
    animes = accederArbol().findall("anime[genero='" + genero + "']") # Obtenemos todas las etiquetas anime donde la subetiqueta genero sea fantasia
    return animes

def MostrarGenero(animes):
    """
    Mostramos los animes de un determinado genero que pasamos como parametro
    """
    # Usamos un bucle for para iterar cada etiqueta anime que contenga el genero deseado
    for anime in animes: # Iteramos los resultados de animes para obtener la informacion de cada etiqueta anime individual
        print("\nNombre del Anime: ", anime.find('nombre').text) # Imprimimos el interior de la etiqueta nombre
        print("Estado: ", anime.find('estado').text) # Imprimimos el interior de la etiqueta estado
        print("Episodios Vistos: ", anime.find('episodiosVistos').text) # Imprimimos el interior de la etiqueta episodios Vistos
