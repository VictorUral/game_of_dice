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
	
number_players = 2 # по умолчанию равно два, возможно сделать по запросу от пользователя, тем самым переделав игру на "неограниченное" колличество игроков

def players_name (number_players):
	''' Принимает колличество игроков, возвращает спсиок с именами игроков '''
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

print_rules ()
players = players_name (number_players)
players_score = players_points (players)
random_player = choice (players) # случайный выбор игрока, который будет ходить первым
index_current_player = players.index (random_player)

while True:
	print (f'\nХодит игрок: {players[index_current_player]}, общий счёт: {players_score[players[index_current_player]]}')
	point = players_moves (players_score[players[index_current_player]])
	players_score[players[index_current_player]] += point
	if players_score[players[index_current_player]] >= 100:
		print (f'\n\t\tПОБЕДА\nИгрок {players[index_current_player]} выиграл с общим счётом: {players_score[players[index_current_player]]}')
		break
	if index_current_player + 1 == len (players):
		index_current_player = 0
	else:
		index_current_player += 1
		
		
