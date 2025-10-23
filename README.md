# Sistemos paskirtis

Šio projekto tikslas yra leisti vartotojams stebėti įvairias naujienas susijusias su sportu bei dalintis jomis. 

Veikimo principas – pačią kuriamą platformą sudaro dvi dalys: internetinė aplikacija, kuria naudosis vartotojai, redaktoriai, administratorius bei aplikacijų programavimo sąsaja 

Neprisijungęs vartotojas galės peržiūrėti naujienas, bei galės prisijungti ir prisiregistruoti. Prisijungęs vartotojas galės peržiūrėti naujienas, kurti jas, bei savąsias redaguoti ir trinti. Redaktoriai galės pridėti, trinti, redaguoti kategorijas, kur bus pridėdamos naujienos, taip pat galės pridėti, trinti, redaguoti naujienas. Administratoriai valdo vartotojus. 

# Funkciniai reikalavimai

Neprisijungęs vartotojas:

1 Prisijungti
2 Registruotis
3 Peržiūrėti naujienas

Prisijungęs vartotojas:

1 Atsijungti
2 Peržiūrėti naujienas
3 Kurti naujienas
4 Redaguoti savo naujienas
5 Trinti savo naujienas

Redaktorius:

1 Valdyti kategorijas
2 Valdyti naujienas

Administratorius:

1 Valdyti vartotojus

# Sistemos architektūra

Sistemos sudedamosios dalys:
• Kliento pusė realizuota naudojant React
• Serverio pusė realizuota naudojant Python Django, o duomenų bazei bus naudojama Postgres

![alt text](Deployement.png)