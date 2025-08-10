from src.utils.logger import *
from src.utils.inputs import *
from src.Banco import Banco
from src.ContaBancaria import ContaBancaria
from os import system

class Menu():
    def __init__(self, banco: Banco):
        self.banco: Banco = banco

    def adicionar_conta(self) -> None:
        self.banco.adicionar_conta(nome=input_nome_validado(),
                                   cpf=input_cpf_validado(),
                                   saldo=input_valor_validado())

    def acessar_conta(self) -> None:
        cpf_solicitado: str = input_cpf_validado()
        if cpf_solicitado not in self.banco.contas:
            alertar("CPF não encontrado.")
            return
        conta_selecionada: ContaBancaria = self.banco.contas[cpf_solicitado]
        while True:
            system('cls')
            confirmar(f"Bem-vindo, {conta_selecionada.nome}!")
            informar("Selecione uma opção:")
            print("[1] Depositar")
            print("[2] Sacar")
            print("[3] Mostrar saldo")
            print("[4] Voltar")
            opcao = input("Opção: ").strip()
            match opcao:
                case "1":
                    conta_selecionada.depositar(input_valor_validado())
                case "2":
                    conta_selecionada.sacar(input_valor_validado())
                case "3":
                    conta_selecionada.mostrar_saldo()
                case "4":
                    informar("Voltando ao menu principal")
                    return
                case _:
                    alertar("Opção inválida. Tente novamente.")
            system('pause')

    def mostrar_contas(self) -> None:
        self.banco.mostrar_contas()

    def transferir(self) -> None:
        self.banco.transferir(cpf_origem=input_cpf_validado(),
                              cpf_destino=input_cpf_validado(),
                              valor=input_valor_validado())