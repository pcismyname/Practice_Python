import numpy as np
def read_file(filename):
  print(f"Reading data from {filename}")
  filename = np.loadtxt(filename,delimiter=",")
  return filename

def query_score(table):
  rows,cols = table.shape
  print(f"Found scores of {rows} student(s) on {cols} subject(s)")
  num = int(input("Enter student no.: "))
  sub = int(input("Enter subject no.: "))
  print(f"Student #{num}'s score on subject #{sub} is {table[num-1][sub-1]}")


def print_fails(table):
  rows,cols = table.shape
  for i in range(0,rows):
    for j in range(0,cols):
      if table[i][j] < 50:
        print(f"Student #{i+1} fails subject #{j+1} with score {table[i][j]}")

def print_student_summary(table):
  print("Student Summary\n===============")
  rows,cols = table.shape 
  for i in range(0,rows):
    s = 0
    for j in range(0,cols):
      s = int(s + table[i][j])
    print(f"Total scores for student #{i+1}: {s}")


def print_subject_summary(table):
  print("Subject Summary\n===============")
  rows,cols = table.shape 
  for i in range(0,cols):
    s = 0
    for j in range(0,rows):
      s = s + table[j][i]
    av = s/rows
    print(f"Average score for subject #{i+1}: {av:.2f}")

def query_student_mean(table):
  rows,cols = table.shape
  num = int(input("Enter student no.: "))
  for i in range(0,cols):
    s = 0
    for j in range(0,cols):
      s = s + table[num-1][j]
  av = s/cols
  print(f"Average score for student #{num} = {av:.2f}")

filename = input("Enter filename: ")
table = read_file(filename)

while (True):
    print("1. Query score")
    print("2. Print failing students")
    print("3. Print student summary")
    print("4. Print subject summary")
    print("5. Query student mean")
    print("6. Quit")
    choice = int(input("Enter choice: "))
    if (choice == 6):
        break
    elif (choice == 1):
        query_score(table)
    elif (choice == 2):
        print_fails(table)
    elif (choice == 3):
        print_student_summary(table)
    elif (choice == 4):
        print_subject_summary(table)
    elif (choice == 5):
        query_student_mean(table)