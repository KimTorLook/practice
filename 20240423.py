"""唐詩欣賞
春曉
春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少？
竹里館
獨坐幽篁裡，彈琴復長嘯。深林人不知，明月來相照。
庭院深深深幾許？楊柳堆煙，簾幕無重數。玉勒雕鞍遊冶處，
樓高不見章台路。雨棋風狂三月暮，門掩黃昏，無計留春住。淚眼問花花不語，亂紅飛過鞦韆去。"""
from inspect import currentframe

""" def main():
    print(currentframe().f_lineno)
    print(currentframe().f_back.f_lineno)
 """

def debug(msg):
    BOLD='\033[1m'
    dark_amber='\033[33m'
    FLASHING='\033[5M'
    END='\033[0m'
    print(f"{currentframe().f_back.f_lineno}.{dark_amber}{msg}{END}")

def error():
    try:
        print(4/0)
    except:
        debug("error")


#Demostration code
#1
def dubug(msg):
    print(f"{currentframe().f_back.f_lineno}.{msg}")

def hello():
    debug("Hello World!")

#2

def debug2(msg):
    dark_amber='\033[33m'
    FLASHING='\033[5M'
    Black="\033[0;30m"        # Black
    Red="\033[0;31m"          # Red
    Green="\033[0;32m"        # Green
    Yellow="\033[0;33m"       # Yellow
    Blue="\033[0;34m"         # Blue
    Purple="\033[0;35m"       # Purple
    Cyan="\033[0;36m"         # Cyan
    White="\033[0;37m"        # White

    # Bold
    BOLD='\033[1m'
    BBlack="\033[1;30m"       # Black
    BRed="\033[1;31m"         # Red
    BGreen="\033[1;32m"       # Green
    BYellow="\033[1;33m"      # Yellow
    BBlue="\033[1;34m"        # Blue
    BPurple="\033[1;35m"      # Purple
    BCyan="\033[1;36m"        # Cyan
    BWhite="\033[1;37m"       # White

    # Underline
    UBlack="\033[4;30m"       # Black
    URed="\033[4;31m"         # Red
    UGreen="\033[4;32m"       # Green
    UYellow="\033[4;33m"      # Yellow
    UBlue="\033[4;34m"        # Blue
    UPurple="\033[4;35m"      # Purple
    UCyan="\033[4;36m"        # Cyan
    UWhite="\033[4;37m"       # White

    # Background
    On_Black="\033[40m"       # Black
    On_Red="\033[41m"         # Red
    On_Green="\033[42m"       # Green
    On_Yellow="\033[43m"      # Yellow
    On_Blue="\033[44m"        # Blue
    On_Purple="\033[45m"      # Purple
    On_Cyan="\033[46m"        # Cyan
    On_White="\033[47m"       # White

    # High Intensty
    IBlack="\033[0;90m"       # Black
    IRed="\033[0;91m"         # Red
    IGreen="\033[0;92m"       # Green
    IYellow="\033[0;93m"      # Yellow
    IBlue="\033[0;94m"        # Blue
    IPurple="\033[0;95m"      # Purple
    ICyan="\033[0;96m"        # Cyan
    IWhite="\033[0;97m"       # White

    # Bold High Intensty
    BIBlack="\033[1;90m"      # Black
    BIRed="\033[1;91m"        # Red
    BIGreen="\033[1;92m"      # Green
    BIYellow="\033[1;93m"     # Yellow
    BIBlue="\033[1;94m"       # Blue
    BIPurple="\033[1;95m"     # Purple
    BICyan="\033[1;96m"       # Cyan
    BIWhite="\033[1;97m"      # White

    # High Intensty backgrounds
    On_IBlack="\033[0;100m"   # Black
    On_IRed="\033[0;101m"     # Red
    On_IGreen="\033[0;102m"   # Green
    On_IYellow="\033[0;103m"  # Yellow
    On_IBlue="\033[0;104m"    # Blue
    On_IPurple="\033[10;95m"  # Purple
    On_ICyan="\033[0;106m"    # Cyan
    On_IWhite="\033[0;107m"   # White

    END='\033[0m'

    print(f"{On_Yellow}{currentframe().f_back.f_lineno}{END}. {On_Blue}{msg}{END}")

def hello2():
    debug2("Hello World!")

#3

dark_amber='\033[33m'
FLASHING='\033[5M'
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White

# Bold
BOLD='\033[1m'
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White

# Underline
UBlack="\033[4;30m"       # Black
URed="\033[4;31m"         # Red
UGreen="\033[4;32m"       # Green
UYellow="\033[4;33m"      # Yellow
UBlue="\033[4;34m"        # Blue
UPurple="\033[4;35m"      # Purple
UCyan="\033[4;36m"        # Cyan
UWhite="\033[4;37m"       # White

# Background
On_Black="\033[40m"       # Black
On_Red="\033[41m"         # Red
On_Green="\033[42m"       # Green
On_Yellow="\033[43m"      # Yellow
On_Blue="\033[44m"        # Blue
On_Purple="\033[45m"      # Purple
On_Cyan="\033[46m"        # Cyan
On_White="\033[47m"       # White

# High Intensty
IBlack="\033[0;90m"       # Black
IRed="\033[0;91m"         # Red
IGreen="\033[0;92m"       # Green
IYellow="\033[0;93m"      # Yellow
IBlue="\033[0;94m"        # Blue
IPurple="\033[0;95m"      # Purple
ICyan="\033[0;96m"        # Cyan
IWhite="\033[0;97m"       # White

# Bold High Intensty
BIBlack="\033[1;90m"      # Black
BIRed="\033[1;91m"        # Red
BIGreen="\033[1;92m"      # Green
BIYellow="\033[1;93m"     # Yellow
BIBlue="\033[1;94m"       # Blue
BIPurple="\033[1;95m"     # Purple
BICyan="\033[1;96m"       # Cyan
BIWhite="\033[1;97m"      # White

# High Intensty backgrounds
On_IBlack="\033[0;100m"   # Black
On_IRed="\033[0;101m"     # Red
On_IGreen="\033[0;102m"   # Green
On_IYellow="\033[0;103m"  # Yellow
On_IBlue="\033[0;104m"    # Blue
On_IPurple="\033[10;95m"  # Purple
On_ICyan="\033[0;106m"    # Cyan
On_IWhite="\033[0;107m"   # White

END='\033[0m'

def debug(msg):
    print(f"{On_Yellow}{currentframe().f_back.f_lineno}{END}. {On_Blue}{msg}{END}")

def error(err):
    print(f"Line:{On_Yellow}{currentframe().f_back.f_lineno}{END}. {FLASHING}{On_Blue}{err}{END}",file=sys.stderr)


def hello3():
    try:
        print(4/0)
    except:
        error("Divided by zero.")

    
if __name__ == "__main__":
    hello3()