from obtener_arbol import *
def BusquedaNombre():
    nombre = input("Introduzca nombre del anime:")
    anime = accederArbol().find("anime[nombre='" + nombre + "']")
    return anime

# Cargamos el archivo XML
def MostrarNombre(nombre):
  if nombre is not None:
    print("\nNombre del Anime: " + nombre.find('nombre').text)
    print("Estado: " + nombre.find('estado').text)
    print("Episodios Vistos: " + nombre.find('episodiosVistos').text)
  else:
     print("No se ha encontrado el anime")

