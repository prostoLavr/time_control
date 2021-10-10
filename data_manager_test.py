from datetime import datetime as dt
import unittest
import table_and_data
import os
import shutil


test_dir = './test_dir'
test_file = './test_dir/test_file.pickle'


class DataManagerLoaderTest(unittest.TestCase):
    @staticmethod
    def clear_dir():
        shutil.rmtree(test_dir)
        os.mkdir(test_dir)

    def test_error_path(self):
        dml = table_and_data.DataManagerLoader()
        self.assertFalse(dml.can_load('/error_path'))

    def test_error_filename(self):
        self.clear_dir()
        self.assertFalse(os.path.isfile(test_file))
        dml = table_and_data.DataManagerLoader()
        self.assertFalse(dml.can_load(test_file))

    def test_error_file(self):
        with open(test_file, 'w') as file:
            file.write('This file is not correct!')
        dml = table_and_data.DataManagerLoader()
        self.assertEqual(dml.load(test_file), -1)

    def test_file_create(self):
        self.clear_dir()
        self.assertFalse(os.path.isfile(test_file))
        dml = table_and_data.DataManagerLoader()
        dml.create_new_df(test_file)
        self.assertTrue(os.path.isfile(test_file))


class DataManagerTest(unittest.TestCase):
    def test_add_task(self):
        error = False
        dm = table_and_data.DataManager()
        dm.create_new_df(test_file)
        dm.add_task('Test task', 'important', '#F00', dt(2021, 10, 9, 14, 0), dt(2021, 10, 9, 15, 10), 'my test:)')
        try:
            dm.df.iloc[0]
        except IndexError:
            error = True
        self.assertFalse(error)

    def test_tasks_getters(self):
        dm = table_and_data.DataManager()
        dm.create_new_df(test_file)
        dm.add_task('Now Task', 'important', '#F00', dt.now(), dt(3021, 10, 9, 15, 10), 'my test:)')
        dm.add_task('Now Task too', 'important', '#F00', dt.now(), None, 'my test:)')
        dm.add_task('Past Task', 'important', '#F00', dt(300, 10, 10, 14, 10), dt(300, 10, 10, 15, 10), 'my test:)')
        dm.add_task('Future Task', 'important', '#F00', dt(3021, 10, 9, 15, 10), dt(3021, 10, 9, 15, 20), 'my test:)')
        dm.add_task('Future Task too', 'important', '#F00', dt(3021, 10, 9, 15, 10), None, 'my test:)')
        self.assertEqual(set(dm.get_plans().Name), {'Future Task', 'Future Task too'})
        self.assertEqual(set(dm.get_started().Name), {'Now Task', 'Now Task too'})
        self.assertEqual(set(dm.get_ended().Name), {'Past Task'})

    def test_tasks_getters_by_time(self):
        dm = table_and_data.DataManager()
        dm.create_new_df(test_file)
        dm.add_task('Now Task', 'important', '#F00', dt.now(), dt(3021, 10, 9, 15, 10), 'my test:)')
        dm.add_task('Now Task too', 'important', '#F00', dt.now(), None, 'my test:)')
        dm.add_task('Past Task', 'important', '#F00', dt(300, 10, 10, 14, 10), dt(300, 10, 10, 15, 10), 'my test:)')
        dm.add_task('Future Task', 'important', '#F00', dt(3021, 10, 9, 15, 10), dt(3021, 10, 9, 15, 20), 'my test:)')
        dm.add_task('Future Task too', 'important', '#F00', dt(3021, 10, 9, 14, 10), None, 'my test:)')

        self.assertEqual(self.get_result(dm, dt(200, 10, 10, 14, 20), dt(4000, 10, 10, 15, 30)),
                         {'Now Task', 'Now Task too', 'Future Task', 'Future Task too', 'Past Task'})
        self.assertEqual(self.get_result(dm, dt(400, 10, 10, 14, 20), dt(4000, 10, 10, 15, 30)),
                         {'Now Task', 'Now Task too', 'Future Task', 'Future Task too'})
        self.assertEqual(self.get_result(dm, dt(3021, 10, 10, 14, 20), dt(3021, 10, 10, 14, 30)),
                         {'Future Task too', 'Now Task too'})
        self.assertEqual(self.get_result(dm, dt(300, 10, 10, 14, 20), dt(400, 10, 10, 14, 30)),
                         {'Past Task'})

    def get_result(self, dm, start_time, end_time):
        res = (*map(lambda x: set(x.Name), dm.get_by_time(start_time, end_time)),)
        return res[0] | res[1]


if __name__ == '__main__':
    unittest.main()
