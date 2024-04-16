#20240411 ~ 13  

class main:
    def __init__(self) -> None:
        self.salaryList = []


    def salaryInput(self,salary) -> None:
        self.salaryList.append(salary)


    def sumation(self) -> int:
        return sum(self.salaryList)


    def average(self) -> float:
        return sum(self.salaryList)/len(self.salaryList)


    def salaryCalculation(self) -> None:
        x = 1
        while True:
            try:
                ask = input(f"請輸入第{x}筆薪水資料:")
                if ask.lower() == 'done' :
                    break
                salary =  int(ask)
                self.salaryInput(salary)
                print(f"總共獲得{self.sumation()}元，每月平均{self.average():.2f}元")
                x += 1                                      #counter 放入loop, 防止 valueError後仍然計數
            except ValueError:
                print(f"plz input Num.")
        print(f"{x-1}筆薪水，共獲得{self.sumation()}元，每月平均{self.average():.2f}元")
        print(f"每月薪水資料︰{self.salaryList}")
        print(f"- 計算完畢 -")

Jacky = main()
Jacky.salaryCalculation()

# 1st times use while True
# familiarly with class_veriable referencing 
# familiarly with class structure
# familiarly with array using
