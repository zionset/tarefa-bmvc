from bottle import Bottle, redirect, request, run

from app.controllers.application import Application

app = Bottle()
ctl = Application()


@app.get("/")
def index():
    redirect("/portal")


# ---------- recurso: portal (login) ----------
@app.get("/portal")
def portal():
    return ctl.render("portal")


@app.post("/portal")
def login():
    return ctl.login(request.forms.username, request.forms.password)


@app.get("/logout")
def logout():
    return ctl.logout()


# ---------- recurso: banco (filmes) ----------
@app.get("/banco")
def banco():
    return ctl.render("banco")


@app.post("/banco")
def create_filme():
    return ctl.create_filme(request.forms.titulo, request.forms.diretor, request.forms.ano)


@app.delete("/banco/<id:int>")
def delete_filme(id):
    return ctl.delete_filme(id)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)
