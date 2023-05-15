# Retorna dia util
Função em teste criada para retornar dia util do mes, sendo o dia util o dia de semana, excluido feriados brasileiros ou feriados americanos.

## Como rodar
Para rodar os testes pra esse codigo basta seguir os passos abaixo:

1. Abra o terminal e baixe esse codigo: 
```shell
git clone https://github.com/cleitonsouza01/pega-dia-uitil

cd pega-dia-uitil
```

2. Crie um ambiente virtual python
```shell
python -m venv venv
```

3. Ative o ambiente virtual
```
venv/bin/activate 
```
se estiver usando Windows
```
venv\Scripts\activate.bat 
```

4. Instale os pacotes requeridos
```shell
python -m pip install -r requirements.txt
```

5. Rode os testes
```shell
pytest
```