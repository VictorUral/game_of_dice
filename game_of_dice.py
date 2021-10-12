# Game of dice (Игра в кости)
# -*- coding: utf8 -*-

from random import randint, choice

def print_rules ():
	''' 
	DOCSTRING: Правила игры 
	INPUT: No input
	OUTPUT: Печататет правила игры
	'''
	print ('Правила игры. \nИгра продолжается пока один из игроков не набёрт 100 очков. \nИгрок может ходить не ограниченное колличество раз, накапливая очки за свой текщий ход, но если выпадет 1 то все накопленные очки згарают и ход переходит второму игроку. Так же игрок может остановится (пропустить ход) в любой момент передав ход второму игроку. \nКоманды в игре: ход -> бросить кубик, стоп -> пропустить ход/завершить текущий ход, правила -> посмотреть правила игры.')

def players_moves (check_player):
	'''
	DOCSTRING: Имитация броска кубика
	INPUT: Общие очки игрока
	OUTPUT: Общие очки игрока, заработанные или не заработанные за ход
	'''
	current_account = 0 # текущие очки игрока
	check_player = check_player # основные очки игрока
	while True:
		p_1 = input ('\nВведите команнду: ').lower() # запрос у игрока на ход
		if p_1 == 'ход':
			rand_num = randint (1, 6) # возвращает случайное число от 1 до 6 (имитация броска кубика)
			if rand_num == 1:
				print (f'Выпала {rand_num}. Вы пропускаете ход, а заработанные очки згарают.')
				current_account = 0 # заработанные очки за ход вычитаються (згарают) от основного счёта
				break
			else:
				print (f'Выпало: {rand_num}')
				current_account += rand_num # заработанные очки плюсуются к текущим очкам
				check_player += rand_num # также заработанные очки плюсуются к общему счёту
				print (f'Текщий счёт: {current_account}, общий счёт: {check_player}')
				if check_player >= 100:
					break
		elif p_1 == 'стоп':
			break
		elif p_1 == 'правила':
			print_rules ()
		else:
			print ('Это не по правилам игры.')
	return current_account
	
def robot_moves (check_player):
	''' Имитирует бросок кубика роботом '''
	num_robo_moves = randint (1, 18) # определяется сколько подряд робот делает ходов
	flags = [True, False]
	flag = choice (flags) # для реализации выбора роботом, либо он делает все ходы, либо на случайном ходе делает "стоп"
	if flag: # если True то робот сделает все ходы
		current_account = 0
		check_player = check_player
		while num_robo_moves != 0:
			rand_num = randint (1, 6)
			if rand_num == 1:
				print (f'Робот выбросил: {rand_num}')
				current_account = 0
				num_robo_moves = 0
				break
			else:
				print (f'Робот выбросил: {rand_num}')
				current_account += rand_num
				check_player += rand_num
				print (f'Текщий счёт: {current_account}, общий счёт: {check_player}')
				num_robo_moves -= 1
				if check_player >= 100:
					break
		return current_account
	else: # иначе робот на случайных ходах сделает команду 'стоп'
		stop_robo_moves = [] # список со случайными ходами робота на которых он будет делать команду "стоп"
		if num_robo_moves >= 10: # если робот будет делать больше 10 ходов то случайно выбирается 5 ходов и добовляются в список
			for x in range (5):
				n = randint (1, num_robo_moves)
				stop_robo_moves.append (n)
		else: # в остальных случаях выбирается 3 хода
			for x in range (3):
				n = randint (1, num_robo_moves)
				stop_robo_moves.append (n)
		robo_stop = choice (stop_robo_moves) # выбираем из списка случайных ходов робота одно число на котором он сделает 'стоп'
		current_account = 0
		check_player = check_player
		while num_robo_moves != 0:
			if num_robo_moves == robo_stop:
				print ('Robo 3000 пропускает ход')
				break
			rand_num = randint (1, 6)
			if rand_num == 1:
				current_account = 0
				num_robo_moves = 0
				break
			else:
				print (f'Робот выбросил: {rand_num}')
				current_account += rand_num
				check_player += rand_num
				print (f'Текщий счёт: {current_account}, общий счёт: {check_player}')
				num_robo_moves -= 1
				if check_player >= 100:
					break
		return current_account

