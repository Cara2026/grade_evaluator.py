# =========================================================
# PROJECT: STUDENT GRADE EVALUATION TOOL
# PURPOSE: This program takes a student's numeric test score 
#          and categorizes it as Excellent, Pass, or Fail.
# =========================================================

def main():
    # STEP 1: Greet the user and explain what the program does.
    print("--- Welcome to the Student Grade Evaluator ---")
    
    # We use a 'try' block to handle potential errors gracefully.
    # If the user enters text instead of a number, the program won't crash.
    try:
        # STEP 2: Ask the user for the student's score.
        # input() grabs the data as text.
        # float() converts that text into a number so we can do math with it.
        score_input = input("Please enter the exam score (from 0 to 100): ")
        score = float(score_input)

        # STEP 3: Validate the range.
        # Check if the score is logically possible (between 0 and 100).
        if score < 0 or score > 100:
            print("Error: The score must be between 0 and 100. Please try again.")
        
        # STEP 4: Start the Grading Logic.
        # The program checks these conditions one by one from top to bottom.
        
        # Check if the score qualifies as "Excellent".
        if score >= 90:
            print(f"Final Score: {score}")
            print("Evaluation Result: Excellent!")
            
        # If not Excellent, check if it is at least a "Pass" (60 or higher).
        elif score >= 60:
            print(f"Final Score: {score}")
            print("Evaluation Result: Pass.")
            
        # If the score doesn't meet any of the above, it falls into this last category.
        else:
            print(f"Final Score: {score}")
            print("Evaluation Result: Fail.")

    # STEP 5: Error Handling.
    # If the 'float()' conversion in Step 2 fails (e.g., the user typed 'ABC'),
    # the program jumps here instead of showing a scary red error.
    except ValueError:
        print("Invalid Input! Please make sure to enter a number (e.g., 85 or 92.5).")

# This line tells Python to start the program by running the 'main' function above.
if __name__ == "__main__":
    main()
