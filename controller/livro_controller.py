from model.livro_model import Livro, LivroModel


class LivroController:
    def __init__(self, model: LivroModel | None = None) -> None:
        self.model = model or LivroModel()

    def cadastrar(
        self, titulo: str, ano_publicacao: int, id_autor: int | None
    ) -> Livro:
        return self.model.cadastrar(titulo, ano_publicacao, id_autor)

    def listar(self) -> list[Livro]:
        return self.model.listar()

    def atualizar(
        self,
        id_livro: int,
        titulo: str,
        ano_publicacao: int,
        id_autor: int | None,
    ) -> bool:
        return self.model.atualizar(
            id_livro, titulo, ano_publicacao, id_autor
        )

    def excluir(self, id_livro: int) -> bool:
        return self.model.excluir(id_livro)
