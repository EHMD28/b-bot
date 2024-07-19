from bbot_core.command_processor import command_processor
from applets.calculator import calc_applet
from bbot_core.std_utils import BBOT_ASCII_ART_COLORED


def main() -> None:
    print("Starting B-bot...")
    print(BBOT_ASCII_ART_COLORED)

    command_processor([
        calc_applet
    ])


if __name__ == "__main__":
    main()
