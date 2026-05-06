from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Olá mundo!"

@app.route('/saudacao')
def saudacao():
    return render_template("saudacao.html")

@app.route('/cursos')
def curso():
    return render_template("cursos.html")

@app.route('/curso/devweb')
def curso_devweb():
    return render_template("curso_devweb.html")

@app.route('/curso/poo')
def curso_poo():
    return render_template("curso_poo.html")

if __name__ == '__main__':
    app.run(debug=True)
