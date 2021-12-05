"""Advent of Code 2021 do site 'https://adventofcode.com/'."""


from typing import Dict


class Submarino(object):
    """A classe submarino, implementa as funções comuns entre outras."""
    def __init__(self):
        """Define variaveis comuns do submarino."""
        
        self.posicao_x = 0
        self.posicao_y = 0
        self.posicao_aim = 0


    def le_arquivo(self, caminho: str) -> list:
        """Le os arquivo de entrada e retorna uma lista."""
        with open(caminho) as arq:
            linhas = arq.read()
        lista = linhas.split("\n")[:-1]
        return lista

    def sonar(self, relatorio) -> list:
        """Sonar recebe uma lista de valores e gera uma lista informando se o 
        valor 'aumentou', 'diminuiu', 'não mudou' e o primeiro item é 'N/A'.
        """

        result = []
        for indice in range(len(relatorio)):
            if indice == 0:
                result.append("N/A")
            else:
                if relatorio[indice] > relatorio[indice - 1]:
                    result.append("aumentou")
                elif relatorio[indice] < relatorio[indice - 1]:
                    result.append("diminuiu")
                else:
                    result.append("nao mudou")
        return result


    def sonar_filtro(self, relatorio: list) -> list:
        """Faz um filtro no valor do relatório, gerando um compilado que é a 
        soma dos 3 ultimos valores."""

        result = []
        for index in range(len(relatorio) - 2):
            result.append(int(relatorio[index]) + int(relatorio[index + 1]) + int(relatorio[index + 2]))
        return result

    def sonar_contagem_de_ocorrencia(self, relatorio: list, ocorrencia: list) -> int:
        """Retorna o numero de ocorrencia no relatório."""

        return relatorio.count(ocorrencia)


    def forward(self, valor: str) -> None:
        self.posicao_x += int(valor)
        self.posicao_y += int(valor) * self.posicao_aim        

    def down(self, valor: str) -> None:
        self.posicao_aim += int(valor)
        

    def up(self, valor: str) -> None:
        self.posicao_aim -= int(valor)

    def movimenta(self, lista: list) -> None:
        for item in lista:
            direcao, valor = item.split(" ")
            if direcao == "forward":
                self.forward(valor)
            elif direcao == "up":
                self.up(valor)
            elif direcao == "down":
                self.down(valor)

    def separa_bit_do_diagnostico(self, bits: str) -> list:
        """Individualiza os bits da cadeia e forma um dicionario"""

        return list(map(int, list(bits)))


    def consolidar_relatorio(self, relatorio: list) -> dict:
        """Consolida os valores dos bits."""
        
        quantidade_bits = len(relatorio[0])
        lista_bit = {}
        for index in range(quantidade_bits):
            lista_bit[f"bit_{index}"] = 0


        for item in relatorio:
            for posicao, bit in enumerate(list(map(int, list(item)))):
                if bit:
                    lista_bit[f"bit_{quantidade_bits - posicao - 1}"] += 1

        for bits in lista_bit:
            if lista_bit[bits] > len(relatorio) * 0.5:
                lista_bit[bits] = 1
            else:
                lista_bit[bits] = 0
        
        return lista_bit


    def calcula_gamma(self, consolidado: dict) -> int:

        
        gamma = 0
        


        for indice in consolidado:
            
            gamma += consolidado[indice] * 2 ** int(indice.split("_")[-1])
        
        return gamma
    
    def calcula_epsilon(self, consolidado: dict) -> int:

        epsilon = 0

        for indice in consolidado:
            if consolidado[indice]:
                consolidado[indice] = 0
            else:
                consolidado[indice] = 1
            
            epsilon += consolidado[indice] * 2 ** int(indice.split("_")[-1])

        return epsilon
