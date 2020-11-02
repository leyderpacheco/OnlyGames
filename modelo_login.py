#!/usr/bin/python3

import mysql.connector
from mysql.connector import errorcode

def __init__(self):
   print ('init')
#class usuarioClass:

def ObtenerUsuario(username, password):
  try:
    cnx = mysql.connector.connect(user='leyder', password = '123', database='onlygames', host='127.0.0.1')
    cursor = cnx.cursor()
    aux=True

    query = ("SELECT * FROM usuarios where username= %s and password = sha(%s)")

    data_usr = (username, password)
    cursor.execute(query, data_usr)
    record = cursor.fetchone()

    #if record:
       #print(f'<p>Bienvenido</p> <h1>{record[0]}</h1>')
       
    #else:
       #print('<h1>Usuario o Contraseña incorrectos</h1> ')

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()
