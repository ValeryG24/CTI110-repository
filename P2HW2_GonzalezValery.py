#Valery Gonzalez
# April 14, 2024
# P2HW2
# Modules grades
 
# Initialize an empty list to store module grades
module_grades = []

# Loop through each module to ask for grades
module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

# Display the results
print(" --------Results-------- ")

# Display the lowest grade
lowest_grade = min(module_grades)
print("Lowest Grade:\t", lowest_grade)
# Display the highest grade

highest_grade = max(module_grades)
print("Highest grade:\t", highest_grade)

# Calculate and display the sum of grades
total_grades = sum(module_grades)
print("Sum of grades:\t", total_grades)

# Calculate and display the average grade
average_grade = total_grades / len(module_grades)
print("Average:\t {:.2f}".format(average_grade))
print(" ---------------------------------------- ")
