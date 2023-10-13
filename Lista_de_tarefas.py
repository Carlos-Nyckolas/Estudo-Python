##IMPORTAÇÕES
import time

##FUNÇÃO PRINCIPAL
def inicio():
    #Welcome
    print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    time.sleep(0.5)
    print("█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█")
    time.sleep(0.5)
    print("█░░║║║╠─║─║─║║║║║╠─░░█")
    time.sleep(0.5)
    print("█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
    time.sleep(0.5)
    print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
    print("")
    time.sleep(0.5)

    #Escolha a tarefa que deseja fazer
    print("O que vocẽ deseja fazer?")
    time.sleep(0.5)
    print("1. Fazer operações basicas")
    time.sleep(0.25)
    print("2. Calcular IMC")
    time.sleep(0.25)
    print("3.")
    time.sleep(0.5)
    Escolha = int(input())

    #Se escolher operações básicas
    if Escolha == 1:
        print("Escolha a operação:")
        time.sleep(0.5)
        print("1.Adição")
        time.sleep(0.25)
        print("2.Subtração")
        time.sleep(0.25)
        print("3.Multiplicação")
        time.sleep(0.25)
        print("4.Divisão")
        time.sleep(0.5)
        conta()

    #Se escolher IMC
    elif Escolha == 2:
        IMC()

    #Caso escolher 
    elif Escolha == 3:
        print("em breve")
    
    #Se digitar número errado
    else:
        inicio()

##FUNÇÕES DE TAREFA
def IMC():
    #Coletando informações para fazer o calculo: entrada
    peso = float(input("Digite seu peso: "))
    altura = float(input("digite sua altura: "))

    #Fazendo contas para receber a resposta: processamento
    imc = peso/(altura*altura)
    if imc <= 18.4:
        saude = "abaixo do peso"
    elif imc <24.9:
        saude = "peso normal"
    elif imc <= 29.9:
        saude = "acima do peso"
    elif imc <= 34.9:
        saude = "obesidade grau I"
    elif imc <= 40:
        saude = "obesiadde grau II"
    else:
        saude = "obediade grau III" 
    
    #Resposta dos cálculos feitos: saida
    print("seu IMC:", imc,"você esta:", saude)
    time.sleep(3)

    #Deseja voltar?
    denovo()
def conta():
    #pegando informação da função inicio()
    Operacao = int(input())

    #Caso escolha soma
    if Operacao == 1:
        print("Escolha quantos números deseja somar:")
        time.sleep(0.5)
        print("1. dois números")
        time.sleep(0.25)
        print("2. três números")
        time.sleep(0.25)
        print("3. quatro números")
        time.sleep(0.5)

        #Coletando informação
        qnumero = int(input())

        #Caso escolha somar dois números
        if qnumero == 1:

            #pegando informações: entrada
            num1 = int(input("Escolha o primeiro número da adição "))
            num2= int(input("Escolha o segundo número da adição "))
            
            #fazendo conta: processamento
            soma= num1 + num2 

            #Resultado das contas: Saída
            print("O resultado da soma é:",soma)
            time.sleep(3)

            #Deseja voltar?
            denovo()

        #Caso escolha somar três números
        elif qnumero == 2:

            #pegando informações: entrada
            num1 = int(input("Escolha o primeiro número da adição "))
            num2= int(input("Escolha o segundo número da adição "))
            num3= int(input("Escolha o segundo número da adição "))

            #fazendo conta: processamento
            soma= num1 + num2 + num3
            
            #Resultado das contas: Saída
            print("O resultado da soma é:",soma)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()

        #Caso escolha somar quatro números
        elif qnumero == 3:

            #pegando informações: entrada
            num1 = int(input("Escolha o primeiro número da adição "))
            num2= int(input("Escolha o segundo número da adição "))
            num3= int(input("Escolha o segundo número da adição "))
            num4= int(input("Escolha o segundo número da adição "))

            #fazendo conta: processamento
            soma= num1 + num2 + num3 + num4
            
            #Resultado das contas: Saída
            print("O resultado da soma é:",soma)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()

        #Caso digite um número não informado
        else:
            inicio()

    #Caso escolha subtrair
    elif Operacao == 2:
        print("Escolha quantos números deseja subtrair:")
        time.sleep(0.5)
        print("1. dois números")
        time.sleep(0.25)
        print("2. três números")
        time.sleep(0.25)
        print("3. quatro números")
        time.sleep(0.5)
        
        #Coletando informção
        qnumero = int(input())

        #Caso escolha subtrair dois números
        if qnumero == 1:

            #Coletando informações: entrada
            num1 = int(input("Escolha o primeiro número da subtração "))
            num2= int(input("Escolha o segundo número da subtração "))

            #Fazendo conta: processamento
            Subtracao= num1 - num2 

            #Resultado da conta: saída
            print("O resultado da Subtracao é:",Subtracao)
            time.sleep(3)

            #Deseja voltar?
            denovo()
        
        #Caso escolha subtrair três números
        elif qnumero == 2:

            #Coletando informações: entrada
            num1 = int(input("Escolha o primeiro número da subtração "))
            num2= int(input("Escolha o segundo número da subtração "))
            num3= int(input("Escolha o segundo número da subtração "))
            
            #Fazendo conta: processamento
            Subtracao= num1 - num2 - num3
            
            #Resultado da conta: saída
            print("O resultado da Subtracao é:",Subtracao)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()

        #Caso escolha subtrair quatro números
        elif qnumero == 3:

            #Coletando informações: entrada
            num1 = int(input("Escolha o primeiro número da subtração "))
            num2= int(input("Escolha o segundo número da subtração "))
            num3= int(input("Escolha o segundo número da subtração "))
            num4= int(input("Escolha o segundo número da subtração "))
            
            #Fazendo conta: processamento
            Subtracao= num1 - num2 - num3 - num4
            
            #Resultado da conta: saída
            print("O resultado da Subtracao é:",Subtracao)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()

        #Caso digite um número não informado  
        else:
            inicio()

    #Caso escolha multiplicar
    elif Operacao == 3:

        
        print("Escolha quantos números deseja multiplicar:")
        time.sleep(0.5)
        print("1. dois números")
        time.sleep(0.25)
        print("2. três números")
        time.sleep(0.25)
        print("3. quatro números")
        time.sleep(0.5)
        
        #Coletando informações
        qnumero = int(input())
        
        #Caso escolha multiplicar dois números 
        if qnumero == 1:
            
            
            #Coletando informções: entrada
            num1 = int(input("Escolha o primeiro número da multiplicação "))
            num2= int(input("Escolha o segundo número da multiplicação "))
            
            #Fazendo conta: provessamento
            multiplicacao= num1 * num2 
            
            #Resultado da conta: saída
            print("O resultado da multiplicação é:",multiplicacao)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()
        
        #Caso escolha multiplicar três números
        elif qnumero == 2:
            
            #Coletando informações: entrada
            num1 = int(input("Escolha o primeiro número da multiplicação "))
            num2= int(input("Escolha o segundo número da multiplicação "))
            num3= int(input("Escolha o segundo número da multiplicação "))
            
            #Fazendo a conta: processamento
            multiplicacao= num1 * num2 * num3
            
            #Resultado da conta: saída
            print("O resultado da multiplicação é:",multiplicacao)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()
        
        #Caso escolha multiplicar quatro números
        elif qnumero == 3:
            
            #Coletando informações: entrada
            num1 = int(input("Escolha o primeiro número da multiplicação "))
            num2= int(input("Escolha o segundo número da multiplicação "))
            num3= int(input("Escolha o segundo número da multiplicação "))
            num4= int(input("Escolha o segundo número da multiplicação "))
            
            #Fazendo a conta: processamento
            multiplicacao= num1 * num2 * num3 * num4
            
            #Resultadp da conta: saída
            print("O resultado da multiplicacão é:",multiplicacao)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()
        
        #Caso digite um numero não informado
        else:
            inicio()

    #Caso escolha dividir
    elif Operacao == 4:
        print("Escolha quantos números deseja dividir:")
        time.sleep(0.5)
        print("1. dois números")
        time.sleep(0.25)
        print("2. três números")
        time.sleep(0.25)
        print("3. quatro números")
        time.sleep(0.5)
        
        #Coletando informação 
        qnumero = int(input())
        
        #Caso escolha dividir dois números 
        if qnumero == 1:
            
            #Coletando informações: entrada
            num1 = int(input("Escolha o primeiro número da divisão "))
            num2= int(input("Escolha o segundo número da divisão "))
            
            #Fazendo conta: processamento
            divisao= num1 /num2 
            
            #Resultado da conta: saída
            print("O resultado da divisão é:",divisao)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()
        
        #Caso escolha divir três números
        elif qnumero == 2:
            
            #Coletando informações: entrada
            num1 = int(input("Escolha o primeiro número da divisão "))
            num2= int(input("Escolha o segundo número da divisão "))
            num3= int(input("Escolha o segundo número da divisão "))
            
            #Fazendo a conta: precessamento 
            divisao= num1 /num2 /num3
            
            #Resultado da conta: saída
            print("O resultado da divisão é:",divisao)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()
        
        #Caso escolha dividir quatro números
        elif qnumero == 3:
            
            #coletando informações: entrada
            num1 = int(input("Escolha o primeiro número da divisão "))
            num2= int(input("Escolha o segundo número da divisão "))
            num3= int(input("Escolha o segundo número da divisão "))
            num4= int(input("Escolha o segundo número da divisão "))
            
            #Fazendo a conta: processamento
            divisao= num1 /num2 /num3 /num4
            
            #Resultado da conta: saída
            print("O resultado da divisão é:",divisao)
            time.sleep(3)
            
            #Deseja voltar?
            denovo()
        
        #Caso digite um número não informado
        else:
            inicio()

    #Caso digite um número não informado
    else:
        inicio()

##FUNÇÃO RECOMEÇAR
def denovo():
    
    #Recebendo a informação: entrada
    print("deseja fazer mais alguma coisa?")
    print("0. não")
    print("1. sim")

    #Processando a resposta: precessamento
    resposta = int(input())
    
    #Caso a resposta seja não: saída
    if resposta == 0:
        exit()

    #Caso a resposta seja sim: saída  
    elif resposta ==1:
        inicio()

##PROGRAMA
inicio()

