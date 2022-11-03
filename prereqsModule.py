from semestersData import getSortedSemesters
import coursesData as data
import re



# Function used to find required courses and their prerequisites
def findPrereqs(filename):
    try:
        courses, prerequisites = [], []
        with open(filename, "r") as file:
            # Open prereqs file and read each line
            for line in file:
                # Find any prereqs in file
                prereqs = re.findall('[A-Z]{4} [0-9].{3,4}', line.rstrip().replace(",", ""))
                course = prereqs.pop(0).rstrip() # grabbing first course
                # Add course to list if missing
                if course not in courses:
                    courses.append(course)
                # Add course to data if doesn't exist
                if course not in data.getCourses().keys():
                    print(f"Adding unknown course '{course}' to data...")
                    data.addCourse(course, "Unknown Course (Fa Sp Su)")
                # Match prereqs to existing course
                for p in prereqs:
                    data.getCourse(course).addPrereq(p.rstrip())
                    if p.rstrip() not in prerequisites:
                        prerequisites.append(p.strip())
            # Lambda function used to sort courses by first digit of each course number (for better prereqs sorting)
            return sorted(courses, key = lambda digit: ord(digit[5])), len(prerequisites)

    except KeyError:
        raise Exception(f"Unexpected error populating course object, aborting.\nPlease check input files and try again.")
    except FileNotFoundError:
        raise Exception(f"File {filename} not found, aborting.\nWas it moved or renamed?")
    except IOError:
        raise Exception(f"Unable to open {filename}, aborting.\nAre other programs blocking it?")
    except Exception:
        raise Exception(f"Unexpected error occurred opening {filename}, aborting.\nIs file corrupted?")



# Function used to sort list of prereqs (so no course comes before its needed prereqs)
# This is recursive!
def sortPrereqs(prereqs, courses):
    try:
        if len(courses) <= 1:
            return prereqs + courses
        # If passes base case, grab next course and its prereqs
        for course in courses:
            for p in data.getCourse(course).prereqs:
                # If prereq is not satisfied, move it to front of list and return
                if p not in prereqs:
                    return sortPrereqs(prereqs, [p] + courses)
            # Otherwise, add course to prereqs if not present
            if course not in prereqs:
                prereqs.append(course)
        return prereqs
    
    except KeyError:
        raise Exception("Course object was not created correctly, aborting.\nPlease check spelling in provided files and try again.")
    except RecursionError:
        raise Exception("Possible loop in prerequisites file, aborting.\nPlease check correctness of provided files.")
    except Exception:
        raise Exception("Unexpected error occurred processing prerequisites, aborting.\nPlease check input files and try again.")



# Function to find missing prereqs
def findMissing(prereqs):
    try:
        for semester in getSortedSemesters():
            for course in semester.courses:
                if course in prereqs:
                    prereqs.remove(course)
        return prereqs

    except Exception:
        raise Exception("Unexpected error occurred finding missing prerequisites, aborting.\nPlease check input files and try again.")



# Function to find prerequisite issues
def findIssues():
    try:
        prereqs, issues = [], {}
        # Go through each course in each semester
        for semester in getSortedSemesters():
            for course in semester.courses:
                if data.getCourse(course) != None:
                    # Go through each prereq in course
                    for prereq in data.getCourse(course).prereqs:
                        # If prereq has not been satisfied then it is an issue
                        if prereq not in prereqs:
                            if course not in issues.keys():
                                issues[course] = [prereq]
                            else:
                                issues[course].append(prereq)
            # Add semester courses to prereqs 
            for course in semester.courses:
                if course not in prereqs:
                    prereqs.append(course)            
        return issues
    
    except KeyError:
        raise Exception("Semester object was not created correctly, aborting.\nPlease check course plan and try again.")
    except Exception:
        raise Exception("Unexpected error occurred finding issues in course plan, aborting.\nPlease check input files and try again.")