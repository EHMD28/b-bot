from bbot_core.command_processor import command_processor
from applets.calculator import calc_applet


def main() -> None:
    command_processor([calc_applet])


if __name__ == "__main__":
    main()
