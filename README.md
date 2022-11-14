# CourseScheduler
Simple course scheduler creator and checker program made in Python.
The software is able to generate a complete course plan based on the input files provided or check for prerequisite issues in an existing course plan.

## Usage
Keep everything within the same folder and run userInterface.py, follow terminal instructions.
* There is a standalone executable version which has not been included in this repository.

## Prereqs
Your prerequisites file MUST be in the form of a comma-separated list.
Your prerequisites file SHOULD contain all courses that are needed by your specific major.
Therefore, on each line, place a course that is needed by your major.
Following each course, list any prerequisites that said course may have.
```
For example (prereqs.csv):
	CPSC 3125, CPSC 2105, CPSC 2108
	CPSC 3131, CPSC 1302
	CPSC 1301K
```
In this file (prereqs.csv), CPSC 3125, CPSC 3131, and CPSC 1301K are my required courses.
CPSC 3125 has the prerequisites of CPSC 2105 and CPSC 2108.
CPSC 3131 has the prerequisites of CPSC 1302.
CPSC 1301K has no prerequisites but is still a required course.

## Excel 
Please use the provided Excel template file for documenting your existing course plan.
DON'T leave blank cells between courses in the same semester.
Place Fall semesters in the leftmost column.
Place Spring semesters in the middle column.
Place Summer semesters in the rightmost column.
Any outputted Excel files will follow this format as well.
```
For example (plan.xlsx):
	Fall 2023	Spring 2024	Summer 2024
	CPSC 1301K	CPSC 1302
	MATH 1113
```
In this file (plan.xlsx), Fall 2023, Spring 2024, and Summer 2024 are my semesters.
Fall is placed in the leftmost column, spring in the middle, and summer in the rightmost.
CPSC 1301K and MATH 1113 are my Fall classes and placed in the two cells directly underneath my Fall 2023 semester cell.
CPSC 1301 is my Spring class and placed in the cell directly beneath my Spring semester cell.
Summer 2024 has no classes associated with it so the cells below it are blank.

## Demo
Starting with a blank template file
![Blank template file](screenshots/blank.png?raw=true)

Passing in the prereqs.csv, but NOT allowing summer courses
![No summer output](screenshots/output1.png?raw=true)

This time allowing summer courses
![Summer output](screenshots/output2.png?raw=true)
