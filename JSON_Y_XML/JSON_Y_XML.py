import os
import json
import xml.etree.ElementTree as ET

# Clase personalizada para manejar datos
class Person:
    def __init__(self, name, age, birth_date, programming_languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, birth_date={self.birth_date}, programming_languages={self.programming_languages})"

# Función para crear JSON
def create_json(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"JSON file {file_name} created.")

# Función para crear XML
def create_xml(file_name, data):
    root = ET.Element("Datos")

    ET.SubElement(root, "Nombre").text = data['name']
    ET.SubElement(root, "Edad").text = str(data['age'])
    ET.SubElement(root, "Fecha_de_nacimiento").text = data['birth_date']

    languages = ET.SubElement(root, "Lenguajes_de_programación")
    for lang in data['programming_languages']:
        ET.SubElement(languages, "Lenguaje").text = lang

    tree = ET.ElementTree(root)
    tree.write(file_name, encoding='utf-8', xml_declaration=True)
    print(f"XML file {file_name} created.")

# Función para leer JSON
def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

# Función para leer XML
def read_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    data = {
        "name": root.find("Nombre").text,
        "age": int(root.find("Edad").text),
        "birth_date": root.find("Fecha_de_nacimiento").text,
        "programming_languages": [lang.text for lang in root.find("Lenguajes_de_programación")]
    }
    return data

# Datos iniciales
data = {
    "name": "Roberto",
    "age": 30,
    "birth_date": "1993-01-01",
    "programming_languages": ["Python", "Java", "C++"]
}

# Archivos
json_file = "datos.json"
xml_file = "datos.xml"

# Crear archivos
create_json(json_file, data)
create_xml(xml_file, data)

# Leer archivos y transformarlos en clase personalizada
json_data = read_json(json_file)
xml_data = read_xml(xml_file)

person_from_json = Person(**json_data)
person_from_xml = Person(**xml_data)

print("\nPerson from JSON:", person_from_json)
print("Person from XML:", person_from_xml)

# Mostrar contenido de los archivos
with open(json_file, 'r', encoding='utf-8') as f:
    print("\nContenido de datos.json:")
    print(f.read())

print("\nContenido de datos.xml:")
tree = ET.parse(xml_file)
ET.dump(tree)

# Eliminar archivos
os.remove(json_file)
os.remove(xml_file)
print("\nArchivos borrados.")
