
from pathlib import Path
from direcoes import (DIREITA, ESQUERDA)
from simbolos_nao_usados import FIM_FITA, INICIO_FITA, SIMBOLO_BRANCO_NOVO
from simbolos import (BRANCO, QUALQUER_COISA)
from estados import (
    ESTADO_ESTACIONARIO, ESTADO_INICIAL_NOVO, ESTADO_INICIAL_REAL, ESTADO_INSERCAO_FINAL0, ESTADO_INSERCAO_FINAL1, ESTADO_INSERCAO_FINAL2, ESTADO_INSERSAO_INICIO)
from typing import List


def read_file(fp: str) -> List[str]:
    with Path(fp).open("r") as file:
        return file.readlines()


def save_file(fp: str, content: List[str]) -> None:
    with Path(fp).open("w+") as file:
        return file.writelines(content)


def parse_all(content: List[str]) -> List[str]:
    parsed_content: List[str] = list()
    for line in content:
        if line.startswith(";"):
            # Comentário
            continue
        # Ler linha
        (
            estado_atual,
            simbolo_leitura,
            direcao,
            simbolo_escrita,
            proximo_estado,
            *_  # resto, desprezar
        ) = line.strip().split(" ")

        parsed = parse(estado_atual, simbolo_leitura,
                       simbolo_escrita, direcao, proximo_estado)

        parsed_content.extend(parsed)

    return parsed_content


def parse(estado_atual: str, simbolo_leitura: str, direcao: str, simbolo_escrita: str, proximo_estado: str) -> List[str]:
    if estado_atual == ESTADO_INICIAL_REAL:
        estado_atual = ESTADO_INICIAL_NOVO
    if proximo_estado == ESTADO_INICIAL_REAL:
        proximo_estado = ESTADO_INICIAL_NOVO
    if simbolo_leitura == BRANCO:
        simbolo_leitura = SIMBOLO_BRANCO_NOVO
    if simbolo_escrita == BRANCO:
        simbolo_escrita = SIMBOLO_BRANCO_NOVO
    if direcao == QUALQUER_COISA:
        return simular_movimento_estacionario(
            estado_atual, simbolo_leitura, simbolo_escrita, proximo_estado)
    elif simbolo_leitura == SIMBOLO_BRANCO_NOVO:
        return [
            f"{estado_atual} {simbolo_leitura} {simbolo_escrita} {direcao} {proximo_estado}\n",
            *simular_operacao_fim_da_fita(estado_atual)
        ]
    return [f"{estado_atual} {simbolo_leitura} {simbolo_escrita} {direcao} {proximo_estado}\n", ]


def simulador_fita_ui_para_di() -> List[str]:
    # As duas primeiras operações colocam £ no inicio da fita
    # A terceira operação simula o movimento a esquerda no inicio da fita para uma máquina do Sipser
    return [
        f"{ESTADO_INICIAL_REAL} {QUALQUER_COISA} {QUALQUER_COISA} {ESQUERDA} {ESTADO_INSERSAO_INICIO}\n",
        f"{ESTADO_INSERSAO_INICIO} {BRANCO} {INICIO_FITA} {DIREITA} {ESTADO_INSERCAO_FINAL0}\n",
        f"{QUALQUER_COISA} {INICIO_FITA} {INICIO_FITA} {DIREITA} {QUALQUER_COISA}\n"
    ]


count_movimento_estacionario = 0


def simular_movimento_estacionario(estado_atual, simbolo_leitura, simbolo_escrita, proximo_estado) -> List[str]:
    global count_movimento_estacionario
    count_movimento_estacionario += 1
    return [
        f"{estado_atual} {simbolo_leitura} {simbolo_escrita} {DIREITA} {ESTADO_ESTACIONARIO}{count_movimento_estacionario}\n",
        f"{ESTADO_ESTACIONARIO}{count_movimento_estacionario} {QUALQUER_COISA} {QUALQUER_COISA} {ESQUERDA} {proximo_estado}\n"
    ]


def simulador_fita_limitador_fim() -> List[str]:
    # As duas primeiras operações colocam £ no inicio da fita
    # A terceira operação simula o movimento a esquerda no inicio da fita para uma máquina do Sipser
    return [
        # Move para esquerda
        f"{ESTADO_INSERCAO_FINAL0} {QUALQUER_COISA} {QUALQUER_COISA} {DIREITA} {ESTADO_INSERCAO_FINAL0}\n",
        # Chega no primeiro branco, escreve fim da fita, começa a retornar
        f"{ESTADO_INSERCAO_FINAL0} {BRANCO} {FIM_FITA} {ESQUERDA} {ESTADO_INSERCAO_FINAL1}\n",
        # Chegando no inicio, volta ao começo, e para o estado inicial
        f"{ESTADO_INSERCAO_FINAL1} {QUALQUER_COISA} {QUALQUER_COISA} {ESQUERDA} {ESTADO_INSERCAO_FINAL1}\n",
        f"{ESTADO_INSERCAO_FINAL1} {INICIO_FITA} {INICIO_FITA} {DIREITA} {ESTADO_INICIAL_NOVO}\n",
    ]


count_fim_fita = 0


def simular_operacao_fim_da_fita(estado_atual: str):
    # Sempre que ler fim da fita, escreve novo branco, move para direita, insere fim da fita, e volta para a esquerda
    global count_fim_fita
    count_fim_fita += 1
    return [
        f"{estado_atual} {FIM_FITA} {SIMBOLO_BRANCO_NOVO} {DIREITA} {ESTADO_INSERCAO_FINAL2}{count_fim_fita}\n",
        f"{ESTADO_INSERCAO_FINAL2}{count_fim_fita} {BRANCO} {FIM_FITA} {ESQUERDA} {estado_atual}\n"
    ]


def main():
    operacoes: List[str] = list()
    operacoes.extend(simulador_fita_ui_para_di())
    operacoes.extend(simulador_fita_limitador_fim())
    unparsed_content = read_file("./data/entrada.in")
    operacoes.extend(parse_all(unparsed_content))
    save_file("./data/saida.out", operacoes)


if __name__ == "__main__":
    main()
