import sys 

def test_simples():
    assert 1 + 1 == 2 

def test_dependente_de_versao():
    if not sys.version_info.minor == 12:
        raise ValueError("Versão inválida") 