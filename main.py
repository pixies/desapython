from pessoa import Pessoa

def formulario():
    nome = input("Digite o Nome do usuario: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu genero: \n\t(M) Masculino\n\t(F) Feminino\n\t(N) Outro\n")
    cidade = input("Digite a cidade que voce reside: ")
    estado = input("Digite o estado que voce reside: ")

    return Pessoa(nome, idade, sexo, cidade, estado)

pessoa1 = Pessoa('Rennan', 26, 'M', 'Fortaleza', 'Ceara')

pessoa2 = formulario()


