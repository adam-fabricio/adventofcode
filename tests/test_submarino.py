from src.submarino import (Submarino, 
                           Cartela)
import pytest

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

def test_somar_tres_proximos_valores_da_lista():
    valor_inicial = "assets/input_test.txt"
    resultado = "assets/dados_3_medidas.txt"
    submarino = Submarino()
    lista_inicial = submarino.le_arquivo(valor_inicial)
    lista_resultado = submarino.le_arquivo(resultado)
    
    assert list(map(str,submarino.sonar_filtro(lista_inicial))) == lista_resultado


def test_gerar_relatorio_do_test_filtrado_pela_soma_dos_tres_valores():
    valor_inicial = "assets/input_test.txt"
    resultado = "assets/dados_3_medidas.txt"
    submarino = Submarino()
    lista_inicial = submarino.le_arquivo(valor_inicial)
    lista_resultado = submarino.le_arquivo(resultado) 
    
    assert  submarino.sonar(lista_resultado) == ["N/A", "aumentou", "nao mudou", "diminuiu", "aumentou", "aumentou", "aumentou", "aumentou"]

def test_ao_receber_um_conjunto_de_bit_deve_segregar_os_bits():
    submarino = Submarino()
    entrada = "10100"
    saida = [1, 0, 1, 0, 0]

    dicionario = submarino.separa_bit_do_diagnostico(entrada)

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

def test_adicionar_linha_na_cartela_deve_adicionar_linha_a_cartela():
    cartela = Cartela()
    dados_teste = '22 13 17 11  0'
    dados_teste2 = ' 8  2 23  4 24'

    cartela.adicionar_linha(dados_teste)

    assert cartela.cartela == [[22, 13, 17, 11, 0]]
    
    cartela.adicionar_linha(dados_teste2)

    assert cartela.cartela == [[22, 13, 17, 11, 0], [8,  2, 23,  4, 24]]

def test_ao_passar_os_dados_deve_cirar_as_cartelas():
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

def test_quando_receber_uma_tupla_deve_marcar_as_linhas_em_um_mapa():
    submarino = Submarino()
    caminho = "assets/lista_turbilhoes_teste.txt"
    lista_turbilhao = submarino.le_arquivo(caminho)
    
    cordenadas_0 = submarino.converte_para_cordenadas(lista_turbilhao[0])
    mapa_turbilhao_0 = submarino.marca_no_mapa(cordenadas_0)


    cordenadas_2 = submarino.converte_para_cordenadas(lista_turbilhao[3])

    mapa_turbilhao_1 = submarino.marca_no_mapa(cordenadas_2)


    assert mapa_turbilhao_0 == {"0, 9": 1, "1, 9": 1, "2, 9": 1, "3, 9": 1, "4, 9": 1, "5, 9": 1}
    assert mapa_turbilhao_1 == {"0, 9": 1, "1, 9": 1, "2, 9": 1, "3, 9": 1, "4, 9": 1, "5, 9": 1}
    assert True == False

"""
def test_quando_receber_uma_lista_de_cordenadas_deve_desenhar_no_mapa():
    submarino = Submarino()
    caminho = "assets/lista_turbilhoes_teste.txt"
    lista_turbilhao = submarino.le_arquivo(caminho)
    
    cordenada_1 = submarino.converte_para_cordenadas(lista_turbilhao[1])
    mapa_turbilhao = submarino.marca_no_mapa(cordenada_1)

""" 