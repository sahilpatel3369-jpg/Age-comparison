""""
This program will let the user use random seed and random generator to
show the nuumbers that are even, odd or zeros in the code. 

"""





import random

num = random.seed(15)
# using random.randint
def main():
    numvalue1 = random.randint(2, 20)
    print("Random generated value:", numvalue1)
    return numvalue1
# counters for even, odd nums
e = 0
odd = 0
z = 0
num = 0
#get the value
numvalue1 = main()
#for i in range with if else statements and listing values
for i in range(numvalue1):
    num = random.randint(0, 99)
    print(num)
    if num == 0:
      z += 1
    else:
  
      if num % 2 == 0:
        e += 1
      else:
        odd += 1
print("There are", e, "even numbers", "and", odd, "odd numbers", "and zero", z, "numbers")
G2 = random.randint(2, 20)
print("The program will generate", G2, "Numbers")
eveng2 = 0
oddg2 = 0
zerog2 = 0
NG2 = ""  
# define
countG2 = 0
while countG2 < G2:
    num = random.randint(0, 99)
    NG2 += str(num) + " "
    if num == 0:
        zerog2 +=  1
    elif num % 2 == 0:
        eveng2 += 1
    else:
        oddg2 += 1
    countG2 += 1
print("The generated numbers are:", NG2)
print("There are", eveng2, "even numbers", "and", oddg2, "odd numbers", "and", zerog2, "zero numbers")
main()


























