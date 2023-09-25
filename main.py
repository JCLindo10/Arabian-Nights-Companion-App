"""
    main.py
    Author: Jakob Lindo
    Created: 9/25/2023

    The driver program for the ToTAN companion app

"""

import other
import encounter

def main():
    while(True):

        #TODO: Make this take in the other and the modifier, splitting on a space
        mod_and_other = input("What have you encountered?\n").split()

        if len(mod_and_other) > 2:
            print("Invalid input")
            continue

        input_modifier, input_other = mod_and_other
        # input_modifier = input("what is its modifier?\n")

        encountered_other = other.Other(input_other, input_modifier)

        print(encountered_other)

        confrontation = encounter.Encounter('test', encountered_other)

        confrontation.display_text()


if __name__ == "__main__":
    main()