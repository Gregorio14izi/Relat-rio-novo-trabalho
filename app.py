from flask import Flask

app = Flask (__name__)

@app.route("/")
def home():
    return "Bem vindo ao site de livros!📚"

@app.route("/LivroEmAlta")
def livro():
    return "Stranger Things"

if __name__ == '__main__':
    app.run("0.0.0.0", port=8000)