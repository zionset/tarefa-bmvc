<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>Cinemateca - Portal</title>
</head>
<body>
  <h1>Cinemateca - Portal</h1>
  % if erro:
  <p style="color: red">{{erro}}</p>
  % end
  <form method="post" action="/portal">
    <p>Usuário: <input type="text" name="username" autofocus></p>
    <p>Senha: <input type="password" name="password"></p>
    <p><button type="submit">Entrar</button></p>
  </form>
</body>
</html>
