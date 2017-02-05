import sqlite3


class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS songs (title text, file_id text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, name, song_id):
        stmt = "INSERT INTO songs (title, file_id) VALUES (?,?)"
        args = (name, song_id)
        self.conn.execute(stmt, args)
        self.conn.commit()


    def get_items(self,name):
        stmt = "SELECT file_id FROM songs where title==name"
        return [x[0] for x in self.conn.execute(stmt)]


