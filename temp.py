""" """ 
#20240331  matplotlib
import matplotlib.pyplot as plt
import tkinter as tk


1# 
Xaxis = input('x axis:')
Yaxis = input('Y axis:')
color = input('color:')
linewidth = input('linewidth:')
linestyle = input('linestyle')
label = input('label:')
plot_para = (Xaxis,Yaxis,color,linewidth,linestyle,label)

def draw_area(plot_para):
    win = tk.Tk()
    win.title('20240331')
    win.geometry('1024x2048')

    
    def line_plot(plot_para):  #唔明
        plt.plot(plot_para)
        plt.legend()
        plt.show()

    line_plot(plot_para)

    #win.mainloop()

draw_area(plot_para)

###################################
amplitude= float(input("amplitude:"))
time     = float(input("time: "))            # unit : second
times    = int(input("times: "))             # Num of wave  
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
cipher.main_loop()