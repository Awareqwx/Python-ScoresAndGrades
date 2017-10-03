from random import randint

def scoresAndGrades():
    j = 0
    g = ""
    for i in range(1, 11):
        j = randint(60, 100)
        if j < 70:
            g = "D"
        elif j < 80:
            g = "C"
        elif j < 90:
            g = "B"
        else:
            g = "A"
        print "Score: " + str(j) + "; Your grade is " + g

scoresAndGrades()