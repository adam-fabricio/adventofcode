"""Advent of Code 2021 do site 'https://adventofcode.com/'."""


import os


class Bingo():

    def __init__(self):
        self.cartelas = []
        self.resultado = 0
        self.cartela_vencedora = []
        self.resultado_vencedor = []

    def gera_numeros_sorteados(self, lista_bingo: list) -> list:
        return [int(i) for i in lista_bingo[0].split(",") if i]
    
    def criar_cartelas(self, lista_bingo: list) -> object:
        for i in range(len(lista_bingo)):
        
            if not i:
                pass
            elif i == len(lista_bingo) -1:
                self.cartelas[-1].adicionar_linha(lista_bingo[i])
            elif not lista_bingo[i] and lista_bingo[i+1]:
                self.cartelas.append(Cartela())
            
            elif lista_bingo[i] and lista_bingo[i+1]:
                self.cartelas[-1].adicionar_linha(lista_bingo[i])
            
            else:
                self.cartelas[-1].adicionar_linha(lista_bingo[i])
            
    def jogar(self, dados_do_bingo: list) -> int:
        numeros_sorteados = self.gera_numeros_sorteados(dados_do_bingo)
        self.criar_cartelas(dados_do_bingo)
        for numero in numeros_sorteados:
            for cartela in self.cartelas:
                if cartela.marcar_numero(numero):
                    self.resultado = cartela.bingo
                    break
            if self.resultado:
                break

    def jogar_2(self, dados_do_bingo: list) -> int:
        numeros_sorteados = self.gera_numeros_sorteados(dados_do_bingo)
        self.criar_cartelas(dados_do_bingo)
        for numero in numeros_sorteados:
            for i, cartela in enumerate(self.cartelas):
                if cartela.marcar_numero(numero):
                    if self.cartela_vencedora == []:
                        self.cartela_vencedora.append(i)
                        self.resultado_vencedor.append(cartela.bingo)
                    elif not i in self.cartela_vencedora:
                        self.cartela_vencedora.append(i)
                        self.resultado_vencedor.append(cartela.bingo)


class Cartela():

    def __init__(self):
        self.cartela = []
        self.ultima_posicao = False
        self.bingo = 0

    def adicionar_linha(self, linha: str) -> None:

        self.cartela.append([int(i) for i in linha.split(" ") if i])

    def marcar_numero(self, numero: int) -> None:
        try:
            linha, coluna = [(lin, col.index(numero)) for lin, col in enumerate(self.cartela) if numero in col][0]
            self.cartela[linha][coluna] = -1
            self.ultima_posicao = (linha, coluna)
        except IndexError:
            self.ultima_posicao = False
        
        if self.verifica_bingo():
            self.bingo = self.somar_cartela() * numero
            return True

    def verifica_bingo(self) -> str:
        if self.ultima_posicao:
            if sum(self.cartela[self.ultima_posicao[0]]) == -5 or sum(list(zip(*self.cartela))[self.ultima_posicao[1]]) == -5:
                return "BINGO"
   
    def somar_cartela(self) -> int:
        return sum([num for row in self.cartela for num in row if num > -1])


