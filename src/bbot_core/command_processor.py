from bbot_core.applets import Applet
import os


def clear_screen() -> None:
    os.system("clear" if os.name == "posix" else "cls")


def print_help() -> None:
    print("Not implemented yet")


def print_version() -> None:
    print("B-bot CLI v.1.0.0")


def command_processor(applets: list[Applet] = None) -> None:
    user_input: str = ""

    keep_running = True
    while keep_running:
        user_input = input("bbot> ")
        
        matched_applet: bool = False
        
        for applet in applets:
            if user_input in applet.keywords:
                applet.start()
                matched_applet = True

        if matched_applet:
            continue

        # checking for default operations
        match user_input:
            case "clear":
                clear_screen()
            case "help":
                print_help()
            case "ver":
                print_version()
            case "exit" | "quit":
                keep_running = False
            case _:
                print("Invalid command")
