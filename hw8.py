import datetime

def get_birthdays_per_week(users):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthdays_per_week = {weekday: [] for weekday in weekdays}
    for user in users:
        birthday = user['birthday']
        if birthday.weekday() >= 5:  
            birthday = birthday + datetime.timedelta(days=7 - birthday.weekday())  
        birthday_day_of_week = birthday.strftime('%A')
        birthdays_per_week[birthday_day_of_week].append(user)
    return birthdays_per_week


users = [
    {'name': 'John', 'birthday': datetime.date(1995, 1, 15)},
    {'name': 'Jane', 'birthday': datetime.date(1987, 6, 25)},
    {'name': 'Bill', 'birthday': datetime.date(1990, 4, 25)},
    {'name': 'Kate', 'birthday': datetime.date(1998, 12, 7)},
    {'name': 'Tom', 'birthday': datetime.date(1985, 3, 10)},
    {'name': 'Sarah', 'birthday': datetime.date(2000, 7, 18)},
    {'name': 'Michael', 'birthday': datetime.date(1992, 9, 5)},
    {'name': 'Sophia', 'birthday': datetime.date(1988, 11, 30)},
    {'name': 'David', 'birthday': datetime.date(1997, 2, 22)},
    {'name': 'Olivia', 'birthday': datetime.date(1993, 10, 12)},
    {'name': 'James', 'birthday': datetime.date(1986, 8, 14)},
    {'name': 'Emma', 'birthday': datetime.date(1994, 5, 6)},
    {'name': 'Daniel', 'birthday': datetime.date(1991, 12, 25)},
]

birthdays = get_birthdays_per_week(users)
for weekday, users in birthdays.items():
    print(f"{weekday}: {', '.join([user['name'] for user in users])}")

print('Saturday : should be greeted on Monday')
print('Sunday : should be greeted on Monday')



