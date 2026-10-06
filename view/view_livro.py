# view/livro_view.py
import psycopg2
from controller.livro_controller import LivroController

def menu_livro(controller: LivroController):
    while True:
        print("\n--- Gerenciar Livro ---")
        print("1. Cadastrar livro")
        print("2. Listar livros ")
        print("3. Atualizar livro")
        print("4. Excluir livro")
        print("5. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                titulo = input("Digite o título do livro: ").strip()
                ano_publicacao = int(input("Digite o ano de publicação: "))
                id_autor_input = input("Digite o ID do autor (ou pressione ENTER se não tiver): ").strip()
                
                # Trata o id_autor caso seja opcional/vazio
                id_autor = int(id_autor_input) if id_autor_input else None

                livro = controller.cadastrar(titulo, ano_publicacao, id_autor)
                print(f"\n Livro '{livro.titulo}' cadastrado com sucesso! ID: {livro.id_livro}")

            except ValueError:
                print("\n Erro: Ano de publicação e ID do autor devem ser números inteiros.")
            except psycopg2.errors.ForeignKeyViolation:
                print("\n Erro: O ID do autor informado não existe no cadastro de autores.")
            except psycopg2.Error as e:
                print(f"\n Erro no banco de dados ao cadastrar livro: {e}")

        elif opcao == "2":
            try:
                livros = controller.listar()
                if not livros:
                    print("\nNenhum livro cadastrado.")
                else:
                    print("\n--- Lista de Livros ---")
                    for l in livros:
                        autor_str = l.nome_autor if l.nome_autor else "Sem Autor Associado"
                        print(
                            f"ID: {l.id_livro} | Título: {l.titulo} | "
                            f"Ano: {l.ano_publicacao} | Autor: {autor_str}"
                        )
            except psycopg2.Error as e:
                print(f"\n Erro ao listar livros: {e}")

        elif opcao == "3":
            try:
                id_livro = int(input("Digite o ID do livro que deseja atualizar: "))
                titulo = input("Digite o novo título: ").strip()
                ano_publicacao = int(input("Digite o novo ano de publicação: "))
                id_autor_input = input("Digite o novo ID do autor (ou pressione ENTER para nenhum): ").strip()
                
                id_autor = int(id_autor_input) if id_autor_input else None

                sucesso = controller.atualizar(id_livro, titulo, ano_publicacao, id_autor)
                if sucesso:
                    print("\n Livro atualizado com sucesso!")
                else:
                    print("\n Nenhum livro encontrado com esse ID.")

            except ValueError:
                print("\n Erro: Os campos de ID e Ano devem conter números inteiros.")
            except psycopg2.errors.ForeignKeyViolation:
                print("\n Erro: O ID do autor informado não existe.")
            except psycopg2.Error as e:
                print(f"\n Erro ao atualizar livro: {e}")

        elif opcao == "4":
            try:
                id_livro = int(input("Digite o ID do livro que deseja excluir: "))
                
                sucesso = controller.excluir(id_livro)
                if sucesso:
                    print("\n Livro excluído com sucesso!")
                else:
                    print("\n Nenhum livro encontrado com esse ID.")

            except ValueError:
                print("\n Erro: O ID deve ser um número inteiro.")
            except psycopg2.Error as e:
                print(f"\n Erro ao excluir livro: {e}")

        elif opcao == "5":
            break
        else:
            print("\n Opção inválida! Tente novamente.")