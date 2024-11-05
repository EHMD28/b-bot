r"""
    a module that contains functionalities that come with every distribution
    of B-bot, regardless of what applets are installed. 
"""

from bbot_core.applets import Applet


def validate_applet(applet: Applet) -> bool: ...


def load_applets() -> list[Applet]:
    """Locates all installed applets, validates them, and loads them into a list
    that can then be used by the rest of the program. See `docs/guide.md` for 
    more details. 

    Returns:
        list[Applet]: a list of all installed applets
    """
    ...
