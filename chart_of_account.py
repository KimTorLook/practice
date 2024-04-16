
def auto_input():
    account_list={}

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

a = auto_input()
