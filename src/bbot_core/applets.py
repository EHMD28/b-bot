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
        start_func: Callable[[], None]
    ) -> None:
        self.name = name
        self.description = description
        self.keywords = keywords
        self.start_func = start_func


    def start(self) -> None:
        self.start_func()
    