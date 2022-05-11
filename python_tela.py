import requests from tkinter import *

def pegar_cotacoes():
  requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL, EUR-BRL, BTC-BRL")
  cotacoes = requisicao.json()

  cotacao_dolar = cotacoes["USDBRL"]["bid"]
  cotacao_euro = cotacoes["EURBRL"]["bid"]
  cotacao_bitcoin = cotacoes["BTCBRL"]["bid"]

  texto_resposta["text"] = f"""
  Dólar: {cotacao_dolar}
  Euro: {cotacao_euro}
  Bitcoin: {cotacao_bitcoin}"""

janela = Tk()
janela.title("Cotação Atual de Moedas")
texto = Label(janela, text="Clieque no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

text_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
