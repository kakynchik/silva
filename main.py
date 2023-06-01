class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"imya: {self.name}")
        print(f"vik: {self.age}")
student1 = Student("marchik", 16)
student1.get_info()
student2 = Student("zheniya", 16)
student2.get_info()