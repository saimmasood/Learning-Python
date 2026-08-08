


print("-------------")
print("Python Quiz")
print("-------------")


questions =[ 
    ["1.Which one is a computer Language","python","c++","both A&B","None","3"],
    ["2.What does OOP stand for?","Object Oriented Programming","Object Ordered Programming","Online Object Programming","Offline Ordered Programming","1"],
    ["3.Which of the following is a relational database management system?","MongoDB","MySQL","Redis","Cassandra","2"],
    ["4.What is the extension of a C++ source file?",".c",".cpp",".cxx","Both B & C","4"],
    ["5.Which data structure operates on a Last In, First Out (LIFO) principle?","Queue","Array","Stack","Tree","3"],
    ["6.What does SQL stand for?","Structured Question Language","Strong Query Language","Structured Query Language","System Query Language","3"],
    ["7.Which of these is not considered a programming language?","Java","HTML","Python","Ruby","2"],
    ["8.Which symbol is used for single-line comments in C++?","/*","//","#","<!--","2"],
    ["9.What is the average time complexity of binary search?","O(n)","O(n log n)","O(log n)","O(1)","3"],
    ["10.Which keyword is used to allocate memory dynamically in C++?","malloc","alloc","new","create","3"],
    ["11.What is the primary purpose of an operating system?","Process management","Memory management","File management","All of the above","4"],
    ["12.Which sorting algorithm is generally considered the fastest for large, random datasets?","Bubble Sort","Merge Sort","Quick Sort","Insertion Sort","3"],
    ["13.What does API stand for?","Application Programming Interface","Application Process Interface","Automated Programming Interface","Advanced Program Integration","1"],
    ["14.What is the correct syntax to output text to the console in C++?","System.out.println();","cout <<","print();","echo","2"],
    ["15.In a database, what is a primary key?","A unique identifier for a record","A key used only for sorting","A key that allows duplicate values","None of the above","1"],
    ["16.Which of the following translates high-level source code into machine code all at once?","Assembler","Compiler","Interpreter","Linker","2"]
]

totalMarks=16
obtainedMarks=0

for i in range(0,len(questions)):

        print(questions[i][0])
        print("1)",questions[i][1],"    2)",questions[i][2])
        print("3)",questions[i][3],"    4)",questions[i][4])

        try:
            n=int(input("\nEnter your answer(1-4): "))
        except ValueError:
            print("Question Wasted, next time enter a valid value!")
            continue

        if(n<1 or n>4):
                print("Choice not in range try agian(1-4)!")
                print("Question Wasted!")
                continue

        if n==int(questions[i][5]):
             obtainedMarks+=1
             print("\nCorrect Answer!\n")
        else:
             print("\nWrong Answer!\n")

print("You Answered ",obtainedMarks," questions Out of 16 Correctly.")
print("Score: ",obtainedMarks)

percentage=float((obtainedMarks/totalMarks)*100)
print(percentage)

if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is an : ",grade)

