from typing import Callable


class Applet:
    """The purpose of the Applet class is to provide a consistent and reusable
    API through which B-bot programs can integrate applets.
    """

    def __init__(self, start_func: Callable[[], None]):
        self.start_func = start_func
    
    def start(self) -> None:
        self.start_func()

        
def validate_applet(applet: Applet) -> bool: ...


def load_applets() -> list[Applet]:
    """Locates all installed applets, validates them, and loads them into a list
    that can then be used by the rest of the program. See `docs/guide.md` for 
    more details. 

    Returns:
        list[Applet]: a list of all installed applets
    """
    ...
