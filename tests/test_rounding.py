def test_known_rounding_issue():
    assert round(2.675, 2) == 2.68  # fails: floating point
