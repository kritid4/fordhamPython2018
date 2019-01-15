# Group Project
# Author: Kriti Dogra

class Student(object):
    def __init__(self, student_id, last, first, year, term, program):
        self.student_id = student_id
        self.last = last
        self.first = first
        self.year = year
        self.term = term
        self.program = program

    def __str__(self):
        return str(self.student_id) + ' ' + str(self.last) + ' ' + str(self.first) + ' ' + str(self.year) + ' ' + str(self.term) + ' ' + str(self.program)
    
    def print_student_detail(self):
        print(self.student_id + '\t' + self.last + '\t' + self.first +
              '\t' + self.year + '\t' + self.term + '\t' + self.program)

    @staticmethod
    def print_header():
        print('ID\tLast\tFirst\tGradYear\tGradTerm\tDegreeProgram')

