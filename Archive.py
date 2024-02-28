import os
import glob
import re
import csv
import json
from io import StringIO
import xml.etree.ElementTree as ET

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