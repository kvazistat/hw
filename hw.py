# -*- coding: utf-8 -*-
#кириллица в консоли (и powershell) Win10_en не работает
#будет и другая версия на русском
#Beware! Crappy english ^^

import sys

if sys.version_info[0] == 2:
	u_input = raw_input
else:
	u_input = input

question = [['The main enemy of the system administrator?', 'manager'], #матрица вопрос/ответ
 ['The worst CMS ever? (hint - from "yellow" company)', 'bitrix'],
 ['Adobe Flash is good or bad?', 'bad'],
 ['What is worse: 1c or perl?', '1c']]
num = ['First', 'Second', 'Third', 'Fourth'] #лист для красивого вывода вопросов
react = ['Damn, how do you do this?!! Next question!','2 of 2!','Rly?!','Aaaargh!'] #негодование по поводу правильного ответа

print('Do you wanna to play a game with me? [y/n]')
a = u_input()
i = ''

if not a == 'y': #нельзя просто так взять и не сыграть со мной в игру
	k = 0
	while not i == 'y':
		k += 1
		print('Wrong answer! (do you know right answer, yeah?)')
		i = u_input()
		if k >= 5:
			print('if you don\'t know the right answer, it\'s YES!')
			break

count = 0 #счетчик по которому выбираются вопросы/ответы
f_count = 0 #мой счет
r_count = 0 #счет игрока
#s = u_input('I\'ll be ask you a few questions and you should give me right answers, undestand? [y/n]\n')
#if s == 'y': хотел пошутить, но получилось скучно
print('So, let\'s start!')
while count < len(question):
		print('\n%s question is.. %s! \nPlease, type your answer, but think twice before writing!\n' % (num[count], question[count][0]))
		answer = u_input()
		if (answer == question[count][1]): #правильный ответ
		    print(react[count])
		    count += 1
		    r_count += 1
		elif (answer == 'quit'): #пропуск ответа
			count += 1
			print('+10 to me^^!\n')
			f_count += 10
		else: #неправильный ответ
			print('\nWrong! Again! Type "quit" if you give up!')
			f_count += 1	
#else:
#	print('You are very booring, bye!')

if f_count < r_count:
    print('\nThanks for playing! \nYour score: %s. My score: %s. Good joob, you win!' % (r_count, f_count))
elif (not f_count == 0):
	print('\nThanks for playing! \nYour score: %s. My score: %s. I\'m win! Don\'t worry^^' % (r_count, f_count))
raw_input('press any key to exit')