-- ...będzie zwracało średnią masę meteorów w każdej z klas

SELECT recclass, avg(mass) AS Avarage_mass
FROM meteorite_landings
GROUP BY recclass;

-- ...będzie zwracało klasy meteorów których średnia waga jest mniejsza niż 5000

SELECT recclass, avg(mass) AS Avarage_mass
FROM meteorite_landings
GROUP BY recclass
HAVING Avarage_mass < 5000;

