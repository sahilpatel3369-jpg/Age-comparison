#Importing Cmath will allow to give the built in pre-coded function

import cmath

def main():
  math1 = input("a coefficient")
#Defining variables and asking for input
  if math1 == "0":
    print("a coefficient must be non zero") 
    math1=input("a coefficient")
  math2= input("b coefficient")
  math3 = input("c coefficient")
#Making the equations and printing out the vertex
  xvertex = -int(math2) /(2 *int(math1))
  yvertex = (int(math1) * xvertex * xvertex) + (int(math2) * xvertex) + int(math3)
  print(xvertex)
  print(yvertex)
#If else statement on wether a Parabola is opening upward or downward
  if int(math1)>0:
    print("Parabola opens upward")
  else:
    print("Parabola opens downward")
#Calcualiting the discriminant 
  discriminant = (int(math2) * int(math2) -4 * int(math1) * int(math3))

  root1 = (-int(math2) + cmath.sqrt(discriminant)) / (2 * int(math1))
  root2 = (-int(math2) - cmath.sqrt(discriminant)) / (2 * int(math1))




main()



