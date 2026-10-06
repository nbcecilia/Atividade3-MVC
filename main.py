from controller.autor_controller import AutorController
from controller.livro_controller import LivroController
from view.biblioteca_view import BibliotecaView


if __name__ == "__main__":
    autor_controller = AutorController()
    livro_controller = LivroController()

    menu = BibliotecaView()
    menu.executar()
