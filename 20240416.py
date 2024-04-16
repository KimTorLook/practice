20240416
#0

def acc_password():
    account_name = input("plz input your account name:")
    password = input("plz input a new password")


#1
'''+3 +4
 sissor encrption
s 65  68
d 100
z 86
Z > A
Mod
'''
def caesar_encrypt():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    chars = input(("input a alphabet: "))
    
    if chars.islower():
        a = lower.index(chars)
        if (a == 24 or a == 25 or a == 26):
            print(lower[a+3-26])
        else:
            print(lower[a+3])


    else:
        a = upper.index(chars)
        print(upper[a+3])
    
caesar_encrypt()