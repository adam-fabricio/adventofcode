from src.submarino import (Submarino, 
                           Cartela)
import pytest

from unittest import skip

def test_quando_ler_arquivo_retornar_uma_lista_de_movimento():
    submarino = Submarino()
    arquivo = "assets/day2_test.txt"

    lista = submarino.le_arquivo(arquivo)

    assert lista == ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

def test_quando_chamar_forward_incrementar_posicao_x():
    submarino = Submarino()
    
    forward = submarino.forward("5")

    assert submarino.posicao_x == 5

def test_quando_chamar_forward_mais_de_uma_vez_incrementar_posicao_x():
    submarino = Submarino()
    
    forward = submarino.forward("5")
    forward = submarino.forward("7")

    assert submarino.posicao_x == 12

def test_quando_chamar_down_incrementar_mira():
    submarino = Submarino()
    
    forward = submarino.down("5")

    assert submarino.posicao_aim == 5

def test_quando_chamar_down_mais_de_uma_vez_incrementar_mira():
    submarino = Submarino()
    
    forward = submarino.down("5")
    forward = submarino.down("7")

    assert submarino.posicao_aim == 12

def test_quando_chamar_up_decrementar_mira():
    submarino = Submarino()
    
    forward = submarino.up("5")

    assert submarino.posicao_aim == -5

def test_quando_chamar_up_mais_de_uma_vez_decrementar_mira():
    submarino = Submarino()
    
    forward = submarino.up("5")
    forward = submarino.up("7")

    assert submarino.posicao_aim == -12

def test_quando_chamar_up_e_down_deve_retornar_o_resultado_y():
    submarino = Submarino()
    
    forward = submarino.up("5")
    forward = submarino.down("7")

    assert submarino.posicao_aim == 2

def test_quando_passar_uma_lista_de_movimento_deve_retornar_o_resultado_da_posicao_x_e_y():

    submarino = Submarino()
    arquivo = "assets/day2_test.txt"
    lista_de_movimento = submarino.le_arquivo(arquivo)

    submarino.movimenta(lista_de_movimento)

    assert (submarino.posicao_x, submarino.posicao_y) == (15, 60)

dados = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
relatorio = ["N/A", "aumentou", "aumentou", "aumentou", "diminuiu", "aumentou", "aumentou", "aumentou","diminuiu", "aumentou"]

def test_quando_gerar_relatorio_primeiro_item_e_NA():
    submarino = Submarino()
    
    assert submarino.sonar(dados)[0] == relatorio[0]

def test_quando_gerar_relatorio_deve_retornar_uma_lista_informando_se_o_valor_e_maior_que_o_anterior():
    submarino = Submarino()

    assert submarino.sonar(dados) == relatorio

def test_quando_passar_um_relatorio_contar_ocorrencia_do_valor():
    submarino = Submarino()
    relatorio = submarino.sonar(dados)
    assert submarino.sonar_contagem_de_ocorrencia(relatorio, "aumentou") == 7

def test_quando_passar_um_arquivo_transformar_em_lista():
    arquivo = "assets/input_test.txt"
    submarino = Submarino()
    lista = submarino.le_arquivo(arquivo)
    
    assert lista == list(map(str, dados))

def test_quando_receber_uma_lista_devesomar_tres_proximos_valores_da_lista():
    valor_inicial = "assets/input_test.txt"
    resultado = "assets/dados_3_medidas.txt"
    submarino = Submarino()
    lista_inicial = submarino.le_arquivo(valor_inicial)
    lista_resultado = submarino.le_arquivo(resultado)
    
    assert list(map(str,submarino.sonar_filtro(lista_inicial))) == lista_resultado

def test_quando_receber_lista_de_itens_deve_gerar_relatorio_do_test_filtrado_pela_soma_dos_tres_valores():
    valor_inicial = "assets/input_test.txt"
    resultado = "assets/dados_3_medidas.txt"
    submarino = Submarino()
    lista_inicial = submarino.le_arquivo(valor_inicial)
    lista_resultado = submarino.le_arquivo(resultado) 
    
    assert  submarino.sonar(lista_resultado) == ["N/A", "aumentou", "nao mudou", "diminuiu", "aumentou", "aumentou", "aumentou", "aumentou"]

def test_quando_receber_um_conjunto_de_bit_deve_segregar_os_bits():
    submarino = Submarino()
    entrada = "10100"
    saida = [1, 0, 1, 0, 0]

    dicionario = submarino.converte_linha_em_lista(entrada)

    assert dicionario == saida

def test_quando_receber_uma_lista_de_bits_deve_consolidar_e_retornar_o_bit_mais_frequente_para_cada_posicao():
        
    submarino=Submarino()
    relatorio_teste = submarino.le_arquivo("assets/diagnostico_exemplo.txt")
    resultado = {"bit_0": 0, "bit_1": 1, "bit_2": 1, "bit_3": 0, "bit_4": 1}

    dicionario = submarino.consolidar_relatorio(relatorio_teste)

    assert dicionario == resultado

def test_quando_receber_o_consolidado_calcular_gamma():
    submarino=Submarino()
    consolidado = {"bit_0": 0, "bit_1": 1, "bit_2": 1, "bit_3": 0, "bit_4": 1}

    gamma = submarino.calcula_gamma(consolidado)

    assert gamma == 22

def test_quando_receber_o_consolidado_calcular_epsilon():
    submarino=Submarino()
    consolidado = {"bit_0": 0, "bit_1": 1, "bit_2": 1, "bit_3": 0, "bit_4": 1}

    gamma = submarino.calcula_epsilon(consolidado)

    assert gamma == 9

