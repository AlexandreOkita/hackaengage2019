from flask import Flask, render_template, request, redirect
from get import get_info
from flask_bootstrap import Bootstrap
from meuprimeirobd import set_info
import random as rd


def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = create_app()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/home.html', methods=['POST', 'GET'])
def caio():
    lista = get_info()
    imagens = ['static/img1.jpg','static/img2.jpg','static/img3.jpg','static/img4.jpg','static/img5.jpg']
    return render_template('home.html', lista = lista, imgs = imagens)

@app.route('/handle_data', methods=['GET','POST'])
def handle_data():
    titulo = request.form["TitleEvent"]
    desc = request.form["Description"]
    local = request.form["Local"]
    data = request.form["Data"]

    set_info(titulo, desc, local, data)
    return redirect("/home.html")

if __name__ == '__main__':
    app.run(debug=True)