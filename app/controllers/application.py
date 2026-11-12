import os
import uuid

from bottle import TEMPLATE_PATH, redirect, request, response, template

from app.controllers.datarecord import DataRecord

# pasta das views (funciona de qualquer diretório)
TEMPLATE_PATH.insert(0, os.path.join(os.path.dirname(__file__), "..", "views", "html"))


class Application:
    def __init__(self):
        self.pages = {"portal": self.portal, "banco": self.banco}
        self.db = DataRecord()
        self.sessions = {}  # session_id -> username

    def render(self, page):
        return self.pages[page]()

    def current_user(self):
        return self.sessions.get(request.get_cookie("session_id"))

    def resposta(self, status, mensagem):
        response.status = status
        return mensagem + "\n"

    # ---------- portal ----------
    def portal(self, erro=None):
        return template("portal", erro=erro)

    def login(self, username, password):
        if not self.db.check_user(username, password):
            response.status = 401
            return self.portal("Usuário ou senha inválidos.")
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = username
        response.set_cookie("session_id", session_id, path="/", httponly=True)
        redirect("/banco")

    def logout(self):
        self.sessions.pop(request.get_cookie("session_id"), None)
        response.delete_cookie("session_id", path="/")
        redirect("/portal")

    # ---------- banco ----------
    def banco(self):  # READ
        username = self.current_user()
        if not username:
            redirect("/portal")
        return template("banco", username=username, filmes=self.db.filmes)

    def create_filme(self, titulo, diretor, ano):  # CREATE (via cURL)
        if not self.current_user():
            return self.resposta(401, "Não autenticado: faça login em /portal.")
        try:
            ano = int(ano)
        except ValueError:
            return self.resposta(400, "O ano deve ser um número.")
        if not titulo.strip() or not diretor.strip():
            return self.resposta(400, "Informe titulo e diretor.")
        filme = self.db.add_filme(titulo.strip(), diretor.strip(), ano)
        return self.resposta(201, "Filme criado com id {}.".format(filme.id))

    def delete_filme(self, id):  # DELETE (via cURL)
        if not self.current_user():
            return self.resposta(401, "Não autenticado: faça login em /portal.")
        if self.db.delete_filme(id):
            return self.resposta(200, "Filme {} removido.".format(id))
        return self.resposta(404, "Filme {} não encontrado.".format(id))