def test_quando_receber_o_consolidado_calcular_o_gerador_de_oxigenio():
    submarino=Submarino()
    relatorio_diagonostico = submarino.le_arquivo("assets/diagnostico_exemplo.txt")
    
    gerador_oxigenio = submarino.calcular_gerador_oxigenio(relatorio_diagonostico)
    
    assert gerador_oxigenio == 23

def test_quando_receber_uma_string_deve_dividir_a_lista():
    entrada_string = "1"
    resultado = ["11110", "10110", "10111", "10101", "11100", "10000", "11001"]


    submarino = Submarino()
    relatorio_diagonostico = submarino.le_arquivo("assets/diagnostico_exemplo.txt")
    lista_nova = submarino.dividir_lista(relatorio_diagonostico, entrada_string)

    assert lista_nova == resultado

def test_quando_receber_uma_string_deve_dividir_a_lista_2():
    entrada_string = "10"
    resultado = ["10110", "10111", "10101","10000"]

    submarino = Submarino()
    relatorio_diagonostico = submarino.le_arquivo("assets/diagnostico_exemplo.txt")
    lista_nova = submarino.dividir_lista(relatorio_diagonostico, entrada_string)

    assert lista_nova == resultado

def test_quando_receber_o_relatorio_calcular_o_purificador_de_CO2():
    submarino=Submarino()
    relatorio_diagonostico = submarino.le_arquivo("assets/diagnostico_exemplo.txt")
    
    purificador_CO2 = submarino.calcular_purificador_de_CO2(relatorio_diagonostico)
    
    assert purificador_CO2 == 10

def test_quando_passar_dados_deve_gerar_lista_de_numeros_sorteados():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)
    numeros_sorteados = submarino.bingo.gera_numeros_sorteados(dados_bingo)
    resultado_test = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

    for i in range(len(numeros_sorteados)):
        assert int(numeros_sorteados[i]) == resultado_test[i]

def test_quando_adicionar_linha_na_cartela_deve_adicionar_linha_a_cartela():
    cartela = Cartela()
    dados_teste = '22 13 17 11  0'
    dados_teste2 = ' 8  2 23  4 24'

    cartela.adicionar_linha(dados_teste)

    assert cartela.cartela == [[22, 13, 17, 11, 0]]
    
    cartela.adicionar_linha(dados_teste2)

    assert cartela.cartela == [[22, 13, 17, 11, 0], [8,  2, 23,  4, 24]]

def test_quando_passar_os_dados_deve_cirar_as_cartelas():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)
    cartela = []
    cartela.append([[22, 13, 17, 11,  0], [ 8,  2, 23,  4, 24], [21,  9, 14, 16,  7], [6, 10,  3,  18,  5], [ 1, 12, 20, 15, 19]])
    cartela.append([[ 3, 15,  0,  2, 22], [ 9, 18, 13, 17,  5], [19,  8,  7, 25, 23], [20, 11, 10, 24,  4], [14, 21, 16, 12,  6]])
    cartela.append([[14, 21, 17, 24,  4], [10, 16, 15,  9, 19], [18,  8, 23, 26, 20], [22, 11, 13,  6,  5], [ 2,  0, 12,  3,  7]])

    submarino.bingo.criar_cartelas(dados_bingo)

    for i in range(len(submarino.bingo.cartelas)):
        assert submarino.bingo.cartelas[i].cartela == cartela[i]

def test_quando_enviar_numero_sorteado_deve_substituir_o_valor_por_menos_um_caso_exista():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)
    submarino.bingo.criar_cartelas(dados_bingo)
    cartela = []
    cartela.append([[14, 21, -1, 24,  4], [10, 16, 15,  9, 19], [18,  8, 23, 26, 20], [22, 11, 13,  6,  5], [ 2,  0, 12,  3,  7]])
    
    submarino.bingo.cartelas[2].marcar_numero(17)

    assert submarino.bingo.cartelas[2].cartela == cartela[0]

def test_quando_marcar_numero_inexistente_deve_marcar_vazio():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)
    submarino.bingo.criar_cartelas(dados_bingo)

    submarino.bingo.cartelas[0].marcar_numero(30)
    
    assert submarino.bingo.cartelas[0].ultima_posicao == False

def test_quando_marcar_numero_existente_deve_salvar_posicao_tupla_linha_e_coluna():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)
    submarino.bingo.criar_cartelas(dados_bingo)

    submarino.bingo.cartelas[0].marcar_numero(4)
    
    assert submarino.bingo.cartelas[0].ultima_posicao == (1, 3)

def test_quando_marcar_todos_numeros_de_uma_linha_deve_retornar_bingo():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)
    submarino.bingo.criar_cartelas(dados_bingo)
    numeros_sorteados = [8,  2, 31, 45, 76, 23,  4, 24]

    for numero in numeros_sorteados:
        submarino.bingo.cartelas[0].marcar_numero(numero)
        if submarino.bingo.cartelas[0].verifica_bingo() == "BINGO":
            resultado = "BINGO"
        
    assert resultado == "BINGO"

def test_quando_marcar_todos_numeros_de_uma_coluna_deve_retornar_bingo():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)
    submarino.bingo.criar_cartelas(dados_bingo)
    numeros_sorteados = [8,  6, 22, 45, 76, 21,  1, 24]

    for numero in numeros_sorteados:
        submarino.bingo.cartelas[0].marcar_numero(numero)
        if submarino.bingo.cartelas[0].verifica_bingo() == "BINGO":
            resultado = "BINGO"
        
    assert resultado == "BINGO"

