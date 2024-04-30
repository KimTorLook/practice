""" #20240331  matplotlib
import matplotlib.pyplot as plt

###################################
amplitude= float(input("amplitude:"))
time     = float(input("time: "))            # unit : second
times    = int(input("times: "))             # unit : Num of wave  
distance = float(input("distance: "))        # unit : meter

def frequency(times,time)->float:            # frequency = number of wave per second
    f = times/time
    return f                                 # Unit : Hz

def wavelength(time, times)->float:
    lamda = time/times
    return lamda                              #unit: meter

def wave_period(lamda=None, times=None, f=None)->float:
    if (lamda==None or times==None):
        T = 1/f
        return T
    else:
        T = lamda/times
        return T

def wave_speed(distance,time)->float:  
        v = distance / time                  # unit-- distance : meter , time : second
        return v                             # unit-- ms-1


#xxx 
def speed_n_period_corelation(distance,time, f=None, T=None)->float:    
    if (f == None or T==None):  
        v = distance / time                  # unit-- distance : meter , time : second
        return v                             # unit-- ms-1
    else:
        v = f * T
        return v

f = frequency(times, time)
lamda = wavelength(time,times)
T = wave_period(time, times)
v = wave_speed(distance, time)

print(frequency(times, time))
print(wavelength(time,times))
print(wave_period(time,times,f))
print(wave_speed(distance,time,))
#print(speed_n_period_corelation(distance,time,f,T))


time = float(input("time: "))            # unit : second
times = int(input("times: "))            # Num of wave  
distance = float(input("distance: "))    # unit : meter

def frequency(times, time) -> float:            # frequency = number of wave per second
    f = times / time
    return f                                    # Unit : Hz

def wave_period(time, times) -> float:
    T = time / times
    return T                                    # Unit: second

def wave_speed(distance, time) -> float:  
    try:
        v = distance / time                     # unit-- distance : meter , time : second
        return v                                # unit-- m/s
    except ZeroDivisionError as Z:
        print(Z)
    except ValueError as V:
        print(V)

# Here's the corrected speed_n_period_corelation function
def speed_n_period_corelation(distance, time, f=None, T=None) -> float:    
    if f is None or T is None:  
        v = distance / time                     # unit-- distance : meter , time : second
        return v                                # unit-- m/s
    else:
        v = f * T
        return v

# Using the functions
f = frequency(times, time)
T = wave_period(time, times)
v = wave_speed(distance, time)

print(f"Frequency: {f} Hz")
print(f"Wave Period: {T} s")
print(f"Wave Speed: {v} m/s")

# Now passing the calculated speed to speed_n_period_corelation function
print(f"Speed using frequency and period: {speed_n_period_corelation(distance, time, f, T)} m/s")





conn = sqlite3.connect('Jewelry.db')

cursor = conn.cursor()

def query_str(**kwarg):
    a = input("key1,value1,key2,value2,key3,value3,key4,value4,key5,value5,key6,value6,key7,value7,")
    table_name = input("table_name")
    for key, value in kwarg.item():
        pass

while s == 0:
    if s ==1:
        cursor.execute("INSERT INTO ")
    elif S == 2:
        select
        cursor.execute('SELECT * FROM `Jewelry`')
    elif s == 3:
        update
    elif s == 4:
        delete
    else: 
        break

    s = input()

cursor.execute('SELECT * FROM `Jewelry`')
records = cursor.fetchall()
print(records)
cursor.close()
conn.close

import requests

class caesar_encrypt():
    def __init__(self):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = lower.upper()
        self.lower = lower
        self.upper = upper

    def storeAndEncrypt(self,statement):
        message = list(statement)
        encrypted = []
        for loop in message:
            if loop.islower():        
                a = self.lower.index(loop)
                if a >= 23 :
                    print(self.lower[a+3-26])
                    encrypted.append(a)
                else:
                    print(self.lower[a+3])
                    encrypted.append(a)
            else:
                a = self.upper.index(loop)
                if a >= 23 :
                    print(self.upper[a+3-26])
                    encrypted.append(a)
                else:
                    print(self.upper[a+3])
                    encrypted.append(a)
        return encrypted

    def mainLoop(self, encrypted):
        statement = input(("input a message: "))
        
        while True:
            if statement.lower == "exit":
                print('---programme closed---')
                break
            self.storeAndEncrypt(statement)
            print(encrypted)

a=caesar_encrypt()
caesar_encrypt.mainLoop(a)


class CaesarEncrypt:
    def __init__(self):
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = self.lower.upper()

    def encrypt(self, chars, shift=3):
        encrypted_message = ""
        for char in chars:
            if char.isalpha():
                alphabet = self.lower if char.islower() else self.upper
                new_position = (alphabet.index(char) + shift) % 26
                encrypted_message += alphabet[new_position]
            else:
                encrypted_message += char
        return encrypted_message

    def main_loop(self):
        while True:
            chars = input("Input a message (type 'exit' to quit): ")
            if chars.lower() == 'exit':
                print('---programme closed---')
                break
            encrypted = self.encrypt(chars)
            print("Encrypted message:", encrypted)

# Create an instance of the CaesarEncrypt class
cipher = CaesarEncrypt()
cipher.main_loop()   """


from inspect import currentframe

def debug(msg):
    BOLD='\033[1m'
    dark_amber='\033[33m'
    FLASHING='\033[5M'
    END='\033[0m'
    Black="\033[0;30m"        # Black
    Red="\033[0;31m"          # Red
    Green="\033[0;32m"        # Green
    Yellow="\033[0;33m"       # Yellow
    Blue="\033[0;34m"         # Blue
    Purple="\033[0;35m"       # Purple
    Cyan="\033[0;36m"         # Cyan
    White="\033[0;37m"        # White

    # Bold
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
    print(f"{currentframe().f_back.f_lineno}.{IGreen}{msg}{END}")

def error():
    try:
        print(4/0)
    except ZeroDivisionError:
        debug("Divide zero error occur")


if __name__ == "__main__":
    error()



