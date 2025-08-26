# Evidencija hladnjaka

Ovo je web aplikacija za vođenje evidencije o namirnicama u hladnjaku.

## Funkcionalnosti
- Dodavanje, uređivanje i brisanje namirnica (CRUD)
- Pregled svih namirnica
- Pregled namirnica kojima uskoro ističe rok trajanja (≤ 3 dana)
- Vizualizacija podataka (Chart.js)
- Frontend izrađen u HTML + Bootstrap
- Backend izrađen u Python (Flask + PonyORM + SQLite)
- Docker podrška

## Pokretanje lokalno

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

pip install -r zahtjevi.txt
python aplikacija.py
```

Otvorite preglednik na: [http://localhost:5000](http://localhost:5000)

## Pokretanje pomoću Dockera

```bash
docker build -t evidencija-hladnjaka .
docker run -p 5000:5000 evidencija-hladnjaka
```

Ili pomoću docker-compose:

```bash
docker-compose up --build
```

## Use Case opis

- Korisnik može dodati novu namirnicu s nazivom, kategorijom, količinom i rokom trajanja
- Korisnik može pregledati sve unesene namirnice
- Korisnik može brisati ili uređivati postojeće namirnice
- Sustav može prikazati namirnice kojima rok ističe unutar 3 dana
- Sustav prikazuje grafikon količina namirnica po kategorijama

👉 Use Case dijagram nacrtati u Lucidchartu na temelju ovog opisa.
