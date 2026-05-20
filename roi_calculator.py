"""ROI calculation module."""


def calculate_roi(initial_investment, final_value):
    """Return the return on investment percentage."""
    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than zero.")

    profit = final_value - initial_investment
    return (profit / initial_investment) * 100


def calculate_profit(initial_investment, final_value):
    """Return the absolute profit or loss."""
    return final_value - initial_investment


def run_roi_simulation():
    print("\n--- ROI CALCULATOR ---")
    initial = float(input("Initial investment (EUR): "))
    final = float(input("Final value (EUR): "))

    roi = calculate_roi(initial, final)
    profit = calculate_profit(initial, final)

    print(f"\nProfit: {profit:.2f} EUR")
    print(f"ROI: {roi:.2f} %")
