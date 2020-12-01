from flask import Flask, render_template,request,redirect,session,jsonify,make_response
import mysql.connector
import os
from steamGames import data

app=Flask(__name__)
app.secret_key=os.urandom(24)

cnx=mysql.connector.connect(user='root', password = 'Millos14', database='onlygames', host='127.0.0.1',auth_plugin='mysql_native_password')
cursor=cnx.cursor()



@app.route('/')
def log():
    return render_template('indexinicial.html')


@app.route('/registro')
def reg():
    return render_template('indexreg.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        
        return render_template('index.html')
        
    else:
        return redirect('/')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    user=request.form.get('usuario')
    password=request.form.get('contraseña')

    query = ("SELECT * FROM usuarios where username= %s and contraseña = SHA(%s)")
    data_usr = (user, password)
    cursor.execute(query, data_usr)
    users=cursor.fetchall()

    if len(users)>0:
        session['user_id']=users[0][0]
        return redirect('/home')
    else:
        return redirect('/')

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    user=request.form.get('usuario')
    mail=request.form.get('correo')
    password=request.form.get('contraseña')

    add_usr = ("INSERT INTO usuarios "
               "(username, correo, contraseña) "
               "VALUES (%s, %s, SHA(%s))")


    data_usr = (user,mail, password)
    cursor.execute(add_usr, data_usr)
    cnx.commit()

    return "usuario registrado"

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/games')
def games():
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)