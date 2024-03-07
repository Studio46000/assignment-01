import sqlite3

class Database:
    def __init__(self,db) :
        self.conn= sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cars (id INTEGER PRIMARY KEY,carbrand TEXT, modelname TEXT, bodytype TEXT, manufacturingyear INTEGER, transmission TEXT, mileage INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM cars")
        rows = self.cur.fetchall()
        return rows
    

    def insert(self, carbrand, modelname, bodytype, manufacturingyear, transmission, mileage):
        self.cur.execute("INSERT INTO cars VALUES (NULL,?, ?, ?, ?, ?,?)",( carbrand,modelname, bodytype, manufacturingyear, transmission, mileage))
        self.conn.commit()
    
    def remove(self,id):
        self.cur.execute("DELETE FROM cars WHERE id=?",(id,))
        self.conn.commit()
    
    def update(self, id, carbrand, modelname, bodytype, manufacturingyear, transmission, mileage):
        self.cur.execute("UPDATE cars SET carbrand=?, modelname=?, bodytype=?, manufacturingyear=?, transmission=?, mileage=? WHERE id=?", (carbrand, modelname, bodytype, manufacturingyear, transmission, mileage, id))
        self.conn.commit()

    
    def __del__(self):
        self.conn.close()

db = Database('sample.db')
db.insert ("Mazda","MX8","Coupe","2023","Manual","9000")


