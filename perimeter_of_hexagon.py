#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This programs calculates the perimeter of a hexagon
#     user inputs the length of one side

import constants


def main():
    # main function
    print("We will be calculating the perimiter of a hexagon.")

    # input
    print("")
    side_length = int(input("Enter the length of one side (cm) : "))

    # process
    perimeter = constants.NUMBER_OF_SIDES * side_length

    # output
    print("The perimeter of this hexagon is {0} cm.".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
