s=input('Enter a string: ')
def tester():
  l=list(s)
  for x in l:
    if x=='' or x==' ':
      l.remove(x)
  print(l)

de

tester()