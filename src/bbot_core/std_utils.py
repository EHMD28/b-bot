r"""
    a module that contains functionalities that come with every distribution
    of B-bot, regardless of what applets are installed. 
"""


from utils.term_colors import (
    FG_BLACK,
    FG_CYAN,
    FG_GREEN,
    FG_WHITE,
    COLOR_RESET
)


BBOT_ASCII_ART_COLORED: str = f'''
     {FG_BLACK}__________________________
     |@@@@@@@@@@@@@@@@@@@@@@@@@|    
     |@@@@@@@@@@@@@@@@@@@@@@@@@|    
     |@@@@@@@@@@@@@@@@@@@@@@@@@|    
     |@@@@@@@@@@@@@@@@@@@@@@@@@|    
  ___________________________________
[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]
    {FG_CYAN}############################{FG_WHITE}       _____          ___{FG_CYAN}
  ################################   {FG_WHITE} |  _  \        |   |{FG_CYAN}               
  ##########{FG_GREEN}$$${FG_CYAN}########{FG_GREEN}$$${FG_CYAN}##########  {FG_WHITE}| | | /        |   |       ____    _____{FG_CYAN}
  #########{FG_GREEN}$$$$${FG_CYAN}######{FG_GREEN}$$$$${FG_CYAN}#########  {FG_WHITE}|  __  \  ===  | /\ \    /  __ \    | |{FG_CYAN}
  #########{FG_GREEN}$$$$${FG_CYAN}######{FG_GREEN}$$$$${FG_CYAN}#########  {FG_WHITE}| |__| /       | \/  \  |  |__| |   | |{FG_CYAN}
  ##########{FG_GREEN}$$${FG_CYAN}########{FG_GREEN}$$${FG_CYAN}##########  {FG_WHITE}|_____/        |_____/   \_____/    |_|{FG_CYAN}
  ##################################  
  ################################       {FG_WHITE}version: 1.0.0{FG_CYAN}
    #########{FG_GREEN}==========={FG_CYAN}#########
      #######################
          #################{COLOR_RESET}
'''
