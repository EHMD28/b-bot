from bbot_core.applets import Applet
import os
import json


def clear_screen() -> None:
    os.system("clear" if os.name == "posix" else "cls")


def print_help() -> None:
    print("Not implemented yet")


def print_version() -> None:
    with open("data/settings.json", "r") as f:
        content: dict = json.load(f)
        version: str = content["version"]
        print(version)


def command_processor(applets: list[Applet] = None) -> None:
    user_input: str = ""
    prompt_str: str = "bbot"

    keep_running = True
    while keep_running:
        user_input = input(f"{prompt_str}> ")

        # TODO: reimplement applets API
        # checking for applets
        for applet in applets:
            if user_input in applet.keywords:
                ...

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
