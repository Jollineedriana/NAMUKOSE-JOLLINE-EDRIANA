#(i)

user_age = int(input("Enter your age: "))

#  Eligibility based on age
if user_age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")


#(ii)

def grade_students(mark):
    try:
        mark = float(mark)
    except ValueError:
        return 'Invalid input'  
        print("Grade A")

    if mark >= 90:
        grade = 'A'
        message = 'Excellent'
        
    elif 80 <= mark < 90:
        grade = 'B'
        message = 'Excellent'
        
    elif 70 <= mark < 80:
        grade = 'C'
        message = 'Good'
        
    elif 60 <= mark < 70:
        grade = 'D'
        message = 'Satisfactory'
        
    else:
        grade = 'F'
        message = 'Needs improvement'
        
        print(grade_students)

    print (grade, message)


# invalid mark
invalid_mark = 'abc'
result_invalid = grade_students(invalid_mark)
print(result_invalid)