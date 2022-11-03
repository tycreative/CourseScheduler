from objectsModule import Semester

semesters = {}

def getSemesters():
    return semesters

def getSortedSemesters():
    return sorted(semesters.values())

def getSemester(semester):
    if semester in semesters.keys():
        return semesters[semester]
    return None

def addSemester(semester):
    if semester not in semesters.keys():
        semesters[semester] = Semester(semester)

def delSemester(semester):
    if semester in semesters.keys():
        semesters.pop(semester)