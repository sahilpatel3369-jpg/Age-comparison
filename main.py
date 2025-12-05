


import cmath


#The function get_a(); will be the a coefficent of the prabola. We will do a while true statment
def get_a():
  while True:
    a = float(input("Enter the a coefficent (a non zero value):"))
    if a == 0:
      print("Error and Try Again")
    else:
      return a
      break


#Return values of equations
def xvertex(a, b, c):

  x = -b / (2 * a)
  return x


def yvertex(a, b, c):

  xtex = xvertex(a, b, c)
  yvertex = (a * cmath.sqrt(xtex)) + (b * xtex) + c
 
  return yvertex


def concavity(a):
  if a > 0:
    print("The parabola opens upward")
  elif a < 0:
    print("The parabola opens downward")


#Discriminant for abc
def discrimiant(a, b, c):
  d = (b**2) - (4 * a * c)
  sol1 = (-b - cmath.sqrt(d)) / (2 * a)
  sol2 = (-b + cmath.sqrt(d)) / (2 * a)
  print("The solutions are {0}, {1}".format(sol1, sol2))
  return d


#Roots
def print_roots(a, b, c):
  d = discrimiant(a, b, c)
  if d > 0:
    root1 = (-b + cmath.sqrt(discrimaint)) / (2 * a)
    root2 = (-b - cmath.sqrt(discrimaint)) / (2 * a)
    print("X1 root coordinate:", root.real)
    print("X2 root coordinate:", root.real)
  elif d == 0:
    root = -b / (2 * a)
    print("X1 root coordinate:", root.real)
  else:
    print("The parabola has no real roots")


def main():
  a = get_a()
  b = float(input("Enter the b coefficent :"))
  c = float(input("Enter the c coefficent :"))
  print("Quadratic Equation Analyzer")
  print(a)
  print(b)
  print(c)
  x = xvertex(a, b, c)
  print(x)
  y = yvertex(a,b,c)
  print(y)
  concavity(a)
  print_roots(a, b, c)
main()
