name = str(input('Insira um nome de usuário: '))
password = str(input('Insira uma senha (diferente do nome de usuário): '))

if name != password:
	print(f'Parabéns, o nome do usuário "{name}" é diferente da senha "{password}"')

while name == password:
	print(f'Infelizmente você não obedeceu as restrições. Tente novamente!')

	name = str(input('Insira um nome de usuário: '))
	password = str(input('Insira uma senha (diferente do nome de usuário): '))

	if name != password:
		print(f'Parabéns, o nome do usuário "{name}" é diferente da senha "{password}"')
