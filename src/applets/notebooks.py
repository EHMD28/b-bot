from bbot_core.applets import Applet
import os


def read_notebook(notebook_name: str) -> None:
    if os.path.exists(f"data/notebooks/{notebook_name}.txt"):
        print("file does exist")


def open_notebook(notebook_name: str) -> None:
    ...


def handle_input(inp: str) -> None:
    match inp:  
        case _:
            pass


def start_notebooks_applet() -> None:
    user_inp: str = ""
    while user_inp not in ["exit", "quit"]:
        user_inp = input("notebooks> ")


# to be exported 
notebooks_applet = Applet(name="notebooks",
                          description="an appplet for creating, reading, and writing notebooks",
                          keywords=["notes", "notebook"],
                          start_func=start_notebooks_applet,
                          help_string="""The notebooks applet allows for users to create, read, write,
                          and delete notebooks
                          """)
