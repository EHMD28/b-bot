from bbot_core.applet import Applet
import os


class NotebooksApplet(Applet):
    def __init__(self): ...


# def read_notebook(notebook_name: str) -> None:
#     if os.path.exists(f"data/notebooks/{notebook_name}.txt"):
#         print("file does exist")


# def open_notebook(notebook_name: str) -> None:
#     ...


# def handle_input(inp: str) -> None:
#     match inp:
#         case _:
#             pass


# def start_notebooks_applet() -> None:
#     user_inp: str = ""
#     while user_inp not in ["exit", "quit"]:
#         user_inp = input("notebooks> ")
