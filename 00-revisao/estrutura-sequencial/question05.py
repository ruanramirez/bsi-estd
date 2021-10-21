height = float(input('Insira uma altura: '))

man = (72.7 * height) - 58
woman = (62.1 * height) - 44.7

print(f'Para homens, o peso ideal é: {round(man, 2)}kg. Para mulheres, o peso ideal é: {round(woman, 2)}kg.')
