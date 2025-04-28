import smtplib
from email.mime.text import MIMEText

class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.courses = {}
        self.schedule = []

    def enroll(self, course):
        self.courses[course] = None
        self.schedule.append(course)
        print(f"{self.name} enrolled in {course}")

    def add_grade(self, course, grade):
        if course in self.courses:
            self.courses[course] = grade
            self.send_email(f"Grade updated for {course}: {grade}")
        else:
            print(f"{self.name} is not enrolled in {course}")

    def withdraw(self, course):
        if course in self.courses:
            del self.courses[course]
            self.schedule.remove(course)
            print(f"{self.name} withdrew from {course}")
        else:
            print(f"{self.name} is not enrolled in {course}")

    def display_grades(self):
        print(f"Grades for {self.name}:")
        for course, grade in self.courses.items():
            print(f"{course}: {grade}")

    def display_schedule(self):
        print(f"Schedule for {self.name}:")
        for course in self.schedule:
            print(course)

    def send_email(self, message):
        msg = MIMEText(message)
        msg['Subject'] = 'Grade Update'
        msg['From'] = 'admin@troyuniversity.edu'
        msg['To'] = self.email

        try:
            with smtplib.SMTP('smtp.example.com') as server:
                server.login('your_username', 'your_password')
                server.sendmail('admin@troyuniversity.edu', self.email, msg.as_string())
            print(f"Email sent to {self.email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

# Example usage
student = Student("Jodryn Briggs", "jordynbriggs2006@gamil.com")
student.enroll("Math 101")
student.add_grade("Math 101", "A")
student.display_grades()
student.display_schedule()
student.withdraw("Math 101")
student.display_schedule()
