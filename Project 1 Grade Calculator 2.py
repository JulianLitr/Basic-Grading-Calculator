Grade = ["A","B","C","D", "F"]
while True:
    try:
        pointspossible = int(input("PUT MAX SCORE: "))
        break
    except Exception:
        print("You need to put in a valid score!")
studentname = input("Student Name: ")
while True:
    try:
        score = (float(input("Student Score: ")) / pointspossible) * 100
        #Grade = round(score / pointspossible * 100)
        if score >= 90:
            #Grade = "A"
            print("{} - Score is {}% - Letter grade is {}".format(studentname,round(score,2) ,Grade[0]))
        elif 89 >= score >= 80:
            #Grade = "B"
            print("{} - Score is {}% - Letter grade is {}".format(studentname,round(score,2) ,Grade[1]))
        elif 79 >= score >= 70:
            #Grade = "C"
            print("{} - Score is {}% - Letter grade is {}".format(studentname,round(score,2) ,Grade[2]))
        elif 69 >= score >= 60:
            #Grade = "D"
            print("{} - Score is {}% - Letter grade is {}".format(studentname,round(score,2) ,Grade[3]))
        elif score <= 59:
            #Grade = "F"
            print("{} - Score is {}% - Letter grade is {}".format(studentname,round(score,2) ,Grade[4]))
        break
    except Exception:
        print("You need to provide a valid score!")

