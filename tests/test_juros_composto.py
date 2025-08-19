import pytest
from juros_composto import calcular_juros_compostos


# VALIDANDO CAPITAL ------------------------------------------------------
    # Validação do capital investido como string
def test_validar_capital_string():
    # Definindo a entrada
    capital = 1000
    taxa = 10
    tempo = 3

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O capital investido deve ser um número (int ou float)."):
        calcular_juros_compostos(capital, taxa, tempo)

    # Validação do capital investido como negativo
def test_validar_capital_negativo():
    # Definindo a entrada
    capital = -1000
    taxa = -10
    tempo = -3

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O capital investido não pode ser negativo."):
        calcular_juros_compostos(capital, taxa, tempo)


# VALIDANDO TAXA DE JUROS----------------------------------------------
def test_calcular_taxa_juros_nmr():
    #define entrada
    entrada = 3

    #executando a função e esperando erro
    with pytest.raises(TypeError, match="A taxa de juros deve ser um número (int ou float)."):
        calcular_juros_compostos(entrada)


def test_calcular_taxa_juros_negativo():
    #define entrada
    entrada = -3

    #executando a função e esperando erro
    with pytest.raises(ValueError, match="A taxa de juros não pode ser negativa."):
        calcular_juros_compostos(entrada)


# VALIDANDO TEMPO -------------------------------------------------------
# Validação do tempo
def test_validar_tempo():
    #Definindo a entrada
    entrada = 10

    #executando a função e esperando o erro
    with pytest.raises(ValueError, match="O tempo deve ser um número (int ou float)."):
        calcular_juros_compostos(entrada)

# validando negativo
def test_validar_tempo_negativo():
    # Definindo a entrada
    entrada = -10

    # executando a função e esperando o erro
    with pytest.raies(TypeError, match="O tempo não pode ser negativo."):
        calcular_juros_compostos(entrada)

