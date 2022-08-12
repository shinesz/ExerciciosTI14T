from Model import Model

class Control:

    def __init__(self):
        self.Model = Model()
        self.opcao = -1
        self.num1 = 0
        self.num2 = 0

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def setNum1(self, num1):
        self.num1 = num1

    def setNum2(self, num2):
        self.num2 = num2

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao








    def menu(self):
        print("Escolha uma das opções abaixo: \n\n " +
                  "0.Sair \n" +
                  "1.Exercicio 1 \n" +
                  "2.Exercicio 2 \n" +
                  "3.Exercicio 3 \n" +
                  "4.Exercicio 4 \n" +
                  "5.Exercicio 5 \n" +
                  "6.Exercicio 6\n"  +
                  "7.Exercicio 7 \n" +
                  "8.Exercicio 8")
        self.setOpcao(int(input()))

    def operacao(self):

        while (self.getOpcao!= 0):
            self.menu()

            if self.getOpcao()== 0:
                print("obrigado!")
                break

            elif self.getOpcao() == 1:
                self.Model.Exercicio1()

            elif self.getOpcao() == 2:
                print ("Digite um número:")
                print(self.Model.Exercicio2(float(input())))

            elif self.getOpcao() == 3:
                print("Digite o valor da base: ")
                base = int(input())
                print("Digite o valor da altura: ")
                alt = int(input())
                print(self.Model.Exercicio3(base, alt))

            elif self.getOpcao() == 4:

                print("Digite quaantos dias você tem:")
                dias = int(input())
                print("Digite quantos meses você tem:")
                meses = int(input())
                print("Digite quantos anos você tem:")
                anos = int(input())
                print("Você tem",self.Model.Exercicio4(dias, meses, anos),"dias")

            elif self.getOpcao() == 5:
                print("Digite a quantidade de votos brancos:")
                branco = int(input())
                print("Digite a quantidade de votos nulos :")
                nulo = int(input())
                print("Digite a quantidade de votos validos:")
                valido = int(input())
                print(self.Model.Exercicio5(branco, nulo, valido))

            elif self.getOpcao() == 6:
                print("Digite o salário: ")
                salario = int(input())
                print("Digite o percentual de reajuste: ")
                perce = int(input())
                print(self.Model.Exercicio6(salario, perce))

            elif self.getOpcao() == 7:
                print("Digite o valor do carro")
                consu = float(input())
                print("O valor do carro com reajuste é:", self.Model.Exercicio7(consu))

            elif self.getOpcao() == 8:
                print("Digite a primeira nota")
                n1 = int(input())
                print("Digite a segunda nota:")
                n2 = int(input())
                print("Digite a  terceira:")
                n3 = int(input())
                print("A nota final é: ",self.Model.Exercicio8(n1, n2, n3))