C: int = 299792458

def main(): 
    # Step 1: User se mass input lena aur usko float mein convert karna
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Step 2: Energy calculate karna using the formula: E = m * C^2
    energy_in_joules: float = mass_in_kg * (C ** 2)
    print("\ne = m * C^2...")  # Formula dikhana
    print(f"m = {mass_in_kg} kg")  # Jo mass user ne enter kiya
    print(f"C = {C} m/s")  # Speed of light
    print(f"{energy_in_joules} joules of energy!")
main()