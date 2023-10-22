lloyd = {
 "name": "Lloyd",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}
alice = {
 "name": "Alice",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}
tyler = {
 "name": "Tyler",
 "homework": [0.0, 87.0, 75.0, 22.0],
 "quizzes": [0.0, 75.0, 78.0],
 "tests": [100.0, 100.0]
}

students = []
students.append(lloyd)
students.append(alice)
students.append(tyler)

def average(numbers):
  total = sum(numbers)
  floatedscore = float(total)
  lengthofscore = len(numbers)
  averagescore = floatedscore / lengthofscore
  return averagescore

def get_average(student):
  aresult = student.get('homework')
  homework = average(aresult)
  bresult = student.get('quizzes')
  quizzes = average(bresult)
  cresult = student.get('tests')
  tests = average(cresult)
  finalgrade = homework/10 + quizzes*3/10 + tests*6/10
  return finalgrade

def get_letter_grade(score):
 if score >= 90:
  return "A"
 elif score >= 80:
  return "B"
 elif score >= 70:
  return "C"
 elif score >= 60:
  return "D"
 else:
  return "E"

def get_Class_average(students):
 results = []
 for student in students:
  studentresult = get_average(student)
  results.append(studentresult)
  averageresult = average(results)
 return averageresult

for student in students:
 print(f"name: {student.get('name')}\nhomework scores: {student.get('homework')}\nquiz scores: {student.get('quizzes')}\ntest scores: {student.get('tests')}")
 aa = get_average(student)
 dd = get_letter_grade(aa)
 print(f"{student.get('name')}'s letter grade is {dd} and score is {aa}")
bb = get_Class_average(students)
print(f"class average: {bb}")
cc = get_letter_grade(bb)
print(f"class average letter grade: {cc}")