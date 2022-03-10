-- 2022. 02. 28.

INSERT INTO szemelyek
(nev,fizetes,telepules,jutalom,lakcim,beosztasAz)
VALUES
("Lakos Kázmér",2830000,"Miskolc",800000,"Pata u. 18.",2);

INSERT INTO Beosztasok
(nev,leiras)
VALUES
("Titkár","" );

UPDATE szemelyek
set
	nev="Gipsz Jakab",
	anyja_neve="Purhab Mária",
	telepules="Bugyi",
	lakcim="Cég utca 12.",
	fizetes=2411000,
	szuletes="1996-03-12",
	jutalom=500,
	beosztasAz=6
WHERE
	az=13112;
	
CREATE TABLE Beoszztasok(
	az INTEGER NOT NULL PRIMARY KEY auto_increment,
	nev VARCHAR(50),
	leiras text
	);

-- móri dolgozó beosztása és nevük
-- összekötés
SELECT szemelyek.nev, Beosztasok.nev
FROM szemelyek inner join Beosztasok
ON szemelyek.beosztasAz = Beosztasok.az
WHERE telepules="Mór";

---------------------------------------------------------------

CREATE DATABASE kontjarmu
CHARACTER set utf8
collate utf8_hungarian_ci;

CREATE TABLE jarmuvek (
	az INTEGER NOT NULL PRIMARY KEY auto_increment,
	rendszam VARCHAR(10) UNIQUE,
	marka VARCHAR(50)
);

INSERT INTO jarmuvek
(az,rendszam,marka)
VALUES
(1,"ABC-123","Opel");

INSERT INTO jarmuvek
(az,rendszam,marka)
VALUES
(1,"ABC-123","Opel");
