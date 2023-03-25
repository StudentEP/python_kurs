operators = ['+', '-', '*', '/', '(', ')']
def rvp(infix):
    stack = []
    postfix = ""
    priority = {'+':1, '-':1, '*':2, '/':2}
    for c in infix:
        if c not in operators:
            postfix += c
        elif c=='(':
            stack.append(c)
        elif c==')':
            while len(stack)>0 and stack[-1]!='(':
                postfix += stack.pop()
            stack.pop()
        else:
            while len(stack)>0 and stack[-1]!='(' and priority[c]<=priority[stack[-1]]:
                postfix += stack.pop()
            stack.append(c)
    while len(stack)>0:
        postfix += stack.pop()
    return postfix

def solve(postfix):
    stack=[]
    for c in postfix.split():
        if c not in operators:
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()
            if c=="+":
                stack.append(right+left)
            if c=="-":
                stack.append(left-right)
            if c=="*":
                stack.append(right*left)
            if c=="/":
                stack.append(left/right)
    return stack.pop()
