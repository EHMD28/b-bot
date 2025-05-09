from bbot_core.applets import Applet
import os
import json


def clear_screen() -> None:
    os.system("clear" if os.name == "posix" else "cls")


def print_standard_help() -> None:
    print("Not implemented yet")


def create_file(path: str) -> None:
    open(path, "x").close()


def print_version() -> None:
    try:
        with open("data/settings.json", "r") as f:
            content: dict = json.load(f)
            version: str = content["version"]
            print(version)
    except FileNotFoundError:
        create_file("data/settings.json")


def command_processor(applets: list[Applet] = None) -> None:
    user_input: str = ""

    keep_running = True
    while keep_running:
        user_input = input("bbot> ")

        # checking for applets
        for applet in applets:
            if user_input in applet.keywords:
                applet.start()

        # checking for default operations
        match user_input.split():
            case ["clear"]:
                clear_screen()
            case ["help", *args]:
                if args:
                    for applet in applets:
                        if args[0] in applet.keywords:
                            applet.print_help()
                else:
                    print_standard_help()
            case ["ver"] | ["version"]:
                print_version()
            case ["exit"] | ["quit"]:
                keep_running = False
            case _:
                print("Invalid command")
