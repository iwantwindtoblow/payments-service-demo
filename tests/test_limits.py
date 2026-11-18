from payments.limits import get_daily_limit


def test_verified_limit():
    assert get_daily_limit(verified=True) == 15_000


def test_unverified_limit():
    assert get_daily_limit(verified=False) == 10_000
