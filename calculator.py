'''
支持加减乘除四则运算计算器
'''
def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

while True:
    a = input("Enter a number or 'q' to quit:")
    if a.lower()=='q':
        break
    b = input("Enter an another or 'q' to quit:")
    if b.lower()=='q':
        break

    try:
        a = int(a)
        b = int(b)
       
        print('a + b =',add(a,b))
        print('a - b =',substract(a,b))
        print('a * b =',multiply(a,b))
        print('a / b =',divide(a,b))
    except ValueError:
        print('Data convert Error !')
        continue
    except ZeroDivisionError:
        print('Zero division Error !')
        continue

    
