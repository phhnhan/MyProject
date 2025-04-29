from student import Student
class Course:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def getDeansList(self):
        deans_list = []
        for student in self.roster:
            if student.getGPA() >= 3.5:
                deans_list.append(student) 
        return deans_list 