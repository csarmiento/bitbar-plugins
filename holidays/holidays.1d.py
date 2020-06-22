#!/usr/bin/env python3

# <bitbar.title>Holidays Informer</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Camilo Sarmiento</bitbar.author>
# <bitbar.author.github>csarmiento</bitbar.author.github>
# <bitbar.desc>How many days left for next holiday</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

from datetime import date


def main():
    holiday_list = ['2020-01-01',
                    '2020-02-24', '2020-02-25',
                    '2020-03-23', '2020-03-24', '2020-03-31',
                    '2020-04-09', '2020-04-10',
                    '2020-05-01', '2020-05-25',
                    '2020-06-15',
                    '2020-07-09', '2020-07-10',
                    '2020-08-17',
                    '2020-10-12',
                    '2020-11-23',
                    '2020-12-07', '2020-12-08', '2020-12-24', '2020-12-25']

    holiday_dates = sorted([date(int(h.split('-')[0]), int(h.split('-')[1]), int(h.split('-')[2])) for h in holiday_list])
    today = date.today()
    i = 0

    while holiday_dates[i] < today and i < len(holiday_dates):
        i += 1

    print(':calendar::palm_tree:')
    print('---')
    if i < len(holiday_dates):
        days_left = (holiday_dates[i] - today).days
        suffix = get_suffix(days_left)

        print(f'{days_left} {day_or_days(days_left)} for next holiday {suffix}')
        print(f'Next holiday {holiday_dates[i]}')
    else:
        print(f'Holidays after {today} not found|color=red')


def day_or_days(days_left):
    if days_left == 1:
        day_or_days = 'day'
    else:
        day_or_days = 'days'
    return day_or_days


def get_suffix(days_left):
    if days_left < 5:
        suffix = ':sunglasses:|color=green'
    elif days_left < 10:
        suffix = ':expressionless:|color=orange'
    else:
        suffix = ':disappointed:|color=red'
    return suffix


main()
