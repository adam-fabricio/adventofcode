from submarino import Submarino

if __name__ == "__main__":

    estrela1 = 8
    estrela2 = 34
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 1 - Parte 1.", "*" * estrela1)
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
    print("*" * estrela1, "Dia 1 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    lista_filtro_medidas = submarino.sonar_filtro(lista)
    relatorio = submarino.sonar(lista_filtro_medidas)
    resultado = submarino.sonar_contagem_de_ocorrencia(relatorio, "aumentou")
    print(f"Após o filtro o valor aumentou {resultado} vezes.")
    
    estrela3 = 13
    print()
    print("*" * estrela2)
    print("*" * estrela3, "Dia 2.", "*" * estrela3)
    print("*" * estrela2)
    print()

    lista_de_movimento = submarino.le_arquivo("assets/day2.txt")
    submarino.movimenta(lista_de_movimento)
    posicao = (submarino.posicao_x, submarino.posicao_y)
    produto_da_posicao = submarino.posicao_x * submarino.posicao_y

    print(f"A posição do submarino é {str(posicao)} e o seu produto é {produto_da_posicao}")

    estrela3 = 13
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 3 - Parte 1.", "*" * estrela1)
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
    print("*" * estrela1, "Dia 3 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()

    gerador_de_oxigenio = submarino.calcular_gerador_oxigenio(relatorio_diagonostico)
    purificador_de_CO2 = submarino.calcular_purificador_de_CO2(relatorio_diagonostico)

    print(f"O valor do gerador de oxigenio é: {gerador_de_oxigenio}.")
    print(f"O valor do purificador de CO2 é: {purificador_de_CO2}.")
    print(f"O valor de oxigênio gerado é: {gerador_de_oxigenio * purificador_de_CO2}.")


    estrela3 = 13
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 4 - Parte 1.", "*" * estrela1)
    print("*" * estrela2)
    print()

    dados_bingo = submarino.le_arquivo("assets/bingo.txt")
    submarino.bingo.jogar(dados_bingo)
    print(f"Resultado do bingo é {submarino.bingo.resultado}")
    
    print()
    print("*" * estrela2)
    print("*" * estrela1, "Dia 4 - Parte 2.", "*" * estrela1)
    print("*" * estrela2)
    print()
    
    submarino.bingo.jogar_2(dados_bingo)
    print(f"Resultado do bingo é {submarino.bingo.resultado_vencedor[-1]}")