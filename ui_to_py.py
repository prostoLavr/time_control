import os

dr = './my_widgets/'
lst = 'gui home_widget task_widget history_widget'.split()

for file in lst:
    os.system(f'pyuic5 {dr}{file}.ui -o {dr}{file}.py')
    print('convert')


def nothing():
    pass
