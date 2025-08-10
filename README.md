
# 💰 Sistema Bancário em Python

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Status](https://img.shields.io/badge/status-concluído%20%7C%20recebendo%20melhorias-blue)

Este projeto é um sistema bancário simples desenvolvido em Python, que permite gerenciar contas bancárias, realizar depósitos, saques, transferências e visualizar informações das contas. Os dados das contas são persistidos em um arquivo CSV.

---

## 🧱 Estrutura do Projeto

```
📄 main.py
📁 src/
├── 📄 Banco.py
├── 📄 ContaBancaria.py
├── 📄 Menu.py
├── 📁 data/
│   └── 📄 RegistrosContas.csv
├── 📁 tests/
│   ├── 📄 test_Banco.py
│   └── 📄 test_ContaBancaria.py
├── 📁 utils/
│   ├── 📄 formatador.py
│   ├── 📄 inputs.py
│   └── 📄 logger.py
📁 notebooks/
└── 📄 tests.ipynb
```

---

## ⚙️ Funcionalidades

- **Adicionar conta:** Criação de novas contas bancárias com nome, CPF e saldo inicial.
- **Acessar conta:** Permite depositar, sacar e consultar saldo de uma conta existente.
- **Mostrar contas:** Exibe todas as contas cadastradas e seus saldos.
- **Transferir:** Realiza transferência de valores entre contas.
- **Persistência:** As contas são salvas e carregadas do arquivo `src/data/RegistrosContas.csv`.

---

## 📌 Principais Arquivos

- `main.py`: Ponto de entrada do sistema, gerencia o menu principal e a interação com o usuário.
- `src/Banco.py`: Implementa a classe Banco, responsável pelo gerenciamento das contas.
- `src/ContaBancaria.py`: Implementa a classe ContaBancaria, que representa uma conta individual.
- `src/Menu.py`: Implementa a classe Menu, responsável pela navegação do usuário.
- `src/utils/`: Funções utilitárias para formatação, entrada de dados e mensagens.
- `src/tests/`: Testes automatizados para as principais funcionalidades.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.12+** instalado.
2. Instale os requisitos (caso queira rodar os testes):
   ```bash
   pip install pytest
   ```
3. Execute o sistema com:
   ```bash
   python main.py
   ```
4. Siga as instruções do menu para utilizar o sistema.

---

## 🧪 Testes

Os testes automatizados estão em:

- `src/tests/test_Banco.py`
- `src/tests/test_ContaBancaria.py`

Para rodar os testes, utilize:

```bash
pytest src/tests/
```

---

## 💡 Observações

- O sistema utiliza o terminal para interação.
- Os dados são persistidos automaticamente ao sair do sistema.
- O arquivo CSV pode ser editado manualmente, mas recomenda-se utilizar o sistema para garantir a integridade dos dados.

---

## 🤝 Contribuições

Pull requests são bem-vindos!  
Se você tiver sugestões, melhorias ou encontrar bugs, fique à vontade para abrir uma issue ou enviar uma PR.

---

Desenvolvido com 💻 por **Lucca Oliveira**.