def test_quando_passar_chamar_funcao_deve_retornar_a_soma_dos_numeros_nao_marcados():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)
    submarino.bingo.criar_cartelas(dados_bingo)

    assert submarino.bingo.cartelas[0].somar_cartela() == 300

    submarino.bingo.cartelas[0].marcar_numero(2)

    assert submarino.bingo.cartelas[0].somar_cartela() == 298

def test_quando_marcar_numero_e_der_bingo_deve_retornar_soma_dos_valores_nao_marcados_vezes_ultimo_valor():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)
    numeros_sorteados = submarino.bingo.gera_numeros_sorteados(dados_bingo)
    submarino.bingo.criar_cartelas(dados_bingo)

    for numero in numeros_sorteados:
        if submarino.bingo.cartelas[2].marcar_numero((numero)):
            break        
    assert submarino.bingo.cartelas[2].bingo == 4512
    
def test_quando_jogar_bingo_deve_retornar_o_resultado_do_bingo():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)

    submarino.bingo.jogar(dados_bingo)

    assert submarino.bingo.resultado == 4512

def test_quando_jogar_bingo_deve_retornar_o_resultado_da_ultima_cartela_dar_bingo():
    submarino = Submarino()
    caminho = "assets/bingo_test.txt"
    dados_bingo = submarino.le_arquivo(caminho)

    submarino.bingo.jogar_2(dados_bingo)

    assert submarino.bingo.resultado_vencedor[-1] == 1924

def test_quando_submarino_reveber_lista_de_linhas_de_vento_deve_separar_em_duas_tuplas():
    submarino = Submarino()
    caminho = "assets/lista_turbilhoes_teste.txt"
    lista_turbilhao = submarino.le_arquivo(caminho)

    assert submarino.converte_para_cordenadas(lista_turbilhao[0]) == [(0,9) ,(5,9)]
    
def test_quando_receber_linhas_repetidas_somar_um_no_valor():
    submarino = Submarino()
    caminho = "assets/lista_turbilhoes_teste.txt"
    lista_turbilhao = submarino.le_arquivo(caminho)


    cordenadas_0 = submarino.converte_para_cordenadas(lista_turbilhao[4])

    cordenadas_1 = submarino.converte_para_cordenadas(lista_turbilhao[2])

    mapa = submarino.marca_no_mapa(cordenadas_0)
    mapa = submarino.marca_no_mapa(cordenadas_1)

    assert mapa == {"7, 1": 1, "7, 2": 1, "7, 3": 1, "7, 4": 2, "7, 0": 1, "3, 4": 1, "4, 4": 1, "5, 4": 1, "6, 4": 1, "8, 4": 1, "9, 4": 1}

def test_quando_receber_as_cordenadas_deve_gerar_um_mapa():

    submarino = Submarino()
    caminho = "assets/lista_turbilhoes_teste.txt"
    lista_turbilhao = submarino.le_arquivo(caminho)
    mapa = {}
    i = 1
    for turbilhao in lista_turbilhao:
        cordenadas = submarino.converte_para_cordenadas(turbilhao)
        mapa = submarino.marca_no_mapa(cordenadas, mapa)

    
    assert mapa == {
                    "0, 0": 1,
                    "2, 0": 1,
                    "7, 0": 1,
                    "8, 0": 1,
                    "1, 1": 1,
                    "2, 1": 1,
                    "3, 1": 1,
                    "7, 1": 2,
                    "2, 2": 2,
                    "4, 2": 1,
                    "6, 2": 1,
                    "7, 2": 1,
                    "8, 2": 1,
                    "3, 3": 1,
                    "5, 3": 2,
                    "7, 3": 2,
                    "1, 4": 1,
                    "2, 4": 1,
                    "3, 4": 2,
                    "4, 4": 3,
                    "5, 4": 1,
                    "6, 4": 3,
                    "7, 4": 2,
                    "8, 4": 1,
                    "9, 4": 1,
                    "3, 5": 1,
                    "5, 5": 2,
                    "2, 6": 1,
                    "6, 6": 1,
                    "1, 7": 1,
                    "7, 7": 1,
                    "0, 8": 1,
                    "8, 8": 1,
                    "0, 9": 2,
                    "1, 9": 2,
                    "2, 9": 2,
                    "3, 9": 1,
                    "4, 9": 1,
                    "5, 9": 1,
                   }

def test_quando_passar_mapa_deve_retornar_soma_dos_pontos_criticos():

    submarino = Submarino()
    caminho = "assets/lista_turbilhoes_teste.txt"
    lista_turbilhao = submarino.le_arquivo(caminho)
    mapa = {}
    for turbilhao in lista_turbilhao:
        cordenadas = submarino.converte_para_cordenadas(turbilhao)
        mapa = submarino.marca_no_mapa(cordenadas, mapa)
    
    assert len(submarino.pontos_criticos(mapa)) == 12

def test_quando_passar_cordenadas_verificar_se_a_linha_e_diagonal():
    submarino = Submarino()
    caminho = "assets/lista_turbilhoes_teste.txt"
    lista_turbilhao = submarino.le_arquivo(caminho)


    cordenadas_0 = submarino.converte_para_cordenadas(lista_turbilhao[1])
    cordenadas_1 = submarino.converte_para_cordenadas(lista_turbilhao[5])

    mapa = submarino.marca_no_mapa(cordenadas_0, {})
    mapa = submarino.marca_no_mapa(cordenadas_1, mapa)

    assert mapa == {
                    "0, 8": 1,
                    "1, 7": 1,
                    "2, 6": 1,
                    "3, 5": 1,
                    "4, 4": 1,
                    "5, 3": 2,
                    "6, 2": 1,
                    "7, 1": 1,
                    "8, 0": 1,
                    "2, 0": 1,
                    "3, 1": 1,
                    "4, 2": 1,
                    "6, 4": 1
                    }

