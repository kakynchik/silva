students_grades = {
    'panialbina': 90,
    'dima': 85,
    'marchik': 95,
    'alek': 92,
    'evgesha': 88
}
best_student = max(students_grades, key=students_grades.get)
print("people z naybilshoyu ocinkoyu:", best_student)