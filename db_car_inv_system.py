import sqlite3

class Database:
    def __init__(self,db) :
        self.conn= sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cars (serialnumber INTEGER, carbrand TEXT, modelname TEXT, bodytype TEXT, manufacturingyear TEXT, transmission TEXT, mileage TEXT, carstatus TEXT)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM cars")
        rows = self.cur.fetchall()
        return rows
    
    # func
    def insert(self, carbrand, modelname, bodytype, manufacturingyear, transmission, mileage, carstatus):
        self.cur.execute("INSERT INTO cars VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",(carbrand,modelname, bodytype, manufacturingyear, transmission, mileage, carstatus))
        self.conn.commit()
    
    def remove(self,serialnumber):
        self.cur.execute("DELETE FROM cars WHERE serial number=?",(serialnumber,))
        self.conn.commit()
    
    def update (self, modelname, bodytype, manufacturingyear, transmission, mileage, carstatus):
        self.cur.execute("UPDATE cars SET modelname =?, bodytype =?, manufacturingyear=?, transmission=?, mileage=?, carstatus=? WHERE serialnumber =? "), (modelname, bodytype, manufacturingyear, transmission, mileage, carstatus)
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()

db = Database('sample.db')
db.insert ("Mazda","MX8","coupe","2023","Manual","9000","Available")


