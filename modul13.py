count_tickets = int(input('Сколько билетов вы хотите приобрести на мероприятие? '))
price_order = 0
for i in range(count_tickets):
    i += 1
    age_for_ticket = int(input(f'Для какого возраста билет №{i}? '))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        price_order += 990
        print('Стоимость билета: 990 руб.')
    else:
        price_order += 1390
        print('Стоимость билета: 1390 руб.')

if count_tickets > 3:
    price_order = price_order - price_order * 0.1
    print(f'Сумма к оплате {price_order} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-и человек')
else:
    print(f'Сумма к оплате {price_order} руб.')

