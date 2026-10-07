

class Stud:
    m1 = int(input("Enter Marks1\n"))
    m2 = int(input("Enter Marks2\n"))
    m3 = int(input("Enter Marks3\n"))
    m4 = int(input("Enter Marks4\n"))
    m5 = int(input("Enter Marks5\n"))

    tot = m1 + m2 + m3 + m4 + m5
    avg = tot / 5

    def bigcal(self):
        if self.avg >= 90:
            print("Grade 1st")
        elif self.avg >= 81:
            print("Grade 2nd")
        elif self.avg >= 71:
            print("Grade 3rd")
        else:
            print("Fourth Grade")

s = Stud()
s.bigcal()
