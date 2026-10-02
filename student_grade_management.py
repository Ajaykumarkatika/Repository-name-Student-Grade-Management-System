# Student Grade Management System

students = {}


def calculate_grade(average):
    """Return a grade based on the average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    return "F"


def get_valid_mark():
    """Read and validate a mark between 0 and 100."""
    while True:
        try:
            mark = float(input("Enter marks (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Invalid marks! Enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def add_student():
    """Add a student and marks for multiple subjects."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    if name in students:
        print("Student already exists!")
        return

    try:
        count = int(input("Enter number of subjects: "))
        if count <= 0:
            print("Number of subjects must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Enter a valid number.")
        return

    subjects = {}

    for i in range(count):
        while True:
            subject = input(f"Enter subject {i + 1} name: ").strip()

            if not subject:
                print("Subject name cannot be empty.")
            elif subject in subjects:
                print("Subject already added!")
            else:
                break

        subjects[subject] = get_valid_mark()

    students[name] = subjects
    print(f"Student '{name}' added successfully!")


def display_student(name):
    """Display one student's academic record."""
    subjects = students[name]
    total = sum(subjects.values())
    average = total / len(subjects)
    grade = calculate_grade(average)

    print("\n------------------------------")
    print(f"Student Name : {name}")
    print("------------------------------")

    for subject, mark in subjects.items():
        print(f"{subject:<15} : {mark:.2f}")

    print("------------------------------")
    print(f"Total         : {total:.2f}")
    print(f"Average       : {average:.2f}")
    print(f"Grade         : {grade}")
    print("------------------------------")


def display_all_students():
    """Display all stored student records."""
    if not students:
        print("\nNo student records available.")
        return

    for name in students:
        display_student(name)


def search_student():
    """Search for a student by name."""
    name = input("Enter student name to search: ").strip()

    if name in students:
        display_student(name)
    else:
        print(f"Student '{name}' not found.")


def main():
    """Run the command-line menu."""
    while True:
        print("\n===================================")
        print("     STUDENT GRADE MANAGEMENT")
        print("===================================")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")
        print("===================================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you for using the Student Grade Management System!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
