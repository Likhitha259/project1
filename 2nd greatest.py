a=eval(input('enter the 1st number :'))
b=eval(input('enter the 2nd number :'))
c=eval(input('enter the 3rd number :'))
d=eval(input('enter the 4th number :'))
if a>b and a>c and a>d: # a is greatest
    if b>c and b>d:
        print(f'{b} is 2nd greatest number')
    elif c>b and c>d:
        print(f'{c} is 2 nd greatest number')
    elif d>b and d>c:
        print(f'{d} is 2nd greatest number')
elif b>a and b>c and b>d: # b is greatest
    if a>c and a>d:
        print(f"{a} is 2nd greatest number")
    elif c>a and c>d:
        print(f'{c} is 2 nd greatest number')
    elif d>a and d>c:
        print(f'{d} is 2nd greatest number')
elif c>a and c>b and c>d: # c is greatest
    if a>b and a>d:
        print(f"{a} is 2nd greatest number")
    elif b>a and b>d:
        print(f'{b} is 2 nd greatest number')
    elif d>a and d>b:
        print(f'{d} is 2nd greatest number')
else:  #d>a and d>b and d>c ,,d is greatest
    if a>b and a>c:
        print(f'{a} is 2nd greatest number')
    elif b>a and b>c:
        print(f'{b} is 2 nd greatest number')
    elif c>b and c>a:
        print(f'{c} is 2nd greatest number')