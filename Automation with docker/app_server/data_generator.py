import random
import datetime

# create a list of random characters
def random_characters(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))

# create a random date between 1/1/2000 and 08/04/2022
def random_date():
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2022, 8, 4)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

# create a random length between 1 and 100
def random_length():
    return random.randint(1,100)


# create a random line of data
def random_line():
    return f'{random_date()},{random_characters(random_length())}'

# create a file with one million lines of data
def create_file():
    with open('sample_data.csv', 'w') as f:
        for i in range(1000000):
            f.write(f'{i},{random_line()}\n')

create_file()