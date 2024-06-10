from bbot_core.applets import Applet


def print_help() -> None:
    print("Not implemented yet")


def print_version() -> None:
    print("Not implemented yet")


def command_processor(applets: list[Applet] = None) -> None:
    user_input: str = ""

    while user_input not in ["quit", "exit"]:
        user_input = input("bbot> ")
        
        for applet in applets:
            if user_input in applet.keywords:
                applet.start()

        # checking for default operations
        match user_input:
            case "help":
                print_help()
            case "ver":
                print_version()

