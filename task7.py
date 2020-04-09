class Students():
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def get_student_info(self):
        print(f"{self.name}, age: {self.age}, major: {self.department}")
    
Steve = Students("Steven Schultz", 23, "English")
Steve.get_student_info()
Johnny = Students("Jonathan Rosenberg", 24, "Biology")
Johnny.get_student_info()
Penny = Students("Penelope Meramveliotakis", 21, "Physics")
Penny.get_student_info()