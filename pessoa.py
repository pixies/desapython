class Pessoa:

    def __init__(self, nome, idade, sexo, cidade, estado):

        self._nome = nome;
        self._idade = idade;
        self._sexo = sexo;
        self._cidade = cidade;
        self._estado = estado;

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print("Atributo modificado!")
        self._nome = nome
        
    @property
    def idade(self):
        return self._idade
        
    @idade.setter
    def idade(self, idade):
        if type(idade) == int:
            self._idade = idade
            print("Atributo modificado!")
        else:
            print("Valor do atributo invalido!")
            pass      

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        if sexo in ["m","M","f","F","o","O"]:
            self._sexo = sexo
            print("Atributo modificado!")
        else:
            print("Valor do atributo invalido!")
            pass        

    @property
    def cidade(self):
        return self._cidade
        
    @cidade.setter
    def cidade(self, cidade):
        print("Atributo modificado!")
        self._cidade = cidade

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        print("Atributo modificado!")
        self._estado = estado

