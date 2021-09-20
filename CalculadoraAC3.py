import abc
from unittest import TestCase, main

class Calculadora(object):
    def calcular(self,primeiroValor,segundoValor,operador):
        operacao = Operacoes().criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(primeiroValor,segundoValor)
            return resultado

class Operacoes(object):
    def criar(self, operador):
        if (operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self,primeiroValor,segundoValor):
        pass

class Soma(Operacao):
    def executar(self, primeiroValor, segundoValor):
        resultado = primeiroValor + segundoValor
        return resultado
class Subtracao(Operacao):
    def executar(self, primeiroValor, segundoValor):
        resultado = primeiroValor - segundoValor
        return resultado
class Divisao(Operacao):
    def executar(self, primeiroValor, segundoValor):
        resultado = primeiroValor / segundoValor
        return resultado
class Multiplicacao(Operacao):
    def executar(self, primeiroValor, segundoValor):
        resultado = primeiroValor * segundoValor
        return resultado    

class Testes(TestCase):
    def test_soma(self):
        calculo_soma = Calculadora()
        result = calculo_soma.calcular(2,6,'soma')
        self.assertEqual(result,8)
        
    def test_multiplicacao(self):
        calculo_multiplicacao = Calculadora()
        result = calculo_multiplicacao.calcular(10,15,'multiplicacao')
        self.assertEqual(result,150)

    def test_divisao(self):
        calculo_divisao = Calculadora()
        result = calculo_divisao.calcular(10,2,'divisao')
        self.assertEqual(result,5)

    def test_subtracao(self):
        calculo_subtracao = Calculadora()
        result = calculo_subtracao.calcular(10,20,'subtracao')
        self.assertEqual(result, -10)



operacao=input("Qual operação deseja executar? \n").lower()
primeiroValor = float(input("Primeiro número:\n"))
segundoValor = float(input("Segundo número:\n"))
resultado = Calculadora().calcular(primeiroValor,segundoValor,operacao)
print("Resultado = {0:g}".format(float(resultado)))
main()