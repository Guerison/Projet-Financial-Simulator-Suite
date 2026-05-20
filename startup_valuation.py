"""Startup valuation module using a revenue multiple method."""


def startup_value(revenue, growth_rate, multiple=5):
    """Estimate startup valuation from revenue, growth and a base multiple."""
    if revenue < 0:
        raise ValueError("Revenue cannot be negative.")
    if growth_rate < 0:
        raise ValueError("Growth rate cannot be negative.")
    if multiple <= 0:
        raise ValueError("Multiple must be greater than zero.")

    adjusted_multiple = multiple + (growth_rate * 10)
    return revenue * adjusted_multiple


def run_startup_simulation():
    print("\n--- STARTUP VALUATION ---")
    revenue = float(input("Annual revenue (EUR): "))
    growth = float(input("Growth rate (example: 0.2 for 20%): "))

    valuation = startup_value(revenue, growth)

    print(f"\nEstimated startup valuation: {valuation:,.2f} EUR")
