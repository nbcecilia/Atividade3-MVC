import os
from dataclasses import dataclass

import psycopg2


@dataclass
class Autor:
    id_autor: int | None
    nome: str
    nacionalidade: str


class AutorModel:
    def __init__(self, dsn: str | None = None) -> None:
        self.dsn = dsn or os.getenv("DATABASE_URL", "dbname=bd_biblioteca")

    def cadastrar(self, nome: str, nacionalidade: str) -> Autor:
        with psycopg2.connect(self.dsn) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO autor (nome, nacionalidade)
                    VALUES (%s, %s)
                    RETURNING id_autor
                    """,
                    (nome, nacionalidade),
                )
                registro = cursor.fetchone()
                if registro is None:
                    raise RuntimeError("Não foi possível cadastrar o autor.")
        return Autor(registro[0], nome, nacionalidade)

    def listar(self) -> list[Autor]:
        with psycopg2.connect(self.dsn) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id_autor, nome, nacionalidade
                    FROM autor
                    ORDER BY id_autor
                    """
                )
                registros = cursor.fetchall()
        return [Autor(*registro) for registro in registros]

    def atualizar(
        self, id_autor: int, nome: str, nacionalidade: str
    ) -> bool:
        with psycopg2.connect(self.dsn) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE autor
                    SET nome = %s, nacionalidade = %s
                    WHERE id_autor = %s
                    """,
                    (nome, nacionalidade, id_autor),
                )
                return cursor.rowcount > 0

    def excluir(self, id_autor: int) -> bool:
        with psycopg2.connect(self.dsn) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM autor WHERE id_autor = %s",
                    (id_autor,),
                )
                return cursor.rowcount > 0
