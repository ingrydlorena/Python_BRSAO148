''' 1 - Crie um programa em Python que peça dois 
números ao usuário, some esses valores e exiba o resultado na tela.
'''
class Soma:
    def solicitacao(self):
        self.num1 = float(input("Diga o primeiro valor: "))
        self.num2 = float(input("Diga o segundo valor: "))

    def soma(self):
        self.calculo_soma = self.num1 + self.num2
        return self.calculo_soma
        

    def saida(self):
        print("Bem vindo a soma com python")
        self.solicitacao()
        print(f"Valores salvos, seu resultado é {self.soma():.2f}")
    
    

resultado = Soma()
resultado.saida()