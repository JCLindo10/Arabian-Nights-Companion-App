"""
    main.py
    Author: Jakob Lindo
    Created: 9/25/2023

    The driver program for the ToTAN companion app

"""

import other

def main():
    while(True):

        #TODO: Make this take in the other and the modifier, splitting on a space
        input_other = input("What have you encountered?")
        input_modifier = input("what is its modifier?")

        other = other(input_other, input_modifier)

        


if __name__ == "__main__":
    main()