from src.submarino import Submarino
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


