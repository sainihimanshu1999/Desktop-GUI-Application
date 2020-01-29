import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.Connection(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY , part text, customer text, retailer text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer , retailer , price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ? , ? , ? , ?)" , (part, customer , retailer ,price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (part, customer, retailer, price, id))
        self.conn.commit()

    def __del__ (self):
        self.conn.close()

#db  = Database('store.db')
#db.insert("8GB DDR4 Ram" , "Jenny Sli" , "YourSHop" , "149")
#db.insert("2GB ULSO Ram" , "Calvin picolo" , "YourSHop" , "199")
#db.insert("16GB DDR4 Ram" , "Bruce Wayne" , "WayneMansion" , "349")
#db.insert("6GB MSCO Ram" , "Tommy Barucha" , "MicroCentre" , "129")
#db.insert("4GB ULSO Ram" , "Joey Tribbiani" , "WayneMansion" , "249")
#db.insert("6GB ULSO Ram" , "Peter Parker" , "StarkFac" , "139")
#db.insert("4GB DDR4 Ram" , "Nikola Tesla" , "EdisonSHop" , "101")