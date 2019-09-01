from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from meuprimeirobd import set_info
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html', desc = 'TOMARA QUE ISSO DÊ CERTO!')

@app.route('/caio', methods=['POST', 'GET'])
def caio():
    return render_template('events.html')

@app.route('/handle_data', methods=['GET','POST'])
def handle_data():
    titulo = request.form["TitleEvent"]
    desc = request.form["Description"]
    local = request.form["Local"]
    data = request.form["Data"]

    set_info(titulo, desc, local, data)
    return redirect("/caio")

if __name__ == '__main__':
    app.run(debug=True)