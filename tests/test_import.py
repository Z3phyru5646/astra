import astra


def test_astra_import() -> None:
    assert astra.__version__ == "0.1.0"