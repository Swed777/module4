print('Задача 6. Игра в кубики')
print()
# Костя играет в азартную игру с кубиками с владельцем заведения.
# Правда, с довольно интересными правилами:
# если у Кости на кубике выпадет столько же или больше, чем у владельца,
# то Костя задолжает разность в тысячах долларов.
# Однако если выпадет меньше,
# то Косте выплатят столько тысяч долларов, сколько будет в сумме очков на кубиках.
 
# На вход в программу подаётся два числа.
# Если первое число больше либо равно второму,
# нужно вывести на экран их разность и отдельной строкой фразу: «Костя платит».
# В противном случае вывести их сумму и отдельной строкой — фразу: «Владелец платит».
# Также последней строкой в результате нужно вывести на экран фразу: «Игра окончена».

# Пример:
# Кубик Кости: 3
# Кубик владельца: 4
# Сумма: 7
# Владелец платит
# Игра окончена

cub_kostya = int(input('Кубик Кости:    '))
cub_boss   = int(input('Кубик Владельца:'))
if cub_kostya >= cub_boss:
  print('Разность = ', (cub_kostya - cub_boss)*1000, '$')
  print('Костя платит')
else:
  print('Сумма =', (cub_kostya + cub_boss)*1000, '$')
  print('Владелец платит')
print('Игра окончена')