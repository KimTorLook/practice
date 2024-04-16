20240411

#用class 同 array 做翻釋

class derk:
    def derk():
        derk = ["one", "two", "three"]
        ask = 0
        while ask != "exit":
            ask = input("pls input:")
            if ask.isnumeric() == True:
                ask2 = int(ask)
                if ask2 > 0 and ask2 < 4:
                    print(derk[ask2-1])
                else:   
                    print("unknow")    
            else:
                print("unknow")
        print('program closed')

derk.derk()
