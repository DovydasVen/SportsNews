# Sistemos paskirtis

Šio projekto tikslas yra leisti vartotojams stebėti įvairias naujienas susijusias su sportu bei dalintis jomis. 

Veikimo principas – pačią kuriamą platformą sudaro dvi dalys: internetinė aplikacija, kuria naudosis vartotojai, redaktoriai, administratorius bei aplikacijų programavimo sąsaja 

Neprisijungęs vartotojas galės peržiūrėti naujienas, bei galės prisijungti ir prisiregistruoti. Prisijungęs vartotojas galės peržiūrėti naujienas, kurti jas, bei savąsias redaguoti ir trinti. Redaktoriai galės pridėti, trinti, redaguoti kategorijas, kur bus pridėdamos naujienos, taip pat galės pridėti, trinti, redaguoti naujienas. Administratoriai valdo vartotojus. 

# Funkciniai reikalavimai

Neprisijungęs vartotojas:
- Prisijungti
- Registruotis
- Peržiūrėti naujienas

Prisijungęs vartotojas:
- Atsijungti
- Peržiurėti naujienas
- Kurti naujienas
- Redaguoti savo naujienas
- Trinti savo naujienas

Redaktorius:
- Valdyti kategorijas
- Valdyti naujienas

Administratorius:
- Valdyti vartotojus

# Sistemos architektūra

Sistemos sudedamosios dalys:
- Kliento pusė realizuota naudojant React
- Serverio pusė realizuota naudojant Python Django, o duomenų bazei bus naudojama Postgres

![alt text](Deployement.jpg)

# Naudotojo sąsaja

Čia pateikiami puslapių wireframe'ai ir jų realizacijos

Pagrindinis puslapis

![pagrindinis wireframe](Pagrindinis-wireframe.png)
![pagrindinis](Pagrindinis.png)

Prisijungimo puslapis

![prisijungimas wireframe](Prisijungimas-wireframe.png)
![prisijungimas](Prisijungimas.png)

Registracijos puslapis

![registracija wireframe](Registracija-wireframe.png)
![registracija](Registracija.png)

Kategorijos įrašų puslapis

![kategorija wireframe](Kategorija-wireframe.png)
![kategorija](Kategorija.png)

Įrašo puslapis

![įrašas wireframe](Irasas-wireframe.png)
![įrašas](Irasas.png)

# API specifikacija

API specifikacija yra pateikta https://sportsnewssite-api.vercel.app/api/docs/ puslapyje.

API schemos .yaml failą galima atsisiųsti iš https://sportsnewssite-api.vercel.app/api/schema/

API specifikacijos vaizdai:

API užklausų sąrašas
![API 1](API1.png)
![API 2](API2.png)

API užklausos panaudojimas bei atsakai
![API3](API3.png)
![API4](API4.png)

# Išvados
Šio projekto metu buvo išmokta REST principais paremtos API sąsajos projektavimas ir kūrimas, autentifikacija ir autorizacija su JWT. Buvo sužinota kaip veikia React framework'as. 