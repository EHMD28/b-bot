from bbot_core.core_utils import Applet


def start_calc_applet() -> None:
    user_inp: str = ""
    while user_inp not in ["exit", "quit"]:
        user_inp = input("calculator> ")
    
# Calculator Applet for Export
calc_applet = Applet(name="Calculator",
                     description="an applet for preforming arithmetic operations",
                     keywords=["calculator", "math"],
                     start_func=start_calc_applet)
    