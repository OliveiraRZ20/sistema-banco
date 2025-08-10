from src.Menu import Menu
from src.Banco import Banco
from src.utils.logger import *
from os import system, path

ARQUIVO_CSV = path.abspath(path.join(path.dirname(__file__), 'src', 'data', 'RegistrosContas.csv'))

banco = Banco()
banco.ler_todas_contas(ARQUIVO_CSV)
menu = Menu(banco)

def main() -> None:
    while True:
        system('cls')
        informar("Selecione uma opção:")
        print("[1] Adicionar conta")
        print("[2] Acessar conta")
        print("[3] Mostrar contas")
        print("[4] Transferir")
        print("[5] Sair")
        opcao = input("Escolha uma opção: ").strip()
        match opcao:
            case "1":
                menu.adicionar_conta()
            case "2":
                menu.acessar_conta()
            case "3":
                menu.mostrar_contas()
            case "4":
                menu.transferir()
            case "5":
                banco.salvar_todas_contas(ARQUIVO_CSV)
                confirmar("Informações salvas com sucesso!")
                informar("Saindo do sistema, tchauzinho!")
                return
            case _:
                alertar("Opção inválida. Tente novamente.")
        if opcao not in ("2", "5"):
            system('pause')

if __name__ == "__main__":
    main()