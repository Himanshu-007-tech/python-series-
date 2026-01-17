
line = 1

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" is line):
     print("Yes python is preasent line no: {line}")
     break
    lineno += 1

else:
    print("No python is not present")