import datetime

def print_header():
    print('--------------------')
    print('    BIRTHDAY APP    ')
    print('--------------------')


def get_birthday_from_user():
    print('When were you born? ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    bday = datetime.date(year=year, month=month, day=day)
    return bday


def compute_days_between_dates(bday, today):
    bday_this_year = datetime.date(today.year, bday.month, bday.day)
    delta = bday_this_year - today
    return delta.days


def print_birthday_info(days):
    if days < 0:
        print('Your birthday {} day(s) ago', format(-days))
    elif days > 0:
        print('Your birthday is coming up in {} day(s)', format(days))
    else:
        print('HAPPY BIRTHDAY!!')


def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.date.today()
    num_of_days = compute_days_between_dates(bday, now)
    print_birthday_info(num_of_days)

main()