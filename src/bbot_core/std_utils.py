r"""
    a module that contains functionalities that come with every distribution
    of B-bot, regardless of what applets are installed. 
"""

import os


def clear_screen() -> None:
    os.system("clear" if os.name == "posix" else "cls")
