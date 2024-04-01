
print('''
Escolha a operação
[1]Saque
[2]Deposito
[3]Extrato
[0]Sair''' )

operacao = int(input())
saldo = 500
extrato = []
limitediario = 3

def deposito (valor, saldo, extrato, /):
    valor = float(input('digite quanto quer depositar: '))
    saldo += valor
    extrato.append(f"deposito: {valor}")     
    print('R${:.2f} depositado com sucesso'.format(valor))
    return saldo, extrato

def saque (*,valor, saldo, extrato):        
    global limitediario
    if limitediario <= 0:
        print('Limites de saques atingido') 
    else:
        valor = float(input('Digite quanto quer sacar: '))
        if saldo < valor:
            print('Saldo insuficiente')
        elif valor > 500:
            print('Valor para saque invalido')
        else:
            saldo -= valor
            extrato.append(f"saque: {valor}")        
            print('R${:.2f} sacado com sucesso'.format(valor))
            limitediario -= 1
            print(limitediario)        
    return saldo, extrato,        
            
def exibir_extrato (saldo, /, *, extrato):
    print('='*5, 'EXTRATO', '='*5)
    print(*extrato, sep= '\n')
    print('='*19)
    print('saldo:R${:.2f}'.format(saldo))
    return saldo, extrato
            
while True:
       
    if operacao == 1: #saque        
            saque(valor=0, saldo=saldo, extrato=extrato)            
                    
    elif operacao == 2: #Deposito 
        saldo, extrato = deposito(0, saldo, extrato)

    elif operacao == 3: #Extrato
        exibir_extrato(saldo, extrato=extrato)

    elif operacao == 0:
        print('Operação finalizada')
        break
        
    else:
        print('Esta não é uma opção valida')
        
    print("Escolha a próxima operação:")
    operacao = int(input())