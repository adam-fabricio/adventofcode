"""Advent of Code dia 2 do site 'https://adventofcode.com/'."""


class Controle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def le_arquivo(self, caminho):
        with open(caminho) as arq:
            linhas = arq.read()
        lista = linhas.split("\n")[:-1]
        return lista
    

    def forward(self, valor):
        self.x += int(valor)
        self.y += int(valor) * self.aim        

    def down(self, valor):
        self.aim += int(valor)
        

    def up(self, valor):
        self.aim -= int(valor)

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
    controle = Controle()
    lista_de_movimento = controle.le_arquivo("assets/day2.txt")
    controle.movimenta(lista_de_movimento)
    print(controle.x, controle.y)
    print(controle.x * controle.y)
