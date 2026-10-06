from controller.autor_controller import AutorController
from controller.livro_controller import LivroController
from view.view_autor import menu_autor
from view.view_livro import menu_livro


class BibliotecaView:
    def __init__(self) -> None:
        self.autor_controller = AutorController()
        self.livro_controller = LivroController()

    def menu_principal(self) -> None:
        while True:
            print("\n" + "=" * 30)
            print("      MENU PRINCIPAL          ")
            print("=" * 30)
            print("1. Gerenciar autor")
            print("2. Gerenciar livro")
            print("3. Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                menu_autor(self.autor_controller)
            elif opcao == "2":
                menu_livro(self.livro_controller)
            elif opcao == "3":
                print("\nSaindo do sistema... Até logo!")
                break
            else:
                print("\n Opção inválida! Tente novamente.")

    def executar(self) -> None:
        self.menu_principal()