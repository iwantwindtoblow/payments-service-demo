from payments.fees import fx_fee


def test_fx_fee():
    assert fx_fee(1000) == 5.0
