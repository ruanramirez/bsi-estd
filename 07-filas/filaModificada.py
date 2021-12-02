class FilaArray:
	CAPACIDADE_PADRAO = 5
	def __init__(self):
		self._dados = [None] * FilaArray.CAPACIDADE_PADRAO
		self._tamanho = 0
		self._inicio = 0

	def __len__(self):
		return self._tamanho
	def is_empty(self):
		return self._tamanho == 0

	def first(self):
		if self.is_empty():
			raise FilaVazia('A Fila está vazia')
		if self._tamanho == FilaArray.CAPACIDADE_PADRAO:
			raise FilaCheia('A Fila está cheia.')
		return self._dados[self._inicio]
