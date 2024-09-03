from typing import Callable


class Applet:
    """The purpose of the Applet class is to provide a consistent and reusable
    API through which B-bot programs can integrate applets.
    """

    def __init__(
        self,
        *,
        name: str,
        description: str,
        keywords: list[str],
        start_func: Callable[[], None],
        help_string: str
    ) -> None:
        self.name = name
        self.description = description
        self.keywords = keywords
        self.start_func = start_func
        self.help_string = help_string


    def start(self) -> None:
        self.start_func()

    def print_help(self) -> None:
        print(self.help_string)
