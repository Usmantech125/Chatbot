def grade():
    while True:
        var1=int(input("Enter your marks: "))
        if var1 >= 90:
            print("A")
        elif var1 >= 80:
            print("B")
        elif var1 >= 70:
            print("C")
        elif var1 >= 60:
            print("D")
        elif var1 >= 40:
            print("E")
        else:
            print("Fail")


grade()