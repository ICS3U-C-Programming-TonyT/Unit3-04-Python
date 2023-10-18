#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 11, 2023
# This is program will tell you if your integer is a negative, positive, or zero.


def main():
    integer = int(input("Enter your integer:\n"))
    if "-" in str(integer):
        print(f"{integer} is a negative number")
    elif integer == 0:
        print(f"{integer} is just zero!")
    else:
        print(f"{integer} is a positive number")


if __name__ == "__main__":
    main()
