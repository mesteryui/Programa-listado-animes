from obtener_arbol import *
def BusquedaNombre():
    nombre1 = input("Introduzca nombre del anime:")
    nombre = accederArbol().find("anime[nombre='" + nombre1 + "']")
    return nombre

# Cargamos el archivo XML
def MostrarNombre(nombre):
  if nombre is not None:
    print("\nNombre del Anime: " + nombre.find('nombre').text)
    print("Estado: " + nombre.find('estado').text)
    print("Episodios Vistos: " + nombre.find('episodiosVistos').text)
  else:
     print("No se ha encontrado el anime")

