from busqueda_nombre import *
from busqueda_genero import *
from nuevo_anime import *
from obtener_arbol import *
# Cargamos el archivo XML
def main():
    tipoBusqueda = input("Indique el tipo de busqueda a realizar:\n 1.Por nombre\n 2.Por genero\n 3.Añadir nuevo anime\n")
    if tipoBusqueda=="1":
        MostrarNombre(BusquedaNombre())
    elif tipoBusqueda=="2":
        MostrarGenero(BuscarGenero())
    elif tipoBusqueda=="3":
        añadirNuevoAnime()

if __name__ == "__main__":
    main()
