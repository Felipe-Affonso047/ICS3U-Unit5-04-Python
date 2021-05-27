#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program calculates the volume of a cylinder

import math


def cylinder_volume(height, radius):
    # this function calculates the volume of a cylinder
    volume = height * radius * 2 * math.pi

    return volume


def main():
    # Is the main function
    try:
        print("This program calculates the volume of a cylinder.\n")

        height = int(input("Enter height in cm: "))
        radius = int(input("Enter radius in cm: "))

        result = cylinder_volume(height, radius)

        print("\nThe cylinder volume is: {}cm²".format(result))
    except Exception:
        print("\nThis input is invalid, please, insert a number.")
    print("\nDone.")


if __name__ == "__main__":
    main()
