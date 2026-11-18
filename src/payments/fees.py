"""FX fees."""

FX_FEE_RATE = 0.005


def fx_fee(amount_eur: float) -> float:
    """Fee for a currency conversion, in euros."""
    return round(amount_eur * FX_FEE_RATE, 2)
