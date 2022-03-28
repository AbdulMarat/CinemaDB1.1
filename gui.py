from db import DB
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,  QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.db = DB()

        # self.db.create_hall("red", 50)
        # self.db.create_hall("blue", 70)
        # self.db.create_hall("green", 75)
        #
        # self.db.create_film("Snatch", "trill",100,120,1)
        # self.db.create_film("Scream", "comedy", 100, 91, 1)
        # self.db.create_film("Friends", "comedy", 100, 61, 1)
        #
        # self.db.create_film("1+1", "drama", 100, 61, 2)
        # self.db.create_film("Forsage", "action", 100, 130, 2)
        #
        # self.db.create_film("Oldboy", "action", 100, 140, 3)



        self.ui = uic.loadUi("ui.ui", self)
        self.window().setWindowTitle("Cinema")

        self.ui.films_btn.clicked.connect(self.draw_films_table)
        self.ui.halls_btn.clicked.connect(self.draw_halls_table)

        self.ui.delete_hall_btn.clicked.connect(self.delete_hall)
        self.ui.delete_film_btn.clicked.connect(self.delete_film)

        self.ui.update_hall_btn.clicked.connect(self.update_hall_db)
        self.ui.update_film_btn.clicked.connect(self.update_film_db)

        self.ui.add_hall_btn.clicked.connect(self.create_hall_db)
        self.ui.add_film_btn.clicked.connect(self.create_film_db)

        self.draw_halls_table()

    def draw_halls_table(self):
        self.table = self.ui.table_place
        self.table.clear()
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(["id","name","seats"])

        res = self.db.read_hall()

        i = 0
        for hall in res:
            self.table.setRowCount(i+1)
            j = 0
            for attribute in hall:
                item = QTableWidgetItem()
                item.setText(str(attribute))
                self.table.setItem(i,j,item)
                j += 1
            i += 1

    def draw_films_table(self):
        self.table = self.ui.table_place
        self.table.clear()
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(["id", "name", "genre", "ticket_cost", "duration", "hall_id"])

        res = self.db.read_film()

        i = 0
        for film in res:
            self.table.setRowCount(i+1)
            j = 0
            for attribute in film:
                item = QTableWidgetItem()
                item.setText(str(attribute))
                self.table.setItem(i, j, item)
                j += 1
            i += 1

    def update_halls_table(self):
        self.table = self.ui.table_place
        self.table.clear()
        self.draw_halls_table();

    def update_films_table(self):
        self.table = self.ui.table_place
        self.table.clear()
        self.draw_films_table();

    def delete_hall(self):
        id = self.id_hall_delete.value()
        if(id != ''):
            self.db.delete_hall(id)
        self.update_halls_table()

    def delete_film(self):
        id = self.id_film_delete.value()
        self.db.delete_hall(id)
        self.update_films_table()

    def update_hall_db(self):
        id = self.id_hall_update.value()
        name = self.new_hall_name.text()
        seats = self.new_hall_seats.value()
        self.db.update_hall(id,name,seats)
        self.update_halls_table()


    def update_film_db(self):
        id = self.id_film_update.value()
        name = self.new_film_name.text()
        genre = self.new_genre.text()
        ticket_cost = self.new_ticket_cost.value()
        duration = self.new_duration.value()
        hall_id = self.new_hall.value()
        self.db.update_film(id, name, genre, ticket_cost, duration, hall_id)
        self.update_films_table()

    def create_hall_db(self):
        name = self.hall_name.text()
        seats = self.hall_seats.value()
        self.db.create_hall(name, seats)
        self.update_halls_table()

    def create_film_db(self):
        name = self.film_name.text()
        genre = self.genre.text()
        ticket_cost = self.ticket_cost.value()
        duration = self.duration.value()
        hall_id = self.hall.value()
        self.db.create_film(name, genre, ticket_cost, duration, hall_id)
        self.update_films_table()