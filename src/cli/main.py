from command_processor import command_processor
from login import user_login, on_login
from os.path import join as pathjoin
import json

def main():
    print('Starting...')
    
    user_chosen: str = user_login()    
    user_logged_in: bool = not (len(user_chosen) == 0)

    
    if not user_logged_in:
        print("Hello, I am B-bot. How may I assist you today?")

        try:            
            while True:
                inp = input('Enter a command: ')
                command_processor(inp)
        except KeyboardInterrupt:
            print('Program Terminated')
        except EOFError:
            print('Program Terminated')
    else:
        print(f"Hello {user_chosen}, I am B-bot. How may I assist you today?")
        
        try:
            with open(pathjoin('configs', 'users', f'{user_chosen}.json')) as f:
                user = json.load(f)
            
            on_login(user)
            
            while True:
                inp = input('Enter a command: ')
                command_processor(inp, user_chosen)
        except KeyboardInterrupt:
            print('Program Terminated')
        except EOFError:
            print('Program Terminated')

    
if __name__ == '__main__':
    main()

