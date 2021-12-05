"""Advent of Code 2021 do site 'https://adventofcode.com/'."""


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


    def forward(self, valor):
        self.posicao_x += int(valor)
        self.posicao_y += int(valor) * self.posicao_aim        

    def down(self, valor):
        self.posicao_aim += int(valor)
        

    def up(self, valor):
        self.posicao_aim -= int(valor)

    def movimenta(self, lista):
        for item in lista:
            direcao, valor = item.split(" ")
            if direcao == "forward":
                self.forward(valor)
            elif direcao == "up":
                self.up(valor)
            elif direcao == "down":
                self.down(valor)

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