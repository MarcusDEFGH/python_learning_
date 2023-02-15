alt = float(input('digite sua altura em metros: '))
gen = input('digite seu gênero de nascimento (masculino ou feminino):')
peso_ideal_F = (alt * 62.1) - 44.7
peso_ideal_M = (alt * 72.7) - 58

if gen in ['f','F','fem','feminino','Feminino']:
    print(f'seu peso ideal é {peso_ideal_F:.2f}kg.')

elif gen in ('masculino','Masculino'):
    print(f'seu peso ideal é {peso_ideal_M:.2f}kg')
