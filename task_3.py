print('Задача 3. Следим за зубами')
print('')
# Стоматолог посоветовал Маше использовать зубную нить каждый чётный день.
# Чтобы не забывать, Маша написала скрипт на Python,
# который в случае чего напоминает ей про совет стоматолога.
# Напишите программу, которая проверяет, чётное ли число ввёл пользователь,
# и выводит соответствующее сообщение.
# Подсказка: для проверки чётности используйте оператор %.

number = int(input('Введите число '))
if number % 2 == 0:
  print('Сегодня нужно использовать зубную нить')
else:
  print('Расслабся и забудь про стоматолога))')
