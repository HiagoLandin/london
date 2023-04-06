def menu():
    print('____________________\nProjeto London\n____________________')
    menu = input('Iniciar o jogo?(s/n)')
    if (menu == 's'):
        print(
            'Quinta-feira, 31 de Outubro, Londres.\nAs ruas da cidade estão cheias para o feriado do Dia das bruxas.\nMesmo com a chuva, escondido no caos, o elemento espera para atacar como uma cobra.\nMas eu também estou lá, observando pacientemente.\nRecebi a tarefa de resgatar a filha de um homem vindo da já quase extinta agência dos Pinkertons.\nO homem veio desesperado ao meu escritório, seus homens já estavam incrédulos sobre tudo,\nencontrar a garota com vida era quase impossível pela percepção deles, mas do ponto de vista do pai,\nnão se tratavam de possibilidades, e sim de esperança, por mais irreal que esta fosse.\nAquele homem, tal qual eu havia presenciado em seu auge de carreira, estava completamente diferente,\napresentava uma tristeza amarga nos olhos, tristeza esta que era omitida pelas grandes olheiras\noriginadas pelas noites em que o mesmo buscava respostas, e sem encontrá-las, acendia um cigarro ao chegar em casa,\npelo menos para tentar aliviar sua mente de seus próprios demônios.\nA última localização conhecida da garota era em um pequeno beco de Whitechapel, e na verdade,\npossuo apenas isso para iniciar a investigação.\n(Em algum lugar não tão distante da agência dos Pinkertons, duas pessoas com visões de mundo bem diferentes entre si,\nrefletem sobre suas escolhas até então, e se deparam com um incerto futuro).')
    character = input('Selecione o protagonista da história:\nClaire:Jovem que presenciou um assassinato e precisa fugir de um perseguidor implacável.(Digite "c")\nJack:Um assassino com visão de mundo deturpada e doentia.(Digite "j")')
    if (menu == 'n'):
        quit()

    return character