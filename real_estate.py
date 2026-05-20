"""Real estate investment calculation module."""


def rental_yield(price, annual_rent, annual_costs):
    """Return net yearly income and net rental yield percentage."""
    if price <= 0:
        raise ValueError("Property price must be greater than zero.")
    if annual_rent < 0:
        raise ValueError("Annual rent cannot be negative.")
    if annual_costs < 0:
        raise ValueError("Annual costs cannot be negative.")

    net_income = annual_rent - annual_costs
    yield_percent = (net_income / price) * 100
    return net_income, yield_percent


def run_real_estate_simulation():
    print("\n--- REAL ESTATE INVESTMENT ---")
    price = float(input("Property price (EUR): "))
    rent = float(input("Annual rent (EUR): "))
    costs = float(input("Annual costs (EUR): "))

    income, yield_percent = rental_yield(price, rent, costs)

    print(f"\nNet yearly income: {income:.2f} EUR")
    print(f"Rental yield: {yield_percent:.2f} %")
