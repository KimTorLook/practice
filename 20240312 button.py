import tkinter as tk
import tkinter.font as tkFont

class App:
    def draw(self):  
        self.btnClickMe=tk.Button(self.root)
        self.btnClickMe["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.btnClickMe["font"] = ft
        self.btnClickMe["fg"] = "#000000"
        self.btnClickMe["justify"] = "center"
        self.btnClickMe["text"] = "click me"
        self.btnClickMe.place(x=240,y=280,width=70,height=25)
        self.btnClickMe["command"] = self.btnClickMe_command

        self.btnClickYou=tk.Button(self.root)
        self.btnClickYou["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.btnClickYou["font"] = ft
        self.btnClickYou["fg"] = "#000000"
        self.btnClickYou["justify"] = "center"
        self.btnClickYou["text"] = "click you"
        self.btnClickYou.place(x=240,y=170,width=70,height=25)
        self.btnClickYou["command"] = self.btnClickYou_command

    def __init__(self, root):
        self.root=root
        #setting title
        self.root.title("exercise")
        #setting window size
        width=600
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.root.after(2000, self.draw)
        self.draw()
        self.root.mainloop()

    def btnClickMe_command(self):
        print("me")


    def btnClickYou_command(self):
        print("you")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
