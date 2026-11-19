from src.config import load_fares

def test_load_fares_returns_expected_valuees():
    fares = load_fares()

    assert fares["stopped"] == 0.02
    assert fares["moving"] == 0.05