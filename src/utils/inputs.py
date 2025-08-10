from src.utils.logger import *

def input_nome_validado() -> str:
    while True:
        nome = input("Digite o nome do titular: ").strip()
        if nome:
            return nome
        alertar("Nome inválido. Tente novamente.")

def input_cpf_validado() -> str:
    while True:
        cpf = input("Digite o CPF do titular (apenas números): ").strip()
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        alertar("CPF inválido. Deve conter 11 dígitos numéricos.")

def input_valor_validado() -> float:
    while True:
        valor = input("Digite o valor (apenas números): ").strip()
        if valor.replace('.', '', 1).isdigit():
            return float(valor)
        alertar("Valor inválido. Tente novamente.")