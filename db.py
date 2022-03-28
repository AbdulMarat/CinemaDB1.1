import sqlite3

class DB():

    def __init__(self):
        self.conn = sqlite3.connect('cinema.db')

        c = self.conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS halls (id INTEGER PRIMARY KEY, name TEXT, seats INTEGER)""")

        c.execute("""CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, ticket_cost INTEGER, duration INTEGER, hall_id INTEGER )""")

        self.conn.commit()
        c.close()

    def create_hall(self, name, seats):
        c = self.conn.cursor()
        c.execute("INSERT INTO halls VALUES (NULL, ?, ?)", (name, seats))
        self.conn.commit()
        c.close()

    def create_film(self, name, genre, ticket_cost, duration, hall_id):
        c = self.conn.cursor()
        c.execute("INSERT INTO films VALUES (NULL, ?, ?, ?, ?, ?)", (name, genre, ticket_cost, duration, hall_id))
        self.conn.commit()
        c.close()

    def read_hall(self):
        c = self.conn.cursor()
        c.execute("""SELECT * FROM halls""")
        res = c.fetchall()
        c.close()
        return res

    def read_film(self):
        c = self.conn.cursor()
        c.execute("""SELECT * FROM films""")
        res = c.fetchall()
        c.close()
        return res

    def update_hall(self, id, name, seats):
        c = self.conn.cursor()
        c.execute("""UPDATE halls SET name = ?, seats = ? WHERE id == ?""", (name, int(seats), int(id)))
        self.conn.commit()
        c.close()


    def update_film(self, id, name, genre, ticket_cost, duration, hall_id):
        c = self.conn.cursor()
        c.execute("""UPDATE films SET name = ?, genre = ?, ticket_cost = ?, duration = ?, hall_id = ? WHERE id == ?""", (name, genre, int(ticket_cost),int(duration),int(hall_id),int(id),))
        self.conn.commit()
        c.close()

    def delete_film(self, id):
        c = self.conn.cursor()
        c.execute("""DELETE FROM films WHERE id = ?""", (int(id),))
        self.conn.commit()
        c.close()

    def delete_film_by_hall_id(self, hall_id):
        c = self.conn.cursor()
        c.execute("""DELETE FROM films WHERE hall_id = ?""", (int(hall_id),))
        self.conn.commit()
        c.close()

    def delete_hall(self, id):
        c = self.conn.cursor()
        c.execute("""DELETE FROM halls WHERE id = ?""", (int(id),))
        c.execute("""SELECT COUNT(id) FROM films WHERE hall_id = ?""", (int(id),))
        counter = c.fetchall()[0][0]
        for i in range(counter):
            self.delete_film_by_hall_id(id)
        self.conn.commit()
        c.close()
