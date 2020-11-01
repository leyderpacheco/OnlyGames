#!/usr/bin/python3
from jinja2 import Template
print('Content-Type: text/html')
print('')

with open('index.html') as f:
        doc = f.read()
        template = Template(doc)
        page = template.render(nombre="Juan", edad=19)
        print(page)
