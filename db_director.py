import sqlite3 as sql
from datetime import datetime as dt
import typing

from status import Status


class DataBase:
    def __init__(self, path: str):
        self.con = sql.connect(path)
        self.cur = self.con.cursor()

    def get_all(self):
        return self.cur.execute('SELECT * FROM Tasks').fetchall()

    @staticmethod
    def format_result(elem: typing.Iterable):
        dct = dict(zip('id_ name description start end status'.split(), elem))
        dct['start'] = dt.strptime(dct['start'], '%Y-%m-%d %H:%M')
        dct['end'] = None if dct['end'] is None else dt.strptime(dct['end'], '%Y-%m-%d %H:%M')
        return dct

    def all(self):
        return map(self.format_result, self.get_all())

    def past(self):
        return map(self.format_result, self.cur.execute(f'SELECT * FROM Tasks WHERE status={Status.done.value}'))

    def future(self):
        return map(self.format_result, self.cur.execute(f'SELECT * FROM Tasks WHERE status={Status.notdone.value}'))

    def now(self):
        return map(self.format_result, self.cur.execute(f'SELECT * FROM Tasks WHERE status={Status.run.value}'))

    def find(self, f_start: str, f_end: str):
        f_start, f_end = dt.strptime(f_start, '%Y-%m-%d %H:%M'), dt.strptime(f_end, '%Y-%m-%d %H:%M')
        return filter(lambda x: x['start'] > f_start and (x['end'] is None or x['end'] < f_end), self.all())

    def set_task_status(self, id_: int, status: Status):
        self.cur.execute(f'UPDATE Tasks SET status = {status} WHERE id = {id_}')
        self.con.commit()

    def start_now(self, name: str):
        print('started with name', name)
        id_ = self.cur.execute('SELECT MAX(id) from Tasks').fetchone()[0] + 1
        values = f'{id_}, "{name}", "None", "{dt.now().strftime("%Y-%m-%d %H:%M")}", NULL, {Status.run.value}'
        q = f'INSERT INTO Tasks VALUES ( {values} )'
        print(q)
        self.cur.execute(q)


if __name__ == '__main__':
    db = DataBase('db.sqlite')
    print(*db.find(*'2000-01-01 00:00 - 3000-01-01 00:00'.split(' - ')))
