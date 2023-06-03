# importar as bibliotecas 
import pandas as pd
# Importar a base de dados

## visualizar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')
pd.set_option('display.max_columns',None)
# print(tabela_vendas)
# faturamento por loja
faturamento =tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
# quantidade de produto vendido por loja 
quantidade=tabela_vendas[['ID Loja', 'Quantidade',]].groupby('ID Loja').sum()
print(quantidade)
#print('-'*50)
# ticket medio de produto por loja
ticket_medio = (faturamento['Valor Final'] / quantidade ['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'ticket médio'})
print(ticket_medio)
# enviar o e-mail com o relatorio 


