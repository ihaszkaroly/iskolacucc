-- Ihász Károly
-- 2022-02-02

create database if not exists kekbt
collate utf8_hungarian_ci;

use kekbt;

-- Tábla létrehozása
create table if not exists ugyfelek(
	az int not null primary key auto_increment,
	nev varchar(50),
	telepules varchar(50),
	vasarlas int
);

--sorok beszúrása

insert into ugyfelek
(nev, telepules, vasarlas)
values
("Pontos Béla","Szolnok",2),
("Sebes Irén","Szeged",1),
("Nyolca Imre","Szolnok",1),
("Lakatos Ferenc","Miskolc",1),
("Asztalos Sándor","Kiskunhalas",1);


-- ORDER BY | GROUP BY

SELECT telepules
FROM szemelyek
WHERE fizetes<30000
GROUP BY telepules
order BY telepules;

UPDATE szemelyek
set
	fizetes = fizetes + 500000
	WHERE fizetes<20000;
	
SELECT telepules AS "Település", SUM(fizetes) AS "Összes Fizetés"
FROM szemelyek
WHERE
	fizetes < 30000
	AND
	telepules LIKE "P%"
GROUP BY telepules
ORDER BY telepules;


SELECT telepules
FROM szemelyek
WHERE
	fizetes<30000
ORDER BY telepules
limit 10;

SELECT nev, fizetes
FROM szemelyek
WHERE
	telepules="Szeged"
ORDER BY fizetes DESC
limit 1
;

SELECT nev, jutalom
FROM szemelyek
WHERE
	telepules="Miskolc"
ORDER BY jutalom DESC
limit 1;

UPDATE szemelyek
set 
	jutalom = jutalom + 12000
WHERE
	az = 5298;
	
INSERT INTO szemelyek
(nev,telepules,fizetes,beosztasAz)
VALUES
("Tenger Zoltán","Szeged",2830000,5);

SELECT telepules, SUM(fizetes)
FROM szemelyek
WHERE 
	fizetes > 800000
GROUP BY telepules
HAVING
	SUM(fizetes) < 20000000
;