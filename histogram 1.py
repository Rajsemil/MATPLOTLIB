import matplotlib.pyplot as plt
import numpy as np
import random
ml_students_age = np.random.randint(18,45, (100))
py_students_age = np.random.randint(15,40, (100))
print(ml_students_age)
print(py_students_age)
plt.hist(ml_students_age)
plt.title("ML Students age histograms")
plt.xlabel("Students age cotegory")
plt.ylabel("No. Students age")
plt.show()