world  = {'sword' : 1.5, 'coin' : 0.5, 'torch' : 2.0, 'meat' : 1.0, 'bow' : 1.1, 'arrow' : 0.2}
inventory = dict(axe=5.0)
limit = 8.0

print('''В один из прекрасных дней вашей заурядной жизни вы решаете коардинально её изменить и отправляетесь 
навстречу приключениям. Так как решение судъбоносное, принимается оно резко и безповоротно. Вы выходите во двор выбиваете из колоды старый,
но крепко лежащий в руке топор и направляетесь в лес навстречу своей судъбе!
Вы уже час в пути. Пока эльфы и орки не спешат вторгнуться в вашу жизнь и сделать ее ход чуть короче, а вот желудок дает понять
что жизнь искателя приключений неплохо бы начать с приема пищи, а не с необдуманных импульсивных действий...
В воздухе витает запах дымы и жженой плоти... Вы воодушевились, неужели это варвары напали на ближайщее поселение и разорили его сожжа дотла все и вся !?
Вы осторожны как никогда прежде. Идете медленно и внимателно вслушиваетесь в каждый шорох.И вот обогнув очередной бурелом вы  
натыкаетесь на стоянку. Конечно не корабль варваров, но проделав долгий путь радость вызывает любой контент. Подождите... да это же настоящий геройский костер
со всеми подобающими атрибутами: вот вам и лук со стрелами, факел вымоченный в моче Антона .  ''')
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
