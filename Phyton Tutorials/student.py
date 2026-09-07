class Student:
    def __init__(self, roll_number, name):
        self.name = name
        self.roll_number = roll_number
        self.__marks = {}  # Encapsulation

    def get_marks(self):
        return self.__marks

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    def calculate_average(self):
        total = 0

        for mark in self.__marks.values():
            total += mark

        average = total / len(self.__marks)

        print(
            f"Average marks for {self.name} "
            f"(Roll Number: {self.roll_number}): {average}"
        )

        return average

    def is_passed(self):
        has_passed = all(
            mark >= 35 for mark in self.__marks.values()
        )

        if has_passed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")

        return has_passed

    def calculate_grade(self):
        percentage = self.calculate_average()

        if percentage >= 90:
            grade = "A"
        elif percentage >= 85:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        print(f"Grade: {grade}")
        return grade


class ReportCard:
    def generate(self, student):
        student_marks = student.get_marks()

        print("\n==============================")
        print(f"Student Name: {student.name}")
        print(f"Roll Number: {student.roll_number}")
        print("==============================")

        print("Marks:")

        for subject, marks in student_marks.items():
            print(f"{subject}: {marks}")

        print("------------------------------")

        student.calculate_average()
        student.is_passed()
        student.calculate_grade()

        print("==============================")


class Classroom:
    def __init__(self, grade, section):
        self.grade = grade
        self.section = section
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def calculate_class_average(self):
        total_average = 0

        for student in self.students:
            total_average += student.calculate_average()

        class_average = total_average / len(self.students)

        print(
            f"\nClass Average for Grade {self.grade} "
            f"Section {self.section}: {class_average}"
        )

        return class_average

    def get_student_by_roll_number(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student

        return None


# --------------------------------
# MAIN PROGRAM
# --------------------------------

# Create a student
a = Student(1, "John")

# Add marks
a.add_marks("Maths", 100)
a.add_marks("Science", 30)

# Create classroom
c = Classroom(10, "A")

# Add student to classroom
c.add_student(a)

# Find student by roll number
student = c.get_student_by_roll_number(1)

if student:
    print("Student found:", student.name)
else:
    print("Student not found")

# Generate report card
report = ReportCard()
report.generate(a)

# Calculate class average
c.calculate_class_average()