"""Transfer limits for payments-service (demo code for the audit sandbox)."""

DAILY_LIMIT_EUR = 10_000
VERIFIED_DAILY_LIMIT_EUR = 15_000


def get_daily_limit(verified: bool) -> int:
    """Daily transfer limit in euros: higher for verified users."""
    return VERIFIED_DAILY_LIMIT_EUR if verified else DAILY_LIMIT_EUR
