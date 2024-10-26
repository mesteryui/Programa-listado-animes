import xml.etree.ElementTree as ET
import busqueda_genero
# Cargamos el archivo XML
arbol = ET.parse("lista-animes.xml")
raiz = arbol.getroot()
print("Indique el tipo de busqueda a realizar:\n 1.Por nombre\n 2.Por genero")
tipoBusqueda = input("Dime el genero por el que quieres buscar:")
if tipoBusqueda=="Por genero":
    busqueda_genero()
