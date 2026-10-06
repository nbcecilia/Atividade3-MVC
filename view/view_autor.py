# view/autor_view.py
import psycopg2
from controller.autor_controller import AutorController

def menu_autor(controller: AutorController):
    while True:
        print("\n--- Gerenciar Autor ---")
        print("1. Cadastrar autor")
        print("2. Listar autores")
        print("3. Atualizar autor")
        print("4. Excluir autor")
        print("5. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome do autor: ").strip()
            nacionalidade = input("Digite a nacionalidade: ").strip()
            
            try:
                autor = controller.cadastrar(nome, nacionalidade)
                print(f"\n Autor '{autor.nome}' cadastrado com sucesso! ID: {autor.id_autor}")
            except psycopg2.Error as e:
                print(f"\n Erro no banco de dados ao cadastrar autor: {e}")

        elif opcao == "2":
            try:
                autores = controller.listar()
                if not autores:
                    print("\nNenhum autor cadastrado.")
                else:
                    print("\n--- Lista de Autores ---")
                    for a in autores:
                        print(f"ID: {a.id_autor} | Nome: {a.nome} | Nacionalidade: {a.nacionalidade}")
            except psycopg2.Error as e:
                print(f"\n Erro ao listar autores: {e}")

        elif opcao == "3":
            try:
                id_autor = int(input("Digite o ID do autor que deseja atualizar: "))
                nome = input("Digite o novo nome: ").strip()
                nacionalidade = input("Digite a nova nacionalidade: ").strip()

                sucesso = controller.atualizar(id_autor, nome, nacionalidade)
                if sucesso:
                    print("\n Autor atualizado com sucesso!")
                else:
                    print("\n Nenhum autor encontrado com esse ID.")
            except ValueError:
                print("\n Erro: O ID deve ser um número inteiro.")
            except psycopg2.Error as e:
                print(f"\n Erro ao atualizar autor: {e}")

        elif opcao == "4":
            try:
                id_autor = int(input("Digite o ID do autor que deseja excluir: "))
                
                sucesso = controller.excluir(id_autor)
                if sucesso:
                    print("\n Autor excluído com sucesso!")
                else:
                    print("\n Nenhum autor encontrado com esse ID.")
            except ValueError:
                print("\n Erro: O ID deve ser um número inteiro.")
            except psycopg2.errors.ForeignKeyViolation:
                print("\n Erro: Não é possível excluir o autor pois existem livros cadastrados vinculados a ele.")
            except psycopg2.Error as e:
                print(f"\n Erro ao excluir autor: {e}")

        elif opcao == "5":
            break
        else:
            print("\n Opção inválida! Tente novamente.")