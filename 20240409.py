import logging
import numbers  


#1
def state():
    arg = 0

    while arg != "exit":
        arg = str(input())
        if arg == "1":
            print("one")       
        elif arg == "2":
            print("two")            
        elif arg == "3":
            print("three")
        elif arg == "exit":
            break
        else:
            print("unknow")


#state()












#2 try to use array
def state2():
    arg = {"1":"one","2":"two","3":"three"}
    question = "0"
    while question != "exit":
        question = str(input())
        if question in arg.keys():
            print(arg[question])
        elif question != arg.keys():
            print("unknow")

#state2()











#3 using class
class main:
    def state2():
        arg = {"1":"one","2":"two","3":"three"}
        question = "0"
        while question != "exit":
            question = str(input())
            if question in arg.keys():
                print(arg[question])
            elif question != arg.keys():
                print("unknow")

main.state2()


20240415
#1 Profitability Ratios
#Gross profit/Sale x 100%
#Profitability Ratio

def gross_profit_ratio(gross_profit, sales):
    return gross_profit / sales *.001

def net_profit_ratio(net_profit, sales):
    return net_profit / sales *.001

def return_on_owners_equity(net_profit, tax, ordinary_share_capital, reserves):
    (net_profit - tax) / (ordinary_share_capital + reserves) * .001
    return 
    
#2 Liquidity Ratio

def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities * .001

def quick_ratio(current_assets, prepaid_expenses,inventory, current_liabilities):
    return (current_assets-inventory-prepaid_expenses)/current_liabilities

#3 effciency ratios

def inventory_turnover_ratio(cost_of_goods_sold,average_stock):
    return cost_of_goods_sold/average_stock

def debtors_collection_period(trade_receivables, sales):
    return trade_receivables / sales * 365

def creditors_payment_period(trade_payables, purchase):
    return trade_payables / purchase * 365

def sales_to_capital_employed(sales, Capital):
    return sales/ Capital

















'''
from data_chart_of_acc import account_list

def auto_input():
    a = len(account_list)
    for x in a:




while True:
        input_account_num = input("account num:")

        if input_account_num.lower() == "done":
            break
        elif input_account_num.lower() == "delete":
            input_delete = input("delete account #:")
            del account_list[input_delete]
            print(f"deleted account:{input_delete}")
            continue
        else:  
            input_account_name = str(input("account name:"))
            account_list[input_account_num] = input_account_name
    print("=== program close! ===")
    print(account_list)
'''
#a = auto_input()

