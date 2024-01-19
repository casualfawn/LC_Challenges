s = '())[]{}}'
charmap = {')':'(', ']':'[', '}':'{'}
stack = []
for closedp in s:
    print(res)
    if closedp in charmap:
        if stack and stack[-1] == charmap[closedp]:
            stack.pop()
        else:
            res = 'false'
    else:
        stack.append(closedp)
if not stack:
    res = 'true'
else:
    res = 'false'


