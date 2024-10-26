import json  # Import the json module to work with JSON files.

class Student:
    """A class to represent a student with attributes and methods to manage grades."""

    def __init__(self, name, student_id):
        """
        Initialize the student with a name, ID, and an empty list of grades.
        Args:
            name (str): Name of the student.
            student_id (str): Student's unique ID.
        """
        self.name = name
        self.id = student_id
        self.grades = []  # Stores the grades of the student.

    def add_grade(self, grade):
        """
        Add a valid grade to the student's list of grades.
        Args:
            grade (int): Grade between 0 and 100.
        """
        if 0 <= grade <= 100:  # Check if the grade is within a valid range.
            self.grades.append(grade)
        else:
            print("Invalid grade! Must be between 0 and 100.")

    def calculate_average(self):
        """
        Calculate the average of the student's grades.
        Returns:
            float: Average grade or 0 if there are no grades.
        """
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def has_passed(self):
        """
        Determine if the student has passed (average >= 60).
        Returns:
            bool: True if passed, False otherwise.
        """
        return self.calculate_average() >= 60

    def to_dict(self):
        """
        Convert student details to a dictionary for JSON storage.
        Returns:
            dict: Student data as a dictionary.
        """
        return {"name": self.name, "id": self.id, "grades": self.grades}

def save_students_to_file(students, filename="students.json"):
    """
    Save a list of students to a JSON file.
    Args:
        students (list): List of Student objects.
        filename (str): Name of the JSON file.
    """
    with open(filename, 'w') as file:
        json_data = [student.to_dict() for student in students]  # Convert each student to a dictionary.
        json.dump(json_data, file, indent=4)  # Write to JSON with indentation for readability.
    print("Students saved to file successfully!")

def load_students_from_file(filename="students.json"):
    """
    Load students from a JSON file.
    Args:
        filename (str): Name of the JSON file.
    Returns:
        list: List of Student objects.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)  # Load data from JSON.
            students = [Student(d["name"], d["id"]) for d in data]  # Create Student objects.
            for student, d in zip(students, data):
                student.grades = d["grades"]  # Assign grades from JSON data.
            print("Students loaded successfully!")
            return students
    except FileNotFoundError:
        print("No saved students found. Starting fresh.")
        return []

def add_student():
    """
    Add a new student by taking user input.
    Returns:
        Student: A new Student object.
    """
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    return Student(name, student_id)

def add_grades(student):
    """
    Add grades for five different subjects for a specific student.
    Args:
        student (Student): The student to whom grades will be added.
    """
    print(f"Adding grades for {student.name}. You will enter grades for 5 subjects.")

    # List of subjects for which grades will be entered.
    subjects = ["Python Programming", "Theory of Programming", "NLP", "Prolog", "Maths"]

    for subject in subjects:
        while True:
            grade_input = input(f"Enter {subject} grade (0-100): ")
            try:
                grade = int(grade_input)
                if 0 <= grade <= 100:
                    student.add_grade(grade)  # Add grade if valid.
                    break  # Exit loop on valid input.
                else:
                    print("Invalid grade! Please enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print("All grades have been added successfully.")

def show_student_info(student):
    """
    Display a student's information, including grades, average, and pass/fail status.
    Args:
        student (Student): The student whose information will be shown.
    """
    print(f"\nStudent: {student.name} (ID: {student.id})")
    print(f"Grades: {student.grades}")
    average = student.calculate_average()
    print(f"Average: {average:.2f}")
    status = "Passed" if student.has_passed() else "Failed"
    print(f"Status: {status}\n")

def main():
    """Main function to run the student grades management system."""
    students = load_students_from_file()  # Load students from file at startup.

    while True:
        print("\n--- Student Grades System ---")
        print("1. Add Student")
        print("2. Add Grades to a Student")
        print("3. Show Student Info")
        print("4. Save Students to File")
        print("5. Load Students from File")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student = add_student()
            students.append(student)  # Add the new student to the list.
            print("Student added successfully!")

        elif choice == '2':
            if not students:
                print("No students available. Add a student first.")
                continue  # Skip to the next iteration if no students are available.
            for i, student in enumerate(students, 1):
                print(f"{i}. {student.name} (ID: {student.id})")
            student_index = int(input("Select a student by number: ")) - 1
            if 0 <= student_index < len(students):
                add_grades(students[student_index])  # Add grades to the selected student.
            else:
                print("Invalid choice.")

        elif choice == '3':
            if not students:
                print("No students available.")
                continue
            for i, student in enumerate(students, 1):
                print(f"{i}. {student.name} (ID: {student.id})")
            student_index = int(input("Select a student by number: ")) - 1
            if 0 <= student_index < len(students):
                show_student_info(students[student_index])  # Show the selected student's info.
            else:
                print("Invalid choice.")

        elif choice == '4':
            save_students_to_file(students)  # Save students to the file.

        elif choice == '5':
            students = load_students_from_file()  # Reload students from the file.

        elif choice == '6':
            print("Exiting... Goodbye!")
            break  # Exit the program.

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Start the program.
