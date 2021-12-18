class Noh:
	def __init__(self,valor_inicial):
		self._dados = valor_inicial
		self._proximo = None
	def getData(self):
		return self._dados
	def getNext(self):
		return self._proximo
	def setData(self, novo_valor):
		self._dados =  novo_valor
	def setNext(self, novo_proximo):
		self._proximo = novo_proximo
	def __str__(self):
		return f"[dados:{self._dados}|proximo:{self._proximo}]"

class ListaNaoOrdenada:
	def __init__(self): #construtor
		self.head = None
		self.tamanho = 0

	def is_empty(self):  #<<<<
		return self.head == None

	def add(self,item):
		temp = Noh(item)
		temp.setNext(self.head)
		self.head = temp
		self.tamanho += 1

	def size(self):
		return self.tamanho

	def search(self,item):
		atual = self.head #atual == temp
		encontrou = False
		while atual != None and not encontrou:
			if atual.getData() == item:
				encontrou = True
			else:
				atual = atual.getNext()
		return encontrou

	def remove(self,item):
		atual = self.head
		anterior = None
		encontrou = False
		self.tamanho -= 1
		while atual != None and not encontrou: #percorre a lista
			if atual.getData() == item:
				encontrou = True
			else:
				anterior = atual
				atual = atual.getNext()

		if anterior == None and encontrou:
			self.head = atual.getNext()
		elif encontrou:
			anterior.setNext(atual.getNext())

	def show(self):
		atual = self.head
		lista = []
		while atual != None: #percorre a lista
			lista.append(atual._dados)
			atual = atual.getNext()
		print(lista)

lista = ListaNaoOrdenada()
lista.add(3)
lista.add(2)
lista.show() #[2,3]
