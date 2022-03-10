-- Ihász Károly
-- 2022-02-07
-- Ifra
-- A dolgozók nevei és fizetésük 
-- devecserről

SELECT nev AS "Név", fizetes as "Fizetés"
FROM szemelyek
WHERE telepules="Devecser";

--Hány dolgozó devecserről

SELECT COUNT(*)
FROM szemelyek
WHERE telepules="Devecser";

SELECT COUNT(*) as "Devecseri Dolgozók"
FROM szemelyek
WHERE telepules="Devecser";

SELECT fizetes AS "Fizetés"
FROM szemelyek
WHERE telepules="Devecser"

SELECT SUM(fizetes) AS "Devecseri fizetések összesen"
FROM szemelyek
WHERE telepules="Devecser";

SELECT AVG(fizetes) AS "Devecseri átlag fizetések"
FROM szemelyek
WHERE telepules="Devecser"

-- Hány dolgozó van több település

SELECT telepules
FROM szemelyek
WHERE telepules="Miskolc" OR
telepules="Hatvan"

-- miskolci akiknek nagyobb fizetés mint 300.000

SELECT nev AS "Név", fizetes AS "Fizetés", telepules AS "Település"
FROM szemelyek
WHERE (telepules="Miskolc" OR
telepules="Hatvan") AND
fizetes>300000

-- miskolci és hatvani dolgozók név szerint abc sorrendbe

SELECT nev as "Név"
FROM szemelyek
WHERE telepules="Miskolc" OR
telepules="Hatvan"
ORDER BY nev