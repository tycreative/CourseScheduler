from objectsModule import Course

# Hardcoded course information (may want to replace this with a database in future)
courses = {
    "CPSC 1105": Course("CPSC 1105 - Introduction to Information Technology (Fa Sp Su)"),
    "MATH 1113": Course("MATH 1113 - Pre-Calculus (Fa Sp Su)"),
    "CPSC 1301K": Course("CPSC 1301K - Computer Science I w/ Lab (Fa Sp Su)"),
    "CPSC 1302": Course("CPSC 1302 - Computer Science II (Fa Sp Su)"),
    "CPSC 2105": Course("CPSC 2105 - Computer Organization (Fa Sp --)"),
    "CPSC 2108": Course("CPSC 2108 - Data Structures (Fa Sp Su)"),
    "CPSC 2115": Course("CPSC 2115 - Information Technology Fundamentals (Fa -- --)"),
    "CPSC 2125": Course("CPSC 2125 - Internet Programming (Fa Sp --)"),
    "MATH 2125": Course("MATH 2125 - Intro to Discrete Math (Fa Sp Su)"),
    "CYBR 2159": Course("CYBR 2159 - Introduction to Computer Networking (Fa Sp --)"),
    "CYBR 2160": Course("CYBR 2160 - Information Security (Fa Sp Su)"),
    "CPSC 3105": Course("CPSC 3105 - Digital Multimedia Development (-- Sp --)"),
    "CYBR 3106": Course("CYBR 3106 - Cybersecurity Risk Management (-- Sp --)"),
    "CYBR 3108": Course("CYBR 3108 - Defensive Programming (Fa -- --)"),
    "CPSC 3111": Course("CPSC 3111 - Cobol Programming (Fa -- --)"),
    "CPSC 3116": Course("CPSC 3116 - z/OS and JCL (Fa -- --)"),
    "CPSC 3118": Course("CPSC 3118 - Graphical User Interface (-- Sp --)"),
    "CYBR 3119": Course("CYBR 3119 - Fundamentals of Digital Forensics (-- Sp --)"),
    "CPSC 3121": Course("CPSC 3121 - Assembly I (-- Sp --)"),
    "CPSC 3125": Course("CPSC 3125 - Operating Systems (Fa Sp --)"),
    "CYBR 3126": Course("CYBR 3126 - Client/Server Security (Fa -- --)"),
    "CYBR 3128": Course("CYBR 3128 - Cybersecurity Management (-- Sp Su)"),
    "CPSC 3131": Course("CPSC 3131 - Database Systems (Fa Sp --)"),
    "CYBR 3135": Course("CYBR 3135 - Infrastructure Security (-- Sp --)"),
    "CYBR 3136": Course("CYBR 3136 - Wireless, IoT, and Mobile Security (Fa -- --)"),
    "CPSC 3137": Course("CPSC 3137 - Natural Language Processing and Text Mining (-- Sp --)"),
    "CPSC 3156": Course("CPSC 3156 - Transaction Processing (-- Sp --)"),
    "CPSC 3165": Course("CPSC 3165 - Professionalism in Computing (Fa Sp Su)"),
    "CPSC 3175": Course("CPSC 3175 - Object-Oriented Design (Fa Sp --)"),
    "MATH 5125U": Course("MATH 5125U - Discrete Math (Fa Sp Su)"),
    "CPSC 3415": Course("CPSC 3415 - IT Practicum (Fa Sp Su)"),
    "CPSC 3555": Course("CPSC 3555 - Special Topics (Fa -- --)"),
    "CPSC 4000": Course("CPSC 4000 - Baccaulaureate Survey (Fa Sp Su)"),
    "CPSC 4111": Course("CPSC 4111 - Game Programming I (Fa -- --)"),
    "CPSC 4112": Course("CPSC 4112 - Game Programming II (-- Sp --)"),
    "CPSC 4113": Course("CPSC 4113 - Game Jam (-- Sp --)"),
    "CPSC 4115": Course("CPSC 4115 - Algorithms Analysis and Design (Fa -- --)"),
    "CPSC 4121": Course("CPSC 4121 - Robotics Programming I (Fa -- --)"),
    "CPSC 4125": Course("CPSC 4125 - Server-Side Web Development (Fa -- --)"),
    "CPSC 4126": Course("CPSC 4126 - Web Development Projects (-- Sp --)"),
    "CPSC 4127": Course("CPSC 4127 - Computer & Network Security (Fa -- --)"),
    "CYBR 4128": Course("CYBR 4128 - Penetration Testing and Countermeasures (-- Sp --)"),
    "CPSC 4130": Course("CPSC 4130 - Mobile Computing (-- Sp --)"),
    "CPSC 4135": Course("CPSC 4135 - Programming Languages (-- Sp --)"),
    "CYBR 4137": Course("CYBR 4137 - Security Policies & Implementation Security (Fa -- --)"),
    "CYBR 4138": Course("CYBR 4138 - Security Auditing for Compliance (-- Sp --)"),
    "CYBR 4139": Course("CYBR 4139 - Security Issues in Legal Context (Fa -- --)"),
    "CPSC 4145": Course("CPSC 4145 - Computer Graphics (Fa -- --)"),
    "CYBR 4145": Course("CYBR 4145 - Security for Web Applications & Social Networking (-- Sp --)"), # conflicting number with above
    "CYBR 4146": Course("CYBR 4146 - Network, Virtualization, & Cloud Communication Infrastructure (Fa -- --)"),
    "CPSC 4148": Course("CPSC 4148 - Theory of Computation (-- Sp --)"),
    "CPSC 4155": Course("CPSC 4155 - Computer Architecture (Fa -- --)"),
    "CPSC 4157": Course("CPSC 4157 - Computer Networks (Fa -- Su)"),
    "CYBR 4160": Course("CYBR 4160 - Applied Cryptography (-- Sp --)"),
    "CYBR 4166": Course("CYBR 4166 - Intrusion Detection & Prevention (-- Sp --)"),
    "CPSC 4175": Course("CPSC 4175 - Software Engineering (Fa -- --)"),
    "CPSC 4176": Course("CPSC 4176 - Senior Software Engineering Project (-- Sp --)"),
    "CPSC 4185": Course("CPSC 4185 - Intro to AI and Machine Learning (-- Sp --)"),
    "CPSC 4205": Course("CPSC 4205 - Senior Project & Portfolio (Fa Sp Su)"),
    "CYBR 4416": Course("CYBR 4416 - Cybersecurity Practicum (Fa Sp Su)"),
    "CPSC 6000": Course("CPSC 6000 - Graduate Exit Exam (Fa Sp Su)"),
    "CPSC 6103": Course("CPSC 6103 - AP CS Principles (-- Sp --)"),
    "CPSC 6105": Course("CPSC 6105 - Fundamental Principles of Computer Science (Fa Sp --)"),
    "CPSC 6106": Course("CPSC 6106 - Fundamentals of Computer Programming and Data Structures (Fa Sp --)"),
    "CPSC 6107": Course("CPSC 6107 - Survey of Modeling and Simulation (Fa Sp Su)"),
    "CPSC 6109": Course("CPSC 6109 - Algorithms Analysis and Design (Fa Sp --)"),
    "CPSC 6114": Course("CPSC 6114 - Fundamentals of Machine Learning (Fa -- --)"),
    "CPSC 6118": Course("CPSC 6118 - Human-Computer Interface Development (Fa -- --)"),
    "CPSC 6119": Course("CPSC 6119 - Object-Oriented Development (-- Sp --)"),
    "CPSC 6124": Course("CPSC 6124 - Advanced Machine Learning (-- Sp --)"),
    "CPSC 6125": Course("CPSC 6125 - Operating Systems Design and Implementation (Fa -- --)"),
    "CPSC 6126": Course("CPSC 6126 - Introduction to Cybersecurity (Fa Sp Su)"),
    "CPSC 6127": Course("CPSC 6127 - Contemporary Issues in DBMS (-- Sp --)"),
    "CPSC 6128": Course("CPSC 6128 - Network Security (-- Sp --)"),
    "CPSC 6129": Course("CPSC 6129 - Computer Language Design and Interpretation (Fa -- --)"),
    "CPSC 6136": Course("CPSC 6136 - Human Aspects of Cybersecurity (Fa -- --)"),
    "CPSC 6138": Course("CPSC 6138 - Mobile Systems and Applications (-- -- Su)"),
    "CPSC 6147": Course("CPSC 6147 - Data Visualization and Presentation (-- Sp --)"),
    "CPSC 6155": Course("CPSC 6155 - Advanced Computer Architecture (-- -- Su)"),
    "CPSC 6157": Course("CPSC 6157 - Network and Cloud Management (Fa -- --)"),
    "CPSC 6159": Course("CPSC 6159 - Cybersecurity Investigations and Crisis Management (Fa -- --)"),
    "CPSC 6167": Course("CPSC 6167 - Cybersecurity Risk Management (-- Sp --)"),
    "CPSC 6175": Course("CPSC 6175 - Web Site Development and Technologies (-- Sp --)"),
    "CPSC 6177": Course("CPSC 6177 - Software Design and Development (-- Sp --)"),
    "CPSC 6178": Course("CPSC 6178 - Software Testing and Quality Assurance (Fa -- --)"),
    "CPSC 6179": Course("CPSC 6179 - Software Project Management (Fa -- --)"),
    "CPSC 6180": Course("CPSC 6180 - Software Measurement and Estimation (Fa -- --)"),
    "CPSC 6185": Course("CPSC 6185 - Intelligent Systems (-- Sp --)"),
    "CPSC 6190": Course("CPSC 6190 - Applied Cryptography (-- Sp --)"),
    "CSMT 6222": Course("CSMT 6222 - Foundation of Cybersecurity Policy and Management (Fa Sp --)"),
    "CSMT 6223": Course("CSMT 6223 - Enterprise Information Security (-- Sp --)"),
    "CSMT 6226": Course("CSMT 6226 - Cloud Computing Security (-- -- Su)"),
    "CSMT 6228": Course("CSMT 6228 - Global Cybersecurity (Fa -- --)"),
    "CSMT 6299": Course("CSMT 6299 - Capstone in Cybersecurity Policy and Management (Fa Sp Su)")
    }


# Helper function to return courses dictionary
def getCourses():
    return courses

def getCourse(course):
    if course in courses.keys():
        return courses[course]
    return None

def addCourse(course, desc):
    if course not in courses.keys():
        courses[course] = Course(course + " " + desc)

def delCourse(course):
    if course in courses.keys():
        courses.pop(course)