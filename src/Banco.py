import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils.logger import *
from src.utils.formatador import formatar_dinheiro
from src.ContaBancaria import ContaBancaria

class Banco():
    def __init__(self):
        self.contas: dict[str, ContaBancaria] = {}

    def ler_todas_contas(self, ARQUIVO_CSV: str) -> None:
        with open(ARQUIVO_CSV, 'r') as file:
            for line in file:
                nome, cpf, saldo = line.strip().split(',')
                self.contas[cpf] = ContaBancaria(nome, cpf, float(saldo))

    def salvar_todas_contas(self, ARQUIVO_CSV: str) -> None:
        with open(ARQUIVO_CSV, 'w') as file:
            for conta in self.contas.values():
                file.write(f"{conta.nome},{conta.cpf},{conta.saldo}\n")

    def mostrar_contas(self) -> bool:
        if len(self.contas) == 0:
            alertar("Nenhuma conta cadastrada.")
            return False
        else:
            for conta in self.contas.values():
                informar(f"- Nome: {conta.nome} -- Saldo atual: {formatar_dinheiro(conta.saldo)}")
            return True

    def adicionar_conta(self, nome: str, cpf: str, saldo: float) -> bool:
        if not nome or not cpf or saldo < 0:
            alertar("Dados inválidos!")
            return False
        if cpf in self.contas.keys():
            alertar("CPF já cadastrado!")
            return False
        else:
            self.contas[cpf] = ContaBancaria(nome, cpf, saldo)
            confirmar(f"Conta de {nome} adicionada com sucesso!")
            return True

    def transferir(self, cpf_origem: str, cpf_destino: str, valor: float) -> bool:
        if cpf_origem in self.contas.keys() and cpf_destino in self.contas.keys() and cpf_destino != cpf_origem:
            if self.contas[cpf_origem].saldo >= valor:
                self.contas[cpf_origem].sacar(valor)
                self.contas[cpf_destino].depositar(valor)
                confirmar(f"Transferência de {formatar_dinheiro(valor)} de {self.contas[cpf_origem].nome} para {self.contas[cpf_destino].nome} realizada com sucesso!")
                return True
            else:
                alertar("Saldo insuficiente para a transferência") 
        else:
            alertar("CPF não encontrado")
        return False