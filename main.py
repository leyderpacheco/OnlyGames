from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def log():
    return render_template('indexinicial.html')


@app.route('/registro')
def reg():
    return render_template('indexreg.html')

@app.route('/home')
def home():
    return render_template('menup.html')

if __name__ == "__main__":
    app.run(debug=True)