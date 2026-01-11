class student:
    def __init__(self, name, age, category):
        # __init__ runs automatically when an object is created
        # It stores the given values as attributes of the object
        self.name = name        # student's name
        self.age = age          # student's age
        self.category = category  # student's category

    def introduction(self):
        # introduction() is a method that uses object attributes
        # to display information about the student
        print(
            f"hi ! my name is {self.name} and my age is {self.age} "
            f"and i belong to {self.category} category"
        )


# Creating objects (instances) of the student class
s1 = student("indrajeet sisodiya", 25, "genral")
s2 = student("divya", 25, "OBC")
s3 = student("chaman", 22, "SC")


# Accessing attributes and calling a method
print(s1.age)          # printing an attribute
s1.introduction()      # calling a method


'''
Output:
25
hi ! my name is indrajeet sisodiya and my age is 25 and i belong to genral category
'''
