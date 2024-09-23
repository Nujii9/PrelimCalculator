<!DOCTYPE html>
<html>
<head>
    <title>Prelim Calculator</title>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <script>
        // Function to check if the student has passed or failed based on number of absences
        function checkAttendance() {
        // Get the number of absences and check if it is greater than or equal to 4 (4 is the maximum number of absences allowed)
        const number_of_absences = parseInt(document.getElementById('number_of_absences').value);
        // Set the result text to "FAILED" if the number of absences is greater than or equal to 4.
        const result = number_of_absences >= 4 ? "FAILED" : "";
        // Set the result text in the HTML
        document.getElementById('result').textContent = result;
        // Clear other result divs
        document.getElementById('inputted_prelim_grade').textContent = "";
        document.getElementById('prelim_result').textContent = "";
        document.getElementById('midterm_final_result').textContent = "";
        document.getElementById('dean_result').textContent = "";
        }
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: url('bgegr.jpg') no-repeat;
            text-align: center;
            padding: 0;
        }
        .container {
            background-color: #111;
            color: #fff;
            max-width: 500px;
            margin: 30px auto;
            padding: 30px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #192ce7;
            border-radius: 5px;
        }
        button {
            background-color: #0a1582;
            color: #000;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            font-size: 16px;
        }
        button:hover {
            background-color: #0f20cb;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background-color: #0f197d;
            border-radius: 5px;
        }
    </style>    
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css">
</head>
<body>
    <div id="container">
        <div class="container">
            <h1>Prelim Grade Calculator</h1>
            <!-- Form to enter number of absences and directs the input to the checkAttendance function -->
            <form oninput="checkAttendance()" id="gradeForm">
                <div>
                <label for="number_of_absences">Number of Absences:</label>
                <input type="number" id="number_of_absences" value="0" min="0" max="100" placeholder="Enter Number of Absences">
                </div>
            </form>
            <!-- Form to enter recitation, quizzes, requirements, and prelim exam grades -->
            <form id="gradeForm">
                <div>
                    <label for="recitation_grade">Recitation Grade:</label>
                    <input type="number" id="recitation_grade" min="1" max="100" placeholder="Enter Recitation Grade: 0-100">
                </div>
                <div>
                    <label for="quizzes_grade">Quizzes Grade:</label>
                    <input type="number" id="quizzes_grade" min="1" max="100" placeholder="Enter Quizzes Grade: 0-100">
                </div>
                <div>
                    <label for="requirements_grade">Requirements Grade:</label>
                    <input type="number" id="requirements_grade" min="1" max="100" placeholder="Enter Requirements Grade: 0-100">
                </div>
                <div>
                    <label for="prelim_exam_score">Prelim Exam Score:</label>
                    <input type="number" id="prelim_exam_score" min="1" max="100" placeholder="Enter Prelim Exam Score: 0-100">
                </div>
                <button type="button" id="calculate_button">Calculate</button>
            </form>
            <!-- Displays the result -->
            <div class="result"></div>
            <h2>Result:</h2>
            <div id="result" class="result"></div>
            <div id="inputted_prelim_grade" class="inputted_prelim_grade"></div>
            <div id="prelim_result" class="prelim_result"></div>
            <div id="midterm_final_result" class="midterm_final_result"></div>
            <div id="dean_result" class="dean_result"></div>
        </div>
    </div>
    <py-script>
    
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
    def calculateFinalGrade(event):
        inputted_prelim_grade = ""
        prelim_result = ""
        midterm_final_result = ""
        dean_result = ""
        result = ""
        
        try:
            # Retrieve inputs
            number_of_absences = Element("number_of_absences").value
            quizzes_grade = Element("quizzes_grade").value
            requirements_grade = Element("requirements_grade").value
            recitation_grade = Element("recitation_grade").value
            prelim_exam_score = Element("prelim_exam_score").value
            
            # Check for missing inputs
            if not number_of_absences or not quizzes_grade or not requirements_grade or not recitation_grade or not prelim_exam_score:
                raise ValueError("Missing or invalid inputs")
            
            # Convert inputs to appropriate types
            number_of_absences = int(number_of_absences)
            quizzes_grade = float(quizzes_grade)
            requirements_grade = float(requirements_grade)
            recitation_grade = float(recitation_grade)
            prelim_exam_score = float(prelim_exam_score)
            
            
            # Validate inputs (0-100)
            if not (0 <= number_of_absences <= 100) or not (0 <= quizzes_grade <= 100) or not (0 <= requirements_grade <= 100) or not (0 <= recitation_grade <= 100) or not (0 <= prelim_exam_score <= 100):
                raise ValueError("Please input valid score")
            
            # Shows the prelim grade
            prelim_grade = calculate_prelim_grade(number_of_absences, quizzes_grade, requirements_grade, recitation_grade, prelim_exam_score)
            inputted_prelim_grade = f"Your Prelim Grade is: {prelim_grade:.2f}"
            
            # Shows the result based on prelim grade
            if prelim_grade < 25.5:
                prelim_result = "It is difficult to pass based on given grades. To pass, make sure to achieve the required grades: "
            elif prelim_grade < 75:
                prelim_result = "To pass with 75% as a minimum subject grade, just try to achieve the required grades for this semester below: "
            else:
                prelim_result = "To pass (75% overall), you need at least:"
            
            # Shows the required midterm and final grades
            if prelim_grade < 75:
                required_midterm_pass, required_final_pass = required_grades_for_target(prelim_grade, 75)
                midterm_final_result = f"Required midterm grade: {required_midterm_pass:.2f}, Required final grade: {required_final_pass:.2f}"
            else:
                required_midterm_pass, required_final_pass = required_grades_for_target(prelim_grade, 75)
                midterm_final_result = f"Required midterm grade: {required_midterm_pass:.2f}, Required final grade: {required_final_pass:.2f}"
            
            # Checks if the student is eligible for dean and shows the dean's list result
            if prelim_grade >= 69:
                required_midterm_deans, required_final_deans = required_grades_for_target(prelim_grade, 90)
                dean_result = f"To qualify for Dean's Lister (90% overall), you need at least: {required_midterm_deans:.2f} for midterm and {required_final_deans:.2f} for finals."
            else:
                dean_result = "Becoming a Dean's Lister is not achievable based on your current Prelim grade."
        
        # Error handling for invalid inputs and resets the input fields
        except ValueError as e:
            result = f"Error: {str(e)}"
            Element("inputted_prelim_grade").element.innerText = ""
            Element("prelim_result").element.innerText = ""
            Element("midterm_final_result").element.innerText = ""
            Element("dean_result").element.innerText = ""
        
        # Shows the results and resets the input fields
        Element("result").element.innerText = result
        Element("inputted_prelim_grade").element.innerText = inputted_prelim_grade
        Element("prelim_result").element.innerText = prelim_result
        Element("midterm_final_result").element.innerText = midterm_final_result
        Element("dean_result").element.innerText = dean_result
        Element("quizzes_grade").element.value = ""
        Element("requirements_grade").element.value = ""    
        Element("recitation_grade").element.value = ""
        Element("prelim_exam_score").element.value = ""
        Element("number_of_absences").element.value = ""
    
    # Set the onclick event for the calculate button to trigger the calculateFinalGrade function
    Element("calculate_button").element.onclick = calculateFinalGrade
    </py-script>
</body>
</html>
