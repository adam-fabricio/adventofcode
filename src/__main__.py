from submarino import Submarino

if __name__ == "__main__":

    estrela1 = 8
    estrela2 = 35
    estrela3 = 13

    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 01 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()


    submarino = Submarino()
    arquivo = "assets/input.txt"
    lista = submarino.le_arquivo(arquivo)
    relatorio = submarino.sonar(lista)
    resultado = submarino.sonar_contagem_de_ocorrencia(relatorio, "aumentou")
    print(f"O valor do relatório aumentou {resultado} vezes.")

    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 01 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    lista_filtro_medidas = submarino.sonar_filtro(lista)
    relatorio = submarino.sonar(lista_filtro_medidas)
    resultado = submarino.sonar_contagem_de_ocorrencia(relatorio, "aumentou")
    print(f"Após o filtro o valor aumentou {resultado} vezes.")
    
    print()
    print("*" * estrela2)
    print("*" * estrela3, "Dia 02.", "*" * estrela3)
    print("*" * estrela2)
    print()

    lista_de_movimento = submarino.le_arquivo("assets/day2.txt")
    submarino.movimenta(lista_de_movimento)
    posicao = (submarino.posicao_x, submarino.posicao_y)
    produto_da_posicao = submarino.posicao_x * submarino.posicao_y

    print(f"A posição do submarino é {str(posicao)} e o seu produto é {produto_da_posicao}")

    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 03 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()

    relatorio_diagonostico = submarino.le_arquivo("assets/diagnostico_consumo.txt")
    consolidado_relatorio = submarino.consolidar_relatorio(relatorio_diagonostico)
    gamma = submarino.calcula_gamma(consolidado_relatorio)
    epsilon = submarino.calcula_epsilon(consolidado_relatorio)

    print(f"O valor de gamma é {gamma}, o valor de epsilon é {epsilon}.")
    print(f"O valor do consumo é {gamma * epsilon}.")


    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 03 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    gerador_de_oxigenio = submarino.calcular_gerador_oxigenio(relatorio_diagonostico)
    purificador_de_CO2 = submarino.calcular_purificador_de_CO2(relatorio_diagonostico)

    print(f"O valor do gerador de oxigenio é: {gerador_de_oxigenio}.")
    print(f"O valor do purificador de CO2 é: {purificador_de_CO2}.")
    print(f"O valor de oxigênio gerado é: {gerador_de_oxigenio * purificador_de_CO2}.")


    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 04 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()

    dados_bingo = submarino.le_arquivo("assets/bingo.txt")
    submarino.bingo.jogar(dados_bingo)
    print(f"Resultado do bingo é {submarino.bingo.resultado}")
    
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 04 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()
    
    submarino.bingo.jogar_2(dados_bingo)
    print(f"Resultado do bingo é {submarino.bingo.resultado_vencedor[-1]}")

    print()
    print("*" * estrela2)
    print("*" * estrela3, "Dia 05.", "*" * estrela3)
    print("*" * estrela2)
    print()

    lista_turbilhao = submarino.le_arquivo("assets/lista_turbilhao.txt")
    mapa = {}
    for turbilhao in lista_turbilhao:
        cordenadas = submarino.converte_para_cordenadas(turbilhao)
        mapa = submarino.marca_no_mapa(cordenadas, mapa)

    soma_de_pontos_criticos = len(submarino.pontos_criticos(mapa))

    print(f"A soma dos valores criticos é {soma_de_pontos_criticos}")

    
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 06 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()

    caminho = "assets/idade_lanternfish.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')

    for dia in range(80):
        lista_idades = submarino.proximo_dia_lanterfish(lista_idades)

    print(f"Após 80 dias terão {len(lista_idades)} lanternfish.") 

    
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 06 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    lista_idades = submarino.le_arquivo(caminho)[0].split(',')
    ciclos = submarino.dicionario_de_ciclo(lista_idades)

    for dia in range(256):
        ciclos = submarino.proximo_dia_dicionario(ciclos)
    
    print(f"Após 80 dias terão {sum(ciclos.values())} lanternfish.")

    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 07 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()

    caminho = "assets/lista_caranguejos.txt"
    lista_caranguejos_str = submarino.le_arquivo(caminho)[0]
    lista_caranguejos = submarino.transforma_lista_de_str_em_int(lista_caranguejos_str)
    mediana = submarino.mediana_lista_caranguejos(lista_caranguejos)
    combustivel = submarino.calculo_combustivel(lista_caranguejos, mediana)


    print(f"O minimo de combustivel gasto para linhar a posição é: {combustivel}")

    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 07 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    media = int(round(sum(lista_caranguejos) / len(lista_caranguejos),0))
    combustivel = submarino.calculo_minimo_combustivel_real(lista_caranguejos, media)
    print(f"O valor minimo de combustivel gasto será: {combustivel}")
    
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 08 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()

    sinais = submarino.le_arquivo("assets/lista_sinais.txt")
    resultado = 0
    for sinal in sinais:
        dict_sinal = submarino.converter_lista_de_sinais(sinal)
        resultado += submarino.contar_saida_1_4_7_8(dict_sinal)
    
    print(f"A quantidade de vezes que aparece 1, 4, 7 e 8 é: {resultado}")
    
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 08 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    resultado = submarino.soma_das_saidas(sinais)
    print(f"A soma de todas as saidas é: {resultado}")
    
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 09 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()

    caminho = "assets/mapa_altura_raw.txt"
    mapa_altura_raw = submarino.le_arquivo(caminho)
    mapa_altura = submarino.gera_mapa_de_altura(mapa_altura_raw)
    resultado = submarino.soma_do_menor_level_de_risco(mapa_altura)

    print(f"A soma do nivel de risco em todos os pontos do mapa é: {resultado}")
        
    
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 09 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    tamanho_bacia = submarino.calcula_tamanho_de_todas_bacias(mapa_altura)
    maiores_bacias = submarino.verifica_tres_maiores_bacias(tamanho_bacia)

    resultado = maiores_bacias[0] * maiores_bacias[1] * maiores_bacias[2]

    print(f"O produto das 3 maiores bacias é: {resultado}")

    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 10 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()


    caminho = "assets/subsistema_de_navegacao.txt"
    subsitema_de_navegacao = submarino.le_arquivo(caminho)
    lista_de_erros = submarino.verifica_corrupcao_arquivo(subsitema_de_navegacao)
    pontos_erros = submarino.calcula_pontos_erros(lista_de_erros)

    print(f"A soma dos erros no subsistema de navegacao é: {sum(pontos_erros)}")

    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 10 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    erros_removidos = submarino.remove_linhas_de_erro_de_navegacao(subsitema_de_navegacao)
    pontos = submarino.calcula_lista_pontos_faltantes(erros_removidos)
    mediana = submarino.calcula_mediana_lista(pontos)

    print(f"A mediana da pontuação é: {mediana}")
    

    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 11 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()

    caminho = "assets/polvo_energia.txt"
    energia_raw = submarino.le_arquivo(caminho)
    energia = submarino.gera_matriz(energia_raw)
    dicionario_energia = submarino.energia_apos_passos(energia, 100)

    print(f"O total de piscadas após 100 passos são: {dicionario_energia['piscados']}")

    passo = submarino.encontra_sincronismo(energia)

    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 11 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    print(f"O primeiro passo onde todos os polvos piscam é: {passo}")
