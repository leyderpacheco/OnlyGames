#!/usr/bin/python3
from jinja2 import Template
from modelo_login import ObtenerUsuario
import cgi

datos = cgi.FieldStorage()

print('Content-Type: text/html')
print('')

username=datos.getvalue('uname')

password=datos.getvalue('passw')

#print(username)

permiso=ObtenerUsuario(username,password)

def render(file,modelo=False):
   with open(file) as f:
     pag=f.read()
     template=Template(pag)
     page = template.render(nombre=datos.getvalue('uname'))
   return page

if permiso:
  p=render("menup.html")
  print(p)
else:
  p=render("menup.html")
  print(p)
