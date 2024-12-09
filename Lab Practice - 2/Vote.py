class Vote(Exception):
    pass

try:
    age = int(input("Enter Age : "))
    if age < 18 :
        raise Vote("Invalid Voter")
    else:
        print ("Valid")

except Vote as e :
    print (e)