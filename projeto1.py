from os import system
from datetime import datetime, timedelta
system('cls')

try:
    tipo_investimento= input('Escolha o tipo de investimento (CDB/LCI):')
    capital_inicial= float(input('Digite o capital inicial:'))
    taxa= float(input('Digite a taxa mensal de juros (%):'))
    meses= int(input('Digite a quantidade de meses:'))
except ValueError:
    print('-----VALOR INCORRETO, TENTE NOVAMENTE!-----')


data_aplicacao= datetime.now()
data_vencimento= data_aplicacao + timedelta(days=meses*30)
data_aplicacao_strf= data_aplicacao.strftime('%d/%m/%y')
data_vencimento_strf= data_vencimento.strftime('%d/%m/%y')

def calculo_montante(capital_inicial, taxa, meses):
    montante= capital_inicial * (1+ taxa/100)**meses
    return montante

print('RESUMO DO INVESTIMENTO:')
print('\n')
print(f'Tipo do investimento: {tipo_investimento}')
print(f'Capital Inicial: R${capital_inicial}')
print(f'Taxa de juros ao mês: {taxa}%')
print(f'Prazo: {meses}')
print(f'Montante: R${calculo_montante(capital_inicial, taxa, meses):.2f}')
print('\n')
print('-----DATAS-----')
print(f'Aplicação: {data_aplicacao_strf}')
print(f'Vencimento: {data_vencimento_strf}')