import unittest
from src.banco import Conta

class TestBank(unittest.TestCase):

    def setUp(self):
        self.conta1 = Conta("123", 1000)
        self.conta2 = Conta("456", 500)

    def teste_deposito(self):
        self.conta1.deposito(500)
        self.assertEqual(self.conta1.balance, 1500)

    def teste_transferencia(self):
        self.conta1.transferencia(self.conta2, 300)
        self.assertEqual(self.conta1.balance, 700)
        self.assertEqual(self.conta2.balance, 800)

    def teste_transferencia_com_valor_insuficiente(self):
        with self.assertRaises(ValueError):
            self.conta1.transferencia(self.conta2, 2000)

    def teste_saque(self):
        self.conta1.saque(500)
        self.assertEqual(self.conta1.balance, 500)

    def teste_saque_com_fundos_insuficientes(self):
        with self.assertRaises(ValueError):
            self.conta1.saque(2000)

    def teste_transferencia_com_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.conta1.transferencia(self.conta2, -100)

    def teste_transferencia_para_conta_inexistente(self):
        conta_inexistente = None
        with self.assertRaises(ValueError):
            self.conta1.transferencia(conta_inexistente, 100)

if __name__ == '__main__':
    unittest.main()
