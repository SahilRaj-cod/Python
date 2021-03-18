x = input("Weight:" )

a = input("(l)lbs OR (k)Kg: ")
    
if a == "k" :
    print(int(x) * 2.205)

elif a == "l" :
    print(int(x) / 2.205)