import argparse
import datetime
import math


def esc(code):
    return f'\033[{code}m'


def write_db(name, data):
    print(name, data, 'Added')


def age_calc(pet_age):
    age_table = [12, 10, 9, 8, 7, 7, 7, 7, 6.5, 6.5, 6.3, 6.2, 6.0, 5.8, 5.6]

    if pet_age < 0.5:
        k = 7
    elif 0.5 <= pet_age < 0.66:
        k = 10
    elif 0.66 <= pet_age < 1:
        k = 12.5
    elif 1 <= pet_age < 1.5:
        k = 14
    elif pet_age == 1.5:
        k = 13.3
    elif 1.5 < pet_age < 2:
        k = 12
    elif pet_age > 16:
        k = 4.8
    else:
        tmp_age = round(pet_age)
        k = age_table[tmp_age - 2]
    return k


def age_corrector(age, d_size):
    cor_table = [[15, 15, 14, 14],
                 [23, 24, 22, 20],
                 [28, 29, 29, 28],
                 [32, 34, 34, 35],
                 [36, 37, 40, 42],
                 [40, 42, 45, 49],
                 [44, 47, 50, 56],
                 [48, 51, 55, 64],
                 [52, 56, 61, 71],
                 [56, 60, 66, 78],
                 [60, 65, 72, 86],
                 [64, 69, 77, 93],
                 [68, 74, 82, 101],
                 [72, 78, 88, 108],
                 [76, 83, 93, 115],
                 [80, 88, 98, 122]
                 ]
    return cor_table[age - 1][d_size - 1]


today = datetime.date.today()

print(esc('32;3;1') + 'DOG TO HUMAN AGE CONVERTER V1.0 Written by D.Morozov / Spain 2019 (C)')
print('Hi! Today is : ', today, esc(0), end='\n\n')
while True:
    dogs_birthday = None
    dog_name = input('Enter your dog name -> ')
    if not dog_name or dog_name == '':
        dog_name = 'Unknow'
        print('You have to input correct name to add it to Database next time ... ')
    try:
        dog_size = int(
            input('Enter the size fo your dog 1-4 ( 1 <=10 kg, 10 < 2 < 20kg, 20 <= 3 < 50kg, 4 > 50 kg ) -> '))
        if dog_size not in (1, 2, 3, 4):
            raise ValueError

        if input('Do you know exactly your pets birthday date ? y/n -> ') in ('y', 'Y', 'д', 'Д'):
            year, month, day = map(int,
                                   (input('Enter your dogs Birthday date in format Year-month-day -> ').split('-')))
            dogs_birthday = datetime.date(year, month, day)
            dog_age = (today.month - dogs_birthday.month + 12 * (today.year - dogs_birthday.year)) / 12.0
        else:
            dog_age = float(input('Enter your dogs age in dogs years -> '))
            dogs_birthday = datetime.date(datetime.date.today().year - round(dog_age), 1, 1)
            print("Warning! You don't specify full date of  birthday - only the year will be saved !")

        print('Dog {} : is {} year(s) old'.format(dog_name, dog_age))
        print('K = {}'.format(age_calc(dog_age)))
        print(esc('32;3;1') + f'Age of {dog_name} in human equivalent is: {(round(dog_age * age_calc(dog_age)))}'
                              f' year(s)' + esc(0))
        if round(dog_age) <= 16:
            print('Age with correction * ( It means that using size and weight of your pet ) : {}'.format(
                age_corrector(round(dog_age), dog_size)))
        else:
            print('Age correction function inaccessible for your dog age , sorry...')
        if input('Do you want to add it to database ? y/n ') in ('y', 'Y', 'д', 'Д'):
            write_db(dog_name, dogs_birthday)

    except ValueError:
        print(esc('31:1:4') + 'Enter correct value ! ' + esc(0))

    if input('Do you like to try with other dog :) y/n -> ') not in ('y', 'Y', 'д', 'Д'):
        break

print(esc('35;3;1') + 'Good luck!' + esc(0))
