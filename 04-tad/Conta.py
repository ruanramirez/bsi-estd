class Conta:
	numero_conta = ''
	nome_correntista = ''
	saldo = -1

from Conta import *

minhaConta = Conta()
minhaConta.numero_conta = '123'
minhaConta.nome_correntista = 'Ruan Ramirez'
minhaConta.saldo = 50.0

outraConta = Conta()
outraConta.numero_conta = '432'
outraConta.nome_correntista = 'Fulado ciclano'
outraConta.saldo = 120.0

lista_correntistas = []
lista_correntistas.append(minhaConta)
lista_correntistas.append(outraConta)


for conta in lista_correntistas:
	nome_conta = conta.nome_correntista
	lista_nomes = []
	lista_nomes.append(nome_conta)

print(lista_nomes)

for conta in lista_correntistas:
	print(f"Número da conta: {conta.numero_conta} - Nome do correntista: {conta.nome_correntista} - Saldo: {conta.saldo}")

	if(conta.saldo < 100):
		print(f'{conta.nome_correntista} seu saldo é inferior a $100')

