even_numbers = [n for n in range(20) if n % 2 == 0]
print(even_numbers)

evens_string = ''.join(str(e) for e in even_numbers)
print(evens_string)
evens_int = int(evens_string)
print(evens_int)