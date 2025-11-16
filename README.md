# Recuperação Inventarios

### Versão dotnet 9 
- Compilado em Self Containned que elimina a necessidade de instalar o Runtime
```bash
dotnet build --sc --configuration Release
./bin/Release/net9.0/'arch'/recup <database.db>
```

### Versão Python 3.1x
- Existe a necessidade de ter python instalado na maquina
```bash
python recup_inventarios.py <database.db>
```

Ambas as versões fazem output de um ficheiro sql que permite fazer a atualização dos dados do inventario que deu erro no terminal.
É preciso alertar o utilizador que não pode tentar entrar no inventario sem fazer backup da base de dados interna do ekanban.
### Backup da BD no pda
- Entrar no ekanban com 6699 / 9966
- aceder ao menu no canto superior direito
- Escolher backup base dados
- confirmar com a equipa de prevenção que o ficheiro foi criado no servidor