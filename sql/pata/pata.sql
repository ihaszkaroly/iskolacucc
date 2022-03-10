create table kerekparok (
	az int not null primary key auto_increment,
	szin varchar(50),
	marka varchar(50),
	ar double,
	kategoriaID int
);

CREATE TABLE kategoria(
	az int not NULL PRIMARY key auto_increment,
	nev VARCHAR(50)
);
--	--	--	--	--	--	--	--
INSERT INTO kategoria
(nev)
VALUES
("Városi"),
("Országúti"),
("Gyerek"),
("Elektromos"),
("Trekking");

INSERT INTO kerekparok
(szin,marka,ar,kategoriaID)
VALUES
("Fehér","Csepel",150000,5),
("Kék","Volga",198000,2),
("Piros","KTM",261234,5);

--Táblák össze kapcsolása--

SELECT szin, marka, ar, nev
FROM kerekparok inner join kategoria
on kerekparok.kategoriaID = kategoria.az;

--	--	--	--	--	--	--	--

INSERT INTO kerekparok
(szin,marka,ar,kategoriaID)
VALUES
("Lila","Gepida",439990,1);

--	--	--	--	--	--	--	--

vasarlasok=(az,kerekparAZ,ugyelAZ,datum)
ugyfelek=(az,nev)