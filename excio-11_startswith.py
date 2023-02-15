hour=str(input("you've just finished the morning routine, what time is it? "))
if hour.startswith('5') or hour.startswith('6') or hour.startswith('7') and hour.endswith(':00'):
    print('leave home and walk to the bus stop')
else:
    print('call an uber')
