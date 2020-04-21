from DS.stacks.stack import Stack

def parentheses_check(exp):
    s = Stack()
    flag = True
    for item in exp:
        if item == '(' or item == '{' or item == '[':
            s.push(item)
        elif item == ')' or item == '}' or item == ']':
            if s.top == -1:
                flag = False
            else:
                temp = s.pop()
                if ((item == ')') and (temp == '{' or temp == '[')) or ((item == '}') and (temp == '[' or temp == '(')) or ((item == ']') and (temp == '(' or temp == '{')):
                    flag = False
    
    if s.top >= 0:
        flag = False
    if flag == True:
        print("Valid Expression")
    else:
        print("Invalid Expression")
        



