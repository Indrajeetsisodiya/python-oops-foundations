class student:
    def __init__(self, name, age, category):
        # __init__ runs automatically when a new object is created
        # It stores the provided values inside the object
        self.name = name        # stores the student's name
        self.age = age          # stores the student's age
        self.category = category  # stores the student's category


# Creating objects (instances) of the student class
s1 = student("indrajeet sisodiya", 25, "genral")
s2 = student("divya", 25, "OBC")
s3 = student("chaman", 22, "SC")


# Accessing and printing object attributes
print(s1.age)
print(s1.category)
print(s2.category)
print(s3.category)


'''
Output:
25
genral
OBC
SC
'''
