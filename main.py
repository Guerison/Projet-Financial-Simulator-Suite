from real_estate import run_real_estate_simulation
from roi_calculator import run_roi_simulation
from startup_valuation import run_startup_simulation


def run_selected_simulation(choice):
    """Route a menu choice to the right simulation."""
    if choice == "1":
        run_roi_simulation()
        return True
    if choice == "2":
        run_real_estate_simulation()
        return True
    if choice == "3":
        run_startup_simulation()
        return True
    if choice == "4":
        print("Goodbye!")
        return False

    print("Invalid choice. Please select an option from 1 to 4.")
    return True


def main():
    is_running = True

    while is_running:
        print("\n==== FINANCIAL SIMULATOR ====")
        print("1 - ROI Calculator")
        print("2 - Real Estate Investment")
        print("3 - Startup Valuation")
        print("4 - Exit")

        choice = input("Choose an option: ").strip()

        try:
            is_running = run_selected_simulation(choice)
        except ValueError as error:
            print(f"Input error: {error}")


if __name__ == "__main__":
    main()
