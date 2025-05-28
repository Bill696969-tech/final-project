def simple_interest(initial, rate, time):
    return (initial * rate * time) / 100
    

def compound_interest(initial, rate, time, n=1):
    amount = initial * (1 + rate / (100 * n)) ** (n * time)
    return amount - initial
    

def main():
    print("!!<< Interest Calculator >>!!")
    print("Please select:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    

    choice = input("Enter your choice (1 or 2): ")
    initial = float(input("Enter the initial amount: "))
    rate = float(input("Enter the annual interest rate %: "))
    time = float(input("Enter the investment length (in years): "))
    

    if choice == "1":
        interest = simple_interest(initial, rate, time)
        print(f"Simple Interest: {interest:.2f}")
    elif choice == "2":
        n = int(input("Enter the number of times interest is compounded per year: "))
        interest = compound_interest(initial, rate, time, n)
        print(f"Compound Interest: {interest:.2f}")
    else:
        print("Invalid choice.")
        

if __name__ == "__main__":
    main()
