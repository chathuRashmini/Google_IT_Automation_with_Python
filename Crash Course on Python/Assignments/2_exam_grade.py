# Students in a class receive their grades as Pass/Fail. 
# Scores of 60 or more (out of 100) mean that the grade is "Pass".
# For lower scores, the grade is "Fail".
# In addition, scores above 95 (not included) are graded as "Top Score".

def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65))
print(exam_grade(55))
print(exam_grade(60))
print(exam_grade(95))
print(exam_grade(100))
print(exam_grade(0))
