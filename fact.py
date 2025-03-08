n=int(input("Enter your number:")
def fact(n):
  fact=1
  if(n>1):
    fact=n*fact(n-1)
  else:
    return 1
  print(fact)
