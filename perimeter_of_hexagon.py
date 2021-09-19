#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This programs calculates the perimeter of a hexagon
#     user inputs the length of one side


def main():
    # this function calculates the perimeter of a hexagon

    # input
    side_length = int(input("Enter the length of one side of the hexagon (cm) : "))

    # process
    perimeter = 6 * side_length

    # output
    print("The perimeter of this hexagon is {0} cm.".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
