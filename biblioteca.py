# Classe que representa um livro da biblioteca
class Livro:
    def __init__(self, titulo, autor, ano, codigo):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.codigo = codigo
        self.status = "Disponível"

#Ordena os livros pelo título
def ordenar_por_titulo(biblioteca):
    for i in range(len(biblioteca)):
        for j in range(i + 1, len(biblioteca)):
            if biblioteca[i].titulo.lower() > biblioteca[j].titulo.lower():
                aux = biblioteca[i]
                biblioteca[i] = biblioteca[j]
                biblioteca[j] = aux
    return biblioteca


# Exibe os dados de um livro na tela
def exibir_livro(livro):
    print("-" * 35)
    print(f"Código : {livro.codigo}")
    print(f"Título : {livro.titulo}")
    print(f"Autor  : {livro.autor}")
    print(f"Ano    : {livro.ano}")
    print(f"Status : {livro.status}")
    print("-" * 35)


# Cadastra um novo livro na biblioteca
def cadastrar_livro(biblioteca):
    print("\n--- Cadastrar Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    codigo = input("Código: ")

    # Verifica se já existe um livro com o mesmo código
    for livro in biblioteca:
        if livro.codigo == codigo:
            print("Erro: já existe um livro com esse código!")
            return biblioteca

    novo_livro = Livro(titulo, autor, ano, codigo)
    biblioteca.append(novo_livro)

    # Mantém a lista ordenada por título após cada cadastro
    biblioteca = ordenar_por_titulo(biblioteca)

    print("Livro cadastrado com sucesso!")
    return biblioteca


# Consulta livros por código ou por autor
def consultar_livro(biblioteca):
    print("\n--- Consultar Livro ---")
    print("1 - Por código")
    print("2 - Por autor")
    opcao = input("Escolha: ")

    if opcao == "1":
        codigo = input("Código: ")
        for livro in biblioteca:
            if livro.codigo == codigo:
                exibir_livro(livro)
                return
        print("Livro não encontrado")

    else:
        if opcao == "2":
            autor = input("Autor: ")
            encontrou = False
            for livro in biblioteca:
                # Comparação sem diferenciar maiúsculas e minúsculas
                if livro.autor.lower() == autor.lower():
                    exibir_livro(livro)
                    encontrou = True
            if not encontrou:
                print("Livro não encontrado")

        else:
            print("Opção inválida!")


# Altera título, autor ou ano de um livro
def alterar_dados(biblioteca):
    print("\n--- Alterar Dados ---")
    codigo = input("Código do livro: ")

    for livro in biblioteca:
        if livro.codigo == codigo:
            print("O que deseja alterar?")
            print("1 - Título")
            print("2 - Autor")
            print("3 - Ano")
            opcao = input("Escolha: ")

            if opcao == "1":
                livro.titulo = input("Novo título: ")
                # Reordena pois o título mudou
                biblioteca = ordenar_por_titulo(biblioteca)
            else:
                if opcao == "2":
                    livro.autor = input("Novo autor: ")
                else:
                    if opcao == "3":
                        livro.ano = input("Novo ano: ")
                    else:
                        print("Opção inválida!")
                        return biblioteca

            print("Dados alterados com sucesso!")
            return biblioteca

    print("Livro não encontrado")
    return biblioteca


# Remove um livro da biblioteca pelo código
def remover_livro(biblioteca):
    print("\n--- Remover Livro ---")
    codigo = input("Código do livro: ")

    for i in range(len(biblioteca)):
        if biblioteca[i].codigo == codigo:
            biblioteca.pop(i)
            print("Livro removido com sucesso!")
            return biblioteca

    print("Livro não encontrado")
    return biblioteca


# Lista todos os livros cadastrados (título e ano)
def listar_todos(biblioteca):
    print("\n--- Lista de Livros ---")

    if len(biblioteca) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in biblioteca:
        print(f"Título: {livro.titulo} | Ano: {livro.ano}")


# Realiza o empréstimo de um livro
def realizar_emprestimo(biblioteca):
    print("\n--- Realizar Empréstimo ---")
    codigo = input("Código do livro: ")

    for livro in biblioteca:
        if livro.codigo == codigo:
            if livro.status == "Disponível":
                livro.status = "Emprestado"
                print("Empréstimo realizado com sucesso!")
            else:
                print("Livro já emprestado")
            return

    print("Livro não encontrado")


# Realiza a devolução de um livro
def realizar_devolucao(biblioteca):
    print("\n--- Realizar Devolução ---")
    codigo = input("Código do livro: ")

    for livro in biblioteca:
        if livro.codigo == codigo:
            if livro.status == "Emprestado":
                livro.status = "Disponível"
                print("Devolução realizada com sucesso!")
            else:
                print("O livro já está disponível")
            return

    print("Livro não encontrado")


# Exibe o menu principal
def exibir_menu():
    print("\n   Sistema de Controle de Biblioteca \n")
    print("1 - Cadastrar livro")
    print("2 - Consultar livro")
    print("3 - Alterar dados")
    print("4 - Remover livro")
    print("5 - Listar todos")
    print("6 - Realizar empréstimo")
    print("7 - Realizar devolução")
    print("8 - Sair")


# Função principal que controla o fluxo do programa
def main():
    biblioteca = []  # Lista que armazena todos os livros

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            biblioteca = cadastrar_livro(biblioteca)
        else:
            if opcao == "2":
                consultar_livro(biblioteca)
            else:
                if opcao == "3":
                    biblioteca = alterar_dados(biblioteca)
                else:
                    if opcao == "4":
                        biblioteca = remover_livro(biblioteca)
                    else:
                        if opcao == "5":
                            listar_todos(biblioteca)
                        else:
                            if opcao == "6":
                                realizar_emprestimo(biblioteca)
                            else:
                                if opcao == "7":
                                    realizar_devolucao(biblioteca)
                                else:
                                    if opcao == "8":
                                        print("Encerrando o sistema. Até logo!")
                                        break
                                    else:
                                        print("Opção inválida! Tente novamente.")


main()
