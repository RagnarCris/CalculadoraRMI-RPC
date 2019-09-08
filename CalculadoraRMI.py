# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:00:53 2019

@author: crist
"""
import Pyro4

@Pyro4.expose
class Calculadora(object):
    
    def somar(self, fatorA, fatorB):
        return (fatorA+fatorB)

    def subtrair(self, fatorA, fatorB):
        return (fatorA-fatorB)
    
    def multiplicar(self, fatorA, fatorB):
        return (fatorA*fatorB)
    
    def dividir(self, fatorA, fatorB):
        if fatorB == 0:
            return ("Voce digitou um denominador invalido, divisao por 0 tem resultado indeterminado")
        else:
            return (fatorA/fatorB)
    
    def gerarResto(self, fatorA, fatorB):
        return (fatorA%fatorB)


daemon = Pyro4.Daemon()					# cria um daemon do Pyro
ns = Pyro4.locateNS() 					# procura o nome do servidor de nomes
server = Calculadora()						# inicia um objeto da classe servidor
uri = daemon.register(server)			# registra o objeto servidor como um objeto do Pyro4
ns.register('servidorCalculadora', uri)	# registra o objeto do Pyro4 como serviço com um nome
print('Servidor rodando')
daemon.requestLoop()	