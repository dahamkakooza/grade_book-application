class Student:
    def __init__(self, email, names):
        """
        Initialize a new student with the given email and names.
        
        :param email: The student's email address.
        :param names: The student's full names.
        """
        self.email = email
        self.names = names
        self.courses_registered = []
        self.gpa = 0.0

    def calculate_gpa(self):
        """
        Calculate the GPA for the student based on registered courses and their grades.
        """
        if not self.courses_registered:
            self.gpa = 0.0
        else:
            total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
            total_credits = sum(course['credits'] for course in self.courses_registered)
            self.gpa = total_points / total_credits if total_credits > 0 else 0.0

    def register_for_course(self, course, grade):
        """
        Register the student for a course with the given grade.
        
        :param course: The course object.
        :param grade: The grade obtained in the course.
        """
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})


class Course:
    def __init__(self, name, trimester, credits):
        """
        Initialize a new course with the given name, trimester, and credits.
        
        :param name: The name of the course.
        :param trimester: The trimester in which the course is offered.
        :param credits: The number of credits the course is worth.
        """
        self.name = name
        self.trimester = trimester
        self.credits = credits


class GradeBook:
    def __init__(self):
        """
        Initialize a new grade book to manage students and courses.
        """
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        """
        Add a new student to the grade book.
        
        :param email: The student's email address.
        :param names: The student's full names.
        """
        student = Student(email, names)
        self.student_list.append(student)
        print(f"Student {names} added successfully.")

    def add_course(self, name, trimester, credits):
        """
        Add a new course to the grade book.
        
        :param name: The name of the course.
        :param trimester: The trimester in which the course is offered.
        :param credits: The number of credits the course is worth.
        """
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        print(f"Course {name} added successfully.")

    def register_student_for_course(self, student_email, course_name, grade):
        """
        Register a student for a course with the given grade.
        
        :param student_email: The email of the student to register.
        :param course_name: The name of the course to register for.
        :param grade: The grade obtained in the course.
        """
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            student.calculate_gpa()
            print(f"Student {student.names} registered for course {course_name} with grade {grade}.")
        else:
            print("Student or course not found.")

    def calculate_ranking(self):
        """
        Calculate and display the ranking of students based on their GPA.
        """
        self.student_list.sort(key=lambda s: s.gpa, reverse=True)
        for rank, student in enumerate(self.student_list, start=1):
            print(f"Rank {rank}: {student.names} with GPA {student.gpa}")

    def search_by_grade(self, grade):
        """
        Search for students who obtained a specific grade in any course.
        
        :param grade: The grade to search for.
        """
        for student in self.student_list:
            for course in student.courses_registered:
                if course['grade'] == grade:
                    print(f"Student {student.names} obtained grade {grade} in course {course['course'].name}")

    def generate_transcript(self, student_email):
        """
        Generate and display the transcript for a specific student.
        
        :param student_email: The email of the student whose transcript to generate.
        """
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print(f"Transcript for {student.names}:")
            for course in student.courses_registered:
                print(f"Course: {course['course'].name}, Grade: {course['grade']}, Credits: {course['credits']}")
            print(f"Overall GPA: {student.gpa}")
        else:
            print("Student not found.")

    def user_interface(self):
        """
        Provide a user interface for interacting with the grade book application.
        """
        while True:
            print("\n--- Grade Book Application ---")
            print("1. Add student")
            print("2. Add course")
            print("3. Register student for course")
            print("4. Calculate ranking")
            print("5. Search by grade")
            print("6. Generate transcript")
            print("7. Exit")
            choice = input("Choose an action: ")

            if choice == '1':
                email = input("Enter student email: ")
                names = input("Enter student names: ")
                self.add_student(email, names)
            elif choice == '2':
                name = input("Enter course name: ")
                trimester = input("Enter course trimester: ")
                credits = float(input("Enter course credits: "))
                self.add_course(name, trimester, credits)
            elif choice == '3':
                student_email = input("Enter student email: ")
                course_name = input("Enter course name: ")
                grade = float(input("Enter grade: "))
                self.register_student_for_course(student_email, course_name, grade)
            elif choice == '4':
                self.calculate_ranking()
            elif choice == '5':
                grade = float(input("Enter grade to search: "))
                self.search_by_grade(grade)
            elif choice == '6':
                student_email = input("Enter student email: ")
                self.generate_transcript(student_email)
            elif choice == '7':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    gradebook = GradeBook()
    gradebook.user_interface()
