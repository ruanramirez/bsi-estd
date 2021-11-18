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
	def __init__(self, placa, marca, modelo, ano, cod):
		self.placa = placa
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.cod = cod

	def imprimeVeiculo(self):
		return f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Código: {self.cod}."

	def imprimeFinalPlaca(self):
		return self.placa[-1]


primeiro_veiculo = Veiculo('ASB4232', 'Toyota', 'AB-1', 2018, 41455)
segundo_veiculo = Veiculo('TTB3141', 'Honda', 'GX-1', 2017, 12145)

lista_veiculos = []

def cadastrarVeiculo(veiculo):
	lista_veiculos.append(veiculo)
	print(f"Veículo de placa: {veiculo.placa} cadastrado")

def removerVeiculo(placa):
	if len(lista_veiculos) != 0:
		for x in lista_veiculos:
			if x.placa == placa:
				lista_veiculos.remove(x)
	print(f'Veículo de placa: {placa} removido')

print(primeiro_veiculo.imprimeVeiculo())
print(primeiro_veiculo.imprimeFinalPlaca())

print(segundo_veiculo.imprimeVeiculo())
print(segundo_veiculo.imprimeFinalPlaca())
cadastrarVeiculo(primeiro_veiculo)
cadastrarVeiculo(segundo_veiculo)
print(len(lista_veiculos))
removerVeiculo("ASB4232")
print(len(lista_veiculos))