class Submarino(object):
    """A classe submarino, implementa as funções comuns entre outras."""
    def __init__(self):
        """Define variaveis comuns do submarino."""
        
        self.posicao_x = 0
        self.posicao_y = 0
        self.posicao_aim = 0
        self.bingo = Bingo()

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

    def converte_linha_em_lista(self, lista: str) -> list:
        """Individualiza os bits da cadeia e forma um dicionario"""

        return list(map(int, list(lista)))

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
            
            elif lista_bit[bits] == len(relatorio) * 0.5:
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

    def dividir_lista(self, relatorio: list, bit_change: str) -> list:
        resultado = [i for i in relatorio if bit_change == i[:len(bit_change)]]
        return resultado

    def calcular_gerador_oxigenio(self, relatorio:list, comum_bit: str = "") -> int:

        if len(relatorio) == 1:
            resultado_consolidado = self.consolidar_relatorio(relatorio)
            return self.calcula_gamma(resultado_consolidado)
        
        else:
            consolidado = self.consolidar_relatorio(relatorio)
            comum_bit += str(consolidado[f"bit_{len(consolidado) - 1 - len(comum_bit)}"])
            novo_consolidado = self.dividir_lista(relatorio, comum_bit)
            return self.calcular_gerador_oxigenio(novo_consolidado, comum_bit)

    def calcular_purificador_de_CO2(self, relatorio:list, comum_bit: str = "") -> int:

        if len(relatorio) == 1:
            resultado_consolidado = self.consolidar_relatorio(relatorio)
            return self.calcula_gamma(resultado_consolidado)
        
        else:
            consolidado = self.consolidar_relatorio(relatorio) 
            if consolidado[f"bit_{len(consolidado) - 1 - len(comum_bit)}"]:
                comum_bit += "0"
            else:
                comum_bit += "1"
            novo_consolidado = self.dividir_lista(relatorio, comum_bit)
            return self.calcular_purificador_de_CO2(novo_consolidado, comum_bit)
        
    def converte_para_cordenadas(self, cordenadas: str) -> list:
        esquerda, direita = cordenadas.split(" -> ")

        return [(int(esquerda.split(",")[0]), int(esquerda.split(",")[1])), 
                (int(direita.split(",")[0]), int(direita.split(",")[1]))]

    def marca_no_mapa(self, cordenadas: list, mapa:dict = {}) -> dict:
        if cordenadas[0][0] == cordenadas[1][0]:
            if cordenadas[1][1] - cordenadas[0][1]  < 0:
                cordenadas[1], cordenadas[0] = cordenadas[0], cordenadas[1]
            for i in range(cordenadas[1][1] - cordenadas[0][1] + 1) :
                try:
                    mapa[f"{cordenadas[0][0]}, {cordenadas[0][1] + i}"] += 1
                except:
                    mapa[f"{cordenadas[0][0]}, {cordenadas[0][1] + i}"] = 1
        elif cordenadas[0][1] == cordenadas[1][1]:
            if cordenadas[1][0] - cordenadas[0][0] < 0:
                cordenadas[1], cordenadas[0] = cordenadas[0], cordenadas[1]
            for i in range(cordenadas[1][0] - cordenadas[0][0] + 1):
                try:
                    mapa[f"{cordenadas[0][0] + i}, {cordenadas[0][1]}"] += 1
                except:
                    mapa[f"{cordenadas[0][0] + i}, {cordenadas[0][1]}"] = 1
        elif cordenadas[0][0] - cordenadas[1][0] == cordenadas[1][1] - cordenadas[0][1]:
            if cordenadas[1][0] - cordenadas[0][0] < 0:
                cordenadas[1], cordenadas[0] = cordenadas[0], cordenadas[1]
            for i in range(cordenadas[1][0] - cordenadas[0][0] + 1):
                try:
                    mapa[f"{cordenadas[0][0] + i}, {cordenadas[0][1] - i}"] += 1
                except:
                    mapa[f"{cordenadas[0][0] + i}, {cordenadas[0][1] - i}"] = 1
        elif cordenadas[0][0] - cordenadas[1][0] == cordenadas[0][1] - cordenadas[1][1]:          
            if cordenadas[1][0] - cordenadas[0][0] < 0:
                cordenadas[1], cordenadas[0] = cordenadas[0], cordenadas[1]
            for i in range(cordenadas[1][0] - cordenadas[0][0] + 1):
                try:
                    mapa[f"{cordenadas[0][0] + i}, {cordenadas[0][1] + i}"] += 1
                except:
                    mapa[f"{cordenadas[0][0] + i}, {cordenadas[0][1] + i}"] = 1
        return mapa

    def pontos_criticos(self, mapa: dict) -> list:
        pontos_criticos = []
        for cordenadas, valor in mapa.items():
            if valor > 1:
                pontos_criticos.append(cordenadas)
        return pontos_criticos

    def proximo_dia_lanterfish(self, lista_de_idade: list) -> list:
        for i in range(len(lista_de_idade)):
            lista_de_idade[i] = int(lista_de_idade[i])
            if lista_de_idade[i] == 0:
                lista_de_idade[i] = 6
                lista_de_idade.append(8)
            else:
                lista_de_idade[i] -= 1
        return lista_de_idade
    
    def dicionario_de_ciclo(self, lista_de_idade: list) -> dict:
        dicionario = {}
        dicionario["ciclo_8"] = lista_de_idade.count("8")
        dicionario["ciclo_7"] = lista_de_idade.count("7")
        dicionario["ciclo_6"] = lista_de_idade.count("6")
        dicionario["ciclo_5"] = lista_de_idade.count("5")
        dicionario["ciclo_4"] = lista_de_idade.count("4")
        dicionario["ciclo_3"] = lista_de_idade.count("3")
        dicionario["ciclo_2"] = lista_de_idade.count("2")
        dicionario["ciclo_1"] = lista_de_idade.count("1")
        dicionario["ciclo_0"] = lista_de_idade.count("0")
        return dicionario
        
    def proximo_dia_dicionario(self, dicionario: dict) -> dict:
        buffer = dicionario["ciclo_8"]
        (
            dicionario["ciclo_8"], dicionario["ciclo_7"], 
            dicionario["ciclo_6"], dicionario["ciclo_5"], 
            dicionario["ciclo_4"], dicionario["ciclo_3"], 
            dicionario["ciclo_2"], dicionario["ciclo_1"], 
            dicionario["ciclo_0"]
        ) = (
            dicionario["ciclo_0"], dicionario["ciclo_8"], 
            dicionario["ciclo_7"] + dicionario["ciclo_0"], 
            dicionario["ciclo_6"], dicionario["ciclo_5"], 
            dicionario["ciclo_4"], dicionario["ciclo_3"], 
            dicionario["ciclo_2"], dicionario["ciclo_1"], 
        )
        return dicionario

    def mediana_lista_caranguejos(self, lista_de_caranguejos: list) -> int:
        lista_de_caranguejos.sort()
        index = len(lista_de_caranguejos)/2
        return lista_de_caranguejos[int(index)]

    def transforma_lista_de_str_em_int(self, lista_str: list) -> list:
        return (list(map(int, list(lista_str.split(",")))))

    def calculo_combustivel(self, lista_posicao: list, posicao_final:int) -> int:
        combustivel = 0
        for posicao in lista_posicao:
            combustivel += ((posicao - posicao_final)**2)**(0.5)
        return combustivel

    def calculo_combustivel_real(self, posicao_inicial:int , posical_final:int) -> int:
        combustivel = 0
        for i in range(int(((posical_final - posicao_inicial)**2)**0.5)):
            combustivel += (((posical_final - posicao_inicial)**2)**0.5) - i
        return combustivel

    def calculo_lista_combustivel_real(self, lista_posicao:list, posicao_final: int) -> int:
        combustivel = 0
        for posicao in lista_posicao:
            combustivel += self.calculo_combustivel_real(posicao, posicao_final)
        return combustivel

    def dividir_lista_metade(self, lista:list) -> list:
        metade = int(round(len(lista)/2))
        return [lista[:metade], lista[metade + 1:]]
    
    def calculo_minimo_combustivel_real(self, lista_posicao: list, media: int):
        combustivel = self.calculo_lista_combustivel_real(lista_posicao, media)
        combustivel_mais = self.calculo_lista_combustivel_real(lista_posicao, media + 1)
        combustivel_menos = self.calculo_lista_combustivel_real(lista_posicao, media - 1)
        if combustivel <= combustivel_mais and combustivel <= combustivel_menos:
            return combustivel
        elif combustivel > combustivel_mais:
            media += 1
            return self.calculo_minimo_combustivel_real(lista_posicao, media)
        else:
            media -= 1
            return self.calculo_minimo_combustivel_real(lista_posicao, media)

    def converter_lista_de_sinais(self, sinal: str) -> dict:
        dicionario = {}
        lista_sinal = sinal.split(" | ")
        dicionario["input"] = lista_sinal[0].split(" ")
        dicionario["output"] = lista_sinal[1].split(" ")
        return dicionario
    
    def contar_saida_1_4_7_8(self, sinal: dict) -> int:
        resultado = 0
        for segmento in sinal["output"]:
            if len(segmento) in [2, 3, 4 , 7]:
                resultado += 1
        return resultado

    def decodifica_sete_segmentos(self, lista_input: list) -> dict:
        decodificador = {}
        lista_decodificador = [["z"]]*10
        i = 0
        while len(decodificador) < 10:
            for sinal in lista_input:
                if len(sinal) == 2:
                    lista_sinal = list(sinal)
                    lista_sinal.sort()
                    decodificador["".join(lista_sinal)] = 1
                    lista_decodificador[1] = lista_sinal
                    lista_input.remove(sinal)
                elif len(sinal) == 3:
                    lista_sinal = list(sinal)
                    lista_sinal.sort()
                    decodificador["".join(lista_sinal)] = 7
                    lista_decodificador[7] = lista_sinal
                    lista_input.remove(sinal)
                elif len(sinal) == 4:
                    lista_sinal = list(sinal)
                    lista_sinal.sort()
                    lista_decodificador[4] = lista_sinal
                    decodificador["".join(lista_sinal)] = 4
                    lista_input.remove(sinal)
                elif len(sinal) == 7:
                    lista_sinal = list(sinal)
                    lista_sinal.sort()
                    decodificador["".join(lista_sinal)] = 8
                    lista_decodificador[8] = lista_sinal
                    lista_input.remove(sinal)
                elif len(sinal) == 5:
                    lista_sinal = list(sinal)
                    lista_sinal.sort()
                    if all(item in lista_sinal for item in lista_decodificador[1]):
                        decodificador["".join(lista_sinal)] = 3
                        lista_decodificador[3] = lista_sinal
                        lista_input.remove(sinal)
                    elif all(item in lista_decodificador[3] + lista_decodificador[4] for item in lista_sinal):
                        decodificador["".join(lista_sinal)] = 5
                        lista_decodificador[5] = lista_sinal
                        lista_input.remove(sinal)
                    elif lista_decodificador[5] != ["z"] and lista_decodificador[3] != ["z"]:
                        decodificador["".join(lista_sinal)] = 2
                        lista_decodificador[2] = lista_sinal
                        lista_input.remove(sinal)
                elif len(sinal) == 6:
                    lista_sinal = list(sinal)
                    lista_sinal.sort()
                    if all(item in lista_sinal for item in lista_decodificador[3] + lista_decodificador[4]):
                        decodificador["".join(lista_sinal)] = 9
                        lista_decodificador[9] = lista_sinal
                        lista_input.remove(sinal)
                    elif lista_decodificador[9] != ["z"] and all(item in lista_sinal for item in lista_decodificador[1]):
                        decodificador["".join(lista_sinal)] = 0
                        lista_decodificador[0] = lista_sinal
                        lista_input.remove(sinal)
                    elif lista_decodificador[9] != ["z"] and lista_decodificador[0] != ["z"]:
                        decodificador["".join(lista_sinal)] = 6
                        lista_decodificador[6] = lista_sinal
                        lista_input.remove(sinal)
        return decodificador
    
    def decodificador_saida(self, lista_saida: list, decodificador: dict):
        for i in range(len(lista_saida)):
            lista_saida[i] = list(lista_saida[i])
            lista_saida[i].sort()
            lista_saida[i] = decodificador["".join(lista_saida[i])]
            lista_saida[i] = lista_saida[i] * 10**(len(lista_saida) -1 - i)
        return sum(lista_saida)
    
    def soma_das_saidas(self, lista_de_sinais: list) -> int:
        resultado = 0
        for sinais in lista_de_sinais:
            sinains_separados = self.converter_lista_de_sinais(sinais)
            decodificador = self.decodifica_sete_segmentos(sinains_separados["input"])
            valor_decodificado = self.decodificador_saida(sinains_separados["output"], decodificador)
            resultado += valor_decodificado
        return resultado

    def gera_mapa_de_altura(self, mapa_de_altura_raw: list) -> list:
        mapa = []
        for linha in mapa_de_altura_raw:
            lista = list(linha)
            lista_inteiro = [int(i) for i in lista]
            mapa.append(lista_inteiro)
        return mapa
    
    def lista_adjacentes(self, mapa: list, posicao: tuple) -> list:
        numero_linhas = len(mapa)
        numero_coluna = len(mapa[0])
        adjacente = []
        if posicao[0] != 0:
            adjacente.append((posicao[0] - 1, posicao[1]))
        if posicao[0] != numero_linhas - 1:
            adjacente.append((posicao[0] + 1, posicao[1]))
        if posicao[1] != 0:
            adjacente.append((posicao[0], posicao[1] - 1))
        if posicao[1] != numero_coluna - 1:
            adjacente.append((posicao[0], posicao[1] + 1))
        return(adjacente)
    
    def soma_do_menor_level_de_risco(self, mapa: list) -> int:
        resultado = 0
        for l in range(len(mapa)):
            for c in range(len(mapa[0])):
                adjacentes = self.lista_adjacentes(mapa,(l,c))
                acumulador = 0
                for p in adjacentes:
                    if mapa[l][c] >= mapa[p[0]][p[1]]:
                        acumulador = 1
                if acumulador == 0:
                    resultado += mapa[l][c] + 1
        return resultado
    
    def lista_menores_pontos(self, mapa:list) -> list:
        resultado = []
        for l in range(len(mapa)):
            for c in range(len(mapa[0])):
                adjacentes = self.lista_adjacentes(mapa,(l,c))
                acumulador = 0
                for p in adjacentes:
                    if mapa[l][c] >= mapa[p[0]][p[1]]:
                        acumulador = 1
                if acumulador == 0:
                    resultado.append((l, c))
        return resultado

    def calcula_tamanho_bacia(self, mapa:list, posicao: tuple, visitados: list) -> int:
        resultado = 0
        adjacentes = self.lista_adjacentes(mapa, posicao)
        for v in visitados:
            if v in adjacentes:
                adjacentes.remove(v)
        for p in adjacentes:
            if mapa[p[0]][p[1]] < 9:
                for a in adjacentes:
                    visitados.append(a)
                visitados.append(posicao)
                resultado += self.calcula_tamanho_bacia(mapa, (p[0], p[1]), visitados)
        return resultado + 1
        
    def calcula_tamanho_de_todas_bacias(self, mapa: list) -> list:
        lista_pontos_criticos = self.lista_menores_pontos(mapa)
        tamanho_bacia = []
        for pontos_criticos in lista_pontos_criticos:
            tamanho_bacia.append(self.calcula_tamanho_bacia(mapa, pontos_criticos, []))
        
        return tamanho_bacia

    def verifica_tres_maiores_bacias(self, lista_tamanhos_bacia: list) -> list:
        lista_tamanhos_bacia.sort()
        return lista_tamanhos_bacia[-3:]

    def verifica_corrupcao_linha(self, linha_navegacao: list, caracter_abertos: list = []) -> str:
        caracter_abertura = ["[", "(", "{", "<"]
        caracter_fechamento = ["]", ")", "}", ">"]
        if linha_navegacao:
            caracter_atual = linha_navegacao.pop(0)
        else:
            return 
        
        if caracter_atual in caracter_abertura:
            caracter_abertos.append(caracter_atual)
            return self.verifica_corrupcao_linha(linha_navegacao, caracter_abertos)
        else:
            if caracter_fechamento.index(caracter_atual) == caracter_abertura.index(caracter_abertos.pop()):
                return self.verifica_corrupcao_linha(linha_navegacao, caracter_abertos)
            else:
                return caracter_atual
                
    def verifica_corrupcao_arquivo(self, subsitema_navegacao: list) -> list:
        lista_erros = []

        for linha in subsitema_navegacao:
            erro = self.verifica_corrupcao_linha(list(linha))
            if erro:
                lista_erros.append(erro)
        
        return lista_erros
 
    def calcula_pontos_erros(self, lista_erros:list) -> list:
        for i in range(len(lista_erros)):
            if lista_erros[i] == ")":
                lista_erros[i] = 3
            elif lista_erros[i] == "]":
                lista_erros[i] = 57
            elif lista_erros[i] == "}":
                lista_erros[i] = 1197
            elif lista_erros[i] == ">":
                lista_erros[i] = 25137
        return lista_erros

    def remove_linhas_de_erro_de_navegacao(self, subsitema_navegacao: list) -> list:
        sistema_navegacao_sem_erros = []
        for i in range(len(subsitema_navegacao)):
            erro = self.verifica_corrupcao_linha(list(subsitema_navegacao[i]))
            if not erro:
                sistema_navegacao_sem_erros.append(subsitema_navegacao[i])
                
        return sistema_navegacao_sem_erros
    
    def gera_lista_caracter_abertos(self, linha_navegacao: list, caracter_abertos: list = []) -> str:
        caracter_abertura = ["[", "(", "{", "<"]
        caracter_fechamento = ["]", ")", "}", ">"]
        if linha_navegacao:
            caracter_atual = linha_navegacao.pop(0)
        else:
            return caracter_abertos
        
        if caracter_atual in caracter_abertura:
            caracter_abertos.append(caracter_atual)
            return self.gera_lista_caracter_abertos(linha_navegacao, caracter_abertos)
        else:
            if caracter_fechamento.index(caracter_atual) == caracter_abertura.index(caracter_abertos.pop()):
                return self.gera_lista_caracter_abertos(linha_navegacao, caracter_abertos)
            else:
                return caracter_atual

    def inverte_lista_caracter(self, lista_caracter_aberto: list) -> list:
        caracter_abertura = ["[", "(", "{", "<"]
        caracter_fechamento = ["]", ")", "}", ">"]
        
        for i in range(len(lista_caracter_aberto)):
            index = caracter_abertura.index(lista_caracter_aberto[i])
            lista_caracter_aberto[i] = caracter_fechamento[index]
        
        return lista_caracter_aberto
        
    def calcula_pontos_faltantes(self, caracters_faltantes: list) -> int:
        caracters_faltantes = caracters_faltantes[::-1]
        
        for i in range(len(caracters_faltantes)):
            if caracters_faltantes[i] == ")":
                caracters_faltantes[i] = 1
            elif caracters_faltantes[i] == "]":
                caracters_faltantes[i] = 2
            elif caracters_faltantes[i] == "}":
                caracters_faltantes[i] = 3
            elif caracters_faltantes[i] == ">":
                caracters_faltantes[i] = 4
        pontos = 0
        for ponto in caracters_faltantes:
            pontos = pontos * 5 + ponto
        
        return pontos

    def calcula_lista_pontos_faltantes(self, lista_navegacao: list) -> list:
        pontos = []
        
        for linha in lista_navegacao:
            lista_abertos = self.gera_lista_caracter_abertos(list(linha), [])
            lista_fechado = self.inverte_lista_caracter(lista_abertos)
            pontos.append(self.calcula_pontos_faltantes(lista_fechado))
        
        return pontos

    def calcula_mediana_lista(self, lista_de_pontos: list) -> int:
        lista_de_pontos.sort()
        mediana = int(len(lista_de_pontos) / 2)
        
        return lista_de_pontos[mediana]

    def gera_matriz(self, lista_de_linhas:list) -> list:
        return [[int(lista_de_linhas[linha][coluna]) for coluna in range(len(lista_de_linhas[linha]))] for linha in range(len(lista_de_linhas))]

    def soma_um_na_matriz(self, matriz: list) -> list:
        matriz = [[item + 1 for item in linha] for linha in matriz]
        matriz = self.resolve_piscada_polvo(matriz, [])
        return matriz
    
    def resolve_piscada_polvo(self, matriz: list, ja_piscado: list) -> list:
        quantidade_ja_piscado = len(ja_piscado)
        posicao_acima_10 = [(linha, coluna) for linha in range(len(matriz)) for coluna in range(len(matriz[linha]))  if matriz[linha][coluna] >= 10] 
        for posicao in posicao_acima_10:
            if posicao not in ja_piscado:
                ja_piscado.append(posicao)
                matriz = self.polvo_pisca(matriz, posicao)
        if quantidade_ja_piscado != len(ja_piscado):
            return self.resolve_piscada_polvo(matriz, ja_piscado)
        else:
            matriz = self.remove_maior_dez(matriz)
            return {"matriz":matriz, "piscados": len(ja_piscado)}
        
    def remove_maior_dez(self, matriz: list) -> list:
        return [[0 if item >= 10 else item for item in linha] for linha in matriz] 
        
    def polvo_pisca(self, matriz: list, posicao: tuple) -> list:
        adjacente = self.lista_adjacentes_aprimorado(matriz, posicao)
        for p in adjacente:
            matriz[p[0]][p[1]] += 1
        return matriz

    def imprimi_matriz(self, matriz:list) -> None:
        [print("".join([str(item) for item in linha])) for linha in matriz]
    
    def lista_adjacentes_aprimorado(self, matriz: list, posicao: tuple) -> list:
        numero_linhas = len(matriz)
        numero_coluna = len(matriz[0])
        adjacente = []
        #  Não estou na primeira linha
        if posicao[0] != 0:
            adjacente.append((posicao[0] - 1, posicao[1]))
            #  Nao estou na primeira coluna
            if posicao[1] != 0:
                adjacente.append((posicao[0] - 1, posicao[1] - 1))
            #  Não estou na última coluna
            if posicao[1] != numero_coluna - 1:
                adjacente.append((posicao[0] - 1, posicao[1] + 1))
        # Não estou na ultima linha
        if posicao[0] != numero_linhas - 1:
            adjacente.append((posicao[0] + 1, posicao[1]))
            #Não estou na primeira coluna
            if posicao[1] != 0:
                adjacente.append((posicao[0] + 1, posicao[1] - 1))
            #  Não estou na última coluna
            if posicao[1] != numero_coluna - 1:
                adjacente.append((posicao[0] + 1, posicao[1] + 1))
        if posicao[1] != 0:
            adjacente.append((posicao[0], posicao[1] - 1))
        if posicao[1] != numero_coluna - 1:
            adjacente.append((posicao[0], posicao[1] + 1))
        return(adjacente)

    def energia_apos_passos(self, matriz: list, passos: int) -> list:
        piscadas_total = 0
        for i in range(passos):
            matriz, piscadas = self.soma_um_na_matriz(matriz).values()
            piscadas_total += piscadas
        return {"matriz": matriz, "piscados": piscadas_total}

    def encontra_sincronismo(self, matriz: list):
        passo = 0
        sincronismo = 1
        while sincronismo != 0:
            matriz, piscadas = self.soma_um_na_matriz(matriz).values()
            sincronismo = sum([num for elem in matriz for num in elem])
            passo += 1
        return passo

    def gera_passagem(self, passagens_raw: list) -> list:
        passagem = []
        for item in passagens_raw:
            passagem.append(item.split("-"))
        return passagem
    
    def gera_vizinhos(self, passagem: list) -> dict:
        dicionario = { caverna: [] for cavernas in passagem for caverna in cavernas }
        for vizinho in passagem:
            dicionario[vizinho[0]].append(vizinho[1])
            dicionario[vizinho[1]].append(vizinho[0])
        return dicionario
    
    def encontrar_caminhos(self, vizinhos: dict ) -> list:
        """ Cria uma lista de caminho até o end."""
        self.vizinhos = vizinhos
        self.caminhos = []
        self.busca_por_profundidade("start")

        return self.caminhos

    def busca_por_profundidade(self, posicao: str, caminho: list = [], \
            visitados: set = set() ):
        """ Busca por profindidade. """
        caminho.append(posicao)
        if posicao.islower() and not posicao == "end":
            visitados.add(posicao)
        if posicao == "end":
            self.caminhos.append(caminho)
            return

        for proxima_posicao in self.vizinhos[posicao]:
            if proxima_posicao in visitados:
                continue
            self.busca_por_profundidade(proxima_posicao, caminho.copy(), visitados.copy() )

    def busca_por_profundidade_2(self, posicao: str, \
            caminho: list = [], \
            visitados: set = { "start" }, \
            visitados_2: set = { "start" } ) -> None:
        """ Busca por profindidade. """
        caminho.append(posicao)
        if posicao.islower() and not posicao == "end":
            if posicao in visitados:
                visitados_2.add(posicao)
            else:
                visitados.add(posicao)
        if posicao == "end":
            self.caminhos.append(caminho)
            return

        for proxima_posicao in self.vizinhos[posicao]:
            if proxima_posicao.islower():
                if proxima_posicao in visitados_2:
                    continue
                elif proxima_posicao in visitados and len(visitados_2) == 2:
                    continue
            self.busca_por_profundidade_2(proxima_posicao, caminho.copy(), \
                    visitados.copy(), visitados_2.copy() )


    def encontrar_caminhos_2(self, vizinhos: dict ) -> list:
        """ Cria uma lista de caminho até o end."""
        self.vizinhos = vizinhos
        self.caminhos = []
        self.busca_por_profundidade_2("start")

        return self.caminhos


    def abre_arquivo(self, nome_arquivo: str) -> str:
        with open(os.path.join("assets", nome_arquivo), 'r') as arquivo:
            arquivo = arquivo.read()
        return arquivo


    def separa_manual(self, manual:str ) -> list:
        return manual.split('\n\n')


    def trata_informacao(self, list_manual: list) -> set:
        return { cordenadas  for cordenadas in list_manual[0].splitlines() }

    def trata_instrucao(self, list_manual: list) -> list:
        return [ [instrucao.split()[2][0], int(instrucao.split("=")[1])] for instrucao in list_manual[1].splitlines() ]

    def dobra_folha(self, informacao: set, instrucao: list) -> set:
        eixo, indice = instrucao
        if eixo == "y":
            ref = 1

        else:
            ref = 0
        remove_item = []
        add_item = []
        for cordenadas in informacao:
            cordenada = cordenadas.split(",")
            if int(cordenada[ref]) > indice:
                cordenada[ref] = str(2 * indice - int(cordenada[ref]))
                remove_item.append(cordenadas)
                add_item.append(",".join(cordenada))

        for item in remove_item:
            informacao.remove(item)

        informacao.update(add_item)

        return informacao

    def print_manual(self, informacao: set) -> None:
        for linha in range(8):
            for coluna in range(50):
                if ",".join(map(str, [coluna, linha])) in informacao:
                    print("#", end='')
                else:
                    print(".", end='')
            print()

