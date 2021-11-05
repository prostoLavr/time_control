import os

dr = './my_widgets/'
for file in filter(lambda x: x.endswith('.ui'), os.listdir(dr)):
    os.system(f'pyuic5 {dr}{file} -o {dr}{file[:-3]}.py')


def nothing():
    pass
