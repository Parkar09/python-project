import matplotlib.pyplot as plt

student_names=["Abhishek","Arnav","Prajval","Aniket","Shriakant","Jay"]
student_marks=[35,47,20,45,25,40]
marks_percentage=[35*100/50,47*100/50,20*100/50,45*100/50,25*100/50,40*100/50]

def line_chart_of_students_and_marks():
    plt.plot(student_names,student_marks)
    plt.title("student marks graph")

    plt.xlabel("student Names")
    plt.ylabel("student marks")
    plt.xlim(xmin=0,xmax=6)
    plt.ylim(ymin=1,ymax=50)
    plt.grid(True)


    plt.show()

def bar_chart_of_student_and_their_percentage():
    left_edges=student_names
    height=marks_percentage
    plt.bar(left_edges,height)
    plt.title("student percentage graph")
    plt.xlabel("student names")
    plt.ylabel("student percentage marks")

    plt.show()

line_chart_of_students_and_marks()
bar_chart_of_student_and_their_percentage()