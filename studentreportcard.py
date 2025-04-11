def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"

def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter numeric value.")

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().upper()
        if choice in ['Y', 'N']:
            return choice
        else:
            print("Invalid input. Please press 'Y' for Yes or 'N' for No.")

def main():
    students = []

    while True:
        print("\n--- Enter Student Details ---")
        name = input("Student Name: ").strip()
        roll = input("Roll Number: ").strip()

        subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
        marks = {}

        for subject in subjects:
            marks[subject] = get_valid_marks(subject)

        total_marks = sum(marks.values())
        percentage = total_marks / len(subjects)
        grade = calculate_grade(percentage)

        students.append({
            "name": name,
            "roll": roll,
            "marks": marks,
            "total": total_marks,
            "percentage": percentage,
            "grade": grade
        })

        print(f"\nRecord of {name} inserted successfully.")
        choice = get_yes_no("Do you want to insert more? Press 'Y' for Yes or 'N' for No: ")
        if choice == 'N':
            break

    # Display all student report cards
    print("\n\n========== STUDENT REPORT CARDS ==========")
    for student in students:
        print("\n------------------------------------------")
        print(f"Name: {student['name']}")
        print(f"Roll Number: {student['roll']}")
        print("Marks:")
        for subject, mark in student['marks'].items():
            print(f"  {subject}: {mark}")
        print(f"Total Marks: {student['total']}")
        print(f"Percentage: {student['percentage']:.2f}%")
        print(f"Grade: {student['grade']}")
        print("------------------------------------------")

if __name__ == "__main__":
    main()
