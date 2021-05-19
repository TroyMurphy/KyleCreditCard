from Kyle.CreditCardCheck import card_check
from Troy.luhnCheck import number_check


def main():
    print("Kyle Luhn Check")
    print("Expect valid")
    card_check(5258901506176905)
    print("Expect invalid")
    card_check(5258910506176905)

    print("Troy Luhn Check")
    print("Expect valid")
    number_check("5258901506176905")
    print("Expect invalid")
    number_check("5258910506176905")


if __name__ == "__main__":
    main()
