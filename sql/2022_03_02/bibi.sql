-- 2022_03_02

CREATE DATABASE
CREATE TABLE
CREATE INDEX

--Átnevez
ALTER TABLE szemelyek
CHANGE COLUMN varos telepules VARCHAR(20);

--Hozzáad
ALTER TABLE szemelyek ADD cim VARCHAR(20);
ALTER TABLE szemelyek ADD fizetes DOUBLE;


szemelyek(az, nev, telepules, cim, fizetes)