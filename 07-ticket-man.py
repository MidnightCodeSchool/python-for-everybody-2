"""
This program prints ticket price based on age
"""

def age_to_price(age: int) -> int:
    """Return the ticket price based on the input age
    """
    if age < 0:
        raise ValueError("Invalid age")

    ADULT_AGE = 18
    SENIOR_AGE = 65

    if age >= SENIOR_AGE:
        return 200
    elif age >= ADULT_AGE:
        return 250
    elif age < ADULT_AGE:
        return 150

def main():
    age = input("How old are you? ")
    age = int(age)
    if age < 0:
        print("Invalid age")
        exit()
    price = age_to_price(age)
    print("Price: ", price)

if __name__ == "__main__":
    main()