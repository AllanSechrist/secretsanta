import random


class Student(object):
    """
    creates student object
    """

    def __init__(self, name_of_student, id):
        self.name = name_of_student
        self.secret_santa = []
        self.id = id

    def pick_secret_santa(self, list_of_students):
        done = False
        while not done:
            random_student = random.sample(list_of_students, 1)
            if self.name == "SHARIYAH\n":
                self.look_for("PERLA\n", list_of_students)
                done = True
            elif self.name == "DESTINY C.\n":
                self.look_for("DESTINY H\n", list_of_students)
                done = True
            elif self.name == "BELEN\n":
                self.look_for("DESTINY C.\n", list_of_students)
                done = True
            elif self.name == "FABIOLA\n":
                self.look_for("JESUS\n", list_of_students)
                done = True




            elif random_student[0].name != self.name:

                done = True
                self.secret_santa = random_student

            elif len(list_of_students) < 1:
                done = True
                self.secret_santa.append("None")

    def look_for(self, name, where):
        for student in where:
            if student.name == name:
                self.secret_santa.append(student)


class ClassList(object):
    """
    creates a list of students
    """

    def __init__(self, filename, secretfile):
        self.class_list = filename
        self.secret_list = secretfile
        self.names = ''
        self.secret_names = ''
        self.student_list = []
        self.secret_santa_list = []

    def open_file(self, ):
        class_list = open(self.class_list, 'r')
        self.names = class_list.readlines()
        class_list.close()

        print(self.names)

    def run_it(self):
        id = 0
        self.open_file()

        Shariyah = Student("SHARIYAH\n", id)
        DestinyC = Student("DESTINY C.\n", id)
        Belen = Student("BELEN\n", id)
        Fabiola = Student("FABIOLA\n", id)

        preselcted = [Shariyah, Belen, Fabiola, DestinyC]

        for selected in preselcted:
            self.student_list.append(selected)
            self.secret_santa_list.append(selected)

        id += 1

        # creates list of objects
        for name in self.names:
            student = Student(name, id)
            self.student_list.append(student)
            self.secret_santa_list.append(student)
            id += 1

        for student in self.student_list:
            student.pick_secret_santa(self.secret_santa_list)
            remove_from_list(student.secret_santa, self.secret_santa_list)

        print(self.student_list)
        # debug
        for student in self.student_list:
            print(student.name,
                  "is secret santa for: " + student.secret_santa[0].name + " " + str(student.secret_santa[0].id),
                  str(student.id))


# manages program
def main():
    list_of_students = ClassList('names.txt', 'secret_santa.txt')
    list_of_students.run_it()
    quit()


"""
def selection_loop():
    done = False
    while not done:
"""


def remove_from_list(copied_to, copied_from):
    for name in copied_to:
        for copy in copied_from:
            if copy == name:
                copied_from.remove(copy)


if __name__ == "__main__":
    main()
