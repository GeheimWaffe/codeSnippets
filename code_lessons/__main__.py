from code_lessons import dataframegenerator
import sys

def main_function():
    # Press the green button in the gutter to run the script.
    df = dataframegenerator.generate_dataframe_1()
    print('This is a dataframe. \n It has the following dtypes : ')
    print(df.dtypes)
    print('as well as the following columns : ')
    print(df.columns)
    print('we can try the following aggregates')
    print('max :')
    print(df.max())
    print('min :')
    print(df.min())

def main(args=None):
    """ The main routine """
    main_function()
    print('this is my program')
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == '__main__':
    sys.exit(main())