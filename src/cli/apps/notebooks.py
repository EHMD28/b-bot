from os.path import join as pathjoin
from os import listdir


NOTEBOOKS_DIR = pathjoin('apps', 'data', 'notebooks')


def create_new_notebook(notebook_name: str):
    try:
        open(pathjoin(NOTEBOOKS_DIR, notebook_name), 'x').close()
    except FileExistsError:
        print('Notebook with that name already exists')


def read_notebook(notebook_name: str):
    ...


def open_notebook(notebook_name: str):
    ...
    

def notebook_command_processor():
    while True:
        notebook_input: str = input('Enter a notebook command: ')
        
        if 'exit' in notebook_input:
            break
        elif ('create' in notebook_input) or ('new' in notebook_input):
            notebook_input = input('Enter name of new notebook: ')
            print(f"Would you like to create new notebook with name '{notebook_input}'? [Yes/No]")
            notebook_input = input()
            if 'n' in notebook_input.lower():
                print(f"Didn't create notebook '{notebook_input}'")
            else:
                create_new_notebook(notebook_input)            
            
    print('Exited notebook editor')
    
    