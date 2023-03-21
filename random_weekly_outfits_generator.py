import random


pecas_roupa = {
                'calca': ['preta wide', 'nude wide', 'verde petroleo'],
                'top': ['cropped branco', 'cropped nude', 'cropped preto', 'blusa vinho'],
                'sapato': ['chunky soles', 'sneakers', 'all star', 'air force']
               }

dias_semana = [
    'lunes', 'martes', 'miércoles', 'jueves', 'viernes'
                ]

for dia in dias_semana:
    outfit_dia = [f'{dia}:']
    # for tipo_peca in pecas_roupa.keys():
    #     outfit_dia.append(tipo_peca)
    for i in range(3):
        outfit_dia.append(f'{list(pecas_roupa.keys())[i].upper()}: {random.choice(list(pecas_roupa.values())[i])}    ')

    print(
        f'{outfit_dia[0]}\n {outfit_dia[2]}\n {outfit_dia[1]} {outfit_dia[3]}\n')

# next step: making the code more concise