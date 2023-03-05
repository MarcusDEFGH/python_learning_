def create_phone_number():
    given_sequence = int(input("Insert the digits of your phone number"))
    phone_number = (f'({given_sequence[0:3]}) {given_sequence[3:6]}-{given_sequence[6:9]}')
    print(phone_number)
create_phone_number()

#to be revisited for fixing/correcting