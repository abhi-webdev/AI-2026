
class Student :
    school_name = "Sanskriti school"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name) :
        cls.school_name = new_name


data = Student("JAM")
data.change_school("TIT School")

print(data.school_name)