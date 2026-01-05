import matplotlib.pyplot as plt   

# student data
students_names = ["sanjay", "rahul", "karan", "wasim", "ajay", "sartaj", "priya"]
students_marks = [35,50,20,45,25,40,25]

# calculating percentage amrks
marks_perc = [(marks / 50) * 100 for marks in students_marks]

# line chart
def marks_line_chart():
    plt.plot(students_names, students_marks, marker='o', linestyle='-', color='pink', ms= 20, mec='r', linewidth='5')
    plt.title("student marks graph")
    plt.xlabel("student names")
    plt.ylabel("marks out of 50")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# bar chart for percentage
def percentage_bar_chart():
    plt.bar(students_names, marks_perc, color='green')
    plt.title("students percentage graph")
    plt.xlabel("student names")
    plt.ylabel("percentage / %")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()

marks_line_chart()
percentage_bar_chart()


import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints, marker='o', linestyle='dotted')
plt.show()