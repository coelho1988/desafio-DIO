import time
print('='*5, 'BANCO', '='*5)
print('''Escolha a operação
[1]Saque
[2]Deposito
[3]Extrato
[4]Novo Usuário
[5]Nova Conta
[6]Lista de Usuários
[7]Lista de Contas
[0]Sair''' )
print('='*17)

saldo = 500
extrato = []
usuario = []
limitediario = 3
agencia = "0001"
conta = 0
listaDeContas = []

def deposito (saldo, extrato, /):
    valor = float(input('digite quanto quer depositar: '))
    saldo += valor
    extrato.append(f"deposito: {valor}")     
    print('R${:.2f} depositado com sucesso'.format(valor))
    time.sleep(1)  
    return saldo, extrato

def saque (*,saldo, extrato, limitediario):       
    
    if limitediario <= 0:
        print('Limites de saques atingido') 
    else:
        valor = float(input('Digite quanto quer sacar: '))
        if saldo < valor:
            print('Saldo insuficiente')
        elif valor > 500:
            print('Valor para saque invalido')
        else:            
            extrato.append(f"saque: {valor}")        
            print('R${:.2f} sacado com sucesso'.format(valor))
            saldo -= valor
            limitediario -= 1
            print('Saques restantes ',limitediario)
            time.sleep(1)        
    return saldo, extrato       
            
def exibir_extrato (saldo, /, *, extrato):
    print('='*5, 'EXTRATO', '='*5)
    print(*extrato, sep= '\n')
    print('='*19)
    print('saldo:R${:.2f}'.format(saldo))
    time.sleep(1)  
    return saldo, extrato
 
def novo_usuario(usuario):
    cpf = int(input('CPF(apenas numeros): '))
    if any(cpf in cliente for cliente in usuario):
        print('CPF já cadastrado')
    else:
        nome = input('nome: ')
        datansc = input('data de nascimento: ')    
        endereco = input('Endereço: ')
        cliente = nome, datansc,cpf,endereco
        usuario.append(cliente)
        print(cliente)  
    time.sleep(1)
    return usuario
 
def nova_conta(usuario):
    global conta
    cpf = int(input('CPF(apenas numeros): '))
    if any(cpf in cliente for cliente in usuario):
        conta += 1
        conta_usuario = agencia, conta, usuario[0]
        listaDeContas.append(conta_usuario)
    else:
        print('CPF não cadastro')
        conta_usuario = None
    return usuario, listaDeContas

def lista_usuario(usuario):
    print('='*6, 'LISTA', '='*6)
    print(*usuario, sep= '\n')
    print('='*19)
    time.sleep(1)  

def lista_contas(listaDeContas, usuario):
    cpf = int(input('CPF(apenas numeros): '))
    if any(cpf in cliente for cliente in usuario):
        print('='*6, 'LISTA', '='*6)
    print(*listaDeContas, sep= '\n')
    print('='*19)
    time.sleep(1)
    
while True:
    
    operacao = int(input())
       
    if operacao == 1: #saque        
            saldo, extrato = saque(saldo=saldo, extrato=extrato, limitediario=limitediario)            
                    
    elif operacao == 2: #Deposito 
        saldo, extrato = deposito(saldo, extrato)

    elif operacao == 3: #Extrato
        exibir_extrato(saldo, extrato=extrato)

    elif operacao == 4: #novo usuario
        usuario = novo_usuario(usuario)
    
    elif operacao == 5: #nova conta
        conta = nova_conta(usuario)
        
    elif operacao == 6: #lista de usuários
        lista_usuario(usuario)
    
    elif operacao == 7: #lista de contas
        lista_contas(listaDeContas,usuario)  
              
    elif operacao == 0: #sair
        print('Operação finalizada')
        break
        
    else:
        print('Esta não é uma opção valida')
        
    print('='*5, 'BANCO', '='*5)
    print('''Escolha a operação
[1]Saque
[2]Deposito
[3]Extrato
[4]Novo Usuario
[5]Nova Conta
[6]Lista de Usuários
[7]Lista de contas
[0]Sair'''  )
    print('='*17)
    