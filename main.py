from pandas_snippets import dataframegenerator

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
