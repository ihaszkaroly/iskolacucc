create database cdotthon
character set utf8
collate utf8_hungarian_ci;

use cdotthon;

create table cd(
    az INT NOT NULL PRIMARY KEY auto_increment,
    cim varchar(50),
    kiadoAz int
);

create TABLE elado(
    az INT NOT NULL PRIMARY KEY auto_increment,
    nev varchar(50)
);

CREATE TABLE zeneszam(
	az INT NOT NULL PRIMARY KEY auto_increment,
	nev VARCHAR(50),
	hossz TIME,
	cdAZ INTEGER,
	eloadoAZ int
);

CREATE TABLE kiado(
	az int NOT NULL PRIMARY KEY auto_increment,
	nev VARCHAR(50)
);
