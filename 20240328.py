import posixpath 
import os.path
import tkinter as tk
import tkinter.font as tkFont


'''
20240328
#try & except
#1
def Jiuyinge()->str:                #九因歌
    for x in range(1,11):
        for y in range(1,11):
            print(f"{x}*{y}={x*y}", end= " ")
        print(end="\n")
    return

Jiuyinge()


#2
def pythagorean( length:float=0.1, high:float=0.1 )->float:
    try:
        length=float(input('length:'))
        high=float(input('high:'))
        c2 = pow(length,2) + pow(high,2)
        c = pow(c2,0.5)
        print( c )
    except ZeroDivisionError as Z :
        print("you are wrong!")
    except ValueError as V:
        print('ValueError')
    except KeyboardInterrupt as K:
        print('KeyboardInterrupt' )
    except EOFError as E:
        print('EOF')
    except FileNotFoundError as F:
        print('filenotfound')
pythagorean()

20240329
#1 nest loop

def cube(length:int=1, width:int=1, high:int=1) -> int:
    mmm=length*width*high
    return mmm

cube()
#2
mass=input("mass:")
speed=input("speed:")
def kinetic_energy(mass,speed):     # E = 0.5 M * V^2
    energy = 0.5*mass*pow(speed,2)  # MASS=KG , speed = m/s
    return energy                   # energy = Joule

kinetic_energy(mass,speed)          # TypeError: can't multiply sequence by non-int of type 'float'

#3 
time     = float(input("time: "))            # unit : second
times    = int(input("times: "))             # Num of wave  
distance = float(input("distance: "))        # unit : meter

def frequency(times,time)->float:            # frequency = number of wave per second
    f = times/time
    return f                                 # Unit : Hz

print(frequency(times))


def wave_period(time, times)->float:
    T = time/times
    return T                                 #unit: second

print(wave_period(time,times))

def wave_speed(distance,time)->float:  
    try:
        v = distance / time                  # unit-- distance : meter , time : second
        return v                             # unit-- ms-1
    except ZeroDivisionError as Z:
        print(Z)
    except ValueError as V:
        print(V)

print(wave_speed(distance,time))

#xxx 
def speed_n_period_corelation(distance,time, f=None, T=None)->float:    
    if f == None:  
        v = distance / time                  # unit-- distance : meter , time : second
        return v                             # unit-- ms-1
    else:
        v = f * T

print(wave_speed(distance,time,frequency,wave_period))

#4
def draw_something():
    for x in range(1,6,1):
        a = "* "
        print(a*x)

draw_something()

20240329
#1 write xxx
  
file_name = str(input('file name:'))

def write_something(file_name:str):
    a = open(file_name, 'w', encoding = 'utf-8')
    content = str(input('please input you content.: '))    
    try:                                                    #input many times , 'done' means finishing input and break the while loop.
        while content != "done":
            if content !='done':
                a.write(content)
                a.write("\n")
                content = str(input('please input you content'))    
            else:
                break
    except FileNotFoundError as F:
        print('錯誤原因', F)                               
    a.close

write_something(file_name)


#靜夜思   
#床前明月光，疑是地上霜。
#舉頭望明月，低頭思故鄉。

#2 read and write

def read_n_write():                         #write lyric into a file"#poetry.txt" and try to read
    try:
        a = open("poetry.txt", 'r+', encoding = 'utf-8')
        a.write("I'll be waiting, all there's left to do is run You'll be the prince and I'll be the princess It's a love story, baby, just say yes")
        a.seek(126)                         #move the pointer position
        print(a.readlines())                #read the whole file
        print(a.tell())                     #check the pointer position
        a.close
    except FileNotFoundError as F:
        print('File not found, 錯誤原因:', F)
read_n_write()

#3
file_name = str(input('file name:'))

def read_n_write(file_name):                         #write lyric into a file"#poetry.txt" and try to read
    a = open(file_name, 'w+', encoding = 'utf-8')
    content = str(input('please input you content'))    

    while content != "done":
        if content !='done':
            a.write(content + "\n")
            content = str(input('please input you content'))    
        else:
            break

    a.seek(0)                           #move the pointer position to begining
    file = os.path.abspath(file_name)
    print(os.path.basename(file))          #testing directory operation command
    print(os.path.dirname(file))
    print(os.path.exists(file))
    print(os.path.getsize(file))
    print(os.path.isabs(file))
    print(os.path.isfile(file))
    print(os.path.isdir(file))
    a.write(file)                      #testing directory operation command
    a.write(os.path.basename(file) + "\n")          #testing directory operation command
    a.write(os.path.dirname(file)+ "\n")
    a.write(str(os.path.exists(file))+ "\n")
    a.write(str(os.path.getsize(file))+ "\n")
    a.write(str(os.path.isabs(file))+ "\n")
    a.write(str(os.path.isfile(file))+ "\n")
    a.write(str(os.path.isdir(file))+ "\n")


        
    print(a.readlines())                #read the whole file
    print(a.tell())                     #check the pointer position
    a.close
read_n_write(file_name)



#20240330

#1
filename = str(input())

def gen_directory(filename):                # directory checking
    a = posixpath.abspath(filename)
    b = posixpath.dirname(a)
    c = posixpath.basename(a)
    d = posixpath.getsize(filename)
    e = posixpath.exists(filename)
    f = posixpath.isabs(a)
    g = posixpath.isfile(filename)
    h = posixpath.isdir(b)
    print(f"abspath={a}")
    print(f"dirname={b}")
    print(f"basename={c}")
    print(f"getsize={d}")
    print(f"exists={e}")
    print(f"isabs={a}")
    print(f"isfile={g}")
    print(f"isdir={h}")    
    return

gen_directory(filename)

#2
filename = str(input("filename"))

def creat_file_n_write_file_data(filename):  # duplicate  with #1 
    a = posixpath.abspath(filename)          
    b = posixpath.dirname(a)
    c = posixpath.basename(a)
    d = posixpath.getsize(filename)
    e = posixpath.exists(filename)
    f = posixpath.isabs(a)
    g = posixpath.isfile(filename)
    h = posixpath.isdir(b)
    return a,b,c,d,e,f,g,h

def write_something(filename):                         # 1.create a file   2.write a poetry and directory to the file   3.write a directory/path to the file

    file = open(filename, "w")
    content = str(input('please input you content.: '))    

    while content != "done":        
        if content !='done':
            file.write(content)
            file.write("\n")
            content = str(input('please input you content.:'))    
        else:
            break

    a = posixpath.abspath(filename)
    b = posixpath.dirname(a)
    c = posixpath.basename(a)
    d = posixpath.getsize(filename)
    e = posixpath.exists(filename)
    f = posixpath.isabs(a)
    g = posixpath.isfile(filename)
    h = posixpath.isdir(b)

    lis = [a,b,c,d,e,f,g,h]
    for x in lis:
        file.write(str(x))
        file.write("\n")
    
print(creat_file_n_write_file_data(filename))
write_something(filename)
'''

#3  xxx

class App:
    def __init__(self, root):
        #setting title
        root.title("10-2-3")
        #setting window size
        width=1024
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        num1=tk.DoubleVar()
        num2=tk.DoubleVar()
        self.result=tk.DoubleVar()
        self.num1 = num1
        self.num2 = num2


        GLineEdit_791=tk.Entry(root)
        GLineEdit_791["bg"] = "#ffffff"
        GLineEdit_791["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_791["font"] = ft
        GLineEdit_791["fg"] = "#333333"
        GLineEdit_791["justify"] = "center"
        GLineEdit_791["textvariable"] = num1
        GLineEdit_791.place(x=70,y=70,width=70,height=25)

        GLabel_592=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_592["font"] = ft
        GLabel_592["fg"] = "#333333"
        GLabel_592["justify"] = "center"
        GLabel_592["text"] = "+"
        GLabel_592.place(x=140,y=70,width=70,height=25)

        GLineEdit_871=tk.Entry(root)
        GLineEdit_871["bg"] = "#ffffff"
        GLineEdit_871["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_871["font"] = ft
        GLineEdit_871["fg"] = "#333333"
        GLineEdit_871["justify"] = "center"
        GLineEdit_871["textvariable"] = num2
        GLineEdit_871.place(x=200,y=70,width=70,height=25)

        GButton_522=tk.Button(root)
        GButton_522["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_522["font"] = ft
        GButton_522["fg"] = "#000000"
        GButton_522["justify"] = "center"
        GButton_522["text"] = "+"
        GButton_522.place(x=290,y=70,width=70,height=25)
        GButton_522["command"] = self.GButton_522_command

        GLabel_959=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_959["font"] = ft
        GLabel_959["fg"] = "#333333"
        GLabel_959["justify"] = "center"
        GLabel_959["textvariable"] = self.result
        GLabel_959.place(x=360,y=70,width=70,height=25)
        return

# XXX
    def GButton_522_command(self):   
        self.result.set(self.num1.get() + self.num2.get())




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()



