-- Ihász Károly | Ifra | 2022-02-23

-- Tiszadobi dolgozók nevei, fizetésük és jutalmuk
SELECT nev AS "Név", fizetes as "Fizetés", jutalom AS "Jutalom"
FROM szemelyek
WHERE telepules="Tiszadob";

-- Mezőtúri dolgozók száma
SELECT COUNT(nev) AS "Dolgozók Száma"
FROM szemelyek
WHERE telepules="Mezőtúr";

-- Pápai dolgozók neve és fizetése akiknek több mint 700ezer
SELECT nev AS "Név", fizetes AS "Fizetés"
FROM szemelyek
WHERE telepules="Pápa" AND fizetes > 700000;