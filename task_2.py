print('Задача 2. Поступление')
print('')
# Степан хочет поступить на бюджет в престижный университет,
# но для этого ему нужно хорошо сдать три экзамена и набрать как минимум 270 баллов.
# Напишите программу,
# которая запрашивает у пользователя результаты ЕГЭ по трём экзаменам
# и проверяет, поступил он в институт или нет. 
# Выведите соответствующее сообщение.
 
# Пример:
# Введите кол-во баллов по русскому языку: 90
# Введите кол-во баллов по математике: 90
# Введите кол-во баллов по информатике: 90
# Поздравляю, ты поступил на бюджет!
 
# Пример 2:
# Введите кол-во баллов по русскому языку: 100
# Введите кол-во баллов по математике: 50
# Введите кол-во баллов по информатике: 70
# К сожалению, ты не прошёл на бюджет.

russan      = int(input('Введите количество баллов по русскому языку '))
mathematics = int(input('Введите количество баллов по математике     '))
inform      = int(input('Введите количество баллов по информатике    '))

if russan + mathematics + inform >= 270:
  print('Поздравляю, ты поступил на бюджет!')
else:
  print('К сожалению, ты не прошёл на бюджет.')