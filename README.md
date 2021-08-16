# Tradutor MT
Autor: Otávio Almeida

## Instruções
O projeto requer a utilização de Python 3.9, ou mais recente, sendo que foi desenvolvido em Python 3.10.

Coloque a entrada no arquivo data/entrada.in

Rode com o comando:
```bash
python3.10 tradutor_mt/tradutor.py
```

A saída estará no arquivo data/saida.out. 

## Restrições
O tradutor utiliza alguns estados auxiliares, assim, o programa de entrada não pode esses mesmos estados, são eles:

    - estado_inicio_novo
    - estado_insercao_inicio
    - estado_insercao_fim0
    - estado_insercao_fim1
    - estado_insercao_fim2, sendo este uma expressão, será criado vários estados que começam com estado_insercao_fim2, dependendo da necessidade
    - estado_estacionario, sendo este uma expressão, será criado vários estados que começam com estado_estacionario, dependendo da necessidade

## Explicação
O tradutor começa colocando £ no inicio da fita, para simular uma fita limita a esquerda, assim, sempre que o cabeçote lê £, ele simplesmente volta para a direita.

Então o tradutor colocar § no final da fita, para que o infinitos brancos a direita não atrapalhem o processamento. Assim, sempre que o cabeçote lê §, ele insere ¢, vai para a direita, adiciona §, e volta para a esquerda, resumindo a operação.

Todas as operações que leem ou escrevem branco são trocadas por ¢, assim, o programa não pode mais escrever branco.

Operações com movimento estacionário são trocados por um movimento a direita, e então por um movimento a esquerda.

O restante das operações são apenas copiadas.
