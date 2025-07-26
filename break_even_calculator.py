def calculate_break_even_time():
    """
    Calculates the break-even time between two investments with different
    initial costs and annual maintenance fees.
    """
    print("--- Break-Even Point Calculator ---")
    print("Please enter the costs without commas or symbols.\n")

    try:
        # --- Get Natural Gas Plant Data ---
        initial_gas = float(input("Enter the initial cost of the Natural Gas plant: $"))
        maint_gas = float(input("Enter the ANNUAL maintenance fee for the Natural Gas plant: $"))

        # --- Get Solar System Data ---
        print("") # Add a space for readability
        initial_solar = float(input("Enter the initial cost of the Solar system: $"))
        maint_solar = float(input("Enter the ANNUAL maintenance fee for the Solar system: $"))

        # --- Perform Calculation ---

        # Check if maintenance costs are the same to avoid division by zero
        if maint_gas == maint_solar:
            if initial_gas == initial_solar:
                print("\nBoth systems have the same initial and maintenance costs. The cost will always be identical.")
            elif initial_solar > initial_gas:
                print("\nWith equal maintenance costs, the solar system will always be more expensive.")
            else:
                print("\nWith equal maintenance costs, the solar system will always be cheaper.")
            return

        # The core break-even formula
        # t = (I_s - I_g) / (M_g - M_s)
        time = (initial_solar - initial_gas) / (maint_gas - maint_solar)

        print("\n--- Result ---")
        if time > 0:
            print(f"✅ The cost for the two systems will break even in {time:.2f} years.")
        else:
            # This occurs if the system with the lower maintenance fee also has a lower initial cost
            print("✅ The solar system is cheaper from the very beginning (t=0).")

    except ValueError:
        print("\n❌ Error: Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculate_break_even_time()
