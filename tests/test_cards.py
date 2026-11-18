from payments.cards import can_pay


def test_card_can_pay():
    assert can_pay(card_frozen=False) is True
