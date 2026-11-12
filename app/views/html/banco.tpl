<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>Cinemateca - Banco</title>
</head>
<body>
  <h1>Cinemateca - Banco de filmes</h1>
  <p>Usuário: {{username}} | <a href="/logout">Sair</a></p>
  <table border="1" cellpadding="6">
    <tr><th>ID</th><th>Título</th><th>Diretor</th><th>Ano</th></tr>
    % for filme in filmes:
    <tr>
      <td>{{filme.id}}</td>
      <td>{{filme.titulo}}</td>
      <td>{{filme.diretor}}</td>
      <td>{{filme.ano}}</td>
    </tr>
    % end
  </table>
</body>
</html>
