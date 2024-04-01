## <h1 align="center">Sistema de Gerenciamento de Livros <img align="center" alt="Nickson-Python" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" /></h1> 

Este é um simples gerenciador de livros em Python. Ele permite cadastrar, consultar e remover livros da lista.

## Funcionalidades

1. **Cadastrar Livro**: Adiciona um novo livro à lista.
2. **Consultar Livro**:
    - Consulta todos os livros cadastrados.
    - Consulta um livro específico pelo ID.
    - Consulta livros por autor.
3. **Remover Livro**: Remove um livro da lista pelo ID.

## Como Usar

1. Clone este repositório para a sua máquina.
2. Execute o arquivo `gerenciador_livros.py`.
3. Siga as instruções no console para cadastrar, consultar ou remover livros.

## Exemplo de Uso

```python
# Cadastrar um livro
cadastrar_livro(1)

# Consultar todos os livros
consultar_livro()

# Consultar livro por ID
consultar_livro()

# Consultar livro por autor
consultar_livro()

# Remover livro
remover_livro()
```

## Exemplo de Resultados

```
Bem-vindo ao software de gerenciamento de livros!
Digite seu nome: Nickson
Olá, Nickson!       

Menu:
1. Cadastrar Livro  
2. Consultar Livro  
3. Remover Livro    
4. Encerrar Programa
Escolha uma opção: 1
Digite o nome do livro: As Crônicas de Narnia
Digite o autor do livro: C. S. Lewis
Digite a editora do livro: Editoral Presença

Menu:
1. Cadastrar Livro
2. Consultar Livro
3. Remover Livro
4. Encerrar Programa
Escolha uma opção: 2

Opções de consulta:
1. Consultar Todos
2. Consultar por Id
3. Consultar por Autor
4. Retornar ao menu
Escolha uma opção: 2
Digite o Id do livro: 1
Nome: As Crônicas de Narnia, Autor: C. S. Lewis, Editora: Editoral Presença

Opções de consulta:
1. Consultar Todos
2. Consultar por Id
3. Consultar por Autor
4. Retornar ao menu
Escolha uma opção: 4

Menu:
1. Cadastrar Livro
2. Consultar Livro
3. Remover Livro
4. Encerrar Programa
Escolha uma opção: 4
Encerrando o programa.
```
