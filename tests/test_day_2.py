import pytest
from src.day_2 import Controle


def test_quando_ler_arquivo_retornar_uma_lista_de_movimento():
    controle = Controle()
    arquivo = "assets/day2_test.txt"

    lista = controle.le_arquivo(arquivo)

    assert lista == ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_quando_chamar_forward_incrementar_posicao_x():
    controle = Controle()
    
    forward = controle.forward("5")

    assert controle.x == 5

def test_quando_chamar_forward_mais_de_uma_vez_incrementar_posicao_x():
    controle = Controle()
    
    forward = controle.forward("5")
    forward = controle.forward("7")

    assert controle.x == 12



def test_quando_chamar_down_incrementar_mira():
    controle = Controle()
    
    forward = controle.down("5")

    assert controle.aim == 5

def test_quando_chamar_down_mais_de_uma_vez_incrementar_mira():
    controle = Controle()
    
    forward = controle.down("5")
    forward = controle.down("7")

    assert controle.aim == 12


def test_quando_chamar_up_decrementar_mira():
    controle = Controle()
    
    forward = controle.up("5")

    assert controle.aim == -5

def test_quando_chamar_up_mais_de_uma_vez_decrementar_mira():
    controle = Controle()
    
    forward = controle.up("5")
    forward = controle.up("7")

    assert controle.aim == -12

def test_quando_chamar_up_e_down_deve_retornar_o_resultado_y():
    controle = Controle()
    
    forward = controle.up("5")
    forward = controle.down("7")

    assert controle.aim == 2

def test_quando_passar_uma_lista_de_movimento_deve_retornar_o_resultado_da_posicao_x_e_y():

    controle = Controle()
    arquivo = "assets/day2_test.txt"
    lista_de_movimento = controle.le_arquivo(arquivo)

    controle.movimenta(lista_de_movimento)

    assert (controle.x, controle.y) == (15, 60)


