import datetime


def print_header():
    print('---------------------------------------------')
    print('                 HELLO WORLD')
    print('---------------------------------------------')
    print()


def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_info(number_of_days):
    if number_of_days < 0:
        print('Your birthday is in {} days!'.format(-number_of_days))
    elif number_of_days > 0:
        print('You had your birthday already this year! {} days ago'.format(
            number_of_days))
    else:
        print("Happy Birthday!")


def indentation_example():
    result = call_to_other_function()

    if result == 'Cool'
        return True


def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_info(number_of_days)


main()
