import win32com.client as win32com

# criar a integração com o outlook
outlook = win32com.client.Dispatch("Outlook.Application")

# criar um email
email = outlook.CreateItem(0)

faturamento = 1500
qtde_produtos = 10
ticket_medio = faturamento / qtde_produtos

# configurar as informações do seu e-mail
email.To = "fulanodetal@gmail.com; johndoe@gmail.com"
email.Subject = "Título de Exemplo"
email.HTMLBody = f"""
<p>Olá John, aqui é o código Python</p>

<p>O faturamento da loja foi de R${faturamento}</p>
<p>Vendemos {qtde_produtos} produtos</p>
<p>O ticket Médio foi de R${ticket_medio}</p>

<p>Atenciosamente,</p>
<p>Ciclano Bezerra</p>
"""

# anexo = "C://Users/ciclano/Downloads/arquivo.xlsx"
# email.Attachments.Add(anexo)

email.Send()
print("E-mail enviado com sucesso!")
