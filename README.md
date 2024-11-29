<h1 align="center">
    🏦 Simulador de Rede Bancária
</h1>


<p align="center"> 
    <a href="#descricao">Descrição</a> • 
    <a href="#funcionalidades">Funcionalidades</a> • 
    <a href="#instalacao">Instalação</a> • 
    <a href="#uso">Como Usar</a> • 
    <a href="#dados">Armazenamento de Dados</a> • 
    <a href="#estrutura">Estrutura do Código</a> 
</p>

---

### 📜 Descrição <a id="descricao"></a>
O **Simulador de Rede Bancária** é uma aplicação desenvolvida em Python que simula as operações básicas de uma rede bancária. Este projeto busca integrar conceitos de **estruturas de dados** e **algoritmos**, permitindo gerenciar contas bancárias, realizar operações financeiras e simular filas de atendimento em caixas eletrônicos.

O objetivo é proporcionar uma visão prática de como sistemas bancários funcionam, enquanto explora a eficiência de estruturas como filas FIFO e gerenciamento de objetos em Python.

---

### ⚙️ Funcionalidades <a id="funcionalidades"></a>

#### 💼 Gerenciamento de Contas
- Cadastro de novas contas com número, titular e saldo inicial.
- Consulta de informações de contas (titular, saldo).
- Remoção de contas cadastradas.
- Registro de todas as transações no histórico da conta.

#### 💸 Operações Financeiras
- **Depósito**: Incrementa o saldo da conta e registra no histórico.
- **Saque**: Verifica saldo disponível antes de realizar a operação.
- **Transferências**: Permite a movimentação de valores entre contas, registrando no histórico de ambas.

#### 🚶‍♂️ Filas de Atendimento
- Simulação de atendimento em caixas eletrônicos usando uma estrutura de **fila FIFO**.
- Adição de clientes à fila para operações como depósito, saque ou consulta.
- Processamento dinâmico da fila, com saída automática dos clientes atendidos.

---

### 🛠️ Instalação <a id="instalacao"></a>

1. Clone o repositório para sua máquina local:
```bash
git clone https://github.com/kaychenderson/SimuladorRedeBarcaria.git
```

2. Navegue até o diretório do projeto:
```bash
cd SimuladorRedeBarcaria
```

3. Execute o programa:
```bash
python banc.py
```
---

### 🚀 Como Usar <a id="uso"></a>

#### Cadastro de Contas:
- Insira o número da conta, o nome do titular e o saldo inicial.
- Exemplo: 'Conta 1: Alice - R$1000,00'.

#### Realização de Operações:
- Depósitos, saques e transferências podem ser realizados diretamente nas contas cadastradas.
- Exemplos:

```bash
conta.depositar(200)  # Adiciona R$200 ao saldo da conta.
conta.sacar(150)      # Retira R$150 do saldo disponível.
conta.transferir(300, conta_destino)  # Move R$300 para outra conta.
```

#### Simulação de Atendimento:
- Adicione clientes à fila para diferentes operações.
- Processe a fila sequencialmente:

```bash
banco.adicionar_cliente_fila(1, "sacar", 50)
banco.processar_fila()  # Atende o cliente e realiza a operação.
```

---

### 💾 Armazenamento de Dados <a id="dados"></a>

- Os dados são armazenados em objetos Python em memória.
- As contas e suas transações ficam disponíveis enquanto o programa estiver em execução.
- Caso precise salvar dados persistentes, o sistema pode ser estendido para utilizar arquivos JSON ou banco de dados.

---

### 📂 Estrutura do Código <a id="estrutura"></a>

- O projeto segue uma estrutura modular, com separação de responsabilidades:

#### Classes Principais:

1. ContaBancaria:

- Representa uma conta bancária, incluindo métodos para depósito, saque, transferência e histórico de transações.

2. SimuladorBanco:

- Controla as funcionalidades do banco, incluindo cadastro de contas, gerenciamento de filas e execução de operações.

#### Estruturas de Dados:

- Dicionário: Para armazenar e acessar contas de forma eficiente.
- Deque: Para simular a fila de atendimento (FIFO).

---

### 💡 Exemplos de Uso

```bash
# Cadastro de contas
banco.cadastrar_conta(1, "Alice", 1000)
banco.cadastrar_conta(2, "Bob", 500)

# Depósito
print(banco.contas[1].depositar(200))

# Transferência
print(banco.contas[1].transferir(300, banco.contas[2]))

# Adicionar cliente à fila e processar
banco.adicionar_cliente_fila(1, "sacar", 50)
print(banco.processar_fila())
``` 