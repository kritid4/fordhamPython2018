# Group Project
# Author: Kriti Dogra

# from GroupProject.Objects import Student

from Objects import Student;

_filename = 'students.txt'


def main():
    try:
        all_students = read_file()
        user_command = '-1'

        while user_command != '0':

            option_command = ('\nWhat would you like to do?\n'
                              + '1: Display All\n'
                              + '2: Starts With' + '\n'
                              + '3: Lookup With Graduating Year\n'
                              + '4: Summary Report\n'
                              + '0: Quit\n')

            user_input = input(option_command).strip()

            try:
                user_input = int(user_input)
                if user_input == 0:
                    print('Thank You For Using Student Query Tool!')
                    return
                elif user_input == 1:
                    display_students(all_students)
                elif user_input == 2:
                    starting_string = input('What string do you want it to start with? ')
                    print_starts_with(all_students, starting_string)
                elif user_input == 3:
                    graduating_yr = input('What graduating year students do you want? ')
                    print_graduating_yr(all_students, graduating_yr)
                elif user_input == 4:
                    year = input('For what year do you want the summary report? ')
                    print_summary_report(all_students, year)
                else:
                    print('Error!!! That was not an option offered...')
            except ValueError:
                print('Error!!! That was not a valid input...')

    except:
        print('Error!!! Error while processing...')

    finally:
        print('Program ending...')


# reads file
# returns a list of class: 'Student'
def read_file():
    try:
        all_students = []
        infile = open(_filename, 'r')
        line = infile.readline()
        i = 0
        while line.strip() != '':
            if i != 0:
                line = line.split()
                student_record = Student(line[0], line[1], line[2], line[3], line[4], line[5])
                all_students.append(student_record)
            line = infile.readline()
            i += 1
        infile.close()
        return all_students
        
    except FileNotFoundError:
        print('ERROR!!! File does not exist')
    except IOError:
        print('ERROR!!! Error while reading file...')


# reads a list of Student classes
# displays a list of all student
def display_students(student_info):
    if len(student_info) > 0:
        Student.print_header()
    else:
        print('No records to display...')
    for student in student_info:
        student.print_student_detail()
    return


# reads a list of Student classes
# displays a list of Student class with first name starting with: starting_str
def print_starts_with(all_students, starting_str):
    # TODO: your code goes here
    
    return


# reads a list of Student classes
# displays a list of Student class with students that are graduating in: year
def print_graduating_yr(all_students, year):
    all_student_year = []
    for student in all_students:
        if student.year == year:
            all_student_year.append(student)

    display_students(all_student_year)


# reads a list of Student classes
# displays a list of Student class with a summary report for: year
def print_summary_report(all_students, year):
    # TODO: your code goes here
    
    return


# if Student Query Tool is entry point, then execute main method
# prevents test code from executing entire program
if __name__ == '__main__':
    main()