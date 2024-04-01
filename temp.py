'''
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
'''
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
'''

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



'''

