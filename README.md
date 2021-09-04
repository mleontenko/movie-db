### Pokretanje:

1. Preuzeti postgres bazu podataka: https://hub.docker.com/r/mleontenko/pg_container_test
2. Pokretanje containera s bazom podataka: 
```
docker start pg_container_test
```
3. Preuzeti aplikaciju: https://hub.docker.com/r/mleontenko/movie-db
4. Pokretanje aplikacije (postgres servis mora biti pokrenut prije):
```
docker start movie-db
```
5. Container od aplikacije će izvršiti skriptu app.py koja će povući podatke i spremiti ih u bazu podataka. Nakon toga će se aplikacija ugasiti, a podatci će biti vidljivi u bazi podataka.