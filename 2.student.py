class School:
    rollStart = 0
    rollList = []

    def __init__(self, name, age, marks):
        School.rollStart += 1
        self.roll = School.rollStart
        self.name = name
        self.age = age
        self.marksToGrade(marks)
        School.rollList.append(self)

    def marksToGrade(self, marks):
        if marks >= 90:
            self.grade = 'A'
        elif 80 <= marks < 89:
            self.grade = 'B'
        elif 70 <= marks < 79:
            self.grade = 'C'
        elif 60 <= marks < 69:
            self.grade = 'D'
        elif 50 <= marks < 59:
            self.grade = 'E'
        else:
            self.grade = 'F'

    def showDetails(self):
        print(f"Name : {self.name}\nAge : {self.age}\nGrade : {self.grade}")


if __name__ == "__main__":
    while True:
        print("\n\n1. Register Student")
        print("2. Display Student")
        print("3. Exit")

        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            name = input("Enter student's name : ")
            age = input("Enter Your Age : ")
            marks = int(input("Enter Your Marks : "))
            student = School(name, age, marks)
            print(f"Student Registered Successfully.\nRoll No : {student.roll}")
        elif choice == 2:
            roll = int(input("Enter Roll Num : "))
            student = next((profile for profile in School.rollList if profile.roll == roll))
            if student:
                student.showDetails()
            # for student in School.rollList:
            #     student.showDetails()
        elif choice == 3:
            break
        else:
            print("Invalid choice! Please enter a valid option (1-3).")
