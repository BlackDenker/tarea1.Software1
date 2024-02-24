import os
import glob
import re
import csv
import json
import xml.etree.ElementTree as ET
from io import StringIO

folder = input("Escriba la carpeta donde se encuentran los archivos: ")
route = input("Escriba la ruta de la carpeta donde se encuentran los archivos: ")
select_word = input("Escriba la palabra que desea buscar: ")

class Entry:
    def __init__(self, folder, route, select_word):
        self.folder = folder,
        self.route = route
        self.select_word = select_word

class Archive:
    def count_files_text(route):
        routes = []
        return routes + glob.glob(os.path.join(route, '*.txt')) + glob.glob(os.path.join(route, '*.csv')) + glob.glob(os.path.join(route, '*.xml')) + glob.glob(os.path.join(route, '*.json'))

    def verify_exist_route(route):
        if os.path.exists(route):
            return True
        
    def get_words_file(route):
        _, extension = os.path.splitext(route)
        with open(route, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            if extension == '.txt':
                words = content.split()
            elif extension == '.csv':
                words = []
                file_csv = StringIO(content)
                reader_csv = csv.reader(file_csv, delimiter=',')
                for row in reader_csv:
                    for text in row:
                        words = words + text.split()
            elif extension == '.json':
                data_json = json.loads(content)
                word_disorganized = [str(value) for value in data_json.values()]
                for word in word_disorganized:
                    words = word.split()
            elif extension == '.xml':
                words = []
                root = ET.fromstring(content)
                word_disorganized = [elemento.text for elemento in root.iter()]
                for word in word_disorganized:
                    words = words + word.split()
        return words

    def delete_score(word):
        return re.sub(r'[^\w\s]', '', word)
    
e = Entry(folder, route, select_word)

if not Archive.verify_exist_route(e.route):
    print("La ruta no existe")
else:
    if len(Archive.count_files_text(e.route)) == 0:
        print("No hay archivos de texto en la ruta")
    else:
        j = 0
        for routes in Archive.count_files_text(e.route):
            i = 0
            for word in Archive.get_words_file(routes):
                if Archive.delete_score(word).lower() == select_word.lower():
                    i += 1
                    j += 1
            print(f"La palabra {select_word} se encontró {i} veces en el archivo {route}")
        print(f"La palabra {select_word} se encontró {j} veces en total")