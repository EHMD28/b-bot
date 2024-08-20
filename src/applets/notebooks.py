from bbot_core.applets import Applet


def notebook_start() -> None:
    user_inp: str = ""
    while user_inp not in ["exit", "quit"]:
        user_inp = input("notebooks> ")


# to be exported 
notebooks_applet = Applet(name="notebooks",
                          description="an appplet for creating, reading, and writing notebooks",
                          keywords=["notes", "notebook"],
                          start_func=notebook_start)
