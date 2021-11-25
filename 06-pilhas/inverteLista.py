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

	def invertList(self):
		stack = Stack()
		newStack = Stack()
		for item in self.items:
			stack.push(item)
		while not stack.isEmpty():
			newStack.push(stack.pop())
		return newStack.items


pilha = Stack()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.invertList()

print(pilha.items)
print(pilha.invertList())
