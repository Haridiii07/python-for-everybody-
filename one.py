# Prompt user for input
score = input("Enter a score between 0.0 and 1.0: ")

try:
    # Convert input to float
    score = float(score)

    # Check if score is within the valid range
    if score < 0.0 or score > 1.0:
        print("Error: Score is out of range.")
    else:
        # Determine the grade based on the score
        if score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        else:
            grade = "F"

        # Print the grade
        print(f" {grade}")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value between 0.0 and 1.0.")