## Sistema Bancário Python
Este é o desafio do Bootcamp da DIO cujo tema é "Criando um Sistema Bancário com Python". Onde a intenção do código é implementar três operações: depósito, saque e extrato para um banco que deseja monetizar suas operações em Python.
**Descrição:**

Este sistema bancário em Python permite que os usuários realizem diversas operações bancárias, como:

* **Depósito:** Adiciona valor à conta do usuário.
* **Saque:** Retira valor da conta do usuário, com limite de valor e número de saques por dia.
* **Extrato:** Exibe todas as movimentações da conta, incluindo depósitos, saques e saldo atual.
* **Novo usuário:** Permite o cadastro de novos clientes no sistema.
* **Nova conta:** Vincula uma conta a um cliente já cadastrado.
* **Listar contas:** Mostra todas as contas cadastradas no sistema.

**Funcionalidades:**

* **Validação de CPF:** O sistema garante que cada CPF seja único no sistema.
* **Limite de saque:** O usuário possui um limite de valor e número de saques por dia.
* **Extrato detalhado:** O extrato mostra data, hora e tipo de cada movimentação.
* **Criação de contas:** O sistema permite a criação de múltiplas contas para um mesmo cliente.

**Tecnologias:**

* **Linguagem de programação:** Python
* **Módulos:** datetime

**Como usar:**

1. Execute o script `main.py`.
2. Siga as instruções na tela para realizar as operações desejadas.

**Observações:**

* Este é um exemplo simples de um sistema bancário.
* Para um sistema completo, seria necessário implementar funcionalidades adicionais, como:
    * Autenticação de usuários
    * Controle de acesso
    * Segurança de dados
    * Integração com outros sistemas bancários

**Exemplo de uso:**

1. **Novo usuário:** Digite seu CPF, nome completo, data de nascimento e endereço.
2. **Nova conta:** Informe o CPF do usuário e a conta será criada.
3. **Depósito:** Digite o valor do depósito e o saldo será atualizado.
4. **Saque:** Digite o valor do saque e o saldo será atualizado, se possível.
5. **Extrato:** Visualize todas as movimentações da sua conta.


**Dúvidas e sugestões:**

* Sinta-se à vontade para abrir um issue no para reportar bugs ou sugerir melhorias.
