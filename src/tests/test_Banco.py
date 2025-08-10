import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Banco import Banco

@pytest.fixture
def banco():
    return Banco()

def test_criar_banco(banco):
    assert isinstance(banco, Banco)
    assert isinstance(banco.contas, dict)
    assert len(banco.contas) == 0

def test_mostrar_contas_ok(banco):
    banco.adicionar_conta(nome="João", cpf="12345678900", saldo=1000.0)
    assert banco.mostrar_contas() is True

def test_mostrar_contas_invalido(banco):
    assert banco.mostrar_contas() is False

def test_adicionar_conta_ok(banco):
    assert banco.adicionar_conta(nome="João", cpf="12345678900", saldo=1000.0)
    assert len(banco.contas) == 1
    assert banco.contas["12345678900"].nome == "João"
    assert banco.contas["12345678900"].saldo == 1000.0

def test_adicionar_conta_duplicada(banco):
    banco.adicionar_conta(nome="João", cpf="12345678900", saldo=1000.0)
    assert banco.adicionar_conta(nome="João", cpf="12345678900", saldo=1000.0) is False

def test_adicionar_conta_invalida(banco):
    assert banco.adicionar_conta(nome="", cpf="12345678900", saldo=1000.0) is False
    assert banco.adicionar_conta(nome="João", cpf="12345678900", saldo=-1000.0) is False

def test_transferir_com_saldo(banco):
    banco.adicionar_conta(nome="João", cpf="12345678900", saldo=1000.0)
    banco.adicionar_conta(nome="Maria", cpf="09876543210", saldo=500.0)
    assert banco.transferir(cpf_origem="12345678900", cpf_destino="09876543210", valor=300.0)
    assert banco.contas["12345678900"].saldo == 700.0
    assert banco.contas["09876543210"].saldo == 800.0

if __name__ == "__main__":
    pytest.main()