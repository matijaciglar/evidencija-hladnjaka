from flask import Flask, render_template, request, jsonify
from pony.orm import Database, Required, db_session, PrimaryKey
from datetime import date, timedelta

app = Flask(__name__)

# Baza podataka (SQLite file u projektu)
db = Database()
db.bind(provider='sqlite', filename='baza.db', create_db=True)

class Namirnica(db.Entity):
    id = PrimaryKey(int, auto=True)
    naziv = Required(str)
    kategorija = Required(str)
    kolicina = Required(int)
    rok_trajanja = Required(date)

db.generate_mapping(create_tables=True)

@app.route('/')
def home():
    return render_template("index.html")

# Dohvati sve namirnice
@app.route('/api/namirnice', methods=['GET'])
@db_session
def get_namirnice():
    namirnice = Namirnica.select()
    return jsonify([{
        "id": n.id,
        "naziv": n.naziv,
        "kategorija": n.kategorija,
        "kolicina": n.kolicina,
        "rok_trajanja": str(n.rok_trajanja)
    } for n in namirnice])

# Dodaj novu namirnicu
@app.route('/api/namirnice', methods=['POST'])
@db_session
def add_namirnica():
    data = request.json
    n = Namirnica(
        naziv=data['naziv'],
        kategorija=data['kategorija'],
        kolicina=int(data['kolicina']),
        rok_trajanja=date.fromisoformat(data['rok_trajanja'])
    )
    return jsonify({"status": "dodano", "id": n.id})

# Uredi namirnicu
@app.route('/api/namirnice/<int:namirnica_id>', methods=['PUT'])
@db_session
def update_namirnica(namirnica_id):
    data = request.json
    n = Namirnica.get(id=namirnica_id)
    if not n:
        return jsonify({"error": "Namirnica ne postoji"}), 404
    n.naziv = data.get('naziv', n.naziv)
    n.kategorija = data.get('kategorija', n.kategorija)
    n.kolicina = int(data.get('kolicina', n.kolicina))
    n.rok_trajanja = date.fromisoformat(data.get('rok_trajanja', str(n.rok_trajanja)))
    return jsonify({"status": "uređeno"})

# Izbriši namirnicu
@app.route('/api/namirnice/<int:namirnica_id>', methods=['DELETE'])
@db_session
def delete_namirnica(namirnica_id):
    n = Namirnica.get(id=namirnica_id)
    if not n:
        return jsonify({"error": "Namirnica ne postoji"}), 404
    n.delete()
    return jsonify({"status": "izbrisano"})

# Namirnice kojima rok ističe unutar 3 dana
@app.route('/api/namirnice/rok', methods=['GET'])
@db_session
def rok_uskoro():
    danas = date.today()
    prag = danas + timedelta(days=3)
    namirnice = Namirnica.select(lambda n: n.rok_trajanja <= prag)
    return jsonify([{
        "id": n.id,
        "naziv": n.naziv,
        "rok_trajanja": str(n.rok_trajanja)
    } for n in namirnice])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
