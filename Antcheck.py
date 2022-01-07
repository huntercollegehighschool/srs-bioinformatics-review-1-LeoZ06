"""
Define a function isDNA that takes a single string as an input. The string is supposed to represent a DNA string that only has molecules A, C, G, and T. The function returns True(the Boolean value) if the string is a valid DNA string, and False if it's not.
"""

def isDNA(dna):
  for i in dna:
    if i != "A" and i != "C" and i != "G" and i != "T":
      return False
  return True