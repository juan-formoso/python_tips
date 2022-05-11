import pyodbc

dados_conexao = (
  "Driver={SQL Server};"
  "Server=DESKTOP-T2JV7P5;"
  "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão realizada com sucesso!")

cursor = conexao.cursor()

id = 4
cliente = "Ciclano Bezerra"
produto = "Notebook"
data = "01/01/2020"
preco = 1500
quantidade = 10

comando = f"""INSERT INTO Database_Example.Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
  VALUES({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()