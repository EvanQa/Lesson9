#input grades from user until entered -999
#save all grades
#print the max grade
#print the lowest grade
#print the average
#if a grade is not between 0-100 ignore
        #.append() adding value to the end of the list
        #.pop() take out value  from the list
        #len = how many thing there is into the list
        #clear() = clear the list
import statistics

grades: list[int] = []
SENTINEL: int = -999
grade: int = 0
while True:
    grade = int(input("enter a grade (-999 to stop):"))
    if grade == SENTINEL:
        break
    if 0 <= grade <= 100:
        continue
    grades.append(grade)
    if len(grades) > 0:
        print(f"Max grade: {max(grades)}")
        print(f"lowest grade: {min(grades)}")
        print(f"average grade: {sum(grades) / len(grades): .2f}")
        print(f"mean == {statistics.mean(grades)}")
else:
     print("no valid grades were entered")


