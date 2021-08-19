def fib_next(a,b,n):
  return (a + b)%n

def is_repeat(a,b):
  return (a==1 and b==0)

def count_repeat(n):
  count = 2
  a = b = 1
  while not is_repeat(a,b):
    temp = fib_next(a,b,n)
    a = b
    b = temp
  return count


def main():
  print("Enter the number you wish to test:",)
  x = int(input())
  temp = count_repeat(x)
  print("The modular Fibonacci sequence for",x,"repeats in",temp,"elements.")

if __name__=="__main__":
  main()

