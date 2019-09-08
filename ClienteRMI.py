# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:15:10 2019

@author: crist
"""
import Pyro4

while True:
    print("\nOpções:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Gerar Resto")
    print("0 - Sair")
    
    op = int(input("\nInforme a opção desejada: "))
	
    if op == 1:
        fatorA = int(input("\nInsira o primeiro fator/parcela da operacao: "))
        fatorB = int(input("Insira o segundo fator/parcela da operacao: "))
        ns = Pyro4.locateNS()
        uri = ns.lookup('servidorCalculadora')
        obj = Pyro4.Proxy(uri)
        print("RESULTADO: "+ str(obj.somar(fatorA, fatorB)))
        
    elif op == 2:
        fatorA = int(input("\nInsira o primeiro fator/parcela da operacao: "))
        fatorB = int(input("Insira o segundo fator/parcela da operacao: "))
        ns = Pyro4.locateNS()
        uri = ns.lookup('servidorCalculadora')
        obj = Pyro4.Proxy(uri)
        print("RESULTADO: "+ str(obj.subtrair(fatorA, fatorB)))
        
    elif op == 3:
        fatorA = int(input("\nInsira o primeiro fator/parcela da operacao: "))
        fatorB = int(input("Insira o segundo fator/parcela da operacao: "))
        ns = Pyro4.locateNS()
        uri = ns.lookup('servidorCalculadora')
        obj = Pyro4.Proxy(uri)
        print("RESULTADO: "+ str(obj.multiplicar(fatorA, fatorB)))
        
    elif op == 4:
        fatorA = int(input("\nInsira o primeiro fator/parcela da operacao: "))
        fatorB = int(input("Insira o segundo fator/parcela da operacao: "))
        ns = Pyro4.locateNS()
        uri = ns.lookup('servidorCalculadora')
        obj = Pyro4.Proxy(uri)
        print("RESULTADO: "+ str(obj.dividir(fatorA, fatorB)))
        
    elif op == 5:
        fatorA = int(input("\nInsira o primeiro fator/parcela da operacao: "))
        fatorB = int(input("Insira o segundo fator/parcela da operacao: "))
        ns = Pyro4.locateNS()
        uri = ns.lookup('servidorCalculadora')
        obj = Pyro4.Proxy(uri)
        print("RESULTADO: "+ str(obj.gerarResto(fatorA, fatorB)))
        
    elif op == 0:
        print("Saindo... Arivederci!")
        exit()
        
    else:
        print("Insira uma opção válida.")