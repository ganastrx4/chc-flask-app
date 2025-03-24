from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/wdd')
def wdd():
    return render_template('wdd.html')  # Asegúrate de que este archivo está en la carpeta templates

@app.route('/buscador')
def bienvenida():
    return render_template('buscador.html')

@app.route('/next-page')
def next_page():
    return render_template('next_page.html')  # O cualquier otra página que desees
if __name__ == '__main__':
    app.run(debug=True)