def test_quando_passar_1_dia_deve_o_diminuir_o_contador_do_ciclo_de_vida_do_lanterfish():
    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)

    lista_idades = submarino.proximo_dia_lanterfish(lista_idades[0].split(','))

    assert lista_idades == [2,3,2,0,1]

def test_quando_o_algum_valor_da_lista_chegar_em_zero_deve_retornar_para_6_e_acrescentar_8_no_final_da_lista():
    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)

    lista_idades = submarino.proximo_dia_lanterfish(lista_idades[0].split(','))
    lista_idades = submarino.proximo_dia_lanterfish(lista_idades)
    
    assert lista_idades == [1,2,1,6,0,8]

def test_quando_se_passar_18_dias_deve_retornar_a_seguinte_lista():
    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')
    
    for dia in range(18):
        lista_idades = submarino.proximo_dia_lanterfish(lista_idades)
    
    assert lista_idades == [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
    assert len(lista_idades) == 26

def test_quando_se_passar_80_dias_deve_retornar_5934():
    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')
    
    for dia in range(80):
        lista_idades = submarino.proximo_dia_lanterfish(lista_idades)

    assert len(lista_idades) == 5934

@skip("Muito Demorado")
def test_quando_se_passar_256_dias_deve_retornar_26984457539():
    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')
    
    for dia in range(256):
        lista_idades = submarino.proximo_dia_lanterfish(lista_idades)

    assert len(lista_idades) == 26984457539

def test_quando_passar_lista_de_idade_converter_deve_converter_em_um_dicionario():
    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')

    ciclos = submarino.dicionario_de_ciclo(lista_idades)

    assert ciclos == {
                        "ciclo_8": 0,
                        "ciclo_7": 0,
                        "ciclo_6": 0,
                        "ciclo_5": 0,
                        "ciclo_4": 1,
                        "ciclo_3": 2,
                        "ciclo_2": 1,
                        "ciclo_1": 1,
                        "ciclo_0": 0
                    }

def test_quando_passar_um_dia_deve_rotacionar_os_valores():
    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')
    ciclos = submarino.dicionario_de_ciclo(lista_idades)

    ciclos = submarino.proximo_dia_dicionario(ciclos)

    assert ciclos == {
                    "ciclo_8": 0,
                    "ciclo_7": 0,
                    "ciclo_6": 0,
                    "ciclo_5": 0,
                    "ciclo_4": 0,
                    "ciclo_3": 1,
                    "ciclo_2": 2,
                    "ciclo_1": 1,
                    "ciclo_0": 1
                }
    
def test_quando_passar_um_18_deve_rotacionar_os_valores():
    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')
    ciclos = submarino.dicionario_de_ciclo(lista_idades)

    for dia in range(18):
        ciclos = submarino.proximo_dia_dicionario(ciclos)

    assert ciclos == {
                    "ciclo_8": 4,
                    "ciclo_7": 1,
                    "ciclo_6": 5,
                    "ciclo_5": 1,
                    "ciclo_4": 2,
                    "ciclo_3": 2,
                    "ciclo_2": 3,
                    "ciclo_1": 5,
                    "ciclo_0": 3
                }

def test_quando_passar_18_dias_deve_retornar_o_numero_de_peixes():

    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')
    ciclos = submarino.dicionario_de_ciclo(lista_idades)

    for dia in range(18):
        ciclos = submarino.proximo_dia_dicionario(ciclos)

    assert sum(ciclos.values()) == 26

def test_quando_passar_80_dias_deve_retornar_o_numero_de_peixes():

    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')
    ciclos = submarino.dicionario_de_ciclo(lista_idades)

    for dia in range(80):
        ciclos = submarino.proximo_dia_dicionario(ciclos)

    assert sum(ciclos.values()) == 5934

def test_quando_passar_256_dias_deve_retornar_o_numero_de_peixes():

    submarino = Submarino()
    caminho = "assets/idade_lanternfish_test.txt"
    lista_idades = submarino.le_arquivo(caminho)[0].split(',')
    ciclos = submarino.dicionario_de_ciclo(lista_idades)

    for dia in range(256):
        ciclos = submarino.proximo_dia_dicionario(ciclos)

    assert sum(ciclos.values()) == 26984457539

def test_quando_passar_uma_lista_de_posicao_caranguejos_deve_calcular_a_mediana():
    submarino = Submarino()
    caminho = "assets/lista_caranguejos_teste.txt"
    lista_caranguejos = submarino.le_arquivo(caminho)[0]
    lista_caranguejos_int = submarino.transforma_lista_de_str_em_int(lista_caranguejos)

    mediana = submarino.mediana_lista_caranguejos(lista_caranguejos_int)

    assert mediana == 2

def test_quando_passar_uma_posicao_deve_calcular_o_valor_do_combustivel():
    submarino = Submarino()
    caminho = "assets/lista_caranguejos_teste.txt"
    lista_caranguejos = submarino.le_arquivo(caminho)[0]
    lista_caranguejos_int = submarino.transforma_lista_de_str_em_int(lista_caranguejos)
    mediana = submarino.mediana_lista_caranguejos(lista_caranguejos_int)

    combustivel = submarino.calculo_combustivel(lista_caranguejos_int, mediana)

    assert combustivel == 37

def test_quando_passar_posicao_inicial_e_posicao_final_calcular_o_valor_combustivel():
    submarino = Submarino()
    posicao_inicial = 1
    posicao_final = 5

    combustivel = submarino.calculo_combustivel_real(posicao_inicial, posicao_final)

    assert combustivel == 10

def test_quando_receber_uma_lista_deve_calcular_a_media():
    submarino = Submarino()
    caminho = "assets/lista_caranguejos_teste.txt"
    lista_caranguejos = submarino.le_arquivo(caminho)[0]
    lista_caranguejos_int = submarino.transforma_lista_de_str_em_int(lista_caranguejos)
    
    media = sum(lista_caranguejos_int)/len(lista_caranguejos_int)

    assert int(round(media,0)) == 5

    combustivel = 0 
    for posicao in lista_caranguejos_int:
        combustivel += submarino.calculo_combustivel_real(posicao,int(round(media,0)))

    assert combustivel == 168

def test_quando_receber_uma_lista_ordenada_dividir_em_duas_listas():

    submarino = Submarino()
    caminho = "assets/lista_caranguejos_teste.txt"
    lista_caranguejos_str = submarino.le_arquivo(caminho)[0]
    lista_caranguejos = submarino.transforma_lista_de_str_em_int(lista_caranguejos_str)
    lista_caranguejos.sort()

    lista_caranguejos_divida = submarino.dividir_lista_metade(lista_caranguejos)

    assert lista_caranguejos_divida == [[0, 1, 1, 2, 2], [4, 7, 14, 16]]

def test_quando_passar_lista_e_media_calcular_o_minimo_combustivel():
    submarino = Submarino()
    caminho = "assets/lista_caranguejos_teste.txt"
    lista_caranguejos = submarino.le_arquivo(caminho)[0]
    lista_caranguejos_int = submarino.transforma_lista_de_str_em_int(lista_caranguejos)
    media = int(round(sum(lista_caranguejos_int)/len(lista_caranguejos_int),0))

    combustivel = submarino.calculo_minimo_combustivel_real(lista_caranguejos_int, media)
    assert combustivel == 168

def test_quando_ler_entrada_deve_retornar_um_dicionario_com_lista_de_input_e_output():
    submarino = Submarino()
    caminho = "assets/lista_sinais_teste.txt"
    lista_de_sinais = submarino.le_arquivo(caminho)
    
    sinais = submarino.converter_lista_de_sinais(lista_de_sinais[0])

    assert sinais ==    {
                            "input": ["be","cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"],
                            "output": ["fdgacbe", "cefdb", "cefbgd", "gcbe"]
                        }

def test_quando_receber_um_dicionario_deve_decodificar_a_saida():
    submarino = Submarino()
    caminho = "assets/lista_sinais_teste.txt"
    lista_de_sinais = submarino.le_arquivo(caminho)
    sinais = submarino.converter_lista_de_sinais(lista_de_sinais[0])

    resultado = submarino.contar_saida_1_4_7_8(sinais)

    valor_final = 0
    for sinal in lista_de_sinais:
        dict_sinal = submarino.converter_lista_de_sinais(sinal)
        valor_final += submarino.contar_saida_1_4_7_8(dict_sinal)
    
    assert valor_final == 26

def test_quando_passar_uma_lista_de_entrada_deve_retornar_dicionario():
    submarino = Submarino()
    lista_de_sinais = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    sinais = submarino.converter_lista_de_sinais(lista_de_sinais)
    sinal_input = sinais["input"]

    traducao = submarino.decodifica_sete_segmentos(sinal_input)

    assert traducao ==  {
                            "abcdefg": 8,
                            "bcdef": 5,
                            "acdfg": 2,
                            "abcdf": 3,
                            "abd": 7,
                            "abcdef": 9,
                            "bcdefg": 6,
                            "abef": 4,
                            "abcdeg": 0,
                            "ab": 1
                        }

def test_quando_passar_o_tradutor_e_a_saida_deve_retornar_o_valor_decodificado():
    submarino = Submarino()
    lista_de_sinais = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    sinais = submarino.converter_lista_de_sinais(lista_de_sinais)
    sinal_input = sinais["input"]
    decodificador = submarino.decodifica_sete_segmentos(sinal_input)
    sinal_saida = sinais["output"]
    
    valor_decodificado = submarino.decodificador_saida(sinal_saida, decodificador)

    assert valor_decodificado == 5353

def test_quando_passar_a_lista_de_codigo_deve_retornar_a_soma_da_saida():
    submarino = Submarino()
    caminho = "assets/lista_sinais_teste.txt"
    lista_de_sinais = submarino.le_arquivo(caminho)

    resultado = submarino.soma_das_saidas(lista_de_sinais)

    assert resultado == 61229

def test_quando_ler_arquivo_deve_retornar_uma_lista_mapa_de_altura():
    submarino = Submarino()
    caminho = "assets/mapa_altura_raw_teste.txt"
    mapa_altura_raw = submarino.le_arquivo(caminho)
    
    mapa_altura = submarino.gera_mapa_de_altura(mapa_altura_raw)

    assert mapa_altura ==   [
                                [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                                [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                                [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                                [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                                [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
                            ]
    
def test_quando_passar_uma_posicao_deve_retornar_par_de_adjacente():
    submarino = Submarino()
    posicao = (0,0)
    mapa_altura =   [
                                [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                                [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                                [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                                [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                                [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
                            ]
    

    adjacentes = submarino.lista_adjacentes(mapa_altura, posicao)

    assert adjacentes == [(1,0), (0,1)]

def test_quando_passar_um_mapa_deve_calcular_a_soma_do_risco():
    submarino = Submarino()
    caminho = "assets/mapa_altura_raw_teste.txt"
    mapa_altura_raw = submarino.le_arquivo(caminho)
    mapa_altura = submarino.gera_mapa_de_altura(mapa_altura_raw)

    resultado = submarino.soma_do_menor_level_de_risco(mapa_altura)

    assert resultado == 15

def test_quando_passar_um_mapa_deve_calcular_a_soma_do_risco_2():
    submarino = Submarino()
    mapa_altura =   [
                                [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                                [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                                [9, 8, 5, 6, 7, 8, 9, 8, 9, 0],
                                [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                                [0, 8, 9, 9, 9, 6, 5, 6, 7, 8]
                            ]


    resultado = submarino.soma_do_menor_level_de_risco(mapa_altura)

    assert resultado == 17

def test_quando_passar_um_mapa_deve_retornar_lista_menores_pontos():
    submarino = Submarino()
    caminho = "assets/mapa_altura_raw_teste.txt"
    mapa_altura_raw = submarino.le_arquivo(caminho)
    mapa_altura = submarino.gera_mapa_de_altura(mapa_altura_raw)

    resultado = submarino.lista_menores_pontos(mapa_altura)

    assert resultado == [(0,1),(0,9),(2,2),(4,6)]

def test_quando_passar_um_ponto_deve_retornar_tamanho_da_bacia():
    submarino = Submarino()
    caminho = "assets/mapa_altura_raw_teste.txt"
    mapa_altura_raw = submarino.le_arquivo(caminho)
    mapa_altura = submarino.gera_mapa_de_altura(mapa_altura_raw)
    posicao = (0,1)

    resultado = submarino.calcula_tamanho_bacia(mapa_altura, posicao, [])

    assert resultado == 3

def test_quando_receber_uma_lista_de_cordenadas_deve_retornar_uma_lista_de_tamanho_das_bacias():
    submarino = Submarino()
    caminho = "assets/mapa_altura_raw_teste.txt"
    mapa_altura_raw = submarino.le_arquivo(caminho)
    mapa_altura = submarino.gera_mapa_de_altura(mapa_altura_raw)
    
    tamanho_bacia = submarino.calcula_tamanho_de_todas_bacias(mapa_altura)

    assert tamanho_bacia == [3, 9, 14, 9]

def test_quando_receber_uma_lista_de_tamanho_de_bacia_deve_retornar_os_3_maiores():    
    submarino = Submarino()
    caminho = "assets/mapa_altura_raw_teste.txt"
    mapa_altura_raw = submarino.le_arquivo(caminho)
    mapa_altura = submarino.gera_mapa_de_altura(mapa_altura_raw)
    tamanho_bacia = submarino.calcula_tamanho_de_todas_bacias(mapa_altura)

    tres_maiores_bacias = submarino.verifica_tres_maiores_bacias(tamanho_bacia)
    
    assert tres_maiores_bacias == [9, 9, 14]

def test_quando_ler_uma_linha_do_subsistema_deve_retornar_o_caracter_com_erro_ou_vazio():
    submarino = Submarino()
    caminho = "assets/subsistema_de_navegacao_teste.txt"
    subsitema_de_navegacao = submarino.le_arquivo(caminho)

    erro = submarino.verifica_corrupcao_linha(list(subsitema_de_navegacao[0]))

    assert erro == None

def test_quando_ler_subsistema_de_navegacao_deve_retornar_lista_de_erros():
    submarino = Submarino()
    caminho = "assets/subsistema_de_navegacao_teste.txt"
    subsitema_de_navegacao = submarino.le_arquivo(caminho)

    lista_de_erros = submarino.verifica_corrupcao_arquivo(subsitema_de_navegacao)

    assert lista_de_erros == ["}", ")", "]", ")", ">"]

def test_quando_ler_lista_de_erros_deve_retornar_lista_de_pontos():
    submarino = Submarino()
    caminho = "assets/subsistema_de_navegacao_teste.txt"
    subsitema_de_navegacao = submarino.le_arquivo(caminho)
    lista_de_erros = submarino.verifica_corrupcao_arquivo(subsitema_de_navegacao)

    pontos_erros = submarino.calcula_pontos_erros(lista_de_erros)

    assert pontos_erros == [1197, 3, 57, 3, 25137]
    assert sum(pontos_erros) == 26397

def test_quando_passar_lista_deve_remover_as_linhas_com_erros():
    submarino = Submarino()
    caminho = "assets/subsistema_de_navegacao_teste.txt"
    subsitema_de_navegacao = submarino.le_arquivo(caminho)

    erros_removidos = submarino.remove_linhas_de_erro_de_navegacao(subsitema_de_navegacao)

    lista_de_erros = submarino.verifica_corrupcao_arquivo(erros_removidos)

    assert lista_de_erros == []

def test_quando_passar_uma_lista_incompleta_deve_retornar_lista_de_caracter_para_fechar():
    submarino = Submarino()
    caminho = "assets/subsistema_de_navegacao_teste.txt"
    subsitema_de_navegacao = submarino.le_arquivo(caminho)
    erros_removidos = submarino.remove_linhas_de_erro_de_navegacao(subsitema_de_navegacao)

    lista_abertos = submarino.gera_lista_caracter_abertos(list(erros_removidos[0]))
    
    converte_para_fechado = submarino.inverte_lista_caracter(lista_abertos)
    assert converte_para_fechado[::-1] == ["}", "}", "]", "]", ")", "}", ")", "]"]

def test_quando_passar_uma_lista_de_caracter_faltante_deve_calcular_pontos2():
    submarino = Submarino()
    caminho = "assets/subsistema_de_navegacao_teste.txt"
    subsitema_de_navegacao = submarino.le_arquivo(caminho)
    erros_removidos = submarino.remove_linhas_de_erro_de_navegacao(subsitema_de_navegacao)
    lista_abertos = submarino.gera_lista_caracter_abertos(list(erros_removidos[0]), [])
    converte_para_fechado = submarino.inverte_lista_caracter(lista_abertos)

    pontos = submarino.calcula_pontos_faltantes(converte_para_fechado)

    assert pontos == 288957

def test_quando_passar_uma_lista_de_pontos_deve_retornar_uma_lista_de_pontos():
    submarino = Submarino()
    caminho = "assets/subsistema_de_navegacao_teste.txt"
    subsitema_de_navegacao = submarino.le_arquivo(caminho)
    erros_removidos = submarino.remove_linhas_de_erro_de_navegacao(subsitema_de_navegacao)

    pontos = submarino.calcula_lista_pontos_faltantes(erros_removidos)
    print(pontos)
    
    assert pontos == [288957, 5566, 1480781, 995444, 294]

def test_quando_passar_uma_lista_de_pontos_deve_ordernar_a_mediana():
    submarino = Submarino()
    pontos = [288957, 5566, 1480781, 995444, 294]

    mediana = submarino.calcula_mediana_lista(pontos)

    assert mediana == 288957

def test_quando_passar_dia_deve_somar_um_de_energia_lista_de_inteiros():
    submarino = Submarino()
    caminho = "assets/polvo_energia_teste.txt"
    energia_polvo_raw = submarino.le_arquivo(caminho)
    energia_polvo = submarino.gera_matriz(energia_polvo_raw)
    energia_polvo_resultado_raw =   [
                                        "6594254334",
                                        "3856965822",
                                        "6375667284",
                                        "7252447257",
                                        "7468496589",
                                        "5278635756",
                                        "3287952832",
                                        "7993992245",
                                        "5957959665",
                                        "6394862637",
                                    ]
    energia_polvo_resultado = submarino.gera_matriz(energia_polvo_resultado_raw)
    
    energia_polvo_proximo_dia = submarino.soma_um_na_matriz(energia_polvo)

    assert energia_polvo_proximo_dia["matriz"] == energia_polvo_resultado

def test_quando_energia_passar_10_deve_somar_1_adjacentes():
    submarino = Submarino()
    energia_raw =           [
                                "6594254334",
                                "3856965822",
                                "6375667284",
                                "7252447257",
                                "7468496589",
                                "5278635756",
                                "3287952832",
                                "7993992245",
                                "5957959665",
                                "6394862637",
                            ]
    energia_raw_result =    [
                                "8807476555",
                                "5089087054",
                                "8597889608",
                                "8485769600",
                                '8700908800',
                                '6600088989',
                                '6800005943',
                                '0000007456',
                                '9000000876',
                                '8700006848',
                            ]
    energia = submarino.gera_matriz(energia_raw)
    energia_resultado = submarino.gera_matriz(energia_raw_result)

    energia = submarino.soma_um_na_matriz(energia) 

    assert energia["matriz"] == energia_resultado
    assert energia["piscados"] == 35

def test_quando_energia_passar_100_passos_deve_retornar():
    submarino = Submarino()
    energia_raw =           [
                                "6594254334",
                                "3856965822",
                                "6375667284",
                                "7252447257",
                                "7468496589",
                                "5278635756",
                                "3287952832",
                                "7993992245",
                                "5957959665",
                                "6394862637",
                            ]
    energia_raw_result =    [
                                '0397666866',
                                '0749766918',
                                '0053976933',
                                '0004297822',
                                '0004229892',
                                '0053222877',
                                '0532222966',
                                '9322228966',
                                '7922286866',
                                '6789998766',

                            ]
    caminho = "assets/polvo_energia_teste.txt"
    energia_raw = submarino.le_arquivo(caminho)
    energia = submarino.gera_matriz(energia_raw)
    energia_resultado = submarino.gera_matriz(energia_raw_result)

    energia = submarino.energia_apos_passos(energia, 100)
    submarino.imprimi_matriz(energia["matriz"])

    assert energia["matriz"] == energia_resultado
    assert energia["piscados"] == 1656

def test_quando_passar_a_lista_deve_encontrar_quando_os_polvos_vao_estar_sincronizados():
    submarino = Submarino()
    caminho = "assets/polvo_energia_teste.txt"
    energia_raw = submarino.le_arquivo(caminho)
    energia = submarino.gera_matriz(energia_raw)

    passo = submarino.encontra_sincronismo(energia)

    assert passo == 195

def test_quando_passar_uma_lista_de_caminho_gerar_uma_lista_splitada():
    submarino = Submarino()
    passagens_raw = submarino.le_arquivo("assets/passagem_mapa_teste.txt")

    passagem = submarino.gera_passagem(passagens_raw)

    assert passagem ==  [["start", "A"], ["start", "b"], ["A", "c"], ["A", "b"], ["b", "d"], ["A", "end"], ["b", "end"]]

def test_quando_passar_a_lista_de_valores_deve_retornar_um_dicionario_de_vizinhos():
    submarino = Submarino()
    passagem = [["start", "A"], ["start", "b"], ["A", "c"], ["A", "b"], ["b", "d"], ["A", "end"], ["b", "end"]]
    vizinhos_resultado =    {
                                "start": ["A", "b"],
                                "A": ["start", "end", "b", "c"],
                                "b": ["start", "end", "A", "d"],
                                "c": ["A"],
                                "d": ["b"],
                                "end": ["A", "b"]
                            }
    
    vizinho = submarino.gera_vizinhos(passagem)

    assert list(vizinho.keys()).sort() == list(vizinhos_resultado.keys()).sort()
    assert list(vizinho.values()).sort() == list(vizinhos_resultado.values()).sort()

def test_quando_passar_dict_de_vizinhos_achar_lista_de_caminho():

    submarino = Submarino()
    vizinhos =              {
                                "start": ["A", "b"],
                                "A": ["start", "end", "b", "c"],
                                "b": ["start", "end", "A", "d"],
                                "c": ["A"],
                                "d": ["b"],
                                "end": ["A", "b"]
                            }
    caminhos_result =   [
                            ["start","A","b","A","c",'A',"end"],
                            ['start','A','b','A','end'],
                            ['start','A','b','end'],
                            ['start','A','c','A','b','A','end'],
                            ['start','A','c','A','b','end'],
                            ['start','A','c','A','end'],
                            ['start','A','end'],
                            ['start','b','A','c','A','end'],
                            ['start','b','A','end'],
                            ['start','b','end'],
                        ]

    caminhos = submarino.encontrar_caminhos(vizinhos)

    assert len(caminhos) == len(caminhos_result)
    assert all([a==b for a, b in zip(sorted(caminhos), sorted(caminhos_result))])

def test_quando_passar_o_mapa_2_deve_contar_19_caminhos():
    submarino = Submarino()
    passagens_raw = submarino.le_arquivo("assets/passagem_mapa_teste_2.txt")
    passagem = submarino.gera_passagem(passagens_raw)
    passagens_dict = submarino.gera_vizinhos(passagem)
    caminhos = submarino.encontrar_caminhos(passagens_dict)

    assert len(caminhos) == 19

def test_quando_passar_o_mapa_3_deve_contar_226_caminhos():
    submarino = Submarino()
    passagens_raw = submarino.le_arquivo("assets/passagem_mapa_teste_3.txt")
    passagem = submarino.gera_passagem(passagens_raw)
    passagens_dict = submarino.gera_vizinhos(passagem)
    caminhos = submarino.encontrar_caminhos(passagens_dict)

    assert len(caminhos) == 226

def test_quando_passar_o_mapa_1_deve_contar_36_caminhos():
    submarino = Submarino()
    passagens_raw = submarino.le_arquivo("assets/passagem_mapa_teste.txt")
    passagem = submarino.gera_passagem(passagens_raw)
    passagens_dict = submarino.gera_vizinhos(passagem)
    caminhos = submarino.encontrar_caminhos_2(passagens_dict)
    [print(i) for i in sorted(caminhos)]
    assert len(caminhos) == 36

def test_quando_passar_o_mapa_2_deve_contar_103_caminhos():
    submarino = Submarino()
    passagens_raw = submarino.le_arquivo("assets/passagem_mapa_teste_2.txt")
    passagem = submarino.gera_passagem(passagens_raw)
    passagens_dict = submarino.gera_vizinhos(passagem)
    caminhos = submarino.encontrar_caminhos_2(passagens_dict)
    [print(i) for i in sorted(caminhos)]
    assert len(caminhos) == 103


def test_quando_passar_o_mapa_3_deve_contar_3509_caminhos():
    submarino = Submarino()
    passagens_raw = submarino.le_arquivo("assets/passagem_mapa_teste_3.txt")
    passagem = submarino.gera_passagem(passagens_raw)
    passagens_dict = submarino.gera_vizinhos(passagem)
    caminhos = submarino.encontrar_caminhos_2(passagens_dict)
    [print(i) for i in sorted(caminhos)]
    assert len(caminhos) == 3509


def test_quando_abrir_um_arquivo_regtorne_a_string():
    submarino = Submarino()
    manual = submarino.abre_arquivo("manual_teste.txt")

    assert type(manual) == str

def test_quando_separar_manual_criar_uma_lista_de_informacao_instrucao():
    submarino = Submarino()
    manual = submarino.abre_arquivo("manual_teste.txt")
    list_manual = submarino.separa_manual(manual)

    assert type(list_manual) == list


def test_quando_tratar_informcao_retorne_uma_lista_de_cordenadas():
    submarino = Submarino()
    manual = submarino.abre_arquivo("manual_teste.txt")
    list_manual = submarino.separa_manual(manual)
    informacao = submarino.trata_informacao(list_manual)

    assert type(informacao) == list

def test_quando_trata_informacao_trazer_as_cordenadas_corretamente():
    submarino = Submarino()
    manual = submarino.abre_arquivo("manual_teste.txt")
    list_manual = submarino.separa_manual(manual)

    informacao = submarino.trata_informacao(list_manual)
    cordenadas_teste = [
            [6,10],
            [0,14],
            [9,10],
            [0,3],
            [10,4],
            [4,11],
            [6,0],
            [6,12],
            [4,1],
            [0,13],
            [10,12],
            [3,4],
            [3,0],
            [8,4],
            [1,10],
            [2,14],
            [8,10],
            [9,0]
            ]

    print(informacao)
    print(cordenadas_teste)

    assert all( a == b for a, b in zip(sorted(informacao), sorted(cordenadas_teste) ) )

