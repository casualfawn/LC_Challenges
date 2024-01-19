s = 'lee(t(c)o)de)'
stack = []
splt = list(s)

for i in range(len(s)):
    if s[i] == '(':
        if len(stack) > 0:
            stack.append(i)
    elif s[i] == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            splt[i] = ''

for i in stack:
    splt[i] = ''






