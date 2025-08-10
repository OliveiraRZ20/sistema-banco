import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ContaBancaria import ContaBancaria

@pytest.fixture
def conta():
    return ContaBancaria (
        nome="ContaTeste",
        cpf="11111111111",
        saldo=0.0
    )

def test_atributos_conta(conta):
    assert conta.nome == "ContaTeste"
    assert conta.cpf == "11111111111"
    assert conta.saldo == 0.0

def test_depositar(conta):
    assert conta.depositar(100.0) is True
    assert conta.saldo == 100.0

def test_sacar_com_saldo(conta):
    conta.depositar(100.0)
    assert conta.sacar(50.0) is True
    assert conta.saldo == 50.0

def test_sacar_sem_saldo(conta):
    assert conta.sacar(50.0) is False
    assert conta.saldo == 0.0

if __name__ == "__main__":
    pytest.main()