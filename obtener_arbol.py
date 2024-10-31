import xml.etree.ElementTree as ET
import os

def accederArbol(nombre):
    """
    Esta funcion permite acceder al arbol de un archivo xml y devuelve el elemento raiz, como parametro pasamos el nombre del xml
    """
    arbol = ET.parse(nombre)
    return arbol.getroot()

def crear_archivo_xml(nombre_archivo, nombre_raiz):
    """
    Esta funcion crea un archivo XML con su elemento raiz le pasamos el nombre del archivo y el nombre del elemento raiz y asi escribe el archvio de forma basica
    """
    raiz = ET.Element(nombre_raiz)
    arbol = ET.ElementTree(raiz)

    with open(nombre_archivo, "wb") as archivo:
        arbol.write(archivo, encoding='utf-8', xml_declaration=True)