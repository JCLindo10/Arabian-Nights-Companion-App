"""
    encounter.py
    Author: Jakob Lindo
    Created: 9/24/2023

    Intended for use in Jakob Lindo's companion app for Tales of The Arabian Nights. Represents the
    whole of the set of real life actions in playing the game called 'Encounter'

"""

class Encounter:
    def __init__(self, text, other):
        self.text = text
        self.other = other

    def modify_text(self, raw_text):
        return raw_text.replace('other', self.other)

    def display_text(self):
        print("placeholder text encounter")

