import matplotlib.pyplot as plt
import numpy as np
students = ["Arun", "Bharath", "Chaitanya", "Dinesh", "Esha"]
marks = [75, 85, 90, 70, 95]
plt.scatter(marks, students)
plt.xlabel('Marks')
plt.ylabel('Students')
plt.title('Student Marks')
plt.grid()
plt.show()  