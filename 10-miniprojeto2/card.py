class Noh:
	def __init__(self,valor_inicial):
		self.dados = valor_inicial
		self.proximo = None
	def getData(self):
		return self.dados
	def getNext(self):
		return self.proximo
	def setData(self, novo_valor):
		self.dados =  novo_valor
	def setNext(self, novo_proximo):
		self.proximo = novo_proximo
	def __str__(self):
		return f"[dados:{self.dados}|proximo:{self.proximo}]"

class Mao:
	def __init__(self):
		self.mao = None

	def adicionar(self, item):
		atual = self.mao
		anterior = None
		parar = False

		while atual != None and not parar:
			if atual.getData() > item:
				parar = True
			else:
				anterior = atual
				atual = atual.getNext()

		temp = Noh(item)
		if anterior == None:
			temp.setNext(self.mao)
			self.mao = temp
		else:
			temp.setNext(atual)
			anterior.setNext(temp)

	def pesquisar(self, item):
		atual = self.mao
		encontrou = False
		parar = False

		while atual != None and not encontrou and not parar:
			if atual.getData() == item:
				encontrou = True
			else:
				if atual.getData() > item:
					parar = True
				else:
					atual = atual.getNext()
		print(encontrou)

	def remover(self,item):
		atual = self.mao
		anterior = None
		encontrou = False
		while atual != None and not encontrou: #percorre a lista
			if atual.getData() == item:
				encontrou = True
			else:
				anterior = atual
				atual = atual.getNext()

		if anterior == None and encontrou:
			self.mao = atual.getNext()
		elif encontrou:
			anterior.setNext(atual.getNext())

	def mostrarMao(self):
		atual = self.mao
		lista = []
		while atual != None: #percorre a lista
			lista.append(atual.dados)
			atual = atual.getNext()
		print(lista)


mao = Mao()
mao.adicionar("6 de paus")
mao.adicionar("4 de paus")
mao.adicionar("5 de paus")
mao.mostrarMao()
mao.pesquisar("6 de paus")
mao.remover("6 de paus")
mao.mostrarMao()
