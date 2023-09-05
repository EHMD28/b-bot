import os


def reset_all():
    rm: str = 'rm' if os.name == 'posix' else 'del'
    os.system(f'{rm} ./configs/users/*.json')
    
    