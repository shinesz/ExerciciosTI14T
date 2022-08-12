class Model :
    def __init__(self):
        pass
        self.A = 0
        self.B = 0

    def Exercicio1(self):

        A = 10
        B = 20

        self.A = B
        self.B = A


        return print("O número A é:", self.A, "\nO número B é:", self.B)

    def Exercicio2(self, num):

        return print("O antecessor do número é: ", num - 1)


    def Exercicio3(self, base, alt):

        return print("a área do retangulo é:", base * alt)

    def Exercicio4(self, dias, meses, anos):
         return ((meses * 30) + dias + (anos * 360))

    def Exercicio5(self, branco, nulo, valido):

        total = branco + nulo + valido
        tbranco = (100 * branco) // total
        tnulo = (100 * nulo) // total
        tvalido = (100 * valido) // total

        return print("Quantidade total de votos:",total,"\nvotos brancos", tbranco, "\nvotos nulos", tnulo ,"\nvotos validos",tvalido)

    def Exercicio6(self,salario , perce):

        salafn = (perce / 100) * salario

        return salafn + salario

    def Exercicio7(self, consu):

        dist = (28/100) * consu
        fabrica = (45/ 100) * consu

        return dist + fabrica + consu

    def Exercicio8(self, n1, n2, n3):

        return (n1 + n2 + n3)/3