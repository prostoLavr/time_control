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
        return dict(zip('id_ name description start end'.split(), elem))

    def all(self):
        return map(self.format_result, self.get_all())

    def get_past(self):
        return filter(lambda x: x is not None and x['end'] < dt.now(), self.all())

    def get_future(self):
        return filter(lambda x: x['start'] > dt.now(), self.all())

    def get_now(self):
        return filter(lambda x: x['start'] < dt.now() and (x['end'] is None or x['end'] > dt.now()), self.all())


if __name__ == '__main__':
    db = DataBase('db.sqlite')
    print(db.get_all())
    times = []
    for x in db.get_all():
        times.extend(x[3:])
    times = [dt.strptime(x, '%Y-%m-%d %H:%M') for x in times]
    print(times)
