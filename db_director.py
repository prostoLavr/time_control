import sqlite3 as sql
from datetime import datetime as dt


get_all_q = 'SELECT * FROM Tasks'


class DataBase:
    def __init__(self, path):
        self.con = sql.connect(path)
        self.cur = self.con.cursor()

    def get_all(self):
        return self.cur.execute(get_all_q).fetchall()

    @staticmethod
    def format_result(elem):
        dct = dict(zip('id_ name description start end'.split(), elem))
        dct['start'] = dt.strptime(dct['start'], '%Y-%m-%d %H:%M')
        dct['end'] = dt.strptime(dct['end'], '%Y-%m-%d %H:%M')
        return dct

    def all(self):
        return map(self.format_result, self.get_all())

    def past(self):
        return filter(lambda x: x is not None and x['end'] < dt.now(), self.all())

    def future(self):
        return filter(lambda x: x['start'] > dt.now(), self.all())

    def now(self):
        return filter(lambda x: x['start'] < dt.now() and (x['end'] is None or x['end'] > dt.now()), self.all())


if __name__ == '__main__':
    db = DataBase('db.sqlite')
    print(*db.all())
