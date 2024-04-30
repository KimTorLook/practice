class caesar_encrypt:
    def __init__(self, shift):
        self.shift = shift
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = self.lower.upper()
        self.other = " `0123456789-=~!@#$%^&*()_+,./<>?;':\"\[\]\{\}|"
        self.encrypted_message = []

    def encryption(self, msg):
        for char in msg:
            if char.islower():
                a = self.lower.index(char)
                b = (a + self.shift) % 26
                self.encrypted_message.append(self.lower[b])
            elif char.isupper():
                a = self.upper.index(char)
                b = (a + self.shift) % 26
                self.encrypted_message.append(self.upper[b])
            else:
                a = self.other.index(char)
                b = (a + self.shift) % 43
                self.encrypted_message.append(self.other[b])

        return self.encrypted_message

    def main(self):
        msg = input("please input a msg to encypte : ")
        while True:
            if msg.lower() == "exit":
                print("----------  Program closed!  ---------")
                break
            else:
                c = self.encryption(msg)
                print(f"encrypted message : {''.join(c)}")
                msg = input("please input a msg to encypte : ")


a = caesar_encrypt(3)
a.main() 