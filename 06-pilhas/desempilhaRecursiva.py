class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return (self.items == [])

	def popAll(self):
		self.items.pop()
		if self.isEmpty():
			print('A pilha está vazia')
		while not self.isEmpty():
			return self.popAll()

pilha = Stack()
pilha.push(1)
pilha.push(1)
pilha.push(1)
pilha.popAll()
print(pilha.items)
