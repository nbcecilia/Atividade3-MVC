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

