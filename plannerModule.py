import semestersData as data
from coursesData import getCourse



# Function to get semester after current
def getNextSemester(current, summer = True):
    try:
        if data.getSemester(current) == None:
            data.addSemester(current)
        semester = data.getSemester(current)
        # Determine next semester based on information of current
        if "fall" in semester.season.lower(): next = "Spring " + str(semester.year + 1)
        elif "spring" in semester.season.lower(): next = ("Summer " if summer else "Fall ") + str(semester.year)
        elif "summer" in semester.season.lower(): next = "Fall " + str(semester.year)
        data.addSemester(next)
        return next
    
    except Exception:
        raise Exception("Unexpected error occurred attempting to grab next semester, aborting.\nMaybe try different parameters?")



# Function to find most recent semester from prereqs
def findMostRecent(prereqs):
    try:
        semesters = data.getSortedSemesters()
        recent = 0
        # Go through prereqs
        for p in prereqs:
            # Find semester of prereq and determine if this is most recent semester
            sem = getCourse(p).semester
            semester = data.getSemester(sem)
            if semesters.index(semester) > recent:
                recent = semesters.index(semester)
        # Return most recent semester
        return f"{semesters[recent].season} {semesters[recent].year}"

    except IndexError:
        raise Exception("Unexpected error occurred attempting to access semester object, aborting.\nPlease check input files and try again.")
    except Exception:
        raise Exception("Unexpected error occurred in finding recent semester, aborting.\nPlease check input files and try again.")



# Helper function to find next appropriate semester (based on course specifics)
def findAppropriateSemester(course, semester, summer):
    try:
        if "fall" in semester.lower() and not course.fall: semester = getNextSemester(semester, summer)
        if "spring" in semester.lower() and not course.spring: semester = getNextSemester(semester, summer)
        if "summer" in semester.lower(): 
            if not summer and (course.fall or course.summer): semester = getNextSemester(semester, summer)
            elif not course.summer: semester = getNextSemester(semester, summer)
        return semester

    except Exception:
        raise Exception("Unexpected error occurred finding appropriate semester, aborting.\nPlease check input files and try again.")



# Function to generate semesters
def generateSemesters(courses, year):
    try:
        for c in courses:
            course = getCourse(c)
            # Determine if course has a semester
            if course.semester == "":
                semester = ("Fall " if course.fall else "Spring " if course.spring else "Summer " if course.summer else "Unknown ") + str(year)
                if course.prereqs != []:
                    semester = getNextSemester(findMostRecent(course.prereqs))
            # Try to skip summer when generating (because summer courses are determined when normalizing)
            if "summer" in semester.lower(): semester = getNextSemester(semester)
            semester = findAppropriateSemester(course, semester, False)
            # Update semesters
            course.semester = semester
            data.addSemester(semester)
            data.getSemester(semester).addCourse(course.name)
    
    except Exception:
        raise Exception("Unexpected error occurred generating semesters, aborting.\nPlease check input files and try again.")



# Function to normalize semesters (number of courses per each semester)
def normalizeSemesters(summer, maximum):
    try:
        for sem in data.getSortedSemesters():
            # While a semester has too many courses or summer is enabled and a course has 0 courses
            while len(sem.courses) > maximum or (summer and len(sem.courses) == 0):
                for c in sem.courses:
                    course = getCourse(c)
                    semester = getNextSemester(course.semester, summer)
                    # Get all needed prereqs for next semester's courses
                    prereqs = []
                    for nextCourse in data.getSemester(semester).courses:
                        prereqs += getCourse(nextCourse).prereqs
                    # Check if current course is a needed prereq (if not, then it can be moved)
                    if course.name not in prereqs:
                        # Continue if summer semester is 'full'
                        if (summer and "summer" in semester.lower() and len(data.getSemester(semester).courses) >= 2):
                            continue
                        # Try to move course (if course season allows it)
                        if findAppropriateSemester(course, semester, summer) == semester:
                            data.getSemester(course.semester).delCourse(course.name)
                            data.getSemester(semester).addCourse(course.name)
                            course.semester = semester
                            break
                # Don't get hung up if no courses can be moved
                break
    
    except Exception:
        raise Exception("Unexpected error occurred normalizing the semesters, aborting.\nMaybe try different parameters?")