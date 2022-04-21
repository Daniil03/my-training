# put your python code here
chto = input()
pi = 3.14
if chto == 'треугольник':
  a = float(input())
  b = float(input())
  c = float(input())
  p = (a + b + c) / 2
  S = (p*(p-a)*(p-b)*(p-c))**0.5
  print(S)
else:
  if chto == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a*b)
  else:
    if chto == 'круг':
      r = float(input())
      print(pi*r**2)
   