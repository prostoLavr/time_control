import sqlite3 as sql
from datetime import datetime as dt
import typing


class DataBase:
    def __init__(self, path: str):
        self.con = sql.connect(path)
        self.cur = self.con.cursor()

    def get_all(self):
        return self.cur.execute('SELECT * FROM Tasks').fetchall()

    @staticmethod
    def format_result(elem: typing.Iterable):
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

    def find(self, f_start: str, f_end: str):
        f_start, f_end = dt.strptime(f_start, '%Y-%m-%d %H:%M'), dt.strptime(f_end, '%Y-%m-%d %H:%M')
        return filter(lambda x: x['start'] > f_start and x['end'] < f_end, self.all())


if __name__ == '__main__':
    db = DataBase('db.sqlite')
    print(*db.find(*'2000-01-01 00:00 - 3000-01-01 00:00'.split(' - ')))
