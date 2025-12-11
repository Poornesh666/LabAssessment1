marks = int(input("Enter the student's marks (0–100): "))

if marks > 100 or marks < 0:
    print("Invalid Marks!")
elif marks >= 95:
    print("Grade: A+")
elif marks >= 90:
    print("Grade: S")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >- 50:
    print("Grade: D")
else:
    print("Grade: F")