with open("log.txt") as f:
    content = f.read()

if("python" is content):
    print("Yes python is preasent")
else:
    print("No python is not present")