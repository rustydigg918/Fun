"""MY SOLUTION

def is_isogram(string):
    return len([i for i in string.lower()]) == len({i for i in string.lower()})

"""

"""
WINNER

def is_isogram(string):
    return len(string) == len(set(string.lower()))
"""