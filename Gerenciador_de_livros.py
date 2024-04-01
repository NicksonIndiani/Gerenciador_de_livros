lista_livro = []

def cadastrar_livro(id_global):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")

    livro = {"id": id_global, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)

def consultar_livro():
    while True:
        print("\nOpções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            for livro in lista_livro:
                print(f"Id: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
        elif opcao == "2":
            id_consulta = int(input("Digite o Id do livro: "))
            for livro in lista_livro:
                if livro["id"] == id_consulta:
                    print(f"Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    break
            else:
                print("Livro não encontrado.")
        elif opcao == "3":
            autor_consulta = input("Digite o nome do autor: ")
            for livro in lista_livro:
                if livro["autor"].lower() == autor_consulta.lower():
                    print(f"Nome: {livro['nome']}, Editora: {livro['editora']}")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def remover_livro():
    id_remover = int(input("Digite o Id do livro a ser removido: "))
    for livro in lista_livro:
        if livro["id"] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso.")
            break
    else:
        print("Livro não encontrado.")

def main():
    print("Bem-vindo ao software de gerenciamento de livros!")
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}!")

    lista_livro = []
    id_global = 1

    while True:
        print("\nMenu:")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")

        opcao_menu = input("Escolha uma opção: ")
        if opcao_menu == "1":
            cadastrar_livro(id_global)
            id_global += 1
        elif opcao_menu == "2":
            consultar_livro()
        elif opcao_menu == "3":
            remover_livro()
        elif opcao_menu == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
    except Exception as e:
        print(f"Erro: {e}")
