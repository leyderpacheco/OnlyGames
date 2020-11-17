from flask import Flask, render_template,request
import mysql.connector

app=Flask(__name__)

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
    return render_template('menup.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    user=request.form.get('usuario')
    password=request.form.get('contraseña')

    query = ("SELECT * FROM usuarios where username= %s and contraseña = %s")
    data_usr = (user, password)
    cursor.execute(query, data_usr)
    users=cursor.fetchall()

    if len(users)>0:
        return render_template('menup.html')
    else:
        return render_template('indexinicial.html')

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    
if __name__ == "__main__":
    app.run(debug=True)