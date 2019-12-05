#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: Sep 2019
# This program calculates the circumference of a circle
#     with user input


import constants


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter radius of the circle (mm): "))
    # process
    circumference = constants.TAU*radius
    # output
    print("")
    print("Circumference is {}mm2".format(circumference))

    if __name__ == "__main__":
        main()
