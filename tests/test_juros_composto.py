import pytest
from juros_composto import calcular_juros_compostos


# ------------------------------------VALIDANDO STRING ------------------------------------------------------
# capital
def test_validar_capital():
    # Definindo a entrada
    capital = "oi"
    taxa = 10
    tempo = 3

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O capital investido deve ser um número (int ou float)."):
        calcular_juros_compostos(capital, taxa, tempo)
# TAXA
def test_validar_taxa():
    #define entrada
    capital = 1000
    taxa = "oi"
    tempo = 3

    #executando a função e esperando erro
    with pytest.raises(ValueError, match="A taxa de juros deve ser um número (int ou float)."):
        calcular_juros_compostos(capital, taxa, tempo)

# TEMPO
def test_validar_tempo():
    #Definindo a entrada
    capital = 1000
    taxa = 10
    tempo = "oi"

    #executando a função e esperando o erro
    with pytest.raises(ValueError, match="O tempo deve ser um número (int ou float)."):
        calcular_juros_compostos(capital, taxa, tempo)

# ------------------------------------VALIDANDO NEGATIVO ----------------------------------------------------
# CAPITAL
def test_validar_capital_negativo():
    # Definindo a entrada
    capital = -1000
    taxa = 10
    tempo = 3

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O capital investido não pode ser negativo."):
        calcular_juros_compostos(capital, taxa, tempo)

# TAXA
def test_validar_taxa_negativo():
    # Definindo a entrada
    capital = 1000
    taxa = -10
    tempo = 3

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O capital investido não pode ser negativo."):
        calcular_juros_compostos(capital, taxa, tempo)

# TEMPO
def test_validar_tempo_negativo():
    # Definindo a entrada
    capital = 1000
    taxa = 10
    tempo = -3

    # executando a função e esperando o erro
    with pytest.raies(ValueError, match="O tempo não pode ser negativo."):
        calcular_juros_compostos(capital, taxa, tempo)


