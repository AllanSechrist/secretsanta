import random


class Student(object):
    """
    creates student object
    """

    def __init__(self, name_of_student):
        self.name = name_of_student
        self.secret_santa = []

    def pick_secret_santa(self, list_of_students):
        done = False
        while not done:
            random_student = random.sample(list_of_students, 1)
            if random_student[0].name != self.name:
                done = True
                self.secret_santa = random_student


class ClassList(object):
    """
    creates a list of students
    """

    def __init__(self, filename):
        self.class_list = filename
        self.names = ''
        self.student_list = []
        self.secret_santa_list = []

    def open_file(self):
        class_list = open(self.class_list, 'r')
        self.names = class_list.readlines()
        class_list.close()

        print(self.names)

    def run_it(self):
        self.open_file()
        # creates list of objects
        for name in self.names:
            student = Student(name)
            self.student_list.append(student)
            self.secret_santa_list.append(student)

        for student in self.student_list:
            student.pick_secret_santa(self.secret_santa_list)
            remove_from_list(student.secret_santa, self.secret_santa_list)

        print(self.student_list)
        # debug
        for student in self.student_list:
            print(student.name, "is secret santa for: " + student.secret_santa[0].name)

# manages program
def main():
    list_of_students = ClassList('names.txt')
    list_of_students.run_it()


def remove_from_list(copied_to, copied_from):
    for name in copied_to:
        for copy in copied_from:
            if copy == name:
                copied_from.remove(copy)

if __name__ == "__main__":
    main()