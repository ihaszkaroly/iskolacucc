--Ihász Károly | 2022_02_09

SELECT nev, fizetes
FROM szemelyek
WHERE telepules="Miskolc"
ORDER BY fizetes DESC;

SELECT telepules
FROM szemelyek
WHERE fizetes > 700000
GROUP BY telepules;