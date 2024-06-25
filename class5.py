class Student:
    def __init__(self,kname,sroll,sbranch,sarea):
        self.kname=kname
        self.sroll=sroll
        self.sbranch=sbranch
        self.sarea=sarea
    def information(self):
        return f"name is :{self.kname} Roll.no is{self.sroll} belongs to {self.sbranch} comes from {self.sarea}"
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.sbranch == other.sbranch
        return False
student=Student(kname="keerthan",sroll=6222,sbranch="cyber",sarea="hyderabad")
student2=Student(kname="raju",sroll=6223,sbranch="cyber",sarea="kamareddy")
print(f"name of the student is {student.kname} roll number is{student.sroll} branch is {student.sbranch} "
      f"and area is {student.sarea}")
print(student==student2)
print(student.information())