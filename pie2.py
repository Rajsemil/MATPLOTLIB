import matplotlib.pyplot as plt
classes = ["Python", 'R', 'Machine Learning', 'Artificial Intelligence', 
           'Data Sciece']
class1_students = [45, 15, 35, 25, 30]
plt.pie(class1_students, labels = classes)
plt.show()