import sqlite3

class DatabaseConnection:
    connection_obj = sqlite3.connect('geek.db')
    cursor = connection_obj.cursor()

    def create_tables (self):
        create_author_table = """
        CREATE TABLE author (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL
        );
        """

        create_magazine_table = """
        CREATE TABLE magazine (
        id INTEGER PRIMARY KEY,
        category VARCHAR,
        name VARCHAR
        );
        """

        create_article_table = """
        CREATE TABLE article (
        id INTEGER PRIMARY KEY,
        title TEXT(50),
        author INTEGER NOT NULL,
        magazine INTEGER NOT NULL,
        FOREIGN KEY (author) REFERENCES author (id)
        );
        """

        self.cursor.execute(create_author_table)
        self.cursor.execute(create_magazine_table)
        self.cursor.execute(create_article_table)
        self.connection_obj.close()

    def create_resource(self, query):
        res = self.cursor.execute(query)
        self.connection_obj.commit()
        self.connection_obj.close()
        return res

    def fetch_resource(self, query):
        res = self.cursor.execute(query)
        self.connection_obj.close()
        return res