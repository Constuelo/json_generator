import os
from pathlib import Path
import json


snippet_ext = '.json'  # Extension name for sublimes snippet files
convert_dir = '/convert'  # Location for input files

path = Path(os.path.dirname(__file__))
content_path = Path(os.path.dirname(__file__) + convert_dir)
list_path = os.listdir(content_path)

dict_object = dict()


for d, s, f in os.walk(content_path):
    for file in f:
        if '.gitignore' not in file:
            name = file.split(".")[0]
            html = os.path.join(d, file)

            with open(html, 'r') as html:
                dict_object[name] = html.read()

            with open('modules.json', 'w') as data:
                json.dump(dict_object, data)

print(f'All good.')