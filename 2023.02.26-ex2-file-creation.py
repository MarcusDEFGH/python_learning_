# https://www.geeksforgeeks.org/how-to-create-filename-containing-date-or-time-in-python/

from datetime import datetime

current_datetime = datetime.now()
print(f'Current date and time is \033[95m{current_datetime}')
str_current_datetime = str(current_datetime)[0:10]
print(str_current_datetime)

file_name = f'{str_current_datetime}.py'
file = open(file_name, 'w')

print(f'File \033[7;93m{file.name}\033[m created successfully')
file.close()

