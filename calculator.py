'''
支持加减乘除四则运算计算器
'''

while True:
    a = input("Enter a number or 'q' to quit:")
    if a.lower()=='q':
        break
    b = input("Enter an another or 'q' to quit:")
    if b.lower()=='q':
        break

    print('a + b =',int(a)+int(b))
    print('a - b =',int(a)-int(b))
    print('a * b =',int(a)*int(b))
    print('a / b =',int(a)/int(b))
    
