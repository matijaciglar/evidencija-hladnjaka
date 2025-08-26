# 🧊 Evidencija hladnjaka

Ovo je web aplikacija za vođenje evidencije o namirnicama u hladnjaku.  
Omogućuje jednostavno praćenje, uređivanje i vizualizaciju namirnica.

---

## 🚀 Funkcionalnosti
- ➕ Dodavanje, ✏️ uređivanje i ❌ brisanje namirnica (CRUD)
- 📋 Pregled svih namirnica
- ⏰ Prikaz namirnica kojima uskoro ističe rok trajanja (≤ 3 dana)
- 📊 Grafička vizualizacija podataka (Chart.js)
- 💻 Frontend: **HTML + Bootstrap**
- ⚙️ Backend: **Python (Flask + PonyORM + SQLite)**
- 🐳 Docker podrška

---

## ⚡ Brzi početak

### Pokretanje lokalno
```bash
python -m venv venv
# Aktivacija virtualnog okruženja
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

pip install -r zahtjevi.txt
python aplikacija.py
```

Aplikacija će biti dostupna na: 👉 [http://localhost:5000](http://localhost:5000)

---

### Pokretanje pomoću Dockera
```bash
docker build -t evidencija-hladnjaka .
docker run -p 5000:5000 evidencija-hladnjaka
```

Ili pomoću **docker-compose**:
```bash
docker-compose up --build
```

---

## 📝 Use Case opis
- Korisnik može dodati novu namirnicu s nazivom, kategorijom, količinom i rokom trajanja  
- Korisnik može pregledati sve unesene namirnice  
- Korisnik može brisati ili uređivati postojeće namirnice  
- Sustav prikazuje namirnice kojima rok ističe unutar 3 dana  
- Sustav prikazuje grafikon količina namirnica po kategorijama  

---

## 📦 Tehnologije
- Python 3.x  
- Flask  
- PonyORM  
- SQLite  
- Chart.js  
- Bootstrap  
- Docker / Docker Compose  

---

