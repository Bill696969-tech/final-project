class InterestCalculator:
    def __init__(self, initial, rate, time):
        if initial <= 0 or rate <= 0 or time <= 0:
            raise ValueError("Initial investment, rate and time must be positive numbers!")
        self.initial = initial
        self.rate = rate
        self.time = time

    def calculate_simple_interest(self):
        return (self.initial * self.rate * self.time) / 100

    def calculate_compound_interest(self, n):
        if n <= 0:
            raise ValueError("Compounding frequency must be a positive integer.")
        amount = self.initial * (1 + self.rate / (100 * n)) ** (n * self.time)
        return amount - self.initial


def main():
    print("!!<< Interest Calculator >>!!")
    print("Please select:")
    print("1. Simple Interest")
    print("2. Compound Interest")

    choice = input("Enter your choice (1 or 2): ")

    try:
        initial = float(input("Enter the initial investment: "))
        rate = float(input("Enter the annual interest rate %: "))
        time = float(input("Enter the investment length (in years): "))

        # Initialize calculator with validated inputs
        calculator = InterestCalculator(initial, rate, time)

        if choice == "1":
            interest = calculator.calculate_simple_interest()
            print(f"Simple Interest: {interest:.2f}")
        elif choice == "2":
            n = int(input("Enter the number of times interest is compounded per year: "))
            interest = calculator.calculate_compound_interest(n)
            print(f"Compound Interest: {interest:.2f}")
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

    except ValueError as ve:
        print(f"❌ Input error: {ve}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
