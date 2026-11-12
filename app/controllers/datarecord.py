import json
import os

from app.models.filme import Filme
from app.models.user_account import User_account

DB = os.path.join(os.path.dirname(__file__), "db")


class DataRecord:
    """Banco de dados em arquivos JSON (usuários e filmes)."""

    def __init__(self):
        self.users = self._ler("user_accounts.json", User_account)
        self.filmes = self._ler("filmes.json", Filme)

    def _ler(self, arquivo, classe):
        with open(os.path.join(DB, arquivo), encoding="utf-8") as f:
            return [classe(**dados) for dados in json.load(f)]

    def _gravar(self, arquivo, objetos):
        with open(os.path.join(DB, arquivo), "w", encoding="utf-8") as f:
            json.dump([vars(o) for o in objetos], f, ensure_ascii=False, indent=2)

    def check_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def add_filme(self, titulo, diretor, ano):
        novo_id = max([f.id for f in self.filmes], default=0) + 1
        filme = Filme(novo_id, titulo, diretor, ano)
        self.filmes.append(filme)
        self._gravar("filmes.json", self.filmes)
        return filme

    def delete_filme(self, id):
        for filme in self.filmes:
            if filme.id == id:
                self.filmes.remove(filme)
                self._gravar("filmes.json", self.filmes)
                return True
        return False
