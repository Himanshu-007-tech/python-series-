class Demo:
    a = 4

o = Demo()
print(o.a)# prints class attributes because instance attributes is not present
o.a = 0# instance attributes is set
print(o.a)# prints the instance attributes because instance attribute is present
print(Demo.a) # prints the class attributes
