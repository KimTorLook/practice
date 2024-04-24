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


def mul():
    debug("Hello")    


if __name__ == "__main__":
    error()