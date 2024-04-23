class caesar_encrypt():
    def __init__(self):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = lower.upper()
        chars = input(("input a alphabet: "))
        self.lower = lower
        self.upper = upper
        self.chars = chars


    def process(self):
        if self.chars.isalpha() == True:
            if self.chars.islower() == True:        
                a = self.lower.index(self.chars)
                if a == 23 or a == 24 or a == 25:
                    print(self.lower[a+3-26])
                else:
                    print(self.lower[a+3])
            else:
                a = self.upper.index(self.chars)
                if a == 23 or a == 24 or a == 25:
                    print(self.upper[a+3-26])
                else:
                    print(self.upper[a+3])
        else:
            print("plz input a alphabet")

a=caesar_encrypt()
caesar_encrypt.process(a)