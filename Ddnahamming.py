"""
Define a function hammingdistance that takes 2 DNA string inputs.

-First the function should check if both strings are valid DNA strands (use the function defined in the 1st part). If it's not, return "error".

-Next, if the strings are of different lengths, the function should also return "error".

-If they are both valid DNA strands and the same length, the function calculates how many of the corresponding nucleotides in each string do not match (known as the Hamming Distance)

For example, hammingdistance("TTAC", "TGAA") should return 2.
"""

def hammingdistance(dna1, dna2):
  x = list(dna1)
  for element in x: 
    if element != "A" and element != "C" and element != "G" and element != "T":
      return ("Error")
  y = list(dna2)
  for element in y: 
    if element != "A" and element != "C" and element != "G" and element != "T":
      return ("Error")
  if len(x) != len(y):
    return ("Error")
  z = 0
  for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
      z += 1
  return z