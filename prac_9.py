a = int(input())
b = int(input())

if a > 0 and b > 0:
    print("The coordinate point (", a, b, ") lies in the First quadrant")
elif a < 0 and b > 0:
    print("The coordinate point (", a, b, ") lies in the Second quadrant")
elif a < 0 and b < 0:
    print("The coordinate point (", a, b, ") lies in the Third quadrant")
elif a > 0 and b < 0:
    print("The coordinate point (", a, b, ") lies in the Fourth quadrant")
else:
    print("The coordinate point (", a,b,") lies in the Mid point")
