from os.path import join as pathjoin
from os import listdir


def create_notebook(notebook_name: str):
    try:    
        open(pathjoin('apps', 'data', 'notebooks',\
                       f'{notebook_name}.txt'), 'x').close()
    except FileExistsError:
        print('A notebook with that name already exists')


def open_notebook(notebook_name: str):
    print(f'PLACEHOLDER | Opened notebook {notebook_name}')
    
    
def choose_notebook():
    notebooks = listdir(pathjoin('apps', 'data', 'notebooks'))
    
    print()
    for notebook in notebooks:
        print(notebook)
    print("*enter 'new' to create new notebook*")
    print()
    
    inp: str = input('Select a notebook: ').lower().split('.')
    if f'{inp[0]}.txt' in notebooks:
        open_notebook(inp)
    elif 'new' in inp:
        inp = input('Enter name of new notebook: ')
        create_notebook(inp)
    else:
        print('Unable to resolve command')

