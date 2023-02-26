class Person():
    def __init__(self,name):
        self.name = name
        print(f'Hi, {name}!')
person1 = Person('Pam')

print('hi, your name is {}'.format(person1.name))