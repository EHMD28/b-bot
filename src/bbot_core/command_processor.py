from bbot_core.core_utils import Applet


def print_help() -> None:
    ...


def command_processor(applets: list[Applet] = None) -> None:
    prompt_string: str = "bbot"
    user_input: str = ""

    while user_input not in ["quit", "exit"]:
        user_input = input(f"{prompt_string}> ")
        
        for applet in applets:
            if user_input in applet.keywords:
                applet.start()

        # checking for default operations
        match user_input:
            case "help":
                pass
            case "ver":
                pass
