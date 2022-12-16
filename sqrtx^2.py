import cmath, math 
a, b, c = (input('введите a: ')), (input('введите b: ')), (input('введите c: '))
if type(c) == complex or type(c) == complex or type(c) == complex: 
    if a != 0:
        d  = (b**2) - (4 * a * c)
    if d == 0:
        x = -b / (2 * a)
        print(f'единственным решением уравнения является :{x}')
    else:
        if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            print(f'{x1}= первый корень', f'{x2}= второй корень', sep='\n')
        elif d < 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            print(f'{x1}= первый корень', f'{x2}= второй корень', sep='\n')
else:
    print('''a = 0 !!!
    уравнение не является квадратным''')