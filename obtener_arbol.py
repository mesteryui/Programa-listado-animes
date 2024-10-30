import xml.etree.ElementTree as ET
import os



def accederArbol():
    arbol = ET.parse("lista-animes")
    return arbol.getroot()

def crear_archivo_xml(nombre_archivo, nombre_raiz):
    raiz = ET.Element(nombre_raiz)
    arbol = ET.ElementTree(raiz)

    with open(nombre_archivo, "wb") as archivo:
        arbol.write(archivo, encoding='utf-8', xml_declaration=True)