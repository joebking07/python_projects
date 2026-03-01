import json


FILE = "student.json"


def load_file():
    try:

        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_file(student):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(student, f, indent=4, ensure_ascii=False)


def menu_display():
    print("\n" + "=" * 60)
    print("       STUDENT'S NOTE MANAGER".center(60))
    print("=" * 60)
    print("1. Added student")
    print("2. Modify student information")
    print("3. Remove student")
    print("4. Display student's list and information about")
    print("5. Added student's note")
    print("6. Modify notes of student")
    print("7. Remove student's note")
    print("8. Display note of student")
    print("9. Quit")
    print("=" * 60)


def add_student():
    student = load_file()
    regist_number = input("enter the registration number:").strip()
    if regist_number in student:
        print("❌this student is already exist!")
    else:
        try:
            Name = input("enter the full name of the student").strip()
            study_field = input("student's field of study").strip()
            if not Name or not study_field:
                print("❌ Name and field of study cannot be empty!")
                return
            student[regist_number] = {
                "name": Name,
                "notes": {},
                "study_field": study_field,
            }
            save_file(student)
            print(" ✅ the student is added successfully")

        except Exception as e:
            print(f"error: {e}")


def display_student():
    student = load_file()
    if not student:
        print("No student exist in the database.")
        return

    print("\n📋 list of all students")
    for i, (regist_number, data) in enumerate(student.items(), 1):

        print(
            f"{i}. Reg # :{regist_number}| name: {data["name"]}| study field: {data["study_field"]}"
        )


def student_display_specifc():
    student = load_file()
    regist_number = input("enter the registration number: ").strip()
    if regist_number not in student:
        print("❌ This student does not exist in database!")
        return

    data = student[regist_number]
    print(f"the student N: {regist_number}")
    print(f" Name: {data["name"]}")
    print(f"the study field: {data["study_field"]}")
    print(f"the note: {data.get('notes', {} )}")


def modif_info_student():
    student = load_file()
    if not student:
        print("❌any student no exisist in database")
        return
    else:
        regist_number = input("enter the registration number: ").strip()
        for i, (regist_number, data) in enumerate(student.items(), 1):
            if regist_number in student:
                print(
                    f"{i}:registration number: {regist_number} -name {data["name"]} note:{data["notes"]} study field:{data["study_field"]} "
                )
                qst = input("enter yes or no to change information of student:").strip()
                if qst == "yes":
                    print("1. name")
                    print("2. study field")
                    info = input(
                        "enter the information that you need do modify:"
                    ).strip()

                    if info == "1":
                        modif_name = input("enter the name :").strip()
                        data["name"] = modif_name
                        break
                    elif info == "2":
                        new_field = input("enter the new study field:").strip()
                        data["study_field"] = new_field
                        break
                    else:
                        print("invalid choice !")
                        return
                save_file(student)
                print("✅ Student information updated successfully!")


def remove_student():
    student = load_file()
    display_student()
    if not student:
        print("❌ any student are in the database")

    regist_number = input("registration number of student: ").strip()
    if regist_number in student:
        name = student[regist_number]["name"]
        del student[regist_number]
        save_file(student)
        print(f"🗑️ this student{name} is removed successfully!")
    else:
        print(f"This student does not exist in our database!")


def note_student():
    student = load_file()
    if not student:
        print("No students in the database.")
        return

    display_student()
    try:
        regist_number = input("registration number of student").strip()
        if regist_number not in student:
            print("this student is not exist in database")
        else:
            num_devoir = float(input("enter the note of written assignement "))
            num_partiel = float(input("enter the note of exams"))

            student[regist_number]["notes"] = {
                "devoir": num_devoir,
                "exams": num_partiel,
            }
            save_file(student)

        print("✅the note are added successfully!")
    except ValueError:
        print("❌ invalid entry for notes!")


def modif_note():
    student = load_file()
    display_note()

    if not student:
        return
    else:
        regist_number = input("registration number of student: ").strip()
        if not regist_number in student or student[regist_number]["notes"] == {}:
            print("❌ this student does not have notes!")
            return

        qst = input("which note  you need to modify?(devoir/Exam): ").strip().lower()
        if qst not in ["exam ,devoir"]:
            print("❌ invalid entry!")
            return
        try:
            if qst == "devoir":
                num_devoir = float(
                    input("enter the note new note of written assignement ")
                )
            elif qst == num_partiel:
                num_partiel = float(input("enter the  new exams note"))
                student[regist_number]["notes"] = {
                    "devoir": num_devoir,
                    "exams": num_partiel,
                }
                save_file(student)

            print("✅the note is modify sucessfully!")
        except ValueError:
            print("invalid entry!")


def remove_note():
    student = load_file()
    display_note()
    if not student:
        return
    else:
        regist_number = input("registration number of student").strip()
        if regist_number not in student or not student[regist_number]["notes"]:
            print("this student not have note!")
            return

        else:
            qst = input("remove option(all/devoir/exams)").strip().lower()
            if qst not in ["all", "devoir", "exams"]:
                print("invalid option!")
                return
            else:
                if qst == "all":
                    student[regist_number]["notes"] = {}
                else:

                    if qst == "devoir":
                        student[regist_number]["notes"]["devoir"] = {}
                    elif qst == "exams":
                        student[regist_number]["notes"]["exams"] = {}
        save_file(student)
        print("🗑️ the note is removed successfully!")


def display_note():
    student = load_file()
    if student == {}:
        print("No note in database!")
        return

    for i, (regist_number, data) in enumerate(student.items(), 1):

        print(
            f"{i} -registration number{regist_number} -student: {data["name"]} -{data["study_field"]} \n -note written assignment:{data["notes"]}"
        )


def main_func_student():

    while True:
        menu_display()
        option = input("enter an option:").strip()
        if option not in [str(i) for i in range(1, 10)]:
            print("❌ Error: invalid entry!")
        else:
            if option == "1":
                add_student()
            elif option == "2":
                modif_info_student()
            elif option == "3":
                remove_student()
            elif option == "4":
                display_student()
            elif option == "5":
                note_student()
            elif option == "6":
                modif_note()
            elif option == "7":
                remove_note()
            elif option == "8":
                display_note()
            elif option == "9":
                print("👋 good bye")
                break


if __name__ == "__main__":
    main_func_student()
