"""
Define a function reversecomplement that takes a DNA string as an input. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA string, the function finds the reverse complement of that string. The reverse complement is found by first reversing the string, then taking the complement of each nucleotide. A and T are complements of each other, and C and G are complements of each other.

For example,
reversecomplement("AAGCT") should return "AGCTT".
"""

def reversecomplement(dna):
  x = list(dna)
  for element in x: 
    if element != "A" and element != "C" and element != "G" and element != "T":
      return ("Error")
  z = ""
  x.reverse()
  for i in x:
    if i == "A":
      z += "T"
    if i == "C":
      z += "G"
    if i == "G":
      z += "C"
    if i == "T":
      z += "A"
  return z