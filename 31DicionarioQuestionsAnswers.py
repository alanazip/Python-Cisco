perguntas = {
    'pergunta1' : {
        'pergunta' : 'quanto é 2+2? ',
        'respostas': { 
            'a' : '1',
            'b' : '4',
            'c' : '5',
            },
            'resposta_certa' : 'b',
    },
    'pergunta2' : {
        'pergunta' : 'quanto é 3*2? ',
        'respostas': { 
            'a' : '4',
            'b' : '10',
            'c' : '6'},
            'resposta_certa' : 'c',
    },
}
print()

respostasCertas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for rk, rv in pv["respostas"].items():
        print(f'[{rk}] : {rv}')


    respostaUsuario = input('Sua resposta: ')

    if respostaUsuario == pv['resposta_certa']:
        print("acertou miseravi")
        respostasCertas += 1
    else:
        print('errou')

    print()

qtdperguntas = len(perguntas)
porcentagemAcerto = respostasCertas / qtdperguntas * 100

print(f'você acertou {respostasCertas} perguntas')
print(f'sua porcentagem de acerto foi de {porcentagemAcerto} %')
