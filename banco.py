print('''Escolha a operação
[1]Saque
[2]Deposito
[3]Extrato
[4]Sair''' )

operacao = int(input())
saldo = 0
extrato = []
limitediario = 3

while True:
       
    if operacao == 1:
        if limitediario > 0:
            saque = float(input('Digite quanto quer sacar: '))
            if saldo > saque and saque <= 500:
                saldo -= saque
                extrato.append(f"saque: {saque}")
                limitediario -= 1
                print('R${:.2f} sacado com sucesso'.format(saque))
            else:
                print('Valor invalido ou saldo insuficiente')
        else:
            print('Limite de Saques diarios execidido')
            
    elif operacao == 2:
        deposito = float(input('digite quanto quer depositar: '))
        saldo += deposito
        extrato.append(f"deposito: {deposito}")     
        print('R${:.2f} depositado com sucesso'.format(deposito))

    elif operacao == 3:
        print('saldo:R${:.2f}',saldo)
        print(*extrato, sep= '\n')

    elif operacao == 4:
        print('Operação finalizada')
        break
        
    else:
        print('Esta não é uma opção valida')
        
    print("Escolha a próxima operação:")
    operacao = int(input())