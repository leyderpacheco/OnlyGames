#!/usr/bin/python3

import mysql.connector
from mysql.connector import errorcode
import cgi

datos = cgi.FieldStorage()

print('Content-Type: text/html')
print('')


try:
  cnx = mysql.connector.connect(user='leyder', password = '123', database='onlygames', host='127.0.0.1')
  cursor = cnx.cursor()

  username=datos.getvalue('uname')
  correo=datos.getvalue('correo')
  password=datos.getvalue('passw')

  print(username)
  print(correo)
  print(password)

  add_usr = ("INSERT INTO usuarios "
               "(username, correo, password) "
               "VALUES (%s, %s, SHA(%s))")


  data_usr = (username,correo, password)
  cursor.execute(add_usr, data_usr)

  print('<h1>Usuario Registrado</h1>')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.commit()

  cursor.close()
  cnx.close()

