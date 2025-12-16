marks = {
    "himanshu": 100,
    "ravi": 34,
    "umesh": 76,
    0: "himanshu"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"himanshu": 91, "shiv": 76})
# print(marks)

print(marks.get("himanshu2"))  #Prints None
print(marks["himanshu2"]) # Returns an error
