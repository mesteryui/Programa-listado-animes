import xml.etree.ElementTree as ET

def accederArbol():
    arbol = ET.parse("lista-animes.xml")
    return arbol.getroot()
