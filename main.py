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
        
        input_modifier, input_other  = input("What have you encountered?\n").split()
        # input_modifier = input("what is its modifier?\n")

        encountered_other = other.Other(input_other, input_modifier)

        print(encountered_other)




if __name__ == "__main__":
    main()