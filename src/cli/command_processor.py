from BBOT_ASCII_ART_COLORED import BBOT_ASCII_ART_COLORED, VERSION
from apps.calc import evaluate_equ, calc_area, calc_volume
from apps.notebooks import notebook_command_processor
from os import system, name


HELP_STRING = """
calculator: ...
    command: 'calc {expression}'
    command: 'calc area {shape}'
    command: 'calc volume {shape}'
notebook: create, read, and edit notebooks
    command: 'note' or 'notebook'
clear: clears the screen of all previous text input
    command: 'clear'
exit: terminates program
    command: 'exit'
version: prints out version of B-bot that you are running.
    command: 'ver' or 'version'
"""


def clear_output():
    system("cls" if name == "nt" else "clear")


def command_processor_without_user(command: str):
    match command.lower().split():
        case ["area", *shape] | ["calc", "area", *shape]:
            calc_area(shape[0])
        case ["volume", *shape] | ["calc", "volume", *shape]:
            calc_volume(shape[0])
        case ["calc", *equ] | ["calculator", *equ]:
            try:
                equ = " ".join(equ)
                equ = equ.replace("^", "**")
                evaluate_equ(equ)
            except SyntaxError:
                print("Please enter an expression")
        case ["note"] | ["notebook"]:
            notebook_command_processor()
        case ["help"]:
            print(HELP_STRING)
        case ["clear"]:
            clear_output()
        case ["ver"] | ["version"]:
            print(BBOT_ASCII_ART_COLORED)
            print(VERSION)
        case ["exit"] | ["goodbye"]:
            raise KeyboardInterrupt
        case _:
            print("Invalid Command")


def command_processor_with_user(command: str, user: dict):

    match command.lower().split():
        case ["area", *shape] | ["calc", "area", *shape]:
            calc_area(shape[0])
        case ["volume", *shape] | ["calc", "volume", *shape]:
            calc_volume(shape[0])
        case ["calc", *equ] | ["calculator", *equ]:
            try:
                equ = " ".join(equ)
                equ = equ.replace("^", "**")
                evaluate_equ(equ)
            except SyntaxError:
                print("Please enter an expression")
        case ["note"] | ["notebook"]:
            notebook_command_processor()
        case ["help"]:
            print(HELP_STRING)
        case ["clear"]:
            clear_output()
        case ["ver"] | ["version"]:
            print(BBOT_ASCII_ART_COLORED)
            print(VERSION)
        case ["exit"] | ["goodbye"]:
            raise KeyboardInterrupt
        case _:
            print("Invalid Command")
