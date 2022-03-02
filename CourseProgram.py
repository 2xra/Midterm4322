"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

import CourseClass as C


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    AdvPy = C.Course(name, crn, seats, status)

    for person in students:
        # I feel objectified as a student.
        personalobject = C.Register(person, crn)
        if AdvPy.get_status() == "open":
            AdvPy.update_seat_count()
            print("Student Name: ", personalobject.get_name())
            print("Course Name: ", AdvPy.get_name())
            print("CRN: ", AdvPy.get_crn())
            print("Seats left: ", AdvPy.get_seats())
            print("\n")
        else:
            print(
                "Sorry ",
                person,
                ", registration is ",
                AdvPy.get_status(),
                " for ",
                AdvPy.get_name(),
                sep="",
            )


main()
