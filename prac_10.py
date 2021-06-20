a=int(input())
b=int(input())
c=int(input())

if a>=65 and b>=55 and c>=50:
    if a+b+c>=190 or a+b>=140:
        print("The candidate is eligible for admission.")
    else:
        print("The candidate is not eligible for admission.")
else:
    print("The candidate is not eligible for admission.")