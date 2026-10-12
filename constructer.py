
class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @staticmethod
    def greet():
        return "Hello, welcome to the class!"
    
teacher.greet()  # Calling the static method without creating an instance
teacher1 = teacher("Mr. Smith", 35)
student = teacher("John", 20)
print(teacher.greet())
print(f"Teacher's name: {teacher1.name},\n Age: {teacher1.age}")
print(f"Student's name: {student.name},\n Age: {student.age}")