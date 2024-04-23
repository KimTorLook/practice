20240416
#0

def acc_password():
    account_name = input("plz input your account name:")
    password = input("plz input a new password")


#1

ASCII Table
+3 +4
Mod


def caesar_encrypt():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    chars = input(("input a alphabet: "))
    
    if chars.islower() == True:
        a = lower.index(chars)
        if a == 23 or a == 24 or a == 25:
            print(lower[a+3-26])
        else:
            print(lower[a+3])
    else:
        a = upper.index(chars)
        if a == 23 or a == 24 or a == 25:
            print(upper[a+3-26])
        else:
            print(upper[a+3])
    print("-- program closed --")
    
#caesar_encrypt()









#2 using class
# using mod
# using loop
# value Error

class caesar_encrypt2:
    def __init__(self):
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = self.lower.upper()
        
    def Encrypt(self, chars, shift=3):
        encrypt_message = ""
        if chars.islower() == True:
            a = self.lower
        else:
            a = self.upper
        b = a.index(chars).mod(26)
        print(encrypt_message)





        print(upper[a+3-26])

        if a >= 23:


    def MainLoop(self):
        chars = input(("input a message to encrypt: "))
        while True:

            print("-- program closed --")

    
#caesar_encrypt2.MainLoop()

