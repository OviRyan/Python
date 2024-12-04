try:
    a = [10,20,30,0]
    b = int(input("Enter Number : "))
    for i in  a:
        result = i/b
        print (result)


except ZeroDivisionError as e :
    print (e)
except ValueError :
    print ("Yiu have a value Error")