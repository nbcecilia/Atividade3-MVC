from model.autor_model import Autor, AutorModel


class AutorController:
    def __init__(self, model: AutorModel | None = None) -> None:
        self.model = model or AutorModel()

    def cadastrar(self, nome: str, nacionalidade: str) -> Autor:
        return self.model.cadastrar(nome, nacionalidade)

    def listar(self) -> list[Autor]:
        return self.model.listar()

    def atualizar(
        self, id_autor: int, nome: str, nacionalidade: str
    ) -> bool:
        return self.model.atualizar(id_autor, nome, nacionalidade)

    def excluir(self, id_autor: int) -> bool:
        return self.model.excluir(id_autor)
