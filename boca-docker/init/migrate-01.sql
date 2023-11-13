\connect bocadb;

CREATE TABLE tagtable(
	tagnumber bigint NOT NULL,
	tagname text,
	contestnumber integer,
	PRIMARY KEY (tagnumber),
	FOREIGN KEY (contestnumber) REFERENCES contesttable (contestnumber)
);

INSERT INTO tagtable(tagnumber, tagname, contestnumber)
VALUES
(1,'hard',2);