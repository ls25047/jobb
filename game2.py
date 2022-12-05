x, y = (0, 0)
print('''введите направление движения и количество шагов на которое должен переместиться персонаж Клоун
Ввод данных производится в формате: 
вверх
5
вниз
6
влево
8
вправо
10''')
while True == True:
    if input('''нажмите любую кнопку чтобы продолжить игру
введите stop для выхода из игры: 
''') == 'stop':
        break
    else:
        napravlenie = str(input('куда идти:'))
        step = int(input('на сколько шагов:'))
        if napravlenie == 'вверх':
            y += step
            print(f'вы находитесь здесь:{x, y}')
        elif napravlenie == 'вниз':
            y -= step
            print(f'вы находитесь здесь:{x, y}')
        elif napravlenie == 'вправо':
            x += step
            print(f'вы находитесь здесь:{x, y}')
        elif napravlenie == 'влево':
            x -= step
            print(f'вы находитесь здесь:{x, y}')

        