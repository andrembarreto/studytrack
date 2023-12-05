from subject_controller import SubjectController, Subject
import os

controller = SubjectController()

def add_subject():
    name = input("Enter the subject name: ")
    workload = int(input("Enter the subject workload: "))
    passing_grade = int(input("Enter the subject passing grade: "))

    try:
        controller.add_subject(Subject(name, workload, passing_grade))
        controller.store()
        print(f"Subject {name} saved successfully!")
    except(ValueError):
        print(f"ERROR: Subject {name} already saved!")


def remove_subject():
    name = input("Enter the name of the subject to be removed: ")
    try:
        controller.remove_subject(name)
        controller.store()
        print("Subject successfully removed!")
    except(KeyError):
        print(f"ERROR: Subject {name} is not saved!")
    
def get_average_term_grade():
    print(f"Average Term Grade: {controller.get_average_term_grade()}")

def get_current_term_credits():
    print(f"Current Term Credits: {controller.get_current_term_credits()}")

def has_enouth_credits_to_graduate():
    minimal_credits = int(input("Enter the minimal credits required to graduate: "))

    print(f"Minimal credits to graduate: {minimal_credits}")
    print(f"Current credits: {controller.get_current_term_credits()}")

    if(controller.has_enough_credits_to_graduate(minimal_credits)):
        print("Congratulations, you have enouth credits to graduate!")
    else:
        print("You don't have enough credits to graduate yet")

def print_subjects():
    if len(controller.subjects) == 0:
        print("\nNo subjects added yet!\n")
    for subject in controller.subjects.values():
        print("*********************************************************************************")
        subject.print()
        print("*********************************************************************************")

def print_subjects_by_passing_grade():
    print("Filter by:")
    print("1. Has passing grade")
    print("2. Has no passing grade")

    has_passing_grade = input("Filter: ")

    if(has_passing_grade == "1"):
        has_passing_grade = True
    elif(has_passing_grade == "2"):
        has_passing_grade = False
    else:
        print("ERROR: invalid option")
        return
    
    if len(controller.subjects) == 0:
        print("\nNo subjects added yet!\n")
    
    for subject in controller.filter_by_passing_grade(has_passing_grade).values():
        print("*********************************************************************************")
        subject.print()
        print("*********************************************************************************")
    
def print_subjects_by_study_goal_overdue():
    print("Filter by:")
    print("1. Study goal has overdue")
    print("2. Study goal has not overdue")

    has_overdue = input("Filter: ")

    if(has_overdue == "1"):
        has_overdue = True
    elif(has_overdue == "2"):
        has_overdue = False
    else:
        print("ERROR: invalid option")
        return
    
    if len(controller.subjects) == 0:
        print("\nNo subjects added yet!\n")
    
    for subject in controller.filter_by_passing_grade(has_overdue).values():
        print("*********************************************************************************")
        subject.print()
        print("*********************************************************************************")

def update_subject_attendance():
    subject_name = input("Enter the subject name: ")
    hours = int(input("Enter the hours to add in subject attendance: "))

    try:
        controller.update_subject_attendance(subject_name, hours)
        controller.store()
        print("Subject attendance updated successfully!")
    except(KeyError):
        print(f"ERROR: Subject {subject_name} is not saved!")
    except(ValueError):
        print(f"The final attendance value cannot be less than 0")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

controller.load()

print("""\
     _             _       _                  _
 ___| |_ _   _  __| |_   _| |_ _ __ __ _  ___| | __
/ __| __| | | |/ _` | | | | __| '__/ _` |/ __| |/ /
\__ | |_| |_| | (_| | |_| | |_| | | (_| | (__|   <
|___/\__|\__,_|\__,_|\__, |\__|_|  \__,_|\___|_|\_\\
                     |___/""")
while True:
    print("\nSelect an option:")
    print("1. List subjects")
    print("2. Add subject")
    print("3. Remove subject")
    print("4. Search subjects by filter")
    print("5. Calculate average term grade")
    print("6. Calculate current credits")
    print("7. Check graduation status")
    print("8. Update subject attendance")

    selected_option = input("Option: ")

    clear_terminal()
    if selected_option == '1':
        print_subjects()
    elif selected_option == '2':
        add_subject()
    elif selected_option == '3':
        remove_subject()
    elif selected_option == '4':
        print("Select the desired filter:")
        print("1. Filter by passing grade")
        print("2. Filter by study goal overdue")
        filter = input("Option: ")
        if filter == '1':
            print_subjects_by_passing_grade()
        elif filter == '2':
            print_subjects_by_study_goal_overdue()
        else:
            print("ERROR: invalid option")
    elif selected_option == '5':
        get_average_term_grade()
    elif selected_option == '6':
        get_current_term_credits()
    elif selected_option == '7':
        has_enouth_credits_to_graduate()
    elif selected_option == '8':
        update_subject_attendance()
    else:
        print("ERROR: invalid option")
