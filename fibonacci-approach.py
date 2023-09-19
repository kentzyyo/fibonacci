#kentzyyo 
def func1(n):  #first function to compute fibonacci using recursion
  if (n <= 1):
    return n
  else:
    return (func1(n - 1) + func1(n - 2))


def func2(n):  # second function to compute fibonacci using iteration
  if n in {0, 1}:  # Base case
    return n
  return func2(n - 1) + func2(n - 2)


def func3(n):  # third function to compute fibonacci using Space Optimisation
  a = 0
  b = 1
  if n < 0:
    print("Incorrect input")
  elif n == 0:
    return a
  elif n == 1:
    return b
  else:
    for i in range(2, n + 1):
      c = a + b
      a = b
      b = c
    return b


if __name__ == "__main__":  # top level code for module importation
  print(
    "+---------------------------------------------------------------------------------------------+"
  )
  print(
    "| Fibonacci Numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597      |"
  )
  print("| The nth position: ", end=" ")
  for i in range(1, 18):
    print(i, end=", ")
  print(
    "\n+---------------------------------------------------------------------------------------------+"
  )

  for i in range(1, 18):
    func1(i)

  n = int(input("Enter the value of N (positive integer): "))
  if (n >= 1):
    print("Using 1st Approach: ", func1(n))  #print output for 1st function
    print("Using 2nd Approach: ", func2(n))  #print output for 2nd function
    print("Using 3rd Approach: ", func3(n))  #print output for 3rd function
  else:
    print(
      "Error: Nth position must be a positive integer"
    )  # else function for error in case the input isn't a positive integer

# print("Error: Nth position must be a positive integer")

file1 = open('D:\DEFENSIVE PROGRAMMING\@ct1_output.out', "w") # output file
file1.write('1\n')
for i in range(2, n+1):
    file1.write(str(func1(i))+'\n')
file1.close()
# end
