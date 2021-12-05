"""Advent of Code dia 1 do site 'https://adventofcode.com/'."""


class Sonar(object):
    """Defini a classe do sonar do submarino."""

    def relatorio(self, dados: list):
        result = []
        for indice in range(len(dados)):
            if indice == 0:
                result.append("N/A")
            else:
                if dados[indice] > dados[indice - 1]:
                    result.append("aumentou")
                elif dados[indice] < dados[indice - 1]:
                    result.append("diminuiu")
                else:
                    result.append("nao mudou")
        return result

    
    def count_relatorio(self, relatorio, referencia):
        return relatorio.count(referencia)

    
    def le_arquivo(self, caminho):
        lista = []
        with open(caminho, "r") as relatorio:
            lista_linhas = relatorio.read()
        lista_str = list(filter(None, lista_linhas.split("\n")))
        result = list(map(int, lista_str))
        return result


    def somar_tres_medidas(self, lista):
        result = []
        for index in range(len(lista) - 2):
            result.append(lista[index] + lista[index + 1] + lista[index + 2])
        return result


if __name__ == "__main__":
    sonar = Sonar()
    arquivo = "assets/input.txt"
    lista = sonar.le_arquivo(arquivo)
    relatorio = sonar.relatorio(lista)
    resultado = sonar.count_relatorio(relatorio, "aumentou")
    lista_filtro_medidas = sonar.somar_tres_medidas(lista)
    relatorio = sonar.relatorio(lista_filtro_medidas)
    resultado = sonar.count_relatorio(relatorio, "aumentou")
    print(resultado)
    