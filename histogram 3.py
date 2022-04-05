import matplotlib.pyplot as plt
import numpy as np
import random
ml_students_age = np.random.randint(18,45, (100))
py_students_age = np.random.randint(15,40, (100))
print(ml_students_age)
print(py_students_age)
bins = [15,20,25,30,35,40,45] # category of ML students age on x axis
plt.figure(figsize = (16,9)) # size of histogram in 16:9 format
plt.hist(ml_students_age, bins, rwidth=0.8, histtype = "bar",
         orientation='vertical', color = "m", label = "ML Student")
plt.title("ML Students age histograms")
plt.xlabel("Students age cotegory")
plt.ylabel("No. Students age")
plt.legend()
plt.show()