f = open("file.text")
print(f.read())
f.close()
#the same can be written using the statement like this:
with open("file.text")as f:
    print(f.read())

    #you dont have to explicitly close the file
    