def alertar(msg: str) -> None:
    print(f"\033[31m[ERRO] {msg}\033[0m")

def informar(msg: str) -> None:
    print(f"\033[33m[INFO] {msg}\033[0m")

def confirmar(msg: str) -> None:
    print(f"\033[32m[SUCESSO] {msg}\033[0m")