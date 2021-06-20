a=int(input())
b=int(input())
c=int(input())

if a==b==c:
    print("This is an Equilateral triangle.")
elif a!=b and a!=c and b!=c:
    print("This is an Scalene triangle.")
elif a==b or a==c and c==b:
    print("This is an Isosceles triangle.")
