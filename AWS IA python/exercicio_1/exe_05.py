'''
Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), 
e mostre o resultado de acordo com a operação escolhida.
'''

class AWS:
    def solicitacao(self):
        self.num1 = int(input("Primeiro numero: "))
        self.num2 = int(input("Segundo numero: "))
        self.operacao = input("Selecione uma operação\n(+)(-)(/)(*)")
        
    def soma(self):
        self.soma_valor = self.num1 + self.num2
        return f'O valor da sua soma é: {self.soma_valor}'
    def subtracao(self):
        self.subtracao_valor = self.num1 - self.num2
        return f'O valor da sua subtração é: {self.subtracao_valor}' 
    def divisao(self):
        self.divisao_valor = self.num1 / self.num2
        return f'O valor da sua divisao é: {self.divisao_valor}' 
    def multiplicacao(self):
        if self.operacao == '*':
            return 'O valor da sua multiplicação é: ' + self.num1 * self.num2