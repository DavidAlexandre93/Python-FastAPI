PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE students (
	id INTEGER NOT NULL,
	name VARCHAR,
	address VARCHAR,
	neighbour VARCHAR,
	city VARCHAR,
	state VARCHAR,
	postal_code VARCHAR,
	PRIMARY KEY (id)
);
INSERT INTO students VALUES(1,'David Alexandre Fernandes','Jardim Novo Record','Rua Ingá','Taboao da Serra','São Paulo','06784-655');
INSERT INTO students VALUES(2,'Joska','Rua de da Paz, 86','Capitão Eduardo','Pereira de Rodrigues','Rio de Janeiro','83392-182');
INSERT INTO students VALUES(3,'Joao','Praia Moraes, 25','Conjunto Taquaril','Jesus de Goiás','Goiás','15319-202');
INSERT INTO students VALUES(4,'Matheus','Esplanada Davi Luiz Freitas, 4','Virgínia','Pires de Minas','Distrito Federal','24123-321');
INSERT INTO students VALUES(5,'Pedro','Vila Beatriz Ramos, 125','Chácara Leonina','Lima','Minas Gerais','32024-590');
INSERT INTO students VALUES(6,'Mariana','Pátio Fogaça, 52','Braúnas','da Rocha do Campo','Amapá','43302-598');
INSERT INTO students VALUES(7,'Micaela','Fazenda Santos, 8','Serra','Correia das Flores','Santa Catarina','76917-907');
INSERT INTO students VALUES(8,'Maik','Lagoa Sarah Moraes, 58','Monte São José','Lopes','Minas Gerais','82636-495');

CREATE INDEX ix_students_id ON students (id);
COMMIT;
