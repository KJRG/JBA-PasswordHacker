# put your python code here
grades = input().split()
num_a_grades = sum((1 for g in grades if g == "A"))
grade_a_ratio = num_a_grades / len(grades)
print(round(grade_a_ratio, 2))
