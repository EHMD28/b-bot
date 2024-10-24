from bbot_core.command_processor import command_processor
from applets.calculator import calc_applet
from applets.notebooks import notebooks_applet
from bbot_core.std_utils import BBOT_ASCII_ART_COLORED

from os import chdir


def main() -> None:
    # this is here to make relative paths more straightforward
    chdir("src")

    print("Starting B-bot...")
    print(BBOT_ASCII_ART_COLORED)

    command_processor([
        calc_applet,
        notebooks_applet
    ])


if __name__ == "__main__":
    main()
