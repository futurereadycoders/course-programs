def main():
    one = int(input("What is your first number? "))
    operator = input("What operation would you like to perform (+, -, *, /)? ")
    two = int(input("What is your second number? "))

    if operator not in ["+", "-", "/", "*"]:
        print("Error: invalid operator.")
        exit(1)

    if operator == "+":
        answer = one + two
    elif operator == "-":
        answer = one - two
    elif operator == "*":
        answer = one * two
    else:
        answer = one / two

    print(f"{one} {operator} {two} equals {answer}.")
    goagain = input("Would you like to ask another question? (y/n) ").lower()
    if goagain == "y":
        main()
    print("Goodbye!")


main()
