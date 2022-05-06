import pathlib

def explore():
    f = pathlib.Path(__file__)
    print('the path of the file is ')
    print(f)
    print(f'the name of the file is {__name__}')
    print(f' the path of the file is {__path__}')