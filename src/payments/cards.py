"""Card controls."""


def can_pay(card_frozen: bool) -> bool:
    return not card_frozen
