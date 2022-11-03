from utilityFunctions import toInt, joinList
import re

# Course Objects
class Course:
    # Split read text into course name, description, and associated seasons
    # Each course object also holds their associated prerequisites and semester location
    def __init__(self, text):
        name = re.search('[A-Z]{4} [0-9].{3,4}', text)
        self.name = name.group(0).rstrip() if name != None else "UNKN ?XXX"
        self.desc = text.split(" - ")[1].lstrip() if " - " in text else "Unknown Course (Fa Sp Su)"
        seasons = re.search('\(.{8}\)', text)
        self.seasons = seasons.group(0).rstrip() if seasons != None else "(Fa Sp Su)"     
        self.fall = True if "fa" in self.seasons.lower() else False
        self.spring = True if "sp" in self.seasons.lower() else False
        self.summer = True if "su" in self.seasons.lower() else False
        self.prereqs = []
        self.semester = ""
    # For displaying course objects
    def __repr__(self):
        if len(self.prereqs) > 0:
            return self.name + " - " + self.desc + ": " + joinList(self.prereqs, "and")
        return self.name + " - " + self.desc + ": No prerequisites."
    # Helper function to add unique prereq to course object
    def addPrereq(self, name):
        if name not in self.prereqs:
            self.prereqs.append(name)
    # Helper function to remove prereq from course object
    def delPrereq(self, name):
        if name in self.prereqs:
            self.prereqs.remove(name)


# Semester Objects
class Semester:
    # Create semester object based on unique name
    # Each semester objects holds associated courses
    def __init__(self, name):
        self.season = name.split(" ")[0] if " " in name else "Unknown"
        self.year = toInt(name.split(" ")[1]) if " " in name else 9999
        self.courses = []
    # For displaying semester objects
    def __repr__(self):
        return self.season + " " + str(self.year) + "\n" + joinList(self.courses.copy(), "and")
    # For sorting semester objects
    def __lt__(self, other):
        if self.year < other.year: return True
        if self.year == other.year:
            if "spring" in self.season.lower() and "spring" not in other.season.lower(): return True
            if "summer" in self.season.lower() and "fall" in other.season.lower(): return True
        return False
    # Helper function to add unique course to semester object
    def addCourse(self, name):
        if name not in self.courses:
            self.courses.append(name)
    # Helper function to remove course from semester object
    def delCourse(self, name):
        if name in self.courses:
            self.courses.remove(name)