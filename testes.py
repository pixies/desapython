import unittest
from main import formulario

teste = formulario()

class TestStringMethods(unittest.TestCase):

    def test_empty(self):
        self.assertNotEqual(teste.nome,'','Atributo vazio')
        self.assertNotEqual(teste.idade,'','Atributo vazio')
        self.assertNotEqual(teste.sexo,'','Atributo vazio')
        self.assertNotEqual(teste.cidade,'','Atributo vazio')
        self.assertNotEqual(teste.estado,'','Atributo vazio')

    def test_inteiro(self):
        self.assertEqual(type(teste.idade), int,'Atributo de idade invalido!')

    def test_idade(self):
        self.assertGreaterEqual(teste.idade,0,'Valor invalido!')

if __name__ == '__main__':
    unittest.main()