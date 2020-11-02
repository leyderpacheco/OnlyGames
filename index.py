#!/usr/bin/python3
from modelo_registro import RegistrarUsuario
import cgi

datos = cgi.FieldStorage()

print('Content-Type: text/html')
print('')

username=datos.getvalue('uname')
correo=datos.getvalue('correo')
password=datos.getvalue('passw')

#print(username)

print(RegistrarUsuario(username,correo,password))
