import pytest
from src.day_1 import Sonar


dados = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
relatorio = ["N/A", "aumentou", "aumentou", "aumentou", "diminuiu", "aumentou", "aumentou", "aumentou","diminuiu", "aumentou"]



def test_quando_gerar_relatorio_primeiro_item_e_NA():
    sonar = Sonar()
    
    assert sonar.relatorio(dados)[0] == relatorio[0]


def test_quando_gerar_relatorio_deve_retornar_uma_lista_informando_se_o_valor_e_maior_que_o_anterior():
    sonar = Sonar()

    assert sonar.relatorio(dados) == relatorio

def test_quando_passar_um_relatorio_contar_ocorrencia_do_valor():
    sonar = Sonar()
    relatorio = sonar.relatorio(dados)
    assert sonar.count_relatorio(relatorio, "aumentou") == 7

def test_quando_passar_um_arquivo_transformar_em_lista():
    arquivo = "assets/input_test.txt"
    sonar = Sonar()
    lista = sonar.le_arquivo(arquivo)
    
    assert lista == dados

def test_somar_tres_proximos_valores_da_lista():
    valor_inicial = "assets/input_test.txt"
    resultado = "assets/dados_3_medidas.txt"
    sonar = Sonar()
    lista_inicial = sonar.le_arquivo(valor_inicial)
    lista_resultado = sonar.le_arquivo(resultado)
    
    assert sonar.somar_tres_medidas(lista_inicial) == lista_resultado


def test_gerar_relatorio_do_test_filtrado_pela_soma_dos_tres_valores():
    valor_inicial = "assets/input_test.txt"
    resultado = "assets/dados_3_medidas.txt"
    sonar = Sonar()
    lista_inicial = sonar.le_arquivo(valor_inicial)
    lista_resultado = sonar.le_arquivo(resultado) 
    
    assert  sonar.relatorio(lista_resultado) == ["N/A", "aumentou", "nao mudou", "diminuiu", "aumentou", "aumentou", "aumentou", "aumentou"]

    