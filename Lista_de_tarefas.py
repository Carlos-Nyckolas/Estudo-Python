#imports
import time



#funções
def inicio():
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
    print("O que vocẽ deseja fazer?")
    time.sleep(0.5)
    print("1. Fazer operações basicas")
    time.sleep(0.25)
    print("2.")
    time.sleep(0.25)
    print("3.")
    time.sleep(0.5)
    Escolha = int(input())
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
    else:
        inicio()
def conta():
    Operacao = int(input())

    if Operacao == 1:
        print("Escolha quantos números deseja somar:")
        time.sleep(0.5)
        print("1. dois números")
        time.sleep(0.25)
        print("2. três números")
        time.sleep(0.25)
        print("3. quatro números")
        time.sleep(0.5)
        qnumero = int(input())
        if qnumero == 1:
            num1 = int(input("Escolha o primeiro número da adição "))
            num2= int(input("Escolha o segundo número da adição "))
            soma= num1 + num2 
            print("O resultado da soma é:",soma)
        elif qnumero == 2:
            num1 = int(input("Escolha o primeiro número da adição "))
            num2= int(input("Escolha o segundo número da adição "))
            num3= int(input("Escolha o segundo número da adição "))
            soma= num1 + num2 + num3
            print("O resultado da soma é:",soma)
        elif qnumero == 3:
            num1 = int(input("Escolha o primeiro número da adição "))
            num2= int(input("Escolha o segundo número da adição "))
            num3= int(input("Escolha o segundo número da adição "))
            num4= int(input("Escolha o segundo número da adição "))
            soma= num1 + num2 + num3 + num4
            print("O resultado da soma é:",soma)
        else:
            inicio()
      
    elif Operacao == 2:
        print("Escolha quantos números deseja subtrair:")
        time.sleep(0.5)
        print("1. dois números")
        time.sleep(0.25)
        print("2. três números")
        time.sleep(0.25)
        print("3. quatro números")
        time.sleep(0.5)
        qnumero = int(input())
        if qnumero == 1:
            num1 = int(input("Escolha o primeiro número da subtração "))
            num2= int(input("Escolha o segundo número da subtração "))
            Subtracao= num1 - num2 
            print("O resultado da Subtracao é:",Subtracao)
        elif qnumero == 2:
            num1 = int(input("Escolha o primeiro número da subtração "))
            num2= int(input("Escolha o segundo número da subtração "))
            num3= int(input("Escolha o segundo número da subtração "))
            Subtracao= num1 - num2 - num3
            print("O resultado da Subtracao é:",Subtracao)
        elif qnumero == 3:
            num1 = int(input("Escolha o primeiro número da subtração "))
            num2= int(input("Escolha o segundo número da subtração "))
            num3= int(input("Escolha o segundo número da subtração "))
            num4= int(input("Escolha o segundo número da subtração "))
            Subtracao= num1 - num2 - num3 - num4
            print("O resultado da Subtracao é:",Subtracao)
        else:
            inicio()

    elif Operacao == 3:
        print("Escolha quantos números deseja multiplicar:")
        time.sleep(0.5)
        print("1. dois números")
        time.sleep(0.25)
        print("2. três números")
        time.sleep(0.25)
        print("3. quatro números")
        time.sleep(0.5)
        qnumero = int(input())
        if qnumero == 1:
            num1 = int(input("Escolha o primeiro número da multiplicação "))
            num2= int(input("Escolha o segundo número da multiplicação "))
            multiplicacao= num1 * num2 
            print("O resultado da multiplicação é:",multiplicacao)
        elif qnumero == 2:
            num1 = int(input("Escolha o primeiro número da multiplicação "))
            num2= int(input("Escolha o segundo número da multiplicação "))
            num3= int(input("Escolha o segundo número da multiplicação "))
            multiplicacao= num1 * num2 * num3
            print("O resultado da multiplicação é:",multiplicacao)
        elif qnumero == 3:
            num1 = int(input("Escolha o primeiro número da multiplicação "))
            num2= int(input("Escolha o segundo número da multiplicação "))
            num3= int(input("Escolha o segundo número da multiplicação "))
            num4= int(input("Escolha o segundo número da multiplicação "))
            multiplicacao= num1 * num2 * num3 * num4
            print("O resultado da multiplicacão é:",multiplicacao)
        else:
            inicio()

    elif Operacao == 4:
        print("Escolha quantos números deseja dividir:")
        time.sleep(0.5)
        print("1. dois números")
        time.sleep(0.25)
        print("2. três números")
        time.sleep(0.25)
        print("3. quatro números")
        time.sleep(0.5)
        qnumero = int(input())
        if qnumero == 1:
            num1 = int(input("Escolha o primeiro número da divisão "))
            num2= int(input("Escolha o segundo número da divisão "))
            divisao= num1 /num2 
            print("O resultado da divisão é:",divisao)
        elif qnumero == 2:
            num1 = int(input("Escolha o primeiro número da divisão "))
            num2= int(input("Escolha o segundo número da divisão "))
            num3= int(input("Escolha o segundo número da divisão "))
            divisao= num1 /num2 /num3
            print("O resultado da divisão é:",divisao)
        elif qnumero == 3:
            num1 = int(input("Escolha o primeiro número da divisão "))
            num2= int(input("Escolha o segundo número da divisão "))
            num3= int(input("Escolha o segundo número da divisão "))
            num4= int(input("Escolha o segundo número da divisão "))
            divisao= num1 /num2 /num3 /num4
            print("O resultado da divisão é:",divisao)
        else:
            inicio()

    else:
        inicio()




#Programa
inicio()

