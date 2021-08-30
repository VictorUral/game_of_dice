# Game of dice (Игра в кости)
# -*- coding: utf8 -*-

from random import randint, choice

def rules_game ():
	''' 
	DOCSTRING: Правила игры 
	INPUT: No input
	OUTPUT: Печататет правила игры
	'''
	print ('\nПрвила игры. \nИгра продолжается пока один из игроков не набёрт 100 очков. \nИгрок может ходить не ограниченное колличество раз, накапливая очки за свой текщий ход, но если выпадет 1 то все накопленные очки згарают и ход переходит второму игроку. Так же игрок может остановится (пропустить ход) в любой момент передав ход второму игроку. \nКоманды в игре: ход -> бросить кубик, стоп -> пропустить ход/завершить текущий ход, правила -> посмотреть правила игры.')

def players_moves (name_player, check_player):
	'''
	DOCSTRING: Имитация броска кубика
	INPUT: Имя игрока и общие очки игрока
	OUTPUT: Общие очки игрока, заработанные или не заработанные за ход
	'''
	current_account = 0 # текущие очки игрока
	check_player = check_player # основные очки игрока
	while True:
		p_1 = input ('Введите команнду: ')
		p_1.lower ()
		if p_1 == 'ход':
			rand_num = randint (1, 6) # возвращает случайное число от 1 до 6 (имитация броска кубика)
			if rand_num == 1:
				print (f'Выпала {rand_num}. Вы пропускаете ход, а заработанные очки згарают.')
				check_player -= current_account # заработанные очки за ход вычитаються (згарают) от основного счёта
				break
			else:
				print (f'Выпало: {rand_num}')
				current_account += rand_num # заработанные очки плюсуются к текущим очкам
				check_player += rand_num # также заработанные очки плюсуются к общему счёту
				print (f'Текщий счёт: {current_account}, общий счёт: {check_player}')
				if check_player == 100 or check_player > 100:
					break
		elif p_1 == 'стоп':
			break
		elif p_1 == 'правила':
			print (rules_game ())
		else:
			print ('Это не по правилам игры.')
	return check_player
				
p_1 = input ('Введите имя первого игрока: ')
if p_1 == '':
	p_1 = 'Player 1'
	
p_2 = input ('Введите имя второго игрока: ')
if p_2 == '':
	p_2 = 'Player 2'
	
check_player_1 = 0
check_player_2 = 0

rules_game ()

flags = [True, False]
flag = choice (flags) # случайный выбор игрока, который первым будет ходить
while True:
	if flag == True:
		print (f'\nХодит игрок: {p_1}, общий счёт: {check_player_1}')
		point = players_moves (p_1, check_player_1)
		check_player_1 = point
		if check_player_1 == 100 or check_player_1 > 100:
			print (f'\n\t\tПОБЕДА\nИгрок {p_1} выиграл с общим счётом: {check_player_1}')
			break
		flag = False
	elif flag == False:
		print (f'\nХодит игрок: {p_2}, общий счёт: {check_player_2}')
		point = players_moves (p_2, check_player_2)
		check_player_2 = point
		if check_player_2 == 100 or check_player_2 > 100:
			print (f'\n\t\tПОБЕДА\nИгрок {p_2} выиграл с общим счётом: {check_player_2}')
			break
		flag = True
		
