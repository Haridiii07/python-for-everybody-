name = input ("What is Your Name:")
grade_input = input ("Enter your grad (0-100):")
score = float(grade_input)

def calculate_grade (score):
    if score >= 90 :
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else : 
        return 'F'
grade = calculate_grade (score) 
print("Hello", name,"Your grad is:", grade ) 

if grade == 'A':
    print("Excellent!")
elif grade == 'B':
    print("Good job!")
elif grade == 'C' or grade == 'D':
    print("Keep improving!")
else:
    print("You need to work harder.")