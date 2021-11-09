import sqlite3 as sql
from datetime import datetime as dt
from datetime import timedelta as td
import typing

from PyQt5.QtCore import QDateTime, QTime

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
        dct['status'] = Status.from_value(dct['status'])
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
        start, end = dt.strptime(f_start, '%Y-%m-%d %H:%M'), dt.strptime(f_end, '%Y-%m-%d %H:%M')
        return self.find_by_pytime(start, end)

    def find_by_pytime(self, start: dt, end: dt):
        return filter(lambda x: x['status'] is Status.done and x['start'] >= start and
                      (x['end'] is None or x['end'] <= end), self.all())

    def set_task_status(self, id_: int, status: Status):
        self.cur.execute(f'UPDATE Tasks SET status = {status} WHERE id = {id_}')
        self.con.commit()

    def get_max_id(self, _n=0):
        try:
            id_ = self.cur.execute('SELECT MAX(id) from Tasks').fetchone()[0] + 1 + _n
        except sql.IntegrityError:
            print('Index error, trying use other id...')
            if _n > 5:
                raise IndexError('Database index error')
            self.get_max_id(_n+1)
            return
        except TypeError:
            id_ = 0
        if _n:
            print('Fix.')
        return id_

    def start_now(self, name: str):
        id_ = self.get_max_id()
        values = f'{id_}, "{name}", "None", "{dt.now().strftime("%Y-%m-%d %H:%M")}", NULL, {Status.run.value}'
        q = f'INSERT INTO Tasks VALUES ( {values} )'
        self.cur.execute(q)
        self.con.commit()

    def set_end_time(self, id_: int, time: dt or None):
        if time is None:
            self.cur.execute(f'UPDATE Tasks SET end = NULL WHERE id = {id_}')
        else:
            time_str = f'"{time.strftime("%Y-%m-%d %H:%M")}"'
            self.cur.execute(f'UPDATE Tasks SET end = {time_str} WHERE id = {id_}')
        self.con.commit()

    def add_to_time(self, name: str, start: QDateTime, duration: QTime):
        start = start.toPyDateTime()
        duration = duration.toPyTime()
        end = (start + td(hours=duration.hour, minutes=duration.minute)).strftime("%Y-%m-%d %H:%M")
        start = start.strftime("%Y-%m-%d %H:%M")
        id_ = self.get_max_id()
        values = f'{id_}, "{name}", "None", "{start}", "{end}", {Status.notdone.value}'
        self.cur.execute(f'INSERT INTO Tasks VALUES ( {values} )')
        self.con.commit()

    def remove_task(self, task_id):
        id_list = map(lambda x: x[0], self.cur.execute('SELECT id FROM Tasks').fetchall())
        assert task_id in id_list, "Task id must be in id's list"
        self.cur.execute(f'DELETE FROM Tasks WHERE id = {task_id}')
        self.con.commit()


if __name__ == '__main__':
    db = DataBase('db.sqlite')
    print(*db.find(*'2000-01-01 00:00 - 3000-01-01 00:00'.split(' - ')))
