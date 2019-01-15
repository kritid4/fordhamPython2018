# Group Project: Test Class
# Author: Kriti Dogra

#from GroupProject.Objects import Student
#from GroupProject import StudentQueryTool

from Objects import Student;
import StudentQueryTool;

all_students_test = []
s1 = Student('100', 'Doe', 'John', '2018', 'Fall', 'MSIS')
s2 = Student('101', 'Smith', 'Jane', '2018', 'Fall', 'MSIS')
s3 = Student('102', 'Black', 'Jake', '2019', 'Fall', 'MSBA')
s4 = Student('103', 'While', 'Bill', '2018', 'Winter', 'MSBA')
s5 = Student('104', 'Smith', 'Anna', '2019', 'Fall', 'MBSA')

all_students_test.append(s1)
all_students_test.append(s2)
all_students_test.append(s3)
all_students_test.append(s4)
all_students_test.append(s5)

print('PRINTING ALL STUDENTS')
StudentQueryTool.display_students(all_students_test)

print('\n\nPRINTING ALL THAT START WITH J')
StudentQueryTool.print_starts_with(all_students_test, 'J')

print('\n\nPRINTING ALL GRADUATING IN 2019')
StudentQueryTool.print_graduating_yr(all_students_test, '2019')

print('\n\nPRINTING SUMMARY REPORT FOR 2018')
StudentQueryTool.print_summary_report(all_students_test, '2019')