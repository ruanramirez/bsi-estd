# Atividade
# Escreva um programa para gerenciar um cadastro de veículos como uma lista na memória do computador. Use o TAD Veiculo e explore os recursos de listas da linguagem Python (guiando-se pelos experimentos dessa subunidade). O programa deverá permitir as seguintes operações (utilize um menu que deve constar também a opção de encerrar o programa):


# - Inserir um veículo na lista (no fim da lista);
# - Remover um veículo da lista, dada a placa deste (executar a operação somente se a lista não estiver vazia e se a placa de fato existir);
# - Consultar o cadastro da seguinte maneira:
# + Dada a placa de um veículo, se a mesma existir, escrever todos os dados do veículo;
# + Se for dado apenas um inteiro de 0 a 9, o programa escreverá todos os dados dos veículos cujos finais de placa sejam o tal número


# TAD Veículo
# Atributos:

# - placa (string composta de 7 dígitos sendo três letras seguidas de quatro números),
# - marca (String que identifica o fabricante),
# - modelo (string com o nome do modelo dado pelo fabricante),
# - ano (ano de fabricação – uma string),
# - cod (código do proprietário – um número inteiro).
# Interface:
# - imprimeVeiculo() - Escreve os dados do Veiculo na saída padrão

# - imprimeFinalPlaca() - Retorna o algarismo final da placa deste veículo.

class Veiculo:
	placa = 'sem cor'
	marca = 'sem marca'
	modelo = 'sem modelo'
	ano = -1
	cod = 'sem código'

	def imprimeVeiculo(self):
		print(self.placa)

	def imprimeFinalPlaca(self):
		print(self.placa)
