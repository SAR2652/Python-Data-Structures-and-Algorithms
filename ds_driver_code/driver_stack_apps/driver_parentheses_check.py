from ds_apps.stack_apps.parentheses_check import parentheses_check

exp = input("Enter an expression : ")
exp = [elem for elem in list(exp) if elem.strip()]
parentheses_check(exp)