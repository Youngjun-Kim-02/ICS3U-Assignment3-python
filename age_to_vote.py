#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program checks if an age is eligible to vote or not


def main():
    # this function checks if an age is eligible to vote or not

    # input
    age = int(input("Enter an age: "))
    print("")

    # process & output
    if age > 18:
        print("Eligible to vote.")
    elif age == 18:
        print("Eligible to vote.")
    else:
        print("Ineligible to vote.")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
