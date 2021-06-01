import numpy as np
from scipy import stats

marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

mean_marks = np.mean(marks_of_students)
print(mean_marks)
median_marks = np.median(marks_of_students)
print(median_marks)
mode_marks = stats.mode(marks_of_students)
print(mode_marks)
