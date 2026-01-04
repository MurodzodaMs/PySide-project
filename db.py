import sqlite3


class DataBase:
    def __init__(self):
        self.connector = sqlite3.connect('local.db')
        self.cursor = self.connector.cursor()

        self.create_table()

    def fetchall(self, query, data=None):
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetchone(self, query, data=None):
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()

    def commit(self, query, data=None):
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        self.connector.commit()

    def create_table(self):
        self.commit('''
        CREATE TABLE IF NOT EXISTS blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type VARCHAR NOT NULL,
            comment TEXT, 
            media_url TEXT,
            url TEXT,
            lesson INTEGER REFERENCES lesson(id)
        );''')
        self.commit('''
        CREATE TABLE IF NOT EXISTS lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            owner INTEGER REFERENCES user(id)
        );''')
        self.commit('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        );''')
        self.commit('''
        CREATE TABLE IF NOT EXISTS lesson_teg (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson INTEGER REFERENCES lesson(id),
            tag TEXT
        );''')

    def close(self):
        self.connector.close()


db = DataBase()


def create_block(block_type, **kwargs):
    comment = kwargs.get('comment')
    media_url = kwargs.get('media_url')
    url = kwargs.get('url')
    lesson = kwargs.get('lesson')

    db.commit('''
    INSERT INTO blocks (type, comment, media_url, url, lesson)
        VALUES (?, ?, ?, ?, ?)''',
              (block_type, comment, media_url, url, lesson)
              )


def read_block():
    return db.fetchall('SELECT * FROM blocks')


def read_blocks_by_lesson(lesson_id):
    return db.fetchall('SELECT * FROM blocks WHERE lesson=?', (lesson_id,))


def check_lesson(title):
    lesson = db.fetchone('select * from lessons where title=?', (title,))
    return bool(lesson)


def get_title_by_lesson_id(lesson_id):
    return db.fetchone('SELECT title from lessons where id = ?', (lesson_id,))


def create_lesson(title):
    db.commit('INSERT INTO lessons (title) VALUES (?)', (title,))


def read_lesson():
    return db.fetchall('SELECT * FROM lessons')


def delete_lesson(lesson_id):
    db.commit('DELETE FROM blocks WHERE lesson = ?', (lesson_id,))
    db.commit('DELETE FROM lessons WHERE ID = ?', (lesson_id,))
