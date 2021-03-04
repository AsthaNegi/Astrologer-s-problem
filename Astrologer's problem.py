#By Astha Negi
a=int(input("Enter a number:"))
b=int(input("Enter 1 for downward pattern and 0 for upward pattern"))
d=bool(b)

if d==True:
 for i in range(a):
  print("\n")
  b=a
  for i in range(b):
    print('*',end=" ")
    a = (b - 1)
elif d==False:
    for i in range(a):
        print("\n")
        c = i
        i = c + 1
        for j in range(i):
            print('*', end=" ")






