from bbot_core.command_processor import command_processor
from bbot_core.misc import print_ascii_art

from os import chdir


def main() -> None:
    # this is here to make relative paths more straightforward
    chdir("src")

    print("Starting B-bot v.1.0.0...")
    print_ascii_art()

    command_processor([
        # calc_applet,
        # notebooks_applet
    ])


if __name__ == "__main__":
    main()
