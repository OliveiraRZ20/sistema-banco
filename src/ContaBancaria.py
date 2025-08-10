import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils.logger import *
from src.utils.formatador import formatar_dinheiro

class ContaBancaria():
    def __init__(self, nome: str, cpf: str, saldo: float):
        self.nome: str = nome
        self.cpf: str = cpf
        self.saldo: float = saldo
    
    def depositar(self, valor: float) -> bool:
        if not valor:
            alertar("Valor inválido!")
            return False
        self.saldo += valor
        confirmar(f"{formatar_dinheiro(valor)} depositados na conta de {self.nome}")
        return True

    def sacar(self, valor: float) -> bool:
        if not valor:
            alertar("Valor inválido!")
        elif valor >= self.saldo:
            alertar("Saldo insuficiente!")
        else:
            self.saldo -= valor
            confirmar(f"{formatar_dinheiro(valor)} sacados da conta de {self.nome}")
            return True
        return False

    def mostrar_saldo(self) -> None:
        informar(f"Saldo atual: {formatar_dinheiro(self.saldo)}")