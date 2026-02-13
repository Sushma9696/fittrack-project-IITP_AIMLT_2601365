student_name=input("Enter student name: ") 
while True:
  mat_marks=int(input("\nEnter Maths marks: "))
  sci_marks=int(input("\nEnter Science marks: "))
  eng_marks=int(input("\nEnter English marks: "))
  if mat_marks==0 or mat_marks>100 or sci_marks==0 or sci_marks>100 or eng_marks==0 or eng_marks>100 :
    print("\nInvalid marks entered")
    break
  else:
    total_marks=mat_marks+sci_marks+eng_marks
    avg_percent=total_marks/3

    if mat_marks<40 or sci_marks<40 or eng_marks<40:
      status="FAIL"
    else:
      status="PASS" 

    if avg_percent>=75:
      grade='A'

    elif avg_percent>=60:
      grade='B'  

    elif avg_percent>=40:
      grade='C'

    else:
      grade="Not Applicable"  

    print(f"\nStudent Name: {student_name}") 
    print(f"\nTotal Marks: {total_marks}")
    print(f"\nPercentage: {avg_percent:.2f}")
    print(f"\nStatus: {status}")

    if status=="PASS":
      print(f"\nGrade: {grade}") 

    break