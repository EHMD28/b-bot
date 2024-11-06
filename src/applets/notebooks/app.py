from bbot_core.applet import Applet


class NotebooksApplet(Applet):
    def notebook_exists(notebook_name: str): ...

    def open_notebook(notebook_name: str): ...

    # Overridden method
    def start(self):
        user_inp: str = ""
        while user_inp not in ["exit", "quit"]:
            user_inp = input("notebooks> ")
