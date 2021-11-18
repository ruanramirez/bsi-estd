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
	placa = 'sem placa'
	marca = 'sem marca'
	modelo = 'sem modelo'
	ano = -1
	cod = -1

	def imprimeVeiculo(self):
		return f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Código: {self.cod}."

	def imprimeFinalPlaca(self):
		return self.placa[-1]

primeiro_veiculo = Veiculo()
primeiro_veiculo.placa = 'ASB4232'
primeiro_veiculo.marca = 'Toyota'
primeiro_veiculo.modelo = 'AB-1'
primeiro_veiculo.ano = 2018
primeiro_veiculo.cod = 41455

segundo_veiculo = Veiculo()
segundo_veiculo.placa = 'TTB3141'
segundo_veiculo.marca = 'Honda'
segundo_veiculo.modelo = 'GX-1'
segundo_veiculo.ano = 2017
segundo_veiculo.cod = 12145

print(primeiro_veiculo.imprimeVeiculo())
print(primeiro_veiculo.imprimeFinalPlaca())

print(segundo_veiculo.imprimeVeiculo())
print(segundo_veiculo.imprimeFinalPlaca())

lista_veiculos = []
lista_veiculos.append(primeiro_veiculo)
lista_veiculos.append(segundo_veiculo)

print(lista_veiculos[0], lista_veiculos[1])
