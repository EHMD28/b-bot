from bbot_core.applets import Applet


def evaluate_expression() -> None: ...


def calc_area() -> None: ...


def calc_volume() -> None: ...


def convert_units() -> None: ...


def start_calc_applet() -> None:
    user_inp: str = ""
    while user_inp not in ["exit", "quit"]:
        user_inp = input("calculator> ")


# Calculator Applet for Export
calc_applet = Applet(
    name="Calculator",
    description="an applet for preforming arithmetic operations",
    keywords=["calculator", "math"],
    start_func=start_calc_applet,
    help_string="""The calculator applet can be used for arithmetic operations, unit conversion,
                     graphing, solving equations, and more. 
                     """,
)
