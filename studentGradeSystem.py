
class StudentGradeSystem:

    rollCount=0;

    def __init__(self,rollNo=-1,name=None,marks=0):
        self.__rollNo=rollNo
        self.__name=name
        self.__marks=marks

    def addStudent(self):
            
        name=input("Enter the name: ")

        try:    
            marks=float(input("Enter the makrs: "))
        except ValueError:
            print("Enter the valid makrs, next time")
            return None

        self.__rollNo=StudentGradeSystem.rollCount
        self.__name=name
        self.__marks=marks

        StudentGradeSystem.rollCount+=1

    def getName(self):
        return self.__name    

    def calculateGrade(self):
            if self.__marks >= 90:
                return "A"
            elif  self.__marks>= 80:
                return "B"
            elif self.__marks>= 70:
                return "C"
            elif self.__marks>= 60:
                return "D"
            else:
             return "F"

    def showStudent(self):
        print("Roll No:",self.__rollNo)
        print("Name: ",self.__name)  
        print("Marks: ",self.__marks) 
        print("Grade: ",self.calculateGrade())
        print("\n")      


def searchStudent(name,stList):

    for i in range(0,len(stList)):
        if name==stList[i].getName():
            return i
    
    return -1


print("--------------------")
print("Student Management System")
print("--------------------\n")

count=0
studentList=[]

while True:

    print("----Menu----\n1.Add Student\n2.Calculate Grade\n3.Show Student\n4.Search Student\n0.Exit!")

    try:
        choice = int(input("Enter Your Choice(0-4): "))
    except ValueError:
        print("Enter a valid choice!")
        continue    

    if(choice<0 or choice>4):
        print("Enter between (0-4)!")
        continue   

    if(choice==1 or choice ==2):

        if(count==0 and choice==2):
            print("No student currently to calculate Grade! First Add one!")
            continue

        elif(choice==1):
            s=StudentGradeSystem()
            s.addStudent()
            studentList.append(s)
            count+=1

        elif(choice==2):
            print(studentList[count-1].calculateGrade())

    elif(choice==3):
        for i in range(0,len(studentList)):
            studentList[i].showStudent()
        
    elif(choice==4):
        name=input("Enter a student name to search: ")
        index=searchStudent(name,studentList) 

        if index==-1:
            print("Student Not Fount is the List!")
        else:
            print("Student Recored Found!")
            studentList[index].showStudent()

    elif(choice==0):
        print("Exiting the Program!")
        break         
        
        
    

