#O programa abaixo solicita que você digite a sua idade e apresenta qual será a sua idade daqui a um ano.
try:
    idade = int(input('Sua idade: '))
    proxima = idade + 1
    print('Ano que vem você terá', proxima, 'anos')
#se o usuário informar letras e não números:
except ValueError:
    print("Entre somente dígitos!")
