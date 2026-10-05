import os
from dataclasses import dataclass

import psycopg2


@dataclass
class Livro:
    id_livro: int | None
    titulo: str
    ano_publicacao: int
    id_autor: int | None


class LivroModel:
    def __init__(self, dsn: str | None = None) -> None:
        self.dsn = dsn or os.getenv("DATABASE_URL", "dbname=bd_biblioteca")

    def cadastrar(
        self, titulo: str, ano_publicacao: int, id_autor: int | None
    ) -> Livro:
        with psycopg2.connect(self.dsn) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO livro (titulo, ano_publicacao, id_autor)
                    VALUES (%s, %s, %s)
                    RETURNING id_livro
                    """,
                    (titulo, ano_publicacao, id_autor),
                )
                registro = cursor.fetchone()
                if registro is None:
                    raise RuntimeError("Não foi possível cadastrar o livro.")
        return Livro(registro[0], titulo, ano_publicacao, id_autor)

    def listar(self) -> list[Livro]:
        with psycopg2.connect(self.dsn) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id_livro, titulo, ano_publicacao, id_autor
                    FROM livro
                    ORDER BY id_livro
                    """
                )
                registros = cursor.fetchall()
        return [Livro(*registro) for registro in registros]

    def atualizar(
        self,
        id_livro: int,
        titulo: str,
        ano_publicacao: int,
        id_autor: int | None,
    ) -> bool:
        with psycopg2.connect(self.dsn) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE livro
                    SET titulo = %s, ano_publicacao = %s, id_autor = %s
                    WHERE id_livro = %s
                    """,
                    (titulo, ano_publicacao, id_autor, id_livro),
                )
                return cursor.rowcount > 0

    def excluir(self, id_livro: int) -> bool:
        with psycopg2.connect(self.dsn) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM livro WHERE id_livro = %s",
                    (id_livro,),
                )
                return cursor.rowcount > 0