def players_name (number_players):
	''' Принимает колличество игроков, возвращает спсиок с именами игроков '''
	if number_players == 1:
		players_list = ['Robo 3000',]
		player_name = input (f'\nВведите имя игрока: ')
		if not player_name.strip ():
			players_list.append ('Player')
		else:
			players_list.append (player_name)
	else:
		a = number_players
		x = 0 # счётчик для порядка запроса имен у игроков
		players_list = [] # список с именами игроков
		no_name_players = 0 # счетчик для игроков которые не ввели имя
		while a != 0:
			x += 1
			player_name = input (f'\nВведите имя {x}-го игрока: ')
			if not player_name.strip (): # если ничего не введено или введены одни пробелы
				no_name_players += 1
				players_list.append ('Player ' + str(no_name_players))
				a -= 1
			else:
				players_list.append (player_name)
				a -= 1
	return players_list
	
def players_points (players_list):
	''' Принимает список с именами игроков, возвращает словарь: ключи - имена игроков, значения - счёт игроков '''
	points_list = {}
	for x in players_list:
		points_list[x] = 0
	return points_list

while True:
	question_num_players = int(input ('Введите количество игрков: '))
	if question_num_players == 1:
		number_players = question_num_players
		print_rules ()
		print ('\nВашим соперником будет: Robo 3000') # уже извтсно, что реальный игрок один и игра будет проходить между двумя игроками
		players = players_name (number_players) # в спике два игрока робот и реальный игрок
		players_score = players_points (players)
		random_player = choice (players)
		index_current_player = players.index (random_player)
		while True:
			if players[index_current_player] == 'Robo 3000': # изначально известно, что один игрок это робот
				print (f'\nХодит: {players[index_current_player]}, общий счёт: {players_score[players[index_current_player]]}')
				point = robot_moves (players_score[players[index_current_player]])
				players_score[players[index_current_player]] += point
				if players_score[players[index_current_player]] >= 100:
					print (f'\n\t\tПОРАЖЕНИЕ\n{players[index_current_player]} выиграл с общим счётом: {players_score[players[index_current_player]]}')
					break
				index_current_player = 1
			else:
				print (f'\nХодит: {players[index_current_player]}, общий счёт: {players_score[players[index_current_player]]}')
				point = players_moves (players_score[players[index_current_player]])
				players_score[players[index_current_player]] += point
				if players_score[players[index_current_player]] >= 100:
					print (f'\n\t\tПОБЕДА\n{players[index_current_player]} выиграл с общим счётом: {players_score[players[index_current_player]]}')
					break
				index_current_player = 0
		break
	elif question_num_players > 1:
		number_players = question_num_players
		print_rules ()
		players = players_name (number_players)
		players_score = players_points (players)
		random_player = choice (players) # случайный выбор игрока, который будет ходить первым
		index_current_player = players.index (random_player) # получаем индекс из списка с игроками который указывает на имя игрока, далее будет использован для реализации поочередности хода между игроками
		while True:
			print (f'\nХодит игрок: {players[index_current_player]}, общий счёт: {players_score[players[index_current_player]]}')
			point = players_moves (players_score[players[index_current_player]])
			players_score[players[index_current_player]] += point
			if players_score[players[index_current_player]] >= 100:
				print (f'\n\t\tПОБЕДА\nИгрок {players[index_current_player]} выиграл с общим счётом: {players_score[players[index_current_player]]}')
				break
			if index_current_player + 1 == len (players): # проверяем если индекс достиг конца списка с игроками
				index_current_player = 0 # то приравниваем его к 0 и ходит начинает первый игрок по списку
			else: # если нет 
				index_current_player += 1 # то прибавляем еденицу и ход переходит к следующему игроку в списке
		break
	else:
		print ('Такого варинта нет.')
		
		
