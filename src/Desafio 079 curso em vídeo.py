numeros = []
numeros.append(int(input('Digite um valor: ')))
print('Valor adicionado com sucesso!')

while True:
    resposta = input('Deseja adicionar outro valor? [S/N]: ')
    if resposta.upper() in 'S':
        print('-=-'*35)
    while True:
        if resposta.upper() not in 'NS':
            print('Seleção inválida, por favor, digite [S] para continuar e [N] para encerrar a aplicação')
            resposta = input()
            if resposta.upper() in 'S':
                print('-=-'*35)
        else:
            break
    if resposta.upper() in 'N':
        break
    num = int(input('Digite um valor: '))
    if num in numeros:
        print('Este valor já existe, não irei adiciona-lo novamente!!')
    else:
        numeros.append(num)
        print('Valor adicionado com sucesso!')

print('-=-'*35)
print(f'''Aplicação encerrada pelo usuário
Aqui está sua lista com todos os valores adicionados, em ordem crescente
{sorted(numeros)}''')