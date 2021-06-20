a=int(input())
if a==2:
    b=int(input("Please enter year: "))
    if (b % 4) == 0:
        if (b % 100) == 0:
            if (b % 400) == 0:
                print("Month have 29 days")
            else:
                print("Month have 28 days")
        else:
            print("Month have 29 days")
    else:
        print("Month have 28 days")
elif a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("Month have 31 days")
else:
    print("Month have 30 days")