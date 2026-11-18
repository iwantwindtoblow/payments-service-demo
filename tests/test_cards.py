from payments.cards import can_pay


def test_frozen_card_cannot_pay():
    assert can_pay(card_frozen=True) is False
