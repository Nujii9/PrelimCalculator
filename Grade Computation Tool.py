# Function to calculate the attendance grade
def calculate_attendance_grade(number_of_absences):
    if number_of_absences < 0 or number_of_absences > 4:
        return "", None
    if number_of_absences >= 4:
        return "FAILED", None
    attendance_score = max(0, 100 - (number_of_absences * 10))
    return attendance_score

# Function to calculate the class standing
def calculate_class_standing(quizzes_grade, requirements_grade, recitation_grade):
    class_standing = (quizzes_grade * 0.40) + (requirements_grade * 0.30) + (recitation_grade * 0.30)
    return class_standing

# Function to calculate the prelim grade
def calculate_prelim_grade(number_of_absences, quizzes_grade, requirements_grade, recitation_grade, prelim_exam_score):
    attendance_score = calculate_attendance_grade(number_of_absences)
    if isinstance(attendance_score, str):
        return attendance_score, None
    class_standing = calculate_class_standing(quizzes_grade, requirements_grade, recitation_grade)
    if isinstance(class_standing, str):
        return class_standing, None
    prelim_grade = (prelim_exam_score * 0.60) + (attendance_score * 0.10) + (class_standing * 0.30)
    return prelim_grade

# Function to calculate required grades for target
def required_grades_for_target(prelim_grade, target):
    required_midterm = (target - (prelim_grade * 0.20)) / 0.80
    required_final = (target - (prelim_grade * 0.20)) / 0.80
    return required_midterm, required_final

# Function for the inputs to calculate the prelim grade
def calculate_final_grade():
    inputted_prelim_grade = ""
    prelim_result = ""
    midterm_final_result = ""
    dean_result = ""
    result = ""
    
    try:
        # Retrieve inputs
        number_of_absences = int(input("Enter number of absences: "))
        quizzes_grade = float(input("Enter quizzes grade: "))
        requirements_grade = float(input("Enter requirements grade: "))
        recitation_grade = float(input("Enter recitation grade: "))
        prelim_exam_score = float(input("Enter prelim exam score: "))
        
        # Validate inputs (0-100)
        if not (0 <= number_of_absences <= 100) or not (0 <= quizzes_grade <= 100) or not (0 <= requirements_grade <= 100) or not (0 <= recitation_grade <= 100) or not (0 <= prelim_exam_score <= 100):
            raise ValueError("Please input valid score")
        
        # Shows the prelim grade
        prelim_grade = calculate_prelim_grade(number_of_absences, quizzes_grade, requirements_grade, recitation_grade, prelim_exam_score)
        inputted_prelim_grade = f"Your Prelim Grade is: {prelim_grade:.2f}"
        print(inputted_prelim_grade)
        
        # Shows the result based on prelim grade
        if prelim_grade < 25.5:
            prelim_result = "It is difficult to pass based on given grades. To pass, make sure to achieve the required grades: "
        elif prelim_grade < 75:
            prelim_result = "To pass with 75% as a minimum subject grade, just try to achieve the required grades for this semester below: "
        else:
            prelim_result = "To pass (75% overall), you need at least:"
        
        print(prelim_result)

        # Shows the required midterm and final grades
        if prelim_grade < 75:
            required_midterm_pass, required_final_pass = required_grades_for_target(prelim_grade, 75)
            midterm_final_result = f"Required midterm grade: {required_midterm_pass:.2f}, Required final grade: {required_final_pass:.2f}"
        else:
            required_midterm_pass, required_final_pass = required_grades_for_target(prelim_grade, 75)
            midterm_final_result = f"Required midterm grade: {required_midterm_pass:.2f}, Required final grade: {required_final_pass:.2f}"
        
        print(midterm_final_result)

        # Checks if the student is eligible for dean and shows the dean's list result
        if prelim_grade >= 69:
            required_midterm_deans, required_final_deans = required_grades_for_target(prelim_grade, 90)
            dean_result = f"To qualify for Dean's Lister (90% overall), you need at least: {required_midterm_deans:.2f} for midterm and {required_final_deans:.2f} for finals."
        else:
            dean_result = "Becoming a Dean's Lister is not achievable based on your current Prelim grade."
        
        print(dean_result)
    
    # Error handling for invalid inputs
    except ValueError as e:
        result = f"Error: {str(e)}"
        print(result)

# Call the function to calculate final grade
calculate_final_grade()
