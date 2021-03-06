"""
Define a function ntcount that takes a string representing a DNA string. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA strand, the function returns a dictionary with the counts of each nucleotide.

For example: 
ntcount("AACTGTA") 
returns {"A": 3, "C": 1, "G": 1, "T": 2}
"""

def ntcount(dna):
  x = list(dna)
  for element in x: 
    if element != "A" and element != "C" and element != "G" and element != "T":
      return ("Error")
  A = x.count("A")
  C = x.count("C")
  G = x.count("G")
  T = x.count("T")
  return {"A":A, "C":C, "G":G, "T":T}