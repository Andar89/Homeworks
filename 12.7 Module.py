per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада:'))
deposit = [num * money/100 for num in list(map(float, per_cent.values()))]
print('Сумма, накопленная за год в каждом из банков: ', deposit)
deposit.sort()
print('Максимальная сумма, которую вы можете заработать - ', deposit[-1])
