import sqlite3
from flask import Flask, g

app = Flask(__name__)
DB_PATH = "app.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(e=None):
    db = g.pop("db", None)
    if db:
        db.close()


def init_db():
    db = sqlite3.connect(DB_PATH)
    db.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)")
    db.commit()
    db.close()


@app.route("/")
def index():
    db = get_db()
    items = db.execute("SELECT * FROM items").fetchall()
    return {"items": [dict(r) for r in items]}


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000)
