#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi

datos = cgi.FieldStorage()

print('Content-Type: text/html') 
print('')


def registrar(username,correo,password):

 try:
   cnx = mysql.connector.connect(user='leyder', password = '123', database='onlybd', host='127.0.0.1')
   cursor = cnx.cursor()

   add_usr = ("INSERT INTO usuario "
               "(username, correo, pass) "
               "VALUES (%s, %s, SHA(%s))")

   data_usr = (username,correo, contraseña)
   cursor.execute(add_usr, data_usr)

 except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
     print("Something is wrong with your user name or password")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
     print("Database does not exist")
   else:
     print(err)

