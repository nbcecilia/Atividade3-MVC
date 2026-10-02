-- Uma tabela autor com id, nome e nacionalidade 
-- e outra tabela livro com id, 
-- título, ano de publicação e o id do autor do livro.

create table autor(
id_autor serial primary key,
nome varchar(50) not null,
nacionalidade varchar(20) not null
);

create table livro(
id_livro serial primary key,
titulo varchar(50) not null,
ano_publicacao int not null,
id_autor int references autor(id_autor)
);

-- Inserindo 5 autores
INSERT INTO autor (nome, nacionalidade) VALUES 
('Machado de Assis', 'Brasileira'),
('J.K. Rowling', 'Britânica'),
('George Orwell', 'Britânica'),
('Clarice Lispector', 'Brasileira'),
('Gabriel García Márquez', 'Colombiana');

-- Inserindo 5 livros (vinculados aos IDs dos autores acima)
INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES 
('Dom Casmurro', 1899, 1),
('Harry Potter e a Pedra Filosofal', 1997, 2),
('1984', 1949, 3),
('A Hora da Estrela', 1977, 4),
('Cem Anos de Solidão', 1967, 5);