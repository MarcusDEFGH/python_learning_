import random

cafe = ['cuscuz croc', 'ovo croc', 'papa', 'vitamina mamao', 'vitamina banana', 'panqueca', 'pao com ovo']
lanche_manha = ['choco 70% ', 'paçoca', 'suco verde', 'fruta', 'banana c/ granola']
almoco = ['macarrao+frango', 'pure', 'papa', 'crepioca', 'feijao e arroz', 'escondidinho']
lanche_tarde = ["vitam ban/mam", "fruta c/ acomp", "yopro c/ acomp", "beb whey c/acomp", "overnight oats", "panqueca geleia"]
jantar  = ['cuscuz c/ ovo', 'bolinho batata airfryer', 'tapioca', 'papa', 'sanduiche']

refeicoes_do_dia = {'C': cafe, 'LM': lanche_manha, 'A': almoco, 'LT': lanche_tarde, 'J': jantar}
dias_semana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

menu_semana = []
menu_dia = []
#https://datatofish.com/dictionary-values-as-list/
# codigos = list(refeicoes_dia.keys())


#consegui. a iteração desejada na ordem certa.
for dia in dias_semana:
    menu_dia.append(f'{dia}:'.upper())
    for cod in refeicoes_do_dia.keys():
        menu_dia.append(f'{cod}:')
        for refeicao in refeicoes_do_dia.values():
            refeicao_sorteada = random.sample(refeicao, 1)
        menu_dia.append(refeicao_sorteada)


print(menu_dia)



    # print(
    #     f'\033[94m{dia}\033[m:')
    # for a in range(5):
    #         print(f'{menu_dia[a]}')
    # print(f'\033[7;93m---------{dia}\033[m:\n   {menu_dia[0]},{menu_dia[1]},{menu_dia[2]},{menu_dia[3]},{menu_dia[4]}')
    #
    # for refeicao in range(0,6):
    #     for codigo in refeicoes_dia.keys():
    #         print(f'{codigo}: {menu_dia[refeicao]}')
    #         refeicao += 1



    #tentando mesmo resultado através de  list comprehension: e com for loop pra essa parte de 'pegar' só o item str
    # (formatado bonitinho, sem " ou [ de cada refeiçao?


# menu = [
#     f'{dia}: {random.sample(ref, 1)}' for dia in dias_semana for ref in refeicoes_dia.values()
#         ]


# print(menu)
    # for ref in refeicoes_dia:
    #     ref_sorteada = random.sample(ref, 1)[0]
    #     menu_dia.append(ref_sorteada)

    # print(
    #     f'\033[94m{dia}\033[m:')
    # for a in range(5):
    #         print(f'{menu_dia[a]}')
#adicionar a regra: se papa de aveia aparecer como prato do cafe da manhã, nao pode aparecer de novo como jantar


#           1   ----------------------------------------------------------------TENTATIVAS ANTERIORES------------------
# cardapio_dia = [(C,LM,AL,LT,J) for C in cafe for LM in lanche_manha for AL in almoco for LT in lanche_tarde for J in jantar]
# print(cardapio_dia)

# for dia in dias_semana:
#     for i in range(5):
#         for ref in refeicoes_dia:
#             menu_dia = f'{dia}: {random.sample(ref,5)}'
#     print(menu_dia)
#           2   --------------------------------------------------------
# funcionou o cód abaixo, mas retorna sequencia de ref de cada um dos 5 tipos, se segunda ate domingo,
# e não o menu c lista com 1 de cada tipo por dia da semana:

# for ref in refeicoes_dia:
#     for dia in dias_semana:
#         print(f'{dia}: {random.sample(ref, 1)}')
# print(card_dia)
#             3--------------------------------------------------------
# for dia_semana in range(7):
#     for refeicao in refeicoes_dia:
#         card_dia.append(random.sample(refeicao,1))
# print(card_dia)
        # print(refeicao)
    #     cardapio_semana = random.sample(refeicao, 5)
    #
    # print(cardapio_semana)