"""
    other.py
    Author: Jakob Lindo
    Created: 9/24/2023

    Describes a class intended to be used as the 'other' in Tales of The Arabian Nights

"""

class Other:
    def __init__(self, base, modifier):
        self.base = base
        self.modifier = modifier

    def __str__(self) -> str:
        if self.modifier.lower()[0] in 'aeiou':
            return f'an {self.modifier} {self.base}'
        else:
            return f'a {self.modifier} {self.base}'
            
