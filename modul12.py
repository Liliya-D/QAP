per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму, которую планируете положить под проценты: '))
print('money = ', money)

deposit = list(map(int, [per_cent['ТКБ']*money/100, per_cent['СКБ']*money/100, per_cent['ВТБ']*money/100, per_cent['СБЕР']*money/100]))

print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))