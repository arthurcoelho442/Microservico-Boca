-- Cria tabela
CREATE TABLE tagtable(
	tagnumber bigint NOT NULL,
	tagname text,
	contestnumber integer,
	PRIMARY KEY (tagnumber),
	FOREIGN KEY (contestnumber) REFERENCES contesttable (contestnumber)
);

-- Cadastra uma nova tag associada à competição dada pelo id_c
INSERT INTO tagtable(tagnumber, tagname, contestnumber)
VALUES
(1,'hard',2);

SELECT *
FROM tagtable;

SELECT *
FROM contesttable;

-- Lista as tags associadas à competição dada pelo id_c
SELECT tagname -- ,contestname, contesttable.contestnumber
FROM tagtable
INNER JOIN contesttable
ON tagtable.contestnumber=contesttable.contestnumber
WHERE contesttable.contestnumber = 2;

-- Mostra a tag dada pelo id_t no contest id_c
SELECT tagname 
FROM tagtable
INNER JOIN contesttable
ON tagtable.contestnumber=contesttable.contestnumber
WHERE contesttable.contestnumber = 2 AND tagnumber = 1;

-- Atualiza a tag dada pelo id_t no contest id_c
UPDATE tagtable 
SET tagname = 'medio'
WHERE contestnumber = 2 AND tagnumber = 1;

SELECT *
FROM tagtable;

-- Remove a tag dada pelo id_t no contest id_c
DELETE FROM tagtable
WHERE contestnumber = 2 and tagnumber = 1;
