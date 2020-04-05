# parenthesis
# Example: a+(b*c)-2-a (a+b*(2-c)-2+a)*2 (a*b-(2+c) 2*(3-a)) )3+b*(2-c)(

def isBalanced (exp):
    stack = []
    wrong = False

    for i in range(0, len(exp)):

        if exp[i] == "(":
            stack.append(exp[i])

        elif exp[i] == ")":
            if stack != []: stack.pop() # if stack isn't empty, pop
            else: wrong = True # if stack is already empty

    if stack == [] and wrong == False: return True
    else: return False 

def main ():
    while True:
        try:
            exp = input()

            if isBalanced(exp) == True: print ("correct")
            else: print ("incorrect")
        except EOFError:
            break

main()