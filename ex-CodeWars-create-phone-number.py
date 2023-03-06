def create_phone_number():
    given_sequence = input("Insert the digits of your phone number")
    phone_number = (f'({given_sequence[0:3]}) {given_sequence[3:6]}-{given_sequence[6:10]}')
    print(phone_number)
create_phone_number()

# 2nd way, not requiring user input
import random

array_list = []
def create_phone_number():
    for n in range(0,10):
        nn = random.randint(0,9)
        array_list.append(nn)
        str_sequence = ''.join(str(e) for e in array_list)
    print(f'\033[1;35m({str_sequence[0:3]}) {str_sequence[3:6]}-{str_sequence[6:10]}\033[m')
create_phone_number()

#3rd way, now using list comprehension

def create_phone_number():
    array_list = [random.randint(0,9) for n in range(0,10)]
    str_sequence = ''.join(str(e) for e in array_list)
    print(f'({str_sequence[0:3]}) {str_sequence[3:6]}-{str_sequence[6:10]}')
create_phone_number()


