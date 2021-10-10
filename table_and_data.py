import pandas as pd
# import numpy as np
import os
from datetime import datetime as dt


INF_TIME = dt(5000, 1, 1)


class DataManagerLoader:
    def __init__(self):
        self.df = None

    @staticmethod
    def can_load(path) -> bool:
        return os.path.isfile(path) and os.access(path, os.R_OK)

    @staticmethod
    def can_save(path):
        dir_path = os.path.dirname(os.path.realpath(path))
        return os.path.isdir(dir_path) and os.access(dir_path, os.W_OK)

    def create_new_df(self, path):
        columns = 'Name Type Color StartTime EndTime Duration Description'.split()
        new_df = pd.DataFrame(columns=columns)
        self.df = new_df
        self.save(path)

    def load(self, path):
        if not self.can_load(path):
            return 1
        try:
            self.df = pd.read_pickle(path)
        except Exception:
            return -1

    def save(self, path) -> int:
        if not self.can_save(path):
            return 1
        if self.df is None:
            return 2
        try:
            self.df.to_pickle(path)
            return 0
        except Exception:
            return -1


class DataManager(DataManagerLoader):
    def add_task(self, name: str, type_: str, color: str, start_time: dt,
                 end_time: dt or None, description: str):
        dct = {'Name': name, 'Type': type_, 'Color': color, 'StartTime': start_time, 'EndTime': end_time,
               'Duration': None if end_time is None else end_time - start_time, 'Description': description}
        self.df = self.df.append(dct, ignore_index=True)

    def get_plans(self):
        return self.df[self.df.StartTime > dt.now()]

    def get_started(self):
        return self.df[(self.df.StartTime < dt.now()) &
                       ((self.df.EndTime >= dt.now()) | (self.df.EndTime.isnull()))]

    def get_ended(self):
        return self.df[self.df.EndTime < dt.now()]

    def get_by_time(self, start_time: dt or None, end_time: dt or None, df=None):
        if start_time is None:
            start_time = dt(1, 1, 1)
        if end_time is None:
            end_time = INF_TIME
        df = df or self.df

        df_null = df[df.EndTime.isnull()]
        res_null = df_null[(df_null.StartTime < end_time)]

        df_notnull = df[df.notnull()]
        res_notnull = df_notnull[(df_notnull.StartTime < end_time) & (start_time < df_notnull.EndTime)]
        return res_null, res_notnull
