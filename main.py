  
""" professor falou q vai avaliar pelo video e precisa que o video esteja completo fazendo todos os testes, inclusive com as exceçoes"""



""""""


from controller.autor_controller import AutorController
from controller.livro_controller import LivroController
from view.biblioteca_view import bibliotecaView


if __name__ == "__main__":
    autor_controller = AutorController()
    livro_controller = LivroController()

    menu = bibliotecaView(autor_controller, livro_controller)
    menu.executar()