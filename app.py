from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "tetilino"


# conexão com banco
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# PAGINA INICIAL (PORTFÓLIO)
@app.route("/")
def home():
    return render_template("landing.html")


# LOGIN
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()

        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username,password)
        ).fetchone()

        if user:
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    db = get_db()

    total = db.execute(
        "SELECT COUNT(*) as total FROM projetos"
    ).fetchone()["total"]

    return render_template("dashboard.html", total=total)


# PROJETOS
@app.route("/projetos")
def projetos():

    if "user" not in session:
        return redirect("/login")

    db = get_db()

    projetos = db.execute(
        "SELECT * FROM projetos"
    ).fetchall()

    return render_template("projetos.html", projetos=projetos)


# KANBAN
@app.route("/kanban")
def kanban():

    db = get_db()

    tarefas = db.execute(
        "SELECT * FROM tarefas"
    ).fetchall()

    return render_template("kanban.html", tarefas=tarefas)


# CLIENTES
@app.route("/clientes")
def clientes():

    db = get_db()

    clientes = db.execute(
        "SELECT * FROM clientes"
    ).fetchall()

    return render_template("clientes.html", clientes=clientes)


# FINANCEIRO
@app.route("/financeiro")
def financeiro():

    db = get_db()

    pagamentos = db.execute(
        "SELECT * FROM financeiro"
    ).fetchall()

    return render_template("financeiro.html", pagamentos=pagamentos)


# UPLOADS
@app.route("/uploads")
def uploads():

    db = get_db()

    arquivos = db.execute(
        "SELECT * FROM arquivos"
    ).fetchall()

    return render_template("uploads.html", arquivos=arquivos)


# LOGOUT
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5001)