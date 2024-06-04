#The try block does not raise any errors, so the else block is executed:

try:
    print("Hello")
except:
    print("Somethig went wrong")
else:
    print("Nothing went wrong")
    