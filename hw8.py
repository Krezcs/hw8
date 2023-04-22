import datetime

def get_birthdays(users):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthdays = {weekday: [] for weekday in weekdays}
    today = datetime.date.today()
    if today.weekday() == 0:  
        today = today - datetime.timedelta(days=2)
    for user in users:
        birthday = user['birthday']
        if birthday.weekday() in [5, 6]:  
            birthday = birthday + datetime.timedelta(days=7 - birthday.weekday())  
        if today.weekday() == 0 and birthday.weekday() in [5, 6]:  
            birthday = birthday - datetime.timedelta(days=2) 
        birthday_day_of_week = birthday.strftime('%A')
        birthdays[birthday_day_of_week].append(user)
    return birthdays

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
    {'name': 'Sophie', 'birthday': datetime.date(1999, 9, 20)},
    {'name': 'Jacob', 'birthday': datetime.date(1996, 6, 18)},
    {'name': 'Grace', 'birthday': datetime.date(1989, 4, 5)},
    {'name': 'William', 'birthday': datetime.date(1992, 1, 30)},
    {'name': 'Lily', 'birthday': datetime.date(1997, 8, 7)},
    {'name': 'Ryan', 'birthday': datetime.date(1987, 11, 10)},
    {'name': 'Ava', 'birthday': datetime.date(1993, 3, 12)},
    {'name': 'Ethan', 'birthday': datetime.date(1995, 10, 1)},
    {'name': 'Mia', 'birthday': datetime.date(1998, 7, 22)},
    {'name': 'Andrew', 'birthday': datetime.date(1990, 2, 15)},
]

birthdays = get_birthdays(users)
for weekday, users in birthdays.items():
    print(f"{weekday}: {', '.join([user['name'] for user in users])}")

print('Saturday : should be greeted on next Monday')
print('Sunday : should be greeted on next Monday')
